import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
code_url = "https://www.iban.com/currency-codes"
currency_url = "https://transferwise.com/gb/currency-converter/"

code_request = requests.get(code_url)
code_soup = BeautifulSoup(code_request.text, "html.parser")

code_table = code_soup.find("table", {"class" : "table"}).find("tbody").find_all("tr")

each_table = []

for i in code_table : 
  country, currency, code, number = i.find_all("td", reculsive=False)

  if "No universal currency" in currency :
    each_table = each_table
  else : 
    each_table.append({"country": country.text, "currency" : currency.text, "code" : code.text, "number" : int(number.text)})

  # enumerate : 순서가 있는 자료형, index와 value 반환
for idx, i in enumerate(each_table, start=0):
  i["index"] = int(idx) # index 표시

def ans_country(text):
  print(text)
  ans = int(input("# : "))
  try :
    if ans <= len(each_table) :
      print(f"{each_table[ans]['country']}")
      return each_table[ans]
    else :
      print("Choose a number from the list")
      return ans_country(text)
  except :
    print("That wasn't a number")
    return ans_country(text)

def ask_amount(country1, country2) :
  try : 
    print(f"\nHow many {country1['code']} do you want to convert to {country2['code']}")
    want_amount = int(input())
    return want_amount
  except ValueError :
    print("That wasn't a number")
    return ask_amount(country1, country2)


print("Welcome to CurrencyConvert PRO 2000")
for i in each_table :
  print("#", i["index"], i["country"])
user_country = ans_country("Where are you from? Choose a country by number")
target_country = ans_country("Now choose another country")

from_code = user_country['code']
to_code = target_country['code']

amount = ask_amount(user_country, target_country)

currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}")
currency_soup = BeautifulSoup(currency_request.text, "html.parser")

result = currency_soup.find("input", {"id" : "cc-amount-to"})
print(result)
if result :   
  result = result['value'] 
  amount = format_currency(amount, from_code, locale = "ko_KR" )
  result = format_currency(result, to_code, locale = "ko_KR" )
  print(f"{amount} is {result}")




# currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}")
# currency_soup = BeautifulSoup(currency_request.text, "html.parser")
# result = currency_soup.find("input", {"id":"cc-amount-to"})
# if result:
#  result = result['value']
#  amount = format_currency(amount, from_code, locale="ko_KR")
#  result = format_currency(result, to_code, locale="ko_KR")
#  print(f"{amount} is {result}")
