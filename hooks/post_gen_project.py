#!/usr/bin/env python
from git import Repo

ansible_role_name = '{{ cookiecutter.role_name }}'

Repo.clone_from("https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx", "ansible_role_name/")
