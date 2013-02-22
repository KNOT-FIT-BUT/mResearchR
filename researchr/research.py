import json
import httplib

class ResearchClass:
    def __init__(self):
        self.conn = httplib.HTTPConnection("researchr.org")
		self.encoding = "UTF-8"
        
    def searchPublication(self, key):
        data = self.makeRequest(self, "search/publication", key)
		return self.decode(data)

    def searchConference(self, key):
        data = self.makeRequest(self, "search/conference", key)
		return self.decode(data)
        
    def getConference(self, key):
        data = self.makeRequest(self, "conference", key)
		return self.decode(data)

    def getPublication(self, key):
        data = self.makeRequest(self, "publication", key)
		return self.decode(data)
			
    def getPerson(self, key):
        data = self.makeRequest("person", key)
        try:
            JSON = json.loads(data.decode(self.encoding))
		except:
			print "Nastala chyba při načítání json."
    
    def getBibliography(self, key):
        data = self.makeRequest("bibliography", key)
        JSON = json.loads(data.decode('UTF-8'))
    
    def makeRequest(self, term, key):
        self.conn.request("GET", "/api/%s/%s" % (term, key))
        res = self.conn.getresponse()
        if res.status != 200:
            print res.reason
        data = res.read()
        return data
		
	def decode(data):
		return json.loads(data.decode(self.encoding))
