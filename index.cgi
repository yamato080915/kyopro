#! /home/yamato0915/miniconda3/envs/flask/bin/python
from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)