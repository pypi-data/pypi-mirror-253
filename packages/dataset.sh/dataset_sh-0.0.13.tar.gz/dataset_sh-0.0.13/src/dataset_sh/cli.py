#!/usr/bin/env python3
import getpass
import json
import os

import click

from dataset_sh import io as dsh_io
from dataset_sh.clients.remote import RemoteClients
from dataset_sh.dependency.parser import parse_file
from dataset_sh.fileio import open_dataset_file
import dataset_sh.constants as DatasetConstants

from .core import DatasetFileMeta
from dataset_sh.clients.local import LocalClient
from dataset_sh.profile import DatasetClientProfileConfig
from .typing.codegen import CodeGenerator
from .utils.misc import parse_dataset_name


@click.group(name='dataset.sh')
def dsh():
    pass


# ··································································
# :oooooooooooo  o8o  oooo                   .oooooo.   oooo   o8o :
# :`888'     `8  `"'  `888                  d8P'  `Y8b  `888   `"' :
# : 888         oooo   888   .ooooo.       888           888  oooo :
# : 888oooo8    `888   888  d88' `88b      888           888  `888 :
# : 888    "     888   888  888ooo888      888           888   888 :
# : 888          888   888  888    .o      `88b    ooo   888   888 :
# :o888o        o888o o888o `Y8bod8P'       `Y8bood8P'  o888o o888o:
# ··································································


@dsh.group(name='file')
def file_cli():
    """cli interface to manage standalone dataset.sh file"""
    pass


@file_cli.command(name='list-collections')
@click.argument('filepath', type=click.Path())
def list_collections(filepath):
    """
    list collections of a dataset
    """
    with open_dataset_file(filepath) as reader:
        collections = reader.collections()
        click.echo(f'Total collections: {len(collections)}')
        for coll in collections:
            click.echo(coll)


@file_cli.command(name='print-code')
@click.argument('filepath', type=click.Path())
@click.argument('collection_name')
def print_code(filepath, collection_name):
    with open_dataset_file(filepath) as reader:
        coll = reader.collection(collection_name)
        code = coll.code_usage()
        schema = coll.config.data_schema
        loader_code = CodeGenerator.generate_file_loader_code(filepath, collection_name, schema.entry_point)
        click.echo(code)
        click.echo('\n\n')
        click.echo(loader_code)


@file_cli.command(name='print-sample')
@click.argument('filepath', type=click.Path())
@click.argument('collection_name')
def print_sample(filepath, collection_name):
    with open_dataset_file(filepath) as reader:
        sample = reader.collection(collection_name).top()
        click.echo(json.dumps(sample, indent=2))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~                                                                         ~
# ~                                                                         ~
# ~                                                                         ~
# ~  oooo                                oooo       .oooooo.   oooo   o8o   ~
# ~  `888                                `888      d8P'  `Y8b  `888   `"'   ~
# ~   888   .ooooo.   .ooooo.   .oooo.    888     888           888  oooo   ~
# ~   888  d88' `88b d88' `"Y8 `P  )88b   888     888           888  `888   ~
# ~   888  888   888 888        .oP"888   888     888           888   888   ~
# ~   888  888   888 888   .o8 d8(  888   888     `88b    ooo   888   888   ~
# ~  o888o `Y8bod8P' `Y8bod8P' `Y888""8o o888o     `Y8bood8P'  o888o o888o  ~
# ~                                                                         ~
# ~                                                                         ~
# ~                                                                         ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dsh.group(name='local')
def local_cli():
    """cli interface to manage dataset.sh project"""
    pass


@local_cli.command(name='import')
@click.argument('name')
@click.argument('file')
@click.option('--tag', '-t', default='latest')
def import_(name, file, tag):
    """import dataset from file"""
    click.echo(f'importing local file from {file}')
    dsh_io.import_file(name, file, tag=tag)


@local_cli.command(name='meta')
@click.argument('name')
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--tag', '-t', help='use this option to select version with tag', default='latest')
def print_meta(name, version, tag):
    """print metadata of a dataset"""
    username, dataset_name = parse_dataset_name(name)
    local_client = LocalClient()
    meta = local_client.get_dataset_meta(username, dataset_name, version=version, tag=tag)
    if meta:
        click.echo(json.dumps(meta, indent=2))


@local_cli.command(name='list-collections')
@click.argument('name')
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--tag', '-t', help='use this option to select version with tag', default='latest')
def list_collections(name, version, tag):
    """
    list collections of a dataset
    """
    username, dataset_name = parse_dataset_name(name)
    local_client = LocalClient()
    version_reader = local_client.get_dataset_dir(username, dataset_name, version=version, tag=tag)
    if version_reader and version_reader.is_valid():
        meta = version_reader.get_dataset_meta()
        meta = DatasetFileMeta(**meta)

        click.echo(f'Total collections: {len(meta.collections)}')
        for coll in meta.collections:
            click.echo(coll.name)


@local_cli.command(name='print-code')
@click.argument('name')
@click.argument('collection_name')
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--tag', '-t', help='use this option to select version with tag', default='latest')
def print_code(name, collection_name, version, tag):
    username, dataset_name = parse_dataset_name(name)
    local_client = LocalClient()
    version_reader = local_client.get_dataset_dir(username, dataset_name, version=version, tag=tag)

    code = version_reader.get_usage_code(collection_name)
    click.echo(code)


@local_cli.command(name='print-sample')
@click.argument('name')
@click.argument('collection_name')
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--tag', '-t', help='use this option to select version with tag', default='latest')
def print_sample(name, collection_name, version, tag):
    username, dataset_name = parse_dataset_name(name)
    local_client = LocalClient()
    version_reader = local_client.get_dataset_dir(username, dataset_name, version=version, tag=tag)
    samples = version_reader.get_sample(collection_name)
    click.echo(json.dumps(samples, indent=2))


@local_cli.command(name='remove')
@click.argument('name')
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--tag', '-t', help='use this option to select version with tag', default=None)
@click.option('--force', '-f', default=False, help='Force remove dataset without confirmation.', is_flag=True)
def remove(name, version, tag, force):
    """remove a managed dataset"""
    local_client = LocalClient()

    username, dataset_name = parse_dataset_name(name)
    do_remove = False

    if force:
        do_remove = True
    else:
        confirmation = click.prompt(f'Are you sure you want to remove all versions of dataset {name}? (y/N): ')
        if confirmation.lower() == 'y':
            do_remove = True

    if do_remove:
        local_client.delete_dataset(username, dataset_name, version=version, tag=tag)


@local_cli.command(name='list')
@click.option('--namespace', '-n', help='select dataset store space to list.')
def list_datasets(namespace):
    """list datasets"""
    items = []
    local_client = LocalClient()
    if namespace:
        items = local_client.list_datasets_in_namespace(namespace).items
    else:
        items = local_client.list_datasets().items

    click.echo(f'\nFound {len(items)} datasets:\n')
    items = sorted(items, key=lambda x: f'{x.namespace} / {x.dataset}')
    for item in items:
        click.echo(f'  {item.namespace}/{item.dataset}')
    click.echo('')


@local_cli.command(name='list-version')
@click.argument('name')
def list_dataset_versions(name):
    """list dataset versions"""
    local_client = LocalClient()
    username, dataset_name = parse_dataset_name(name)
    version = local_client.list_versions(username, dataset_name)

    click.echo(f'\nFound {len(version)} versions:\n')
    for item in version:
        click.echo(f'  {item}')
    click.echo('')


@local_cli.command(name='tag')
@click.argument('name')
@click.argument('tag')
@click.argument('version')
def tag_dataset_version(name, tag, version):
    local_client = LocalClient()
    username, dataset_name = parse_dataset_name(name)
    local_client.set_tag(username, dataset_name, tag=tag, version=version)


@local_cli.command(name='untag')
@click.argument('name')
@click.argument('tag')
def untag_dataset_version(name, tag):
    local_client = LocalClient()
    username, dataset_name = parse_dataset_name(name)
    local_client.remove_tag(username, dataset_name, tag=tag)


@local_cli.command(name='tag-info')
@click.argument('name')
@click.argument('tag')
def print_tag_info(name, tag):
    local_client = LocalClient()
    username, dataset_name = parse_dataset_name(name)
    tagged_version = local_client.get_tag_info(username, dataset_name, tag=tag)
    if tagged_version:
        click.echo(f"{tag} : {tagged_version}")
    else:
        click.echo(f"{tag} do not exists")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~                                                                                                    ~
# ~                                                                                                    ~
# ~                                                                                                    ~
# ~  ooooooooo.                                             .                  .oooooo.   oooo   o8o   ~
# ~  `888   `Y88.                                         .o8                 d8P'  `Y8b  `888   `"'   ~
# ~   888   .d88'  .ooooo.  ooo. .oo.  .oo.    .ooooo.  .o888oo  .ooooo.     888           888  oooo   ~
# ~   888ooo88P'  d88' `88b `888P"Y88bP"Y88b  d88' `88b   888   d88' `88b    888           888  `888   ~
# ~   888`88b.    888ooo888  888   888   888  888   888   888   888ooo888    888           888   888   ~
# ~   888  `88b.  888    .o  888   888   888  888   888   888 . 888    .o    `88b    ooo   888   888   ~
# ~  o888o  o888o `Y8bod8P' o888o o888o o888o `Y8bod8P'   "888" `Y8bod8P'     `Y8bood8P'  o888o o888o  ~
# ~                                                                                                    ~
# ~                                                                                                    ~
# ~                                                                                                    ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dsh.group(name='remote')
def remote_cli():
    """cli interface to manage dataset.sh project"""
    pass


@remote_cli.command(name='set-tag')
@click.argument('name')
@click.argument('tag')
@click.argument('version')
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
@click.option('--profile', '-p', 'profile_name', help='host address.', default=None)
def tag_remote(name, version, tag, host, profile_name):
    """fetch dataset from remote"""
    client = RemoteClients.create_client(host, profile_name=profile_name)
    username, dataset_name = parse_dataset_name(name)
    client.set_tag(username, dataset_name, tag, version)


@remote_cli.command(name='tag-info')
@click.argument('name')
@click.argument('tag')
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
@click.option('--profile', '-p', 'profile_name', help='host address.', default=None)
def print_tag_remote(name, tag, host, profile_name):
    """fetch dataset from remote"""
    client = RemoteClients.create_client(host, profile_name=profile_name)
    username, dataset_name = parse_dataset_name(name)
    click.echo(client.resolve_tag(username, dataset_name, tag).version)


@remote_cli.command(name='list-versions')
@click.argument('name')
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
@click.option('--profile', '-p', 'profile_name', help='host address.', default=None)
def list_remote_versions(name, host, profile_name):
    """fetch dataset from remote"""
    client = RemoteClients.create_client(host, profile_name=profile_name)
    username, dataset_name = parse_dataset_name(name)
    versions = client.list_versions(username, dataset_name)
    for v in versions:
        click.echo(v)


@remote_cli.command(name='fetch')
@click.argument('name')
@click.option('--tag', '-t', help='use this option to select version with tag', default=None)
@click.option('--version', '-v', help='use this option to select version', default=None)
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
def fetch_remote(name, version, tag, host):
    """fetch dataset from remote"""
    dsh_io.fetch_remote(name, version=version, tag=tag, host=host)


@remote_cli.command(name='upload')
@click.argument('target_name')
@click.option('--file', '-f', 'file', help='path to local dataset to upload.', default=None)
@click.option('--version', '-v', help='use this option to select version to upload', default=None)
@click.option('--tag', '-t', help='tag name of this version in remote.', default=None)
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
@click.option('--profile', '-p', 'profile_name', help='host address.', default=None)
def upload(target_name, file, version, tag, host, profile_name):
    """upload dataset to server"""

    local_client = LocalClient()
    local_client.upload_to_remote(host, target_name, version=version, file=file, tag=tag, profile_name=profile_name)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~                                                                                                   ~
# ~                                                                                                   ~
# ~                                                                                                   ~
# ~  ooooooooo.                          o8o                         .        .oooooo.   oooo   o8o   ~
# ~  `888   `Y88.                        `"'                       .o8       d8P'  `Y8b  `888   `"'   ~
# ~   888   .d88' oooo d8b  .ooooo.     oooo  .ooooo.   .ooooo.  .o888oo    888           888  oooo   ~
# ~   888ooo88P'  `888""8P d88' `88b    `888 d88' `88b d88' `"Y8   888      888           888  `888   ~
# ~   888          888     888   888     888 888ooo888 888         888      888           888   888   ~
# ~   888          888     888   888     888 888    .o 888   .o8   888 .    `88b    ooo   888   888   ~
# ~  o888o        d888b    `Y8bod8P'     888 `Y8bod8P' `Y8bod8P'   "888"     `Y8bood8P'  o888o o888o  ~
# ~                                      888                                                          ~
# ~                                  .o. 88P                                                          ~
# ~                                  `Y888P                                                           ~
# ~                                                                                                   ~
# ~                                                                                                   ~
# ~                                                                                                   ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dsh.group(name='project')
def project_cli():
    """cli interface to manage dataset.sh project"""
    pass


@project_cli.command(name='install')
@click.argument('file_path')
def install_project(file_path):
    """import dataset from a dataset project file, or add a dataset to a dataset project file"""

    local_client = LocalClient()
    dep = parse_file(file_path)
    for host_group in dep.datasets_by_host:
        host = host_group.host
        for dataset_item in host_group.datasets:
            username, dataset_name = parse_dataset_name(dataset_item.name)
            local_client.fetch_remote(host, username, dataset_name, version=dataset_item.version, tag=dataset_item.tag)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~                                                                                           ~
# ~                                                                                           ~
# ~                                                                                           ~
# ~    .oooooo.                          .o88o.  o8o                  .oooooo.   oooo   o8o   ~
# ~   d8P'  `Y8b                         888 `"  `"'                 d8P'  `Y8b  `888   `"'   ~
# ~  888           .ooooo.  ooo. .oo.   o888oo  oooo   .oooooooo    888           888  oooo   ~
# ~  888          d88' `88b `888P"Y88b   888    `888  888' `88b     888           888  `888   ~
# ~  888          888   888  888   888   888     888  888   888     888           888   888   ~
# ~  `88b    ooo  888   888  888   888   888     888  `88bod8P'     `88b    ooo   888   888   ~
# ~   `Y8bood8P'  `Y8bod8P' o888o o888o o888o   o888o `8oooooo.      `Y8bood8P'  o888o o888o  ~
# ~                                                   d"     YD                               ~
# ~                                                   "Y88888P'                               ~
# ~                                                                                           ~
# ~                                                                                           ~
# ~                                                                                           ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dsh.group(name='config')
def config_cli():
    """cli interface to manage dataset.sh project"""
    pass


@config_cli.command(name='add-access-key')
@click.option('--host', '-h', 'host', help='host address or alias.', default=None)
@click.option('--name', '-n', 'profile_name', help='profile name.', default=None)
def add_key(host, profile_name):
    """
    Add access key to dataset.sh client.
    Args:
        host: HOST url.
        profile_name: (Optional) you can refer this key using this profile name.

    Returns:

    """
    cfg = DatasetClientProfileConfig.load_profiles()
    if host is None:
        host = input('Host: ').strip()

    if cfg.find_matching_profile(url=host):
        click.echo("")
        click.echo('Find existing profile with the same host.')
        click.echo('You can use profile name to select which key to use in the future.')
        click.echo("")

    if profile_name is None:
        profile_name = input('Profile Name (Optional): ').strip()
        if profile_name == '':
            profile_name = None

    key = getpass.getpass('Enter your access key (Your input will be hidden): ').strip()

    if key == '' or key is None:
        click.echo('Key is empty. \n')
        raise click.Abort()

    cfg.add_profile(host, key, name=profile_name)
    cfg.save()

    click.echo(f'New profile saved in {DatasetConstants.CONFIG_JSON}')


@config_cli.command(name='set-host-alias')
@click.argument('name')
@click.argument('host')
def set_alias(name, host):
    """
    Add host alias.

    Args:
        name: which alias to remove
        host: address of host

    Returns:

    """
    RemoteClients.add_alias(name, host)


@config_cli.command(name='remove-host-alias')
@click.argument('name')
def remove_alias(name):
    """
    Remove host alias.

    Args:
        name: which alias to remove

    Returns:

    """
    RemoteClients.remove_alias(name)


@config_cli.command(name='alias')
@click.argument('name')
def print_alias(name):
    """
    Remove host alias.

    Args:
        name: which alias to remove

    Returns:

    """
    a = RemoteClients.resolve_alias(name)
    click.echo(a)


cli = dsh

if __name__ == '__main__':  # pragma: no cover
    cli()
