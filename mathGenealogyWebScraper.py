# This script would crawl the math genealogy project and extract all usesful information about a professor, given her ID
# The script would extract the following information
# - Name
# - School
# - Year
# - Dissertation
import requests
from bs4 import BeautifulSoup



def scrapeAdvisorIDs(professor_id):
    # return the ID(s) of a professor's advisor(s)
    URL = "https://mathgenealogy.org/id.php?id=" + professor_id
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')

    # find all IDs on the webpage except the chronological one
    ids = []
    for link in soup.find_all('a'):
        if link.get('href') is not None and 'id.php?id' in link.get('href') and 'Chrono' not in link.get('href'):
            ids.append(link.get('href').split('=')[1])
    # print(ids)

    # find all IDs in a table (those are students)
    try:
        trs = soup.find_all('tr')
        student_ids = []
        for tr in trs:
            if tr.find('a'):
                student_ids.append(tr.find('a').get('href').split('=')[1])
        # print(student_ids)
    except:
        student_ids = []

    # return set difference as list
    return list(set(ids) - set(student_ids))


def scrapeProfessorDetails(ids):
    # return the name, school, and year of a professor
    names = []
    schools = []
    years = []
    for id in ids:
        URL = "https://mathgenealogy.org/id.php?id=" + id
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        professor_details = soup.find_all('span')


        names.append(soup.findAll('h2')[0].get_text().strip())
        schools.append(professor_details[1].get_text().strip())
        years.append(professor_details[0].get_text()[-4:].strip())

    return (names, schools, years)


# id = '151763'
# print(scrapeAdvisorIDs(id))