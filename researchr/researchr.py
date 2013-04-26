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

    def __searchUsefulUrls(self, urls, rootUrl):
        """
        Search for usefull urls. If cycle found next page of urls it call itself.
        If cycle found url of person, it call itself too.
        If cycle found publication, it save this publication into file.

        @type  urls: dict
        @param urls: List of urls from which we get only the applicable.
        @type  rootUrl: string
        @param rootUrl: Root url from which we began to look for.
        """
        refFound = 0
        for url in urls:
            # search for next url
            if "/explore/authors/1/" in url and "researchr.org/" not in url and url not in rootUrl:
                print("Nasel jsem dalsi uroven: %s" % url)
                refFound = 1
                urls = getUrlsFromPage(url)
                self.searchUsefulUrls(urls, url)

            # search for people
            elif "/alias/" in url and "advised" not in url and "researchr.org/" not in url and "/alias/" not in rootUrl and refFound == 0:
                print("Nasel jsme alias: %s" % url)
                urls = getUrlsFromPage(url)
                self.searchUsefulUrls(urls, url)

            # search for publications
            elif "/publication/" in url and "researchr.org/" not in url:
                print("Nasel jsem publikaci: %s" % url)
                with open(filename, "ab") as myFile:
                    myFile.write(url.replace("/publication/","")+ ";")

    def __getUrlsFromPage(self,url):
        """
        Search for urls on page.

        @type  url: dict
        @param url: Url of page where we want to find urls.
        @rtype: dict
        @return: List of urls.
        """
        req = urllib2.Request("http://researchr.org%s" % url)
        userAgents = ["Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
                           "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0",
                           "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
                           "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1",
                           "Opera/6.01 (Windows XP; U) [de]",
                           "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.6.30 Version/10.63",
                           "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; de) Opera 8.02",
                           "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.50 [en]",
                           "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2b5) Gecko/20091204 Firefox/3.6b5",
                           "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17"
                            ]
        req.add_header('User-agent', userAgents[random.randint(0, 11)])
        try:
            resp = urllib2.urlopen(req)                                                                          
        except:
            try:
                time.sleep(random.uniform(70, 100))
                req = urllib2.Request("http://researchr.org%s" % url)
                req.add_header('User-agent', userAgents[random.randint(0, 11)])
                resp = urllib2.urlopen(req)
            except:
                time.sleep(random.uniform(500, 600))
                try:
                    req = urllib2.Request("http://researchr.org%s" % url)
                    req.add_header('User-agent', userAgents[random.randint(0, 11)])
                    resp = urllib2.urlopen(req)
                except:
                    print("Error in url: %s" % url)
        try:
            content = resp.read()
        except:
            print("Error in url: %s" % url)
        time.sleep(random.uniform(0.9, 2.5))
        urls = re.findall('/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        return urls
    
    def getPublicationsNames(self, filename, mainLetter):
        """
        Get name of all publications which are in reaearchr menu.

        @type  filename: string
        @param filename: Filename where we want to save results.
        @type  mainLetter: string
        @param mainLetter: First letter of authors from which we will find their publications.
        """
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.searchUsefulUrls(self.getUrlsFromPage("/explore/authors/1/%s%s" % (mainLetter,letter)),"/explore/authors/1/%s%s" % (mainLetter,letter))
