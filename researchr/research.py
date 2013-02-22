import dict2xml
from dict2xml import dict2xml
import json
import httplib

class ResearchClass:
    def __init__(self):
        self.conn = httplib.HTTPConnection("researchr.org")
        
    def searchPublication(self, key):
        data = self.makeRequest(self, "search/publication", key)
        JSON = json.loads(data.decode('UTF-8'))

    def searchConference(self, key):
        data = self.makeRequest(self, "search/conference", key)
        JSON = json.loads(data.decode('UTF-8'))
        
    def getConference(self, key):
        data = self.makeRequest(self, "conference", key)
        JSON = json.loads(data.decode('UTF-8'))

    def getPublication(self, key):
        data = self.makeRequest(self, "publication", key)
        JSON = json.loads(data.decode('UTF-8'))

    def getPerson(self, key):
        data = self.makeRequest("person", key)
        try:
            JSON = json.loads(data.decode('UTF-8'))
    
    def getBibliography(self, key):
        data = self.makeRequest("bibliography", key)
        JSON = json.loads(data.decode('UTF-8'))
    
    def makeRequest(self, term, key):
        self.conn.request("GET", "/api/%s/%s" % (term, key))
        res = self.conn.getresponse()
        if res.status != 200:
            return res.reason
        data = res.read()
        return data
