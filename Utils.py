import os
import shutil
from tkinter.filedialog import askdirectory
from MusicAnalyzer import MusicAnalyzer


def create_workspace(directory):

    directories = []

    workspace = directory + "/" + "Workspace"

    if os.path.exists(workspace):
        shutil.rmtree(workspace)

    os.mkdir(workspace)

    directories.append(directory)
    directories.append(workspace)

    return directories


def prepare_files(directories):

    musicAnalyzer = MusicAnalyzer()

    files = musicAnalyzer.list_files(directories)
    musicAnalyzer.copy_files_to_workspace(files, directories)
    converted_files = musicAnalyzer.convert_mp3_to_wav(files, directories)
    converted_files = musicAnalyzer.rename_files(converted_files, directories)
    musicAnalyzer.convert_stereo_to_mono(converted_files, directories)
    return files
