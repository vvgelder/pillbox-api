from endpoint import Endpoint 

class Api(object):

    def __init__(self, apiurl='http://localhost/api', username=None, password=None, token=None):
        self.apiurl = apiurl
        self.username = username
        self.password = password
        self.token = token

        self.headers = {}
        self.headers['Content-Type'] = 'application/json'
        self.headers['Accept'] = "application/json; indent=4"
        if token:
            self.headers['Authorization'] = token
        self.auth=None
        if username and password:
            self.auth = (username,password)

        self.tenants = Endpoint('tenants')
