# This script would crawl the math genealogy project and extract all usesful information about a professor, given her ID
# The script would extract the following information
# - Name
# - School
# - Year
# - Dissertation



import requests
from bs4 import BeautifulSoup


def scrapeAdvisorDetails(id):
 
    URL = "https://mathgenealogy.org/id.php?id=" + id
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    advisor_details = soup.find_all('span')


    name = soup.findAll('h2')[0].get_text().strip()
    school = advisor_details[1].get_text().strip()
    year = advisor_details[0].get_text()[-4:].strip()
    dissertation = advisor_details[3].get_text().strip()

    return (name, school, year, dissertation)


id = '66476'
print(scrapeAdvisorDetails(id))