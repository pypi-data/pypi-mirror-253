import abc
import json
import os
from dataclasses import dataclass
from typing import Optional, List

from pydantic import BaseModel

from dataset_sh.core import DatasetFileMeta
from dataset_sh.typing.codegen import CodeGenerator
from dataset_sh.utils.misc import readfile_or_default, read_jsonl


class FolderWithMarker:
    base: str

    def __init__(self, base):
        self.base = base

    @abc.abstractmethod
    def marker_file(self) -> str:
        raise NotImplementedError()

    def post_create(self):
        return

    def is_valid(self):
        return os.path.isfile(self.marker_file())

    def create_base(self):
        os.makedirs(self.base, exist_ok=True)

    def create(self):
        self.create_base()
        if not self.is_valid():
            with open(self.marker_file(), 'w') as out:
                out.write('1')
            self.post_create()

    def create_if_not_exists(self):
        if not self.is_valid():
            self.create()


class DatasetHomeFolderFilenames:
    MARKER = '.dataset.marker'
    META = 'meta.json'
    DATA_FILE = 'file'


@dataclass
class DatasetVersionHomeFolder(FolderWithMarker):
    base: str

    def __init__(self, base):
        super().__init__(base)
        self.base = base

    def marker_file(self):
        return os.path.join(self.base, DatasetHomeFolderFilenames.MARKER)

    def meta(self):
        return os.path.join(self.base, DatasetHomeFolderFilenames.META)

    def datafile(self):
        return os.path.join(self.base, DatasetHomeFolderFilenames.DATA_FILE)

    def code_example(self, collection_name):
        return os.path.join(self.base, f'usage_code_{collection_name}.py')

    def sample_file(self, collection_name):
        return os.path.join(self.base, f'data_sample_{collection_name}.jsonl')

    # File paths are done.

    def get_dataset_meta(self):
        return json.loads(readfile_or_default(self.meta()))

    def get_dataset_file_path(self):
        return self.datafile()

    def get_sample(self, collection):
        if os.path.isfile(self.sample_file(collection)):
            with open(self.sample_file(collection)) as fd:
                return list(read_jsonl(fd))
        return []

    def get_usage_code(self, collection_name):
        meta = self.get_dataset_meta()
        meta = DatasetFileMeta(**meta)
        cs = [c for c in meta.collections if c.name == collection_name]
        if len(cs) > 0:
            cg = CodeGenerator()
            return cg.generate_all(cs[0].data_schema)
        else:
            return ''


class DatasetNamespaceFolder(FolderWithMarker):
    base: str

    def __init__(self, base):
        super().__init__(base)
        self.base = base

    def marker_file(self):
        return os.path.join(self.base, '.dataset.namespace.marker')

    def list_dataset(self):
        datasets = []
        for dataset_name in os.listdir(self.base):
            dataset_dir = os.path.join(self.base, dataset_name)
            dataset_home_folder = DatasetBaseFolder(dataset_dir)
            if dataset_home_folder.is_valid():
                datasets.append(dataset_name)
        return datasets


@dataclass
class DatasetBaseFolder(FolderWithMarker):
    base: str

    def __init__(self, base):
        super().__init__(base)
        self.base = base

    def post_create(self):
        os.makedirs(os.path.join(self.base, 'version'), exist_ok=True)

    def marker_file(self):
        return os.path.join(self.base, '.dataset.base.marker')

    def version_folder(self):
        return os.path.join(self.base, 'version')

    def tag_file(self):
        return os.path.join(self.base, 'tag')

    def set_tag(self, tag: str, version: str):
        tags = self.read_tag_file()
        tags['tags'][tag] = version
        self.write_tag(tags)
        return self

    def remove_tag(self, tag):
        tags = self.read_tag_file()
        del tags['tags'][tag]
        self.write_tag(tags)
        return self

    def resolve_tag(self, tag) -> Optional[str]:
        tags = self.read_tag_file()
        return tags['tags'].get(tag, None)

    def read_tag_file(self):
        if os.path.exists(self.tag_file()):
            with open(self.tag_file()) as fd:
                return json.load(fd)
        else:
            return {"tags": {}}

    def write_tag(self, tags):
        with open(self.tag_file(), 'w') as fd:
            json.dump(tags, fd)
        return self

    def list_tags(self):
        tags = self.read_tag_file()
        return tags['tags']

    def list_versions(self) -> List[str]:
        items = []
        for version_id in os.listdir(self.version_folder()):
            version_folder = DatasetVersionHomeFolder(os.path.join(self.version_folder(), version_id))
            if version_folder.is_valid():
                items.append(version_id)
        return items

    def get_version(self, version_id) -> DatasetVersionHomeFolder:
        version_folder = DatasetVersionHomeFolder(os.path.join(self.version_folder(), version_id))
        return version_folder

    def get_by_tag(self, tag) -> Optional[DatasetVersionHomeFolder]:
        version_id = self.resolve_tag(tag)
        if version_id:
            version_folder = DatasetVersionHomeFolder(os.path.join(self.version_folder(), version_id))
            return version_folder
        return None
