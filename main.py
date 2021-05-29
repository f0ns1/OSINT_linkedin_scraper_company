# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from linkedin_scraper import Person, actions,Company
from selenium import webdriver
import json
from json2html import *



def get_personal_data(person):
    try:
        print(person.contacts)
        print(person.name)
        print(person.driver)
        print(person.accomplishments)
        print(person.company)
        print(person.job_title)
        print(person.linkedin_url)
        print(person.about)
        print(person.experiences)
        print(person.educations)
        print(person.interests)
        print(person.accomplishments)
        print(person.driver)
        person.scrape(close_on_complete=True)
    except ValueError:
        print(ValueError)

def get_person_list(list):
    data={}
    count=0
    for person in list:
        print(person)
        data['person-'+str(count)] = str(person)
        count +=1
    return data
def get_company_data(company):
    try:
        data={}
        data['name'] = company.name
        data['linkedin_url'] = company.linkedin_url
        data['about_us'] = company.about_us
        data['website'] = company.website
        data['headquarters'] = company.headquarters
        data['affiliated_companies'] = company.affiliated_companies
        data['company_size'] = company.company_size
        data['company_type'] = company.company_type
        data['company_employees'] = get_person_list(company.employees)
        data['founded'] = company.founded
        data['industry'] = company.industry
        data['showcase_pages'] = company.showcase_pages
        data['website'] = company.showcase_pages
        json_dump = json.dumps(data)
        html = json2html.convert(json = json_dump)
        print(json_dump)
        print(html)
        write_report(html ,"ALTEN_OSINT.html")
    except ValueError:
        print(ValueError)

def write_report(data, name):
    with open(name, mode="w", encoding="utf8") as f:
        f.write(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()
    email ="yourEmail"
    password = "your credentials"
    actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal
    company = Company("https://www.linkedin.com/company/alten", driver=driver, scrape=True)
    print(company)
    get_company_data(company)

