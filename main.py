import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def get_alba_link():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("tbody").find("tr")
  superbrands = soup.find("div", {"id":"MainSuperBrand"})
  brands = superbrands.find("ul", {"class":"goodsBox"}).find_all("li", {"class" : "impact"})
  alba_link = []
  company_list = []
  for brand in brands :
    link = brand.find("a")["href"]
    company = brand.find("strong").string
    alba_link.append(link)
    company_list.append(company)
  return alba_link, company_list
  
# find url
def extract_info(html) : 
  try :
    place = html.find("td", {"class": "local first"}).get_text().replace("\xa0", " ")
  except :
    place = "None"
    
  title = html.find("span", {"class" : "company"})
  if title is not None :
    title = title.get_text(strip=True)
  else :
    title = "None"
  time = html.find("span", {"class" : "time"})
  if time is not None :
    time = time.get_text(strip=True)
  else :
    time = "None"
  pay = html.find("td", {"class":"pay"})
  if pay is not None :
    pay = pay.get_text(strip=True)
  else :
    pay = "None"
  date = html.find("td", {"class":"regDate last"})
  if date is not None :
    date = date.get_text(strip=True)
  else :
    date = "None"

  return {
    "place" : place,
    "title" : title,
    "time" : time,
    "pay" : pay,
    "date" : date
  }
 

def extract_jobs(links):
  jobs = []
  for i in range(len(links)):
    result = requests.get(f"{links[i]}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr")
    for result in results:
      job = extract_info(result)
      jobs.append(job)
    print(jobs)
    
    return jobs

def save_to_file(infos, company_list):
  for i in range(len(company_list)) : 
    file = open(f"{company_list[i]}.csv", mode = "w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for info in infos :
      writer.writerow(list(info.values()))
    return

def main():
  link_list, company_list = get_alba_link()
  infos = extract_jobs(link_list)
  infos = infos[1::2]
  save_to_file(infos, company_list)

main()