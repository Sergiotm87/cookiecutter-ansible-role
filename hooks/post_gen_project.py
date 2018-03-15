#!/usr/bin/env python
from git import Repo
import os
import shutil

Repo.clone_from('https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx', '{{cookiecutter.role_name}}', branch='master')

path = os.getcwd()+"/{{cookiecutter.role_name}}/"
moveto = os.getcwd()+"/"
files = os.listdir(path)
files.sort()
for f in files:
    src = path+f
    dst = moveto+f
    shutil.move(src,dst)
os.rmdir('{{cookiecutter.role_name}}')
