import json
import httplib

class ResearchrClass:
    def __init__(self):
        self.conn = None
	self.encoding = "UTF-8"
        
    def searchPublications(self, key, index):
        data = self.makeRequest("search/publication", key, index)
	return self.decode(data)

    def searchConferences(self, key, index):
        data = self.makeRequest("search/conference", key, index)
	return self.decode(data)
        
    def getConference(self, key):
        data = self.makeRequest("conference", key, "")
	return self.decode(data)

    def getPublication(self, key):
        data = self.makeRequest("publication", key, "")
	return self.decode(data)
			
    def getPerson(self, key):
        data = self.makeRequest("person", key, "")
        return self.decode(data)
        
    def getBibliography(self, key):
        data = self.makeRequest("bibliography", key, "")
        return self.decode(data)
    
    def makeRequest(self, term, key, index):
        if not index=="":
            try:
                int(index)
            except:
                print "Second parametr must be number."
                return
        self.conn = httplib.HTTPConnection("researchr.org")
        self.conn.request("GET", "/api/%s/%s/%s" % (term, key, index))
        res = self.conn.getresponse()
        if res.status != 200:
            print "Page return error code %d: %s" % (res.status, res.reason)
            return
        data = res.read()
        return data
		
    def decode(self, data):
        self.conn.close()
        return json.loads(data.decode(self.encoding))
        
