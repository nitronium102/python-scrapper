import os
import requests

def content() :
  os.system('clear')
  print("Welcome to IsItDown.py!")
  url = input("Please write a URL or URLs you want to check. (separated by comma)\n")
  split_url = url.split(",")
  s_url = []
  for each_url in split_url:
    replace_url = each_url.replace(" ", "")
    s_url.append(replace_url)

  for st_url in s_url :
    lower_url = st_url.lower()
    if ".com" not in lower_url:
      print(f"{lower_url} is not a valid syntax!")
    else :
      if lower_url.startswith("http://"):
        try :
          result = requests.get(lower_url)
          print(f"{lower_url} is up!")
        except : 
          print(f"{lower_url} is down!")
      else :
        ori_url = "http://" + lower_url
        try :
          result = requests.get(ori_url)
          print(f"{ori_url} is up!")
        except : 
          print(f"{ori_url} is down!")

def answer():
  ans = input("Do you want to start over? : ")
  up_ans = ans.upper()
  if up_ans == 'Y' or up_ans == 'YES' :
    content()
  elif up_ans == 'N' or up_ans == 'NO':
    print("k, bye!")
  else :
    print("That's not a valid answer")
    answer()

content()
answer()
  
