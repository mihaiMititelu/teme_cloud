import json
import urllib
from urllib import request


def ask_for(service, id):
    '''
    Returns responses from the previous two services,
    based on the third server's requested parameters
    :param service: which service is called
    :param id: the id of the requested resource
    :return: the JSON encoded response from the solicited API
    '''
    port = None
    if service is 'names':
        port = '80'
        response = urllib.request.urlopen('http://127.0.0.1:' + port + '/' + service + '/' + str(id)).read() \
            .decode('utf-8')
        return response
    elif service is 'numbers':
        port = '8080'
        response = urllib.request.urlopen('http://127.0.0.1:' + port + '/' + service + '/' + str(id)).read() \
            .decode('utf-8')
        return response
