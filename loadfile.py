import sys,os

def load(filename):
    tardict={}
    for line in open(filename):
        line=line.strip()
        if not line:
            continue
        mylist=line.split('->')
        fis=mylist[0].strip()
        sec=mylist[1].strip()
        if fis == 'title':
            title=sec
            tardict[title]={}
        else:
            tardict[title][fis]=sec.split(',')
    return tardict

if __name__ == '__main__':
    tardict=load('stock.conf')
    
            
            

    
