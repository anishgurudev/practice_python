#Your task is to create a Python script that reads URLs from an Excel spreadsheet,
# makes HTTP requests to those URLs, fetches the responses, validates the responses,
# and stores the results in another Excel sheet.

import pandas as pd
import requests



excel_file = '/Users/anishkumar/PycharmProjects/PythonProjects/practice_python/Tests/S_test/URLs.xlsx'
import json

#reading from exel
df = pd.read_excel(excel_file,sheet_name= 'urls', usecols=['URL'] )

# putting the urls from the sheet
urls = df.URL

# creating data dictionary for output
data = {'URL': [], 'Status Code': [], 'Validation Result': []}

# go through every url in the urls
for url in urls:
    data['URL'].append(url)
# handling the RequestException for the response status code
    try:
        res = requests.get(url)
        data['Status Code'].append(res.status_code)
    except requests.exceptions.RequestException as e:
        print(f'Error while fetching URL {url}:', e)
# validating the response code
    if 200 <= res.status_code <= 299 :
        print(res.url, end=" ")
        print(res.status_code, end=" ")
        print('Valid')
        data['Validation Result'].append('Valid')
    else :
         print('Invalid')
         data['Validation Result'].append('Invalid')
         print(res.raise_for_status())


# modifying to Excel
data_to_excel = pd.ExcelWriter(excel_file,mode = "a")

# creating Dataframe to enter data
wf = pd.DataFrame(data)

# write DataFrame to excel
wf.to_excel(data_to_excel,sheet_name= 'Results8',index= False)

# save the excel
data_to_excel.close()

print('DataFrame is written to Excel File successfully.')










