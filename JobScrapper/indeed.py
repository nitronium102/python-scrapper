import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  # pagination(soup) : find div, return class : pagination > url 다듬어서 필요한 링크 가져옴
  pagination = soup.find("div", {"class" : "pagination"})

  # 링크 안의 span을 추출
  links = pagination.find_all('a')

  # 링크 안의 span을 추출
  # remove the last one
  pages = []
  for link in links[:-1] :
    # span 찾아서 넣기
    pages.append(int(link.string))
    max_page = pages[-1]
  return max_page

def extract_job(html):
  title = html.find("h2", {"class" : "title"}).find("a")["title"]
  # find : first one
  company = html.find("span", {"class" : "company"})
  if company : 
    company_anchor = company.find("a")
    if company_anchor is not None : 
      company = str(company_anchor.string) # company has a link
    else : 
      company = str(company.string) # company doesn't has link
    company = company.strip() # 빈칸 비워준다
  else : 
    company = None

  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {
    'title' : title,
    'company' : company, 
    'location' : location, 
    'link' : f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
   }


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start = {page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    for result in results : 
        job = extract_job(result)
        jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs