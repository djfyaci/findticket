#coding:utf-8
import requests
import json
import smtplib
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def spider():
    user_agent = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")
    headers = {"User-Agent":user_agent,
                "Referer":'https://app.yinxiang.com/OutboundRedirect.action?dest=https%3A%2F%2Fkyfw.12306.cn%2Fotn%2FleftTicket%2FqueryA%3FleftTicketDTO.train_date%3D2017-01-01%26leftTicketDTO.from_station%3DBJP%26leftTicketDTO.to_station%3DXNO%26purpose_codes%3DADULT',
                "Host":"kyfw.12306.cn",
                'Connection':'keep-alive',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding':'gzip, deflate, sdch, br',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Cache-Control':'max-age=0',
                'Upgrade-Insecure-Requests':'1',
                'Cookie':'JSESSIONID=AFF2EED9DBE70BEE23748CB6D4CBD424; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u897F%u5B81%2CXNO; _jc_save_fromDate=2017-01-01; _jc_save_toDate=2016-12-20; _jc_save_wfdc_flag=dc; BIGipServerotn=116392458.50210.0000'
                }
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2017-01-01&leftTicketDTO'\
        '.from_station=BJP&leftTicketDTO.to_station=XNO&purpose_codes=ADULT'
    url1 = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-12-30&from_station=NJH&to_station=SHH'
    payload = {'leftTicketDTO.train_date':'2017-01-01', 'leftTicketDTO.from_station':'BJP','leftTicketDTO.to_station':'XNO','purpose_codes':'ADULT'}
    r = requests.get(url, headers, params=payload, verify=False)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    print r.content

def sendmail():
    pass

def main():
    pass

def test():
    spider()

if __name__ == '__main__':
    test()
