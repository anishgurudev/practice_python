

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

data = {'URL': [], 'Status Code': [], 'Validation Result': []}
# go through every url in the urls
for url in urls:
    data['URL'].append(url)
    # do the request for this url
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'Error while fetching URL {url}:', e)
    data['Status Code'].append(res.status_code)
    if 200 <= res.status_code <= 299 :
        print(res.url, end=" ")
        print(res.status_code, end=" ")
        print('Valid')
        data['Validation Result'].append('Valid')
    else :
        print('Invalid')
        data['Validation Result'].append('Invalid')
        print(res.raise_for_status())

# writing to Excel
data_to_excel = pd.ExcelWriter(excel_file,mode = "a")

#creating Dataframe
wf = pd.DataFrame(data)

# write DataFrame to excel
wf.to_excel(data_to_excel,sheet_name= 'Results4',index= False)

# save the excel
data_to_excel.close()



# print('DataFrame is written to Excel File successfully.')










