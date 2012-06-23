#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from strapper import app

CGIHandler().run(app)
