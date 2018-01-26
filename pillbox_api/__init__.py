# -*- coding: utf-8 -*-

import requests
import simplejson as json
import urllib

class _api():
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

    def endpoint(self, resource):
        return '{}/{}'.format(self.apiurl,resource)

class tenants(_api):

    def listTenants(self):
        return requests.get(self.endpoint('tenants'), auth=self.auth, headers=self.headers) 

    def findTenant(self, name):
        url = '{}?where={{"tenantid": "{}"}}'.format(self.endpoint('tenants'), name)
        return requests.get(url, auth=self.auth, headers=self.headers) 

    def createTenant(self, data):
        return requests.post(self.endpoint('tenants'), json.dumps(data), auth=self.auth, headers=self.headers) 

    def updateTenant(self, tenantID, etag, data):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.patch(self.endpoint('tenants/{}'.format(tenantID)), json.dumps(data), auth=self.auth, headers=self.headers)

    def deleteTenant(self, tenantID, etag):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.delete(self.endpoint('tenants/{}'.format(tenantID)), auth=self.auth, headers=headers)

class operators(_api):

    def listOperators(self):
        return requests.get(self.endpoint('operators'), auth=self.auth, headers=self.headers) 

    def findOperator(self, opName):
        url = '{}?where={{"name": "{}"}}'.format(self.endpoint('operators'), opName)
        return requests.get(url, auth=self.auth, headers=self.headers) 

    def createOperator(self, data):
        return requests.post(self.endpoint('operators'), json.dumps(data), auth=self.auth, headers=self.headers) 

    def updateOperator(self, opID, etag, data):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.patch(self.endpoint('operators/{}'.format(opID)), json.dumps(data), auth=self.auth, headers=self.headers)

    def deleteOperator(self, opID, etag):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.delete(self.endpoint('operators/{}'.format(opID)), auth=self.auth, headers=headers)

class secrets(_api):

    def listSecretsStores(self,where=None):
        url = "{}?sort=category,name".format(self.endpoint('secrets'))
        if where:
            url = '{}&where={}'.format(url,where)
        return requests.get(url, auth=self.auth, headers=self.headers) 

    def findSecretsStore(self, store):
        url = '{}?where={{"name": "{}"}}'.format(self.endpoint('secrets'), store)
        return requests.get(url, auth=self.auth, headers=self.headers)

    def createSecretsStore(self, data):
        return requests.post(self.endpoint('secrets'), json.dumps(data), auth=self.auth, headers=self.headers)

    def updateSecretsStore(self, passwordID, etag, data):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.patch(self.endpoint('secrets/{}'.format(passwordID)), json.dumps(data), auth=self.auth, headers=headers)

    def deleteSecretsStore(self, passwordID, etag):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.delete(self.endpoint('secrets/{}'.format(passwordID)), auth=self.auth, headers=headers)

class groups(_api):

    def listGroups(self,where=None):
        url = "{}?sort=name".format(self.endpoint('groups'))
        if where:
            url = '{}&where={}'.format(url,where)
        return requests.get(url, auth=self.auth, headers=self.headers) 

    def deleteGroup(self, groupID, etag):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.delete(self.endpoint('groups/{}'.format(groupID)), auth=self.auth, headers=headers)

    def deleteGroups(self):
        headers = self.headers
        return requests.delete(self.endpoint('groups/'), auth=self.auth, headers=headers)

class hosts(_api):

    # list or show hosts (dependi
    def listHosts(self, where=None, projection='{"name": 1}'):
        url = "{}?sort=name".format(self.endpoint('hosts'))
        if where:
            url = '{}&where={}'.format(url, urllib.urlencode(where))
        if projection:
            url = '{}&projection={}'.format(url, urllib.urlencode(projection))
        return requests.get(url, auth=self.auth, headers=self.headers) 

    # delete specific host
    def deleteHost(self, hostID, etag):
        headers = self.headers
        headers['If-Match'] = etag
        return requests.delete(self.endpoint('hosts/{}'.format(hostID)), auth=self.auth, headers=headers)

    # delete all hosts
    def deleteHosts(self):
        headers = self.headers
        return requests.delete(self.endpoint('hosts/'), auth=self.auth, headers=headers)
