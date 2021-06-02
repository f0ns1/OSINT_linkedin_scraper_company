#!/usr/bin/python3
from linkedin_scraper import Person, actions,Company
from selenium import webdriver
import json
from json2html import *



def get_personal_data(person):
    try:
        #print(person)
        data = {}
        data['name'] = str(person.name)
        data['accomplishments'] = str(person.accomplishments)
        data['company'] = str(person.company)
        data['job_title'] = str(person.job_title)
        data['linkedin_url'] = str(person.linkedin_url)
        data['about'] = str(person.about)
        data['experiences'] = str(person.experiences)
        data['educations'] = str(person.educations)
        data['interests'] = str(person.interests)
        data['contacts'] = get_person_list(person.contacts)
        json_dump = json.dumps(data)
        html = json2html.convert(json=json_dump)
        #print(json_dump)
        print(html)
        write_report(html, str(person.linkedin_url).split("/")[4]+".html")
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
        #print(json_dump)
        print(html)
        write_report(html ,"campues_ciberseguridad.html")
    except ValueError:
        print(ValueError)

def write_report(data, name):
    with open(name, mode="w", encoding="utf8") as f:
        f.write(data)
        f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()
    email ="fonso.gonzalezsan@gmail.com"
    password = "mvpem.88"
    if len(sys.argv) == 5:
        email=sys.argv[1]
        password = sys.argv[2]
        if sys.argv[3] == 'company':
            actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal
            company = Company(sys.argv[4], driver=driver, scrape=True)
            get_company_data(company)
        elif sys.argv[3] == 'person':
            actions.login(driver, email, password)
            person = Person(sys.argv[4], driver=driver, scrape=True)
            get_personal_data(person)
    else:
        print("Usage: python3 program: email credentials comapny|person url")


