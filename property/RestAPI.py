# -*- coding: utf-8 -*-
import cherrypy
import threading
class RestFullFuncs(object):

    def __init__(self):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        print ('qqq')
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def singletopology(self):
        data=cherrypy.request.json
        return data

class RestAPI(threading.Thread):
    def __init__(self):
        print ('Initializing')

    def begin(self):
        print ('beginning')
        cherrypy.config.update({'server.socket_host': 'localhost','server.socket_port': 8080,})
        cherrypy.quickstart(RestFullFuncs(),"/tm/v0.0/rest/")