#!/usr/bin/python

from paver.easy import *
import paver
import os
import glob
import shutil
import sys

sys.path.append(os.path.dirname(__file__))

@task
def setup():
    sh('python -m pip install -U coverage parameterized radon')


@task
def run():
    sh('python src/GUI.py')


@task
def test():
    sh('python -m coverage run --source src --omit src/GUI.py -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')

@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("*/__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass

@task
def radon():
    sh('radon cc src/master_mind.py -a -nb')
    sh('radon cc src/master_mind.py -a -nb > radon.report')
    if os.stat("radon.report").st_size != 0:
        raise Exception('radon found complex code')



@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
    pass

