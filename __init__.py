"""
crawl stock information

author:lucky
date:2017-04-20


…or create a new repository on the command line

echo "# yahoo-crawler" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/nofounture/yahoo-crawler.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin https://github.com/nofounture/yahoo-crawler.git
git push -u origin master

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
"""
import httplib2
import re

url = "https://finance.yahoo.com/quote/NLY?p=NLY"
h = httplib2.Http(".cache")
response, content = h.request("https://finance.yahoo.com/quote/NLY?p=NLY", "GET")
# rs = re.findall("\"preMarketPrice\": \{\"raw\": (.*), \"fmt\": \"(.*)\"}", content.decode("utf-8"))
#match the present price
rs = re.findall("\"preMarketPrice\":\{\"raw\":(\d+\.\d+)\,\"fmt\"", content.decode("utf-8"),re.DOTALL)
#TODO store the result into the database
#11.73
print(rs[0])
