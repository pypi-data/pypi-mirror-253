import os

from dataset_sh.clients.local import LocalClient
from dataset_sh.fileio import DatasetFileReader
from dataset_sh.utils.misc import parse_dataset_name


def open_dataset(name: str) -> 'DatasetFileReader':
    """
    Read a managed dataset file by name.
    :param name: name of the dataset file to locate
    :return:
    """
    local_client = LocalClient()
    username, dataset_name = parse_dataset_name(name)
    located = local_client.get_dataset_file_path(username, dataset_name)
    if located and os.path.exists(located):
        return DatasetFileReader(located)
    else:
        raise FileNotFoundError()


def import_file(name, file, replace=False, tag='latest'):
    """
    Import a dataset file, by dfault it will be tagged as latest.
    Args:
        name:
        file:
        replace:
        tag:

    Returns:
    """
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    local_client.import_file(file, username, dataset, replace=replace, tag=tag)


def fetch_remote(
        name,
        version=None,
        tag=None,
        host='https://export.dataset.sh/dataset',
):
    """
    Fetch a dataset from a remote server.

    Args:
        name: name of the dataset
        version:
        tag:
        host:

    Returns:

    """
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    local_client.fetch_remote(host, username, dataset, tag=tag, version=version)


def exists(
        name,
        version=None,
        tag=None,
) -> bool:
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    vf = local_client.get_dataset_dir(username, dataset, tag=tag, version=version, allow_none=True)
    if vf and vf.is_valid():
        return True
    return False


def delete_dataset(
        name,
):
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    return local_client.delete_dataset(username, dataset)


def delete_dataset_version_by_tag(
        name,
        tag,
):
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    return local_client.delete_dataset_version(username, dataset, tag=tag)


def delete_dataset_version_by_version(
        name,
        version,
):
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    return local_client.delete_dataset_version(username, dataset, version=version)


def locate_file(
        name,
        version=None,
        tag=None
):
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    d = local_client.get_dataset_dir(username, dataset, tag=tag, version=version)
    return d.datafile()


def get_latest_version(
        name,
):
    local_client = LocalClient()
    username, dataset = parse_dataset_name(name)
    return local_client.get_tag_info(username, dataset, tag='latest')


def list_datasets(namespace=None):
    local_client = LocalClient()
    if namespace:
        datasets = local_client.list_datasets_in_namespace(namespace)
        return [f"{item.namespace}/{item.dataset}" for item in datasets.items]
    else:
        datasets = local_client.list_datasets()
        return [f"{item.namespace}/{item.dataset}" for item in datasets.items]


def list_namespaces():
    local_client = LocalClient()
    datasets = local_client.list_namespaces()
    return [item for item in datasets.namespaces]
