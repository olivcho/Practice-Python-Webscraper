#Insignificant edit at 7:49 1/30

# To scrape job listings from fake website

'''
Base URL: https://realpython.github.io/fake-jobs/
Specific Location: https://realpython.github.io/fake-jobs/jobs/legal-executive-2.html
Appends: jobs/job-name.html
'''

#requests --> requesting data from website
#BeautifulSoup --> html data parsing library
import requests
from bs4 import BeautifulSoup

#takes a url, requests html/background info, and turns it into an object
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL, timeout=5)

#prints all html text
# print(page.text)

#creates a beautifulsoup object from "page" and uses sets up html parser as the object's parser
soup = BeautifulSoup(page.content, "html.parser")

'''
<h2 class="title is-5">Senior Python Developer</h2>
<h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
<p class="location">Stewartbury, AA</p>
'''

results = soup.find(id = "ResultsContainer")
#prettify adds html spacing to "results"
# print(results.prettify())

#finds job elements
job_elements = results.find_all("div", class_="card-content")
#prints each job element with spaces after
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
    
#goes through each job element and returns title, company, and location for each
for job_element in job_elements:
    title = job_element.find("h2", class_= "title")
    company = job_element.find("h3", class_= "subtitle")
    location = job_element.find("p", class_= "location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()

def job_search():

    job_tag = input("Input job tag: ").lower()

    #searches through jobs and returns a list of all matches with job_tag 
    python_jobs = results.find_all(
            "h2", string=lambda text: job_tag in text.lower()
        )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]
    for job_element in python_job_elements:
        links = job_element.find_all("a")
        #prints each individual python job from the python job list
        link = links[1]
        print(job_element.find("h2", class_= "title").text + ":")
        #"href" attribute finds the url link
        link_url = link["href"]
        #prints the url link -- f tells Python to take characters between {} as literal values
        print(f"Apply here: {link_url}\n")
    
    if len(python_jobs) == 0:
        return("did not work")
    
while job_search() == "did not work":
    print("Invalid tag")
    job_search()
