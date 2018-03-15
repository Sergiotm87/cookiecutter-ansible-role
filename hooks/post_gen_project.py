#!/usr/bin/env python
from git import Repo
import os
import shutil

#clone repository
Repo.clone_from('{{cookiecutter.ansible_url}}', '{{cookiecutter.role_name}}', branch='master')

#copy all files from repository to working directory (cannot clone into not empy directory)
path = os.getcwd()+"/{{cookiecutter.role_name}}/"
moveto = os.getcwd()+"/"
files = os.listdir(path)
files.sort()
for f in files:
    src = path+f
    dst = moveto+f
    shutil.move(src,dst)
os.rmdir('{{cookiecutter.role_name}}')
