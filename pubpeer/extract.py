# extract html wget "https://pubpeer.com/api/search/?q=Mycosphaerella+arachidis&from=40"
#
# make a loop to get all .. by step 40 ?
# you will get 
#   'index.html?q=Mycosphaerella+arachidis'          
# ....
# 'index.html?q=Mycosphaerella+arachidis&from=120' 
#
# after get all pubpeer page from html

"""
use this script to get all independante page with comment.
import json
import sys
import pprint

for n in range(1, len(sys.argv)):
  with open(sys.argv[n]) as f:
    d = json.load(f)
    for j in d["publications"]:
       print("wget \"https://pubpeer.com/publications/%s\" " % j["pubpeer_id"])
"""


import json
from bs4 import BeautifulSoup
import sys
import os

def parsefile(html_file):
    # Lire le contenu HTML
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Extraction des données
    result = {
        "data_publication": [],
        "publication_authors": [],
        "comments": []
    }

    # Extraction des attributs "data-publication" et "publication-authors"
        
    for tag in soup.find_all(attrs={":data-publication": True}):
        print("****")
        #if tag[":data-publication"] == "[]":
        #    continue
        try :
        #print(tag[":data-publication"])
        #print(json.loads(tag[":data-publication"]))
            result["data_publication"].append(json.loads(tag[":data-publication"]))
        except Exception as e:
            pass
        #result["data_publication"].append(json.loads(tag[":data-publication"]))
        #result["data_publication"].append(tag[":data-publication"])

    for tag in soup.find_all(attrs={":authors": True}):
        try :
            result["publication_authors"].append(json.loads(tag[":authors"]))
        except Exception as e:
            pass

    for tag in soup.find_all(attrs={":data-comments": True}):
        try :
            result["comments"].append(json.loads(tag[":data-comments"]))
        except Exception as e:
            pass


    # Sauvegarde dans un fichier JSON bien formaté
    with open("json/%s.json" % (html_file) , "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Extraction terminée. Résultat dans 'extraction_result.json'")


# do this script.py pubpeer/* if you store all wget in pubpeer directory.
# after mkdir in pubpeer a json dir


for n in range(1,len(sys.argv)):
    if os.path.isdir(sys.argv[n]):
        continue
    parsefile(sys.argv[n])
