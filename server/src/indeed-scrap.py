import requests # http requests
from bs4 import BeautifulSoup # Webscrape
from collections import defaultdict # Default dictionary: store a list with each key
import pandas as pd     # DF

# this was used for the person contacting me who had these details for their system
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Skills & Place of Work
skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the # of pages to scrape: '))

indeed_posts=[]

for page in range(no_of_pages):
    # Connecting to India Indeed
        url = 'https://ca.indeed.com/jobs?q=' + skill + \
            '&l=' + place + '&sort=date' +'&start='+ str(page * 10)
        
        # Get request to indeed with headers above (you don't need headers!)
        response = requests.get(url, headers=headers)
        html = response.text

        # Scrapping the Web (you can use 'html' or 'lxml')
        soup = BeautifulSoup(html, 'lxml')

        # Outer Most Entry Point of HTML:
        outer_most_point = soup.find('div', attrs={'id': 'mosaic-provider-jobcards'})

        # Check if outer_most_point is not None
        if outer_most_point:
            # Find all <ul> elements within outer_most_point
            ul_elements = outer_most_point.find_all('ul')
            
            for i in ul_elements:
                # rest of the code
            # Job Title:
                job_title=i.find('h2',{'class':'jobTitle jobTitle-color-purple jobTitle-newJob'})
    #             print(job_title)
                if job_title != None:
                    jobs=job_title.find('a').text

                # Company Name:
                if i.find('span', {'class': 'companyName'}) != None:
                    company = i.find('span', {'class': 'companyName'}).text

                        
                # Links: these Href links will take us to full job description
                if i.find('a') != None:
                        links=i.find('a',{'class':'jcs-JobTitle'})['href']
                        
                # Salary if available:
                if i.find('div',{'class':'attribute_snippet'}) != None:
                        salary=i.find('div',{'class':'attribute_snippet'}).text

                else:
                        salary='No Salary'

                # Job Post Date:
                if i.find('span', attrs={'class': 'date'}) != None:
                        post_date = i.find('span', attrs={'class': 'date'}).text

                # Put everything together in a list of lists for the default dictionary
                indeed_posts.append([company,jobs,links,salary, post_date])
            
            
# put together in list

# (create a dictionary with keys and a list of values from above "indeed_posts")
indeed_dict_list=defaultdict(list)

# Fields for our DF 
indeed_spec=['Company','job','link','Salary','Job_Posted_Date']
# list of lists containing jobs with (company,job_title, href_link,salary,when job posted)
indeed_posts[0:2]
print(indeed_posts)