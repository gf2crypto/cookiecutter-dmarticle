""" Copying the files after rendering. """
import os
import sys
import json
import shutil


WORKING_DIR = os.getcwd()
OPTION_FILE = os.path.join(WORKING_DIR, 'options.json')


def customize_tex_files(language='ru'):
    """Copy LaTeX files.

    Theme includes two subtheme: ru and en.
    After rendering It needs delete unused files and
    copy right files in working folder.
    """
    if language.startswith('ru'):
        tex_dir = os.path.join(WORKING_DIR, 'ru')
    else:
        tex_dir = os.path.join(WORKING_DIR, 'en')
    for srcname in os.listdir(tex_dir):
        src = os.path.join(tex_dir, srcname)
        dst = os.path.join(WORKING_DIR, srcname)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    for srcname in ['ru', 'en']:
        shutil.rmtree(os.path.join(WORKING_DIR, srcname))
    os.remove(OPTION_FILE)


if __name__ == "__main__":
    with open(OPTION_FILE) as file:
        options = json.load(file)
    customize_tex_files(options['language'])
