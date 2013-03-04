import json
import httplib
from exceptions import *


class ResearchrClass:
    def __init__(self):
        self.conn = None
	self.encoding = "UTF-8"
        
    def searchPublications(self, key, index):
        """
        Search publications on researchr.org.

        @type  key: string
        @param key: The search term.
        @type  index: number
        @param index: The page of results.
        @rtype:   dict
        @return:  Index, kind of search, array of results and the search term.
        """
        data = self.__makeRequest("search/publication", key, index)
	return self.__decode(data)

    def searchConferences(self, key, index):
        """
        Search conferences on researchr.org.

        @type  key: string
        @param key: The search term.
        @type  index: number
        @param index: The page of results.
        @rtype:   dict
        @return:  Index, kind of search, array of results and the search term.
        """
        data = self.__makeRequest("search/conference", key, index)
	return self.__decode(data)
        
    def getPublication(self, key):
        """
        Get the publication from researchr.org.

        @type  key: string
        @param key: The name of a publication, which we want to find the record.
        @rtype:   dict
        @return:  Detail informations of publication.
        """
        data = self.__makeRequest("publication", key, "")
	return self.__decode(data)
			
    def getPerson(self, key):
        """
        Get the person (author) from researchr.org.

        @type  key: string
        @param key: The name of a person, which we want to find the record.
        @rtype:   dict
        @return:  Detail informations of person.
        """
        data = self.__makeRequest("person", key, "")
        return self.__decode(data)
        
    def getBibliography(self, key):
        """
        Get the bibliography from researchr.org.

        @type  key: string
        @param key: The name of a bibliography, which we want to find the record.
        @rtype:   dict
        @return:  Detail informations of bibliography.
        """
        data = self.__makeRequest("bibliography", key, "")
        return self.__decode(data)
    
    def __makeRequest(self, term, key, index):
        """
        Make request to researchr.org for get content.

        @type  term: string
        @param term: The name of service.
        @type  key: string
        @param key: The search term.
        @rtype:   string
        @return:  Data in JSON format.
        """
        if not index=="":
            try:
                int(index)
            except:
                raise ValueError("Index parameter must be a number")
        self.conn = httplib.HTTPConnection("researchr.org")
        self.conn.request("GET", "/api/%s/%s/%s" % (term, key, index))
        res = self.conn.getresponse()
        if res.status != 200:
            raise HTTPStatusException("Page return error code %d: %s" % (res.status, res.reason))
        data = res.read()
        return data
		
    def __decode(self, data):
        """
        Decode data.

        @type  data: string
        @param data: Data you want to decode.
        @rtype:   dict
        @return:  Decoded data (clear dict format).
        """
        self.conn.close()
        return json.loads(data.decode(self.encoding))
        
