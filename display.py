import requests
url= 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'

response=requests.get(url)
if response.status_code==200:
    print("下載成功")
    weather=response.json