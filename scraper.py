import requests
import json
from bs4 import BeautifulSoup

class Program:
    def __init__(self, title, desc):
        self.name = title
        self.desc = desc

def getDepartment(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    programs = soup.findAll('h4')
    desc = soup.findAll("div", {"class": "small content"})

    sep = 'mehr'
    campus = []
    
    i = 0

    for p in programs:
        title = p.text.strip()
        content = desc[i].text.split(sep, 1)[0].replace('\n',"").lstrip().rstrip()
        program = Program(title,content)
        campus.append(program)
        i = i + 1

    return campus

    
hagenberg = getDepartment('https://www.fh-ooe.at/en/hagenberg-campus/study/degree-programmes/v/sg/list/bachelor/all/all/9/all/')
linz = getDepartment('https://www.fh-ooe.at/en/linz-campus/study/degree-programmes/v/sg/list/bachelor/all/all/7/all/')
steyr = getDepartment('https://www.fh-ooe.at/en/steyr-campus/study/degree-programmes/v/sg/list/bachelor/all/all/8/all/')
wels = getDepartment('https://www.fh-ooe.at/en/wels-campus/study/degree-programmes/v/sg/list/bachelor/all/all/6/all/')



