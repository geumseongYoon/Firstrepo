from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
import configparser
import subprocess
import json
import uuid
import requests
from collections import defaultdict
import os
import sys

euid = os.geteuid()
if euid != 0:
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print('Running. Your euid is', euid)
