import json
import os
import shutil
import tempfile
import uuid
import warnings
from typing import Optional, Dict

from dataset_sh import constants as DatasetConstants
from dataset_sh.fileio import open_dataset_file
from dataset_sh.clients.common import DatasetNamespaceFolder, DatasetBaseFolder, DatasetVersionHomeFolder
from dataset_sh.clients.remote import RemoteClients
from dataset_sh.profile import DatasetClientProfileConfig
from dataset_sh.models import NamespaceList, DatasetListingResults, DatasetInfoSnippet, DatasetFileInternalPath
from dataset_sh.utils.files import checksum
from dataset_sh.utils.misc import parse_dataset_name


def get_fullname(username, dataset_name, tag, version):
    fullname = f'{username}/{dataset_name}'
    if version:
        fullname = f'{username}/{dataset_name}:version={version}'
    elif tag:
        fullname = f'{username}/{dataset_name}:tag={tag}'
    else:
        fullname = f'{username}/{dataset_name}:tag=latest'
    return fullname


# def correct_version_and_tag(version, tag):
#     if version:
#         return version, None
#     elif tag:
#         return None, tag
#     return None, 'latest'


class LocalClient:
    def __init__(self, store_base=None):
        if store_base is None:
            store_base = DatasetConstants.STORAGE_BASE
        self.base = store_base
        self.profiles = DatasetClientProfileConfig.load_profiles().profiles

    def get_namespace_home(self, namespace) -> DatasetNamespaceFolder:
        return DatasetNamespaceFolder(os.path.join(self.base, namespace))

    def list_namespaces(self) -> NamespaceList:
        base_dir = self.base
        namespaces = []

        if os.path.exists(base_dir):

            for namespace in os.listdir(base_dir):
                if self.get_namespace_home(namespace).is_valid():
                    namespaces.append(namespace)

        return NamespaceList(namespaces=namespaces)

    def list_datasets(self, namespace=None) -> DatasetListingResults:
        if namespace:
            return self.list_datasets_in_namespace(namespace=namespace)

        base_dir = self.base
        datasets = []

        if os.path.exists(base_dir):
            for namespace in os.listdir(base_dir):
                namespace_home = os.path.join(base_dir, namespace)
                nshf = DatasetNamespaceFolder(namespace_home)
                if nshf.is_valid():
                    for dataset_name in nshf.list_dataset():
                        datasets.append(DatasetInfoSnippet(
                            namespace=namespace,
                            dataset=dataset_name,
                        ))

        return DatasetListingResults(items=datasets)

    def list_datasets_in_namespace(self, namespace) -> DatasetListingResults:
        base_dir = self.base
        datasets = []

        namespace_home = os.path.join(base_dir, namespace)
        nshf = DatasetNamespaceFolder(namespace_home)

        if os.path.isdir(namespace_home):
            for dataset_name in nshf.list_dataset():
                datasets.append(DatasetInfoSnippet(
                    namespace=namespace,
                    dataset=dataset_name,
                ))
        return DatasetListingResults(items=datasets)

    def get_dataset_base_dir(self, username, dataset_name) -> DatasetBaseFolder:
        store_dir = os.path.join(self.base, username, dataset_name)
        return DatasetBaseFolder(store_dir)

    def list_versions(self, username, dataset_name) -> list[str]:
        return self.get_dataset_base_dir(username, dataset_name).list_versions()

    def get_version(self, username, dataset_name, version_id) -> Optional[DatasetVersionHomeFolder]:
        return self.get_dataset_base_dir(username, dataset_name).get_version(version_id)

    def get_by_tag(self, username, dataset_name, tag) -> Optional[DatasetVersionHomeFolder]:
        return self.get_dataset_base_dir(username, dataset_name).get_by_tag(tag)

    def list_version_tags(self, username, dataset_name) -> Dict[str, str]:
        return self.get_dataset_base_dir(username, dataset_name).list_tags()

    def get_tag_info(self, username, dataset_name, tag) -> Optional[str]:
        return self.get_dataset_base_dir(username, dataset_name).resolve_tag(tag)

    def set_tag(self, username, dataset_name, tag, version):
        self.get_dataset_base_dir(username, dataset_name).set_tag(tag, version)

    def remove_tag(self, username, dataset_name, tag):
        self.get_dataset_base_dir(username, dataset_name).remove_tag(tag)

    def get_dataset_dir(self, username, dataset_name, version=None, tag=None, allow_none=False) -> Optional[
        DatasetVersionHomeFolder]:
        vf = None
        if version:
            vf = self.get_version(username, dataset_name, version)
        elif tag:
            vf = self.get_by_tag(username, dataset_name, tag)
        else:
            vf = self.get_by_tag(username, dataset_name, 'latest')

        if not allow_none:
            if vf is None or not vf.is_valid():
                fullname = get_fullname(username, dataset_name, version=version, tag=tag)
                raise ValueError(f'{fullname} do not exists')
        return vf

    def get_dataset_meta(self, username, dataset_name, version=None, tag=None):
        vf = self.get_dataset_dir(username, dataset_name, version, tag)
        return vf.get_dataset_meta()

    def get_dataset_file_path(self, username, dataset_name, version=None, tag=None):
        vf = self.get_dataset_dir(username, dataset_name, version, tag)
        return vf.get_dataset_file_path()

    def get_sample(self, username, dataset_name, collection, version=None, tag=None):
        vf = self.get_dataset_dir(username, dataset_name, version, tag)
        return vf.get_sample(collection)

    #
    def get_usage_code(self, username, dataset_name, collection_name, version=None, tag=None):
        vf = self.get_dataset_dir(username, dataset_name, version, tag)
        return vf.get_usage_code(collection_name)

    def dataset_exist(self, username, dataset_name):
        dataset_home_folder = self.get_dataset_base_dir(username, dataset_name)
        return dataset_home_folder.is_valid()

    def dataset_version_exist(self, username, dataset_name, version) -> bool:
        ver = self.get_version(username, dataset_name, version)
        if ver and ver.is_valid():
            return True
        return False

    def delete_dataset(self, username, dataset_name):
        vf = self.get_dataset_base_dir(username, dataset_name)
        shutil.rmtree(vf.base)

    def delete_dataset_version(self, username, dataset_name, version=None, tag=None):
        vf = self.get_dataset_dir(username, dataset_name, version, tag)
        shutil.rmtree(vf.base)

    def import_file(
            self,
            file,
            username,
            dataset_name,
            verify_version=None,
            tag='latest',
            replace=False,
            remove_source=False,
    ):
        version_hex = checksum(file)

        if verify_version and verify_version != version_hex:
            raise ValueError('provided version do not match file signature.')

        if self.dataset_version_exist(username, dataset_name, version=version_hex):
            if not replace:
                warnings.warn(f'dataset {username}/{dataset_name} version {version_hex} already exists')
                return

        dataset_folder = self.get_version(username, dataset_name, version_id=version_hex)
        os.makedirs(
            dataset_folder.base, exist_ok=False
        )

        if remove_source:
            shutil.move(file, dataset_folder.datafile())
        else:
            shutil.copy2(file, dataset_folder.datafile())

        self.extract_sample_and_code_usage(dataset_folder.datafile(), dataset_folder)

        dataset_folder.create()
        self.get_namespace_home(username).create()
        self.get_dataset_base_dir(username, dataset_name).create()

        if tag:
            self.set_tag(username, dataset_name, tag, version_hex)
        return version_hex

    def fetch_remote(
            self,
            host,
            username,
            dataset_name,
            version=None,
            tag=None,
            profile_name=None,
    ):
        """
        fetch a dataset from a remote server.

        by default this function will fetch the latest.

        Args:
            host:
            username:
            dataset_name:
            version:
            tag:
            profile_name:

        Returns:

        """
        remote_client = RemoteClients.create_client(host, profile_name=profile_name)
        should_tag = version is None

        if version is None and tag is None:
            tag = 'latest'

        if version is None or version == '':
            version = remote_client.resolve_tag(username, dataset_name, tag=tag)

        if version is None or version == '':
            fullname = get_fullname(username, dataset_name, version=version, tag=tag)
            raise ValueError(f'cannot resolve {fullname}')

        if self.dataset_version_exist(username, dataset_name, version):
            raise ValueError(f'dataset {username}/{dataset_name} version {version} already exists')

        with tempfile.TemporaryDirectory() as temp_dir:
            file_name = str(uuid.uuid4())
            temp_file_path = os.path.join(temp_dir, file_name)
            remote_client.download_version_to(temp_file_path, username, dataset_name, version)
            tag = tag if should_tag else None
            self.import_file(temp_file_path, username, dataset_name, tag=tag, verify_version=version)

        return version

    def upload_file_to_remote(self, file, host, name, profile_name=None, tag=None):
        remote_client = RemoteClients.create_client(host, profile_name=profile_name)
        username, dataset_name = parse_dataset_name(name)
        remote_client.upload(
            file,
            username,
            dataset_name,
            tag=tag
        )

    def upload_to_remote(self, host, target_name, name=None, file=None, profile_name=None, tag=None, version=None):

        file_path = None

        if file:
            file_path = file
        else:
            if tag:
                username, dataset_name = parse_dataset_name(target_name)
                file_path = self.get_dataset_file_path(username, dataset_name, tag=tag)
            elif version:
                username, dataset_name = parse_dataset_name(target_name)
                file_path = self.get_dataset_file_path(username, dataset_name, version=version)
            else:
                tag = 'latest'
                username, dataset_name = parse_dataset_name(target_name)
                file_path = self.get_dataset_file_path(username, dataset_name, tag=tag)

        if file_path is None or not os.path.exists(file_path):
            raise FileNotFoundError()

        remote_client = RemoteClients.create_client(host, profile_name=profile_name)

        username, dataset_name = parse_dataset_name(target_name)
        remote_client.upload(
            file_path,
            username,
            dataset_name,
            tag=tag
        )

    def find_matching_profile(self, url, profile_name=None):
        if profile_name is not None:
            for p in self.profiles:
                if p.name == profile_name:
                    return p
        else:
            for p in self.profiles:
                if url.startswith(p.host):
                    return p

    @staticmethod
    def extract_sample_and_code_usage(data_file, dataset_folder):
        with open_dataset_file(data_file) as reader:
            meta_file_dest = dataset_folder.meta()
            with reader.zip_file.open(DatasetFileInternalPath.META_FILE_NAME, 'r') as fd:
                with open(meta_file_dest, 'wb') as out:
                    out.write(fd.read())

            for coll_name in reader.collections():
                coll = reader.collection(coll_name)
                with open(dataset_folder.sample_file(coll_name), 'w') as out:
                    samples = coll.top(n=10)
                    for item in samples:
                        out.write(f'{json.dumps(item)}\n')
                with open(dataset_folder.code_example(coll_name), 'w') as out:
                    code = coll.code_usage()
                    out.write(code)
