#coding:utf-8

import time
import threading
import random
from urllib import request
from time import sleep
import re
import os

#设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
import socket
socket.setdefaulttimeout(3)

outFile = "ip_proxy.txt"
checkip_url = "http://www.xinshangmeng.com/xsm2/?Version=2018090100"
checkip_url = "https://www.baidu.com"

header_selfdefine = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}

httpResult=[]
httpsResult=[]
httpResult_check=[]
httpsResult_check=[]

def get_ip():
    #获取代理IP，返回列表
    http_tmp=[]
    https_tmp=[]
    try:
        for page in range(1,2):
            req = request.Request('http://www.xicidaili.com/nn/%s'%page)
            req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
            resp = request.urlopen(req)
            IPContent=resp.read().decode('UTF-8')
            trs_str = re.findall(r'<tr.*?>(.*?)</tr>',IPContent, re.S)
        
            for tr_str in trs_str[1:]:
                tds_str = re.findall(r'<td.*?>(.*?)</td>',tr_str, re.S)
                ip = tds_str[1].strip()
                port = tds_str[2].strip()
                protocol = tds_str[5].strip()
                if protocol == 'HTTP':
                    http_tmp.append( 'http://' + ip + ':' + port)
                elif protocol =='HTTPS':
                    https_tmp.append( 'https://' + ip + ':' + port)
            sleep(2)
    except:
        pass
        print('get_ip error')
    return http_tmp,https_tmp
def get_ip2():
    #获取代理IP，返回列表
    http_tmp=[]
    https_tmp=[]
    try:
        for page in range(1,2):
            req = request.Request('https://www.kuaidaili.com/free/inha/%s'%page)
            req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
            resp = request.urlopen(req)
            IPContent=resp.read().decode('UTF-8')
            trs_str = re.findall(r'<tr.*?>(.*?)</tr>',IPContent, re.S)
        
            for tr_str in trs_str[1:]:
                tds_str = re.findall(r'<td.*?>(.*?)</td>',tr_str, re.S)
                ip = tds_str[0].strip()
                port = tds_str[1].strip()
                protocol = tds_str[3].strip()
                if protocol == 'HTTP':
                    http_tmp.append( 'http://' + ip + ':' + port)
                elif protocol =='HTTPS':
                    https_tmp.append( 'https://' + ip + ':' + port)
            sleep(2)
    except:
        pass
        print('get_ip2 error')
    return http_tmp,https_tmp

def get_ip3():
    #获取代理IP，返回列表
    http_tmp=[]
    https_tmp=[]
    try:
        for page in range(1,10):
            req = request.Request('http://www.ip3366.net/free/?stype=1&page=%s'%page)
            req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
            resp = request.urlopen(req)
            IPContent=resp.read().decode('gb2312')
            trs_str = re.findall(r'<tr.*?>(.*?)</tr>',IPContent, re.S)
        
            for tr_str in trs_str[1:]:
                tds_str = re.findall(r'<td.*?>(.*?)</td>',tr_str, re.S)
                ip = tds_str[0].strip()
                port = tds_str[1].strip()
                protocol = tds_str[3].strip()
                if protocol == 'HTTP':
                    http_tmp.append( 'http://' + ip + ':' + port)
                elif protocol =='HTTPS':
                    https_tmp.append( 'https://' + ip + ':' + port)
            sleep(2)
    except:
        pass
        print('get_ip2 error')
    return http_tmp,https_tmp

def get_ip_from_file():
    #获取代理IP，返回列表
    http_tmp=[]
    https_tmp=[]
    try:
        fs=open(outFile,'r')
        proxy_ls=fs.read().split('\r\n')
        fs.close()
        for proxt_data in proxy_ls:
            if 'http:' in proxt_data:
                http_tmp.append( proxt_data)
            elif 'https:' in proxt_data:
                https_tmp.append( proxt_data)
    except:
        pass
        print('get_ip_from_file error')
    return http_tmp,https_tmp


def open_url(url_addr,proxy_type,proxy_addr,time=3):
    req = request.Request(url=url_addr)
    req.set_proxy(proxy_addr,proxy_type)
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
    page=request.urlopen(req,timeout=time)
    page.read()
#验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页 http
def cip(x,y):
    global httpResult_check
    proxy_str=x+':'+y
    try:
        #print (proxy_str)
        open_url('http://www.pconline.com.cn/','http',proxy_str)
        open_url('http://www.xinshangmeng.com/','http',proxy_str)
        open_url('http://www.tuniu.com/','http',proxy_str)

        httpResult_check.append('http://' + proxy_str)
    except:
        x=1
        #print('cip error')
    else:
        print('---------------------------cip success '+ proxy_str)
    
#验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页。https
def csip(x,y):
    global httpsResult_check
    proxy_str=x+':'+y
    try:
        #print (proxy_str)
        open_url('https://www.baidu.com/','https',proxy_str)
        open_url('https://ip.cn/','https',proxy_str)
        httpsResult_check.append('https://' + proxy_str)
    except:
        x=1
        #print('csip error')
    else:
        print('---------------------------csip success ' + proxy_str)



def main():
    global httpResult
    global httpsResult
    global httpResult_check
    global httpsResult_check
	
    #http_tmp,https_tmp=get_ip_from_file()
    #httpResult[len(httpResult):]=http_tmp
    #httpsResult[len(httpsResult):]=https_tmp

    #http_tmp,https_tmp = get_ip()
    #httpResult[len(httpResult):]=http_tmp
    #httpsResult[len(httpsResult):]=https_tmp

    #http_tmp,https_tmp = get_ip2()
    #httpResult[len(httpResult):]=http_tmp
    #httpsResult[len(httpsResult):]=https_tmp
	
    http_tmp,https_tmp = get_ip3()
    httpResult[len(httpResult):]=http_tmp
    httpsResult[len(httpsResult):]=https_tmp

    httpResult=list(set(httpResult))
    httpsResult=list(set(httpsResult))

    print('finish get_ip')
    #print(httpResult)
    #print(httpsResult)
    threads = []
    #open(outFile,"a").truncate()
    for i in httpResult:
        a = str(i.split(":")[-2][2:].strip())
        b = str(i.split(":")[-1].strip())
        t = threading.Thread(target=cip,args=(a,b,))
        threads.append(t)

    for i in range(len(httpResult)):
        threads[i].start()  
    for i in range(len(httpResult)):
        threads[i].join()
    print('finish cip')


    threads1 = []
    #open(outFile,"a").truncate()
    for i in httpsResult:
        a = str(i.split(":")[-2][2:].strip())
        b = str(i.split(":")[-1].strip())
        t = threading.Thread(target=csip,args=(a,b,))
        threads1.append(t)

    for i in range(len(httpsResult)):
        threads1[i].start()  
    for i in range(len(httpsResult)):
        threads1[i].join()
    print('finish csip')

    proxy_now=[]
    if os.path.exists(outFile) == True:
    	fs=open(outFile,'r')
    	proxy_now=fs.read().split('\n')
    	fs.close()
    for addr in httpResult_check:
        print(addr)
        proxy_now.append(addr.strip())
    for addr in httpsResult_check:
        print(addr)
        proxy_now.append(addr.strip())
    
    proxy_now=list(set(proxy_now))
    proxy_now.sort()
    print(proxy_now)
    fs=open(outFile,'w')
    for addr in proxy_now:
    	fs.write(addr+'\r\n')
    fs.close()

def test_cip():
    print(1)
    req = request.Request(url='https://ip.cn/')
    #req = request.Request(url='http://2018.ip138.com/ic.asp')
    #req = request.Request(url='http://www.8684.cn/ip')
    #req = request.Request(url='https://www.baidu.com/')
    #req.set_proxy('218.14.115.211:3128','http') #普通代理
    req.set_proxy('118.190.95.35:9001','http') #高匿代理

    #req.set_proxy('106.75.164.15:3128','https') #高匿代理
    
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')

    page=request.urlopen(req)
    #print(page.read().decode('utf-8'))
    print(page.read().decode('gbk'))


if __name__ == '__main__':
    main()
    #get_ip()
    
    #cip('118.190.95.35','9001')
    #test_cip()