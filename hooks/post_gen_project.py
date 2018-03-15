#!/usr/bin/env python
from git import Repo
import os

Repo.clone_from('https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx', '{{cookiecutter.role_name}}', branch='master')

print os.getcwd()
