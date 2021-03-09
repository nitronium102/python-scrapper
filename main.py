import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def get_info(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  table = soup.find("table", {"class" : "table"}).find("tbody").find_all("tr")

  each_table = []

  for i in table : 
    country, currency, code, number = i.find_all("td", reculsive=False)

    if "No universal currency" in currency :
      each_table = each_table
    else : 
      each_table.append({
        "country": country.text, 
        "currency" : currency.text, 
        "code" : code.text, 
        "number" : int(number.text)
        })

  # enumerate : 순서가 있는 자료형, index와 value 반환
  for idx, i in enumerate(each_table, start=0):
    i["index"] = int(idx) # index 표시

  return each_table

def ans_input(table):
  ans = int(input("# : "))
  try :
    if ans <= len(table) :
      print(f"You choose {table[ans]['country']}")
      print(f"The currency code is {table[ans]['code']}")
    else :
      print("Choose a number from the list")
      ans_input(table)
  except :
    print("That wasn't a number")
    ans_input(table)

def main(URL):
  print("Hello! Please choose select a country by number")
  table = get_info(URL)
  for i in table :
    print("#", i["index"], i["country"])
  
  # print(table)
  ans_input(table)

main(url)