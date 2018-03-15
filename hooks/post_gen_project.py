#!/usr/bin/env python
import git
import os

git.Git(os.getcwd()).clone("https://github.com/Sergiotm87/kitchen-ansible-WordpressNginx")
