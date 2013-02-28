import researchr

from researchr import *

r = ResearchrClass()

#getPerson example:
print("getPerson(\"eelcovisser\")")
person = r.getPerson("eelcovisser")
print "Fullname of person: %s " % (person["fullname"])
print "Id of person: %s" % (person["id"])
print "Key of person: %s" % (person["key"])

print("Autor write %d publications." % len(person["publications"]))

for publicationOfAuthor in person["publications"]:
    print "Name: %s Year: %s ," % (publicationOfAuthor["key"], publicationOfAuthor["year"]), 
print "\n" * 2

#getPublication example:
print("getPublication(\"HemelKGV-2010\")")
publication = r.getPublication("HemelKGV-2010")

print "Title of publication: %s" % publication["title"]
print "Year of publicate: %s" % publication["year"]

print "Authors of this publication:"
for authorOfPublication in publication["authors"]:
    print "Fullname: %s, url: %s " % (authorOfPublication["person"]["fullname"],authorOfPublication["person"]["url"]) 
print "\n" * 2

#getBibliography example:
print("getBibliography(\"systematic-review\")")
bibliography = r.getBibliography("systematic-review")

print "Name of bibliography: %s" % bibliography["name"]
print "Number of founded publications: %s" % len(bibliography["publications"])
print "\n" * 2

#searchPublications example:
print "searchPublications(\"web+service\"),0"
publications = r.searchPublications("web+service",0)
publicationsPage2 = r.searchPublications("web+service", 2)

print "Page %s:" % publications["index"]
print "Kind: %s" % publications["kind"]
print "Number of results: %s" % len(publications["result"])
print "\n" 
print "searchPublications(\"web+service\",2)"
print "Page %s:" % publicationsPage2["index"]
print "Number of results: %s" % len(publicationsPage2["result"])
print "\n" * 2

#searchConferences example:
print("searchConferences(\"web+service\",2)")
conferences = r.searchConferences("web+service",0)
conferencesPage3 = r.searchConferences("web+service",3)
print "Page %s:" % conferences["index"]
print "Kind: %s" % conferences["kind"]
print "Number of results: %s" % len(conferences["result"])

print "Founded conferences on page 1:"
for conference in conferences["result"]:
    print "Country: %s" % (conference["country"]), 
print "\n" 
print "searchConferences(\"web+service\",3)"
print "Page %s:" % conferencesPage3["index"]
print "Number of results: %s" % len(conferencesPage3["result"])

