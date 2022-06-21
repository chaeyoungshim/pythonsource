# train.xlsx

from numpy import record
from openpyxl import load_workbook
import re

path = "./rpabasic/crawl/download/"
wb = load_workbook(path + "train.xlsx")
ws = wb.active

pattern = re.compile(" Mr\.")
for each_row in ws.rows:
    print(each_row[3].value)
    if len(pattern.findall(each_row[3].value)) > 0:
        print(each_row[3].value)

# pattern = re.compile(" [A-Za-z]+\.")

# Name 출력 - Brand, Mr. Owen Narris, Cumings, Mrs. John Bradley
# for each_row in ws.rows:
#     print(each_row[3].value)
#     print(pattern.findall(each_row[3].value))
# print(pattern.search(each_row[3].value).group())
