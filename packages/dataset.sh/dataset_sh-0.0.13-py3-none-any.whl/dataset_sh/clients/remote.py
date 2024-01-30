import json
import os
import warnings
from typing import Optional, List

import requests
from pydantic import BaseModel, Field, ValidationError

from dataset_sh import constants as DatasetConstants
from dataset_sh.profile import DatasetClientProfileConfig
from dataset_sh.utils.files import download_url, upload_to_url, read_url_json


class HostAlias(BaseModel):
    name: str
    host: str


class HostAliasList(BaseModel):
    aliases: List[HostAlias] = Field(default_factory=list)

    def resolve_alias(self, name) -> Optional[str]:
        for item in self.aliases:
            if item.name == name:
                return item.host
        if name == 'default':
            return DatasetConstants.CENTRAL_HOST
        return None

    def save(self):
        config_file = DatasetConstants.ALIAS_FILE
        data = self.model_dump(mode='json')
        with open(config_file, 'w') as out:
            json.dump(data, out, indent=4)

    def add_alias(self, name, host):
        HostAliasList.is_valid_host_address(host, throw=True)
        for item in self.aliases:
            if item.name == name:
                item.host = host
                return
        self.aliases.append(HostAlias(name=name, host=host))
        return self

    def remove_alias(self, name):
        aliases = []
        for item in self.aliases:
            if item.name != name:
                aliases.append(item)
        self.aliases = aliases
        return self

    @staticmethod
    def load_from_disk():
        config_file = DatasetConstants.ALIAS_FILE
        if os.path.exists(config_file):
            with open(config_file, 'r') as content:
                try:
                    json_content = json.load(content)
                    ret = HostAliasList(**json_content)
                    return ret
                except (ValidationError, json.decoder.JSONDecodeError):
                    warnings.warn('cannot parse profile config')
        return HostAliasList()

    @staticmethod
    def resolve_host_or_alias(host: Optional[str]):

        if host is None:
            host = 'default'

        if '://' in host:
            return host
        host_addr = HostAliasList.load_from_disk().resolve_alias(host)
        if host_addr:
            if host_addr.startswith('http://') or host_addr.startswith('https://'):
                return host_addr
            else:
                raise ValueError(f'Invalid host address: {host_addr}, it must starts with https:// or http://')

    @staticmethod
    def is_valid_host_address(host_addr, throw=True):
        if host_addr.startswith('http://') or host_addr.startswith('https://'):
            return True
        else:
            if throw:
                raise ValueError(f'Invalid host address: {host_addr}, it must starts with https:// or http://')
            else:
                return False


class TagResolveResult(BaseModel):
    version: Optional[str] = None


class ListVersionResult(BaseModel):
    versions: list[str]


def url_join(base_url, *path_items):
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    return '/'.join([base_url, *path_items])


class RemoteClients(object):
    profiles: DatasetClientProfileConfig = DatasetClientProfileConfig.load_profiles()

    @staticmethod
    def create_client(base_url_or_host_alais: str, profile_name=None):
        if base_url_or_host_alais is None or base_url_or_host_alais.strip() == '':
            base_url_or_host_alais = DatasetConstants.CENTRAL_HOST

        host_url = HostAliasList.resolve_host_or_alias(base_url_or_host_alais.strip())

        if host_url is None:
            raise ValueError(f'Unable to resolve host: {base_url_or_host_alais}')

        client = RemoteClient(host_url)
        client.resolve_profile(RemoteClients.profiles, profile_name)
        return client

    @staticmethod
    def add_alias(name, host):
        HostAliasList.load_from_disk().add_alias(name, host).save()

    @staticmethod
    def remove_alias(name):
        HostAliasList.load_from_disk().remove_alias(name).save()

    @staticmethod
    def resolve_alias(name):
        return HostAliasList.resolve_host_or_alias(name)


class RemoteClient(object):
    base_url: str

    def __init__(self, base_url):
        self.base_url = base_url
        self.access_key = None

    def resolve_profile(self, profiles: DatasetClientProfileConfig, profile_name):
        return profiles.find_matching_profile(self.base_url, profile_name)

    def get_headers(self):
        if self.access_key:
            return {"X-DATASET-SH-ACCESS-KEY": self.access_key}
        return None

    def get_upload_url(self, username, dataset_name) -> str:
        base_url = url_join(self.base_url, 'dataset', username, dataset_name)
        return base_url

    def get_remote_target_url(self, username, dataset_name, version) -> str:
        base_url = url_join(self.base_url, 'dataset', username, dataset_name)
        return url_join(base_url, 'version', version, 'file')

    def download_version_to(self, loc, username, dataset_name, version):
        url = self.get_remote_target_url(username, dataset_name, version)
        download_url(url, loc, self.get_headers())

    def upload(self, from_location, username, dataset_name, tag=None):
        upload_url = self.get_upload_url(username, dataset_name)
        params = {}
        if tag:
            params['tag'] = tag

        headers = self.get_headers()
        upload_to_url(upload_url, from_location, headers, params, f'{username}/{dataset_name}')

    def resolve_tag(self, username, dataset_name, tag) -> Optional[TagResolveResult]:
        api_url = url_join(self.base_url, 'dataset', username, dataset_name, 'tag', tag)
        headers = self.get_headers()
        resp = requests.get(
            api_url,
            headers=headers,
        )
        resp.raise_for_status()
        return TagResolveResult(**resp.json())

    def set_tag(self, username, dataset_name, tag, version):
        api_url = url_join(self.base_url, 'dataset', username, dataset_name, 'tag', tag)
        headers = self.get_headers()

        resp = requests.post(
            api_url,
            json={'version': version},
            headers=headers,
        )
        resp.raise_for_status()

    def resolve_tag_or_version(self, username, dataset_name, tag=None, version=None) -> Optional[TagResolveResult]:
        if version is not None:
            return version
        elif tag:
            return self.resolve_tag(username, dataset_name, tag)
        return self.resolve_tag(username, dataset_name, 'latest')

    def list_versions(self, username, dataset_name) -> ListVersionResult:
        api_url = url_join(self.base_url, 'dataset', username, dataset_name, 'version')
        headers = self.get_headers()
        resp = requests.get(
            api_url,
            headers=headers,
        )
        resp.raise_for_status()
        return ListVersionResult(**resp.json())
