def generate_download_code_py(hostname, dataset_name):
    template = f'''
import dataset_sh
dataset_sh.fetch_remote("{dataset_name}", host="{hostname}")
    '''.strip()
    return template


def generate_download_code_bash(hostname, dataset_name):
    template = f'''
dataset.sh remote fetch {dataset_name} -h {hostname}
    '''.strip()
    return template


def generate_download_code_py_with_version(hostname, dataset_name, version):
    template = f'''
import dataset_sh
dataset_sh.fetch_remote("{dataset_name}", host="{hostname}", version="{version}")
    '''.strip()
    return template


def generate_download_code_bash_with_version(hostname, dataset_name, version):
    template = f'''
dataset.sh remote fetch {dataset_name} -h {hostname} -v {version}
    '''.strip()
    return template


def generate_download_code_py_with_tag(hostname, dataset_name, tag):
    template = f'''
import dataset_sh
dataset_sh.fetch_remote("{dataset_name}", host="{hostname}", tag="{tag}")
    '''.strip()
    return template


def generate_download_code_bash_with_tag(hostname, dataset_name, tag):
    template = f'''
dataset.sh remote fetch {dataset_name} -h {hostname} -t {tag}
    '''.strip()
    return template


def generate_download_code(language, hostname, dataset_name, version=None, tag=None):
    if language == 'bash':
        if version:
            return generate_download_code_bash_with_version(hostname, dataset_name, version)
        elif tag:
            return generate_download_code_bash_with_tag(hostname, dataset_name, tag)
        else:
            return generate_download_code_bash(hostname, dataset_name)
    if language == 'python':
        if version:
            return generate_download_code_py_with_version(hostname, dataset_name, version)
        elif tag:
            return generate_download_code_py_with_tag(hostname, dataset_name, tag)
        else:
            return generate_download_code_py(hostname, dataset_name)
