import json
import httplib
import sys

class ResearchClass:
    def __init__(self):
        self.conn = None
	self.encoding = "UTF-8"
        
    def searchPublication(self, key, index):
        data = self.makeRequest("search/publication", key, index)
	return self.decode(data)

    def searchConference(self, key, index):
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
                print "Druhy parametr musi byt cislo"
                return
        try:
            self.conn = httplib.HTTPConnection("researchr.org")
            self.conn.request("GET", "/api/%s/%s/%s" % (term, key, index))
            print "/api/%s/%s/%s" % (term, key, index)
        except:
            print "Nastala chyba pri ziskavani dat z webu."
            return
        try:
            res = self.conn.getresponse()
        except:
            print "Nastala chyba pri ziskavani dat z webu."
            return
        if res.status != 200:
            print "Odeslany pozadavek vratil chybu: %s" % res.reason
            return
        data = res.read()
        return data
		
    def decode(self, data):
        try:
            return json.loads(data.decode(self.encoding))
        except:
	    print "Nastala chyba pri nacitani json."
	    return
        
