mResearchR
==========

Python API module for ResearchR.org

**Try it**

In ./bin/example/ you can find example app using researchr.py module.

**About**

Module have one class "ResearchrClass", this class have these methods:

**searchPublications(key, index)** - for search publications on researchr.org
searchPublications return dictionary.

- key: search term
- index: page of results (101 results on page)

using: 
 publications = r.searchPublications("web+service",0)

for more information: *https://merlin.fit.vutbr.cz/nlp-wiki/index.php/Rrs_researchr#Vyhled.C3.A1v.C3.A1n.C3.AD*




**searchConferences(key, index)** - for search conferences on researchr.org
searchConferences return dictionary.

- key: search term
- index: page of results (101 results on page)

using: 
 conferences = r.searchConferences("web+service",0)

for more information: *https://merlin.fit.vutbr.cz/nlp-wiki/index.php/Rrs_researchr#Vyhled.C3.A1v.C3.A1n.C3.AD*
