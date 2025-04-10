#Your task is to create a Python script that reads URLs from an Excel spreadsheet,
# makes HTTP requests to those URLs, fetches the responses, validates the responses,
# and stores the results in another Excel sheet.

import pandas as pd
import requests
from openpyxl.workbook import Workbook



excel_file = '/Users/anishkumar/PycharmProjects/PythonProjects/practice_python/Tests/S_test/URLs.xlsx'
import json

#reading from exel
df = pd.read_excel(excel_file,sheet_name= 'urls', usecols=['URL'] )
# print(df.at[0,'URL'])
# req = requests.get(df.at[0,'URL'])

# putting the urls from the sheet
urls = df.URL


data_dict = {}
main_lst = []
# go through every url in the urls
for url in urls:
    sub_lst=[]
    sub_lst.append(url)
    data_dict[url] = []



    # do the request for this url
    res = requests.get(url)
    data_dict[url].append(res.status_code)
    sub_lst.append(res.status_code)
    if 200 <= res.status_code <= 299 :
        print(res.url, end=" ")
        print(res.status_code, end=" ")
        print('Valid')
        data_dict[url].append('Valid')
        sub_lst.append('Valid')

    else :
        print('Invalid')
        data_dict[url].append('Invalid')
        sub_lst.append('Invalid')

        print(res.raise_for_status())

    mai
# writing to Excel
data_to_excel = pd.ExcelWriter(excel_file,mode = "a")

df1 = pd.DataFrame(data_dict ,)

# write DataFrame to excel
df1.to_excel(data_to_excel,sheet_name= 'Results1')

# save the excel
data_to_excel.close()



# print('DataFrame is written to Excel File successfully.')




