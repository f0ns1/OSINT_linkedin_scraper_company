# OSINT_linkedin_scraper_company


You must follow the installation and configuration instructions of: 
https://pypi.org/project/linkedin-scraper/

Abaut selenium web driver and linkedin scraper library
I should modify a little bit the source code of libary on the company.py class in order to obtain better results on the final HTML report for the OSINT personal tool:


      def __parse_employee__(self, employee_raw):
            try:
                linkedin_url=None
                name=None
                possition = None
                try:
                    name = (employee_raw.text.split("\n") or [""])[0].strip()
                    possition = (employee_raw.text.split("\n") or [""])[1].strip()
                    tag = employee_raw.find_element_by_tag_name("a")
                    tag = employee_raw.find_element_by_tag_name("div")
                    linkedin_url = employee_raw.parent.find_element_by_tag_name("a").get_attribute("href")
                except:
                    pass
                return Person(
                    linkedin_url,
                    name+": "+possition,
                    driver = self.driver,
                    get = False,
                    scrape = False
                    )
            except:
                return None
                
                
 
