#!usr/bin/python

import xlrd
import urllib,urllib2
url1 = 'http://api.test.com/create'
xlsfile1 = r'D:\\py_workspace\\api.xlsx'
def api_info(url,data):
  url_value = urllib.urlencode(data)
  full_url = urllib2.Request(url,url_value)
  response = urllib2.urlopen(full_url)
  content = eval(response.read())
  code = content.get("code")
  return code
def excel_data(xlsfile):
  book = xlrd.open_workbook(xlsfile)
  api_sheet = book.sheet_by_index(0)
  nrows = api_sheet.nrows
  for i in range(1,nrows):
    client_id = api_sheet.cell(i,0)
    password = api_sheet.cell(i,1)
    sign = api_sheet.cell(i,2)
    ex_code = api_sheet.cell(i,3)
    if api_sheet.cell(i,0).ctype != 0:
      cv = str(int(client_id.value))
    else:
      cv = client_id.value
    pv = password.value
    sv = sign.value
    data1 = {'client_id':cv,'password':pv,'sign':sv}
    ac_code = api_info(url1,data1)
    if ac_code == ex_code.value:
      print "pass"
    else:
      print "fail"

excel_data(xlsfile1)