"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(list_name, item):
  if (item in list_name):
    return True
  else :
    return False

def get_x(list_name, idx):
  idx = int(idx)
  return list_name[idx]

def add_x(list_name, new):
  list_name.append(new)

def remove_x(list_name, bye):
  list_name.remove(bye)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #




