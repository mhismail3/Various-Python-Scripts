#!/usr/bin/python3

import os, shutil


def create_dir(name, path="."):
    if os.path.exists(path+"/"+name): print('Error: Directory already exists')
    else: os.makedirs(path+"/"+name)


def delete_dir(name):
    os.removedirs(name)


def rename_dir(old, new):
    os.rename(old, new)


def set_dir(name=".."):
    os.chdir(name)


def backup_dir(path=".", newpath="backup"):
    if os.path.exists(newpath):
        print('Error: Cannot overwrite existing directory')
    else: shutil.copytree(path, newpath)


def move_dir(path, newpath):
    if not os.path.exists(newpath): os.makedirs(newpath)
    shutil.move(path, newpath)
