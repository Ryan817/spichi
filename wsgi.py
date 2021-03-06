# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: wsgi.py
#          Desc: 
#        Author: ifkite
#         Email: holahello@163.com
#      HomePage: http://github.com/ifkite
#    LastChange: 2017-06-26 23:29:15
# =============================================================================
'''


from wsgiref.simple_server import make_server
from spichi import create_app


if __name__ == '__main__':
    app = create_app()
    httpd = make_server(host='', port=8848, app=app)
    # a method of BaseServer, which's in /lib/python2.7/SocketServer.py
    httpd.serve_forever()
