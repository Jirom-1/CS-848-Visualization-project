#This script is designed to scrape the CS Uwaterloo website to extract all professors and their specializations
# The information extracted would be
# - Name
# - Specialization
# - Website


from importlib.metadata import packages_distributions
import requests
from bs4 import BeautifulSoup
import pandas as pd

specializations = ['algorithms-and-complexity', 'artificial-intelligence-and-machine-learning', 'bioinformatics',
'computer-algebra-and-symbolic-computation', 'computer-graphics', 'cryptography-security-and-privacy-crysp',
'data-systems', 'formal-methods', 'health-informatics',' human-computer-interaction-hci', 'programming-languages',
'quantum-computing', 'scientific-computation', 'software-engineering', 'systems-and-networking']

def scrapeCSProfessors(specialization):
    columns = ['Name', 'Specialization']
    professors = pd.DataFrame(columns=columns)
    url = "https://cs.uwaterloo.ca/research/research-areas/" + specialization
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    professor_lists = soup.findAll("div", {"class": "col-50"})
    index = 0
    for professor_list in professor_lists:
        for professor in str.split(professor_list.get_text().strip().replace("\t",""), "\n"):
            professor_info = {'Name' : professor, 'Specialization' : specialization }
            professor_info = pd.DataFrame(data=professor_info, index = [i])
            professors = pd.concat([professors, professor_info])
            index += 1

    return  professors
            


columns = ['Name', 'Specialization']
professors = pd.DataFrame(columns=columns)
for i in range(len(specializations)):
    (professor_info) = scrapeCSProfessors(specializations[i])
    professors = pd.concat([professors, professor_info])
    professors.to_csv('cs_professors.csv')

