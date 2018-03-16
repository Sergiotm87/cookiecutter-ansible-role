#!/usr/bin/env python
from git import Repo,remote
import os
import shutil
from github import Github

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

#create a repo using name/pass or token
#g = Github(os.environ['gituser'], os.environ['gitpass'])
g = Github(os.environ['gittoken'])
u = g.get_user()
newrepo = u.create_repo('{{cookiecutter.repo_name}}')

#push to new repo
repo = Repo(os.getcwd(), search_parent_directories=True)
remote = repo.create_remote('testapi', url='https://'+os.environ['gituser']+':'+os.environ['gitpass']+'@github.com/'+{{cookiecutter.github_user}}+'/'+{{cookiecutter.repo_name}})
remote.push(refspec='{}:{}'.format('master', 'master'))
