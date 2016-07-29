#!/usr/bin/python 
# -*- coding:utf-8 -*-
import sys,os
import lxml
import urllib,urllib2
import loadfile
import framework
import time
today=time.strftime("%Y-%m-%d",time.localtime(time.time()))
tardict=loadfile.load('stock.conf')
for title,realvalue in tardict.items():
    for realurl in realvalue['url']:
        buf=framework.downurl(realurl)
        if buf:
            reslist=framework.jixx(buf,realvalue)
            for item in reslist:
                res='\t'.join(item)
                if res:
                    print res.strip()
        print
