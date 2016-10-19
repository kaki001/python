import os
import subprocess
import shutil
from gittle import Gittle

for proname, gitpath in projects.iteritems():
    projectPath = workpath + proname;
    if not os.path.isdir(projectPath) :
        os.makedirs(projectPath);
    else :
        shutil.rmtree(projectPath, ignore_errors=True);
        os.makedirs(projectPath);
    os.chdir(projectPath);
    print(projectPath);
    print(gitpath);
    masterPath = projectPath + "/master";
    if os.path.isdir(masterPath):
        os.rmdir("masterPath");
    productPath = projectPath + "/product";
    if os.path.isdir(productPath) :
        os.rmdir(productPath);
    os.system("git clone -b develop " + gitpath);