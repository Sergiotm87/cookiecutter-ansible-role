#!/usr/bin/env python
from git import Repo

role_name = {{cookiecutter.role_name}}

Repo.clone_from("https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx", role_name)
