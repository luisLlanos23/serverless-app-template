from os import mkdir
from os.path import exists, isdir
from .configuration_values import ConfigurationPaths

def configure_directories() -> None:
    if not exists(ConfigurationPaths.root) or not isdir(ConfigurationPaths.root):
        mkdir(ConfigurationPaths.root)
    if not exists(ConfigurationPaths.download_folder) or not isdir(ConfigurationPaths.download_folder):
        mkdir(ConfigurationPaths.download_folder)