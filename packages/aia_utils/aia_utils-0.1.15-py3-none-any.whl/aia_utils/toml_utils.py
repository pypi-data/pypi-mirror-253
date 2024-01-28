import tomli

def _get_project_meta(toml_file: str = 'pyproject.toml'):
    with open(toml_file, mode='rb') as pyproject:
        return tomli.load(pyproject)['tool']['poetry']

def getVersion(toml_file: str = 'pyproject.toml'):
    return _get_project_meta(toml_file)['version']