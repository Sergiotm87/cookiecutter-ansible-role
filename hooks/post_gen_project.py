#!/usr/bin/env python
from git import Repo
import os

print os.getcwd()

Repo.clone_from('https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx', '../{{cookiecutter.role_name}}', branch='master')
