from os.path import join as join_path, realpath


class ConfigurationPaths:
    root: str = realpath(join_path('/tmp', 'resources/'))
    download_folder: str = realpath(join_path(root, 'downloads/'))
    output_folder: str = realpath(join_path(root, 'out/'))
