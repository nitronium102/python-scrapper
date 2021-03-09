import os
import csv
import requests
from bs4 import BeautifulSoup

cell_name = ['NCI-H23', 'EKVX', 'NCI-H522', 'KM20L2', 'A549/ATCC', 'NCI-H322M', 'CCRF-CEM', 'SK-OV-3', 'NCI-H226', 'HOP-62', 'OVCAR-5', 'HCT-116', 'HT29', 'NCI-H460', 'NCI/ADR-RES', 'K-562', 'U251', 'RXF 393', 'HOP-18', 'DMS 114', 'LOX IMVI', 'DLD-1', 'HOP-92', 'Malme-3M', 'SW-620', 'HCC-2998', 'Hs 578T', 'HL-60(TB)', 'SNB-75', 'KM12', 'LXFL 529', 'SF-295', 'HCT-15', 'SK-MEL-28', 'IGROV1', 'T-47D', 'MCF7', 'MDA-MB-435', 'DMS 273', 'COLO 205', 'Calu-1', 'OVCAR-8', 'MDA-MB-231/ATCC', 'OVCAR-3', 'ACHN', 'RPMI-8226', 'OVCAR-4', 'DU-145', 'UO-31', 'UACC-62', 'SK-MEL-2', 'MOLT-4', 'SF-268', 'SK-MEL-5', 'BT-549', 'SNB-19', 'MDA-N', 'P388', 'TK-10', 'P388/ADR', 'SR', 'XF 498', 'A498', 'SN12C', 'SW-1573', 'MLI-019', '786-0', 'CAKI-1', 'UACC-257', 'LXFS 650L', 'RXF-631', 'MLI-076', 'SF-539', 'M14', 'MLI-045', 'RKOp53RE1', 'M19-MEL', 'UABLG22', 'PC-3', 'HT29p53RE22', 'HCT-116/P', 'SNB-78', 'H1299p53RE29', 'HCT-116/CMV-2', 'RKO Waf1', 'HCT-116/E6-1', 'HCT-116/CMV-1', 'HCT-116/E6-2', 'SK-BR-3', 'HCT-116/PV', 'HCT-116/P21/A', 'HCT-116/P21/B', 'COLO 741', 'HCT-116/P21/C', 'CXF 264L', 'MAXF 401', 'COLO 746', 'MDA-MB-468', 'SN12K1', 'T47D FOS1', 'T47D NFkB15', 'T47D ERE4', 'UISO-BCA-1', 'MCF7-E6', 'MDA-MB-435S', 'MLI-059', 'CACO-2', 'NB4', 'Mar-Bel', 'WI-38', 'UOK-57', 'CCD-19Lu', 'UOK-57LN', 'ZR-75-1', 'ZR-75-30', 'RPMI-7951', 'VDSO/P', 'MCF7/ATCC', 'VDSO/CMV-8', 'VDSO/CMV-9', 'VDSO/E6-18', 'VDSO/E6-19', 'NYH', 'NYH/ICRF-187-1', 'SW-156', 'CHO', 'TK-164', 'CHO/159-1', 'SF-767', 'SF-763', 'A431', 'OHS', 'A-Fos 2', 'RH18', 'A-Fos 3', 'DB', 'A-JUN 1', 'A-JUN 3', 'MEXF 514L', 'ES-2', 'A-C/EBP 3', 'A-CREB 1', 'TSU-PRI', 'A-CREB 2', 'HT', 'RL', 'RXF 486L', 'UABMEL3', 'JCA-1', 'ND-1', 'SW 1088', 'SW 1783', 'SMS-KCNR', 'A204/ATCC', 'A673', 'TE85', 'CHA-59', 'RH30', 'RD']
# file = open("./PythonHome/list.txt","r")
# cell_list = file.readlines()
# print(cell_list)
os.system("clear")

def write_company(each_cells, i):
  if i == 0 : 
    file = open("cell_line.csv", mode = "w")
  else : 
    file = open("cell_line.csv", mode = "a")
  writer = csv.writer(file)
  writer.writerow(["Cell_line", "name", "disease", "category"])
  for cell in each_cells :
    writer.writerow(list(cell.values()))
  return


def extract_info(html, word) :
  to_text = html.text
  to_list = to_text.split("\n")
  name = to_list[0]
  disease = to_list[11]
  category = to_list[12]
  return {
    "Cell_line" : word,
    "name" : name,
    "disease" : disease,
    "category" : category
  }

def extract_infos(link, word):
  each_cells = []
  result = requests.get(link)
  soup = BeautifulSoup(result.text, "html.parser")
  t_body = soup.find("div", {"class" : "s-results"}).find("div", {"class":"row"})
  rows = t_body.find_all("div", {"class" : "inner-results"})
  for row in rows:
    info = extract_info(row, word)
    each_cells.append(info)
  
  return each_cells

for i in range(len(cell_name)) :
  URL = f"https://scicrunch.org/resources/Cell%20Lines/search?q={cell_name[i]}&l={cell_name[i]}"
  print(f"getting {i}th cell")
  a = extract_infos(URL, cell_name[i])
  write_company(a, i)
