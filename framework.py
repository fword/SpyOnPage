import sys,os
import urllib,urllib2
from lxml import etree
import socket
import traceback
import time
socket.setdefaulttimeout(5)
def jixx(content,mydict):
    res=[]
    tree=etree.HTML(content)
    try:
        for i in range(1,int(mydict['num'][0])+1):
            aa=[]
            for item in mydict['pattern']:
                if item.find('%d')!=-1:
                    r = tree.xpath(item%i)
                else:
                    r = tree.xpath(item)
                if len(r):
                    if mydict['type'][0].strip()=='text':
                        if r[0].text:
                            aa.append(r[0].text.encode('utf-8').strip())
                    else:
                        fmat=mydict['type'][0].strip()
                        aa.append(r[0].get(fmat).encode('utf-8').strip())

                    #aa.append(kks+r[0].get('href').encode('utf-8').strip())
            res.append(aa)
        
        #print tar
        return res
    except:
        traceback.print_exc()
        return res
def downurl(tarurl):
    for i in range(3):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,         like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
            req = urllib2.Request(url=tarurl,headers=headers)
            content =urllib2.urlopen(req, timeout=5).read()
            return content
        except:
            traceback.print_exc()
            pass
