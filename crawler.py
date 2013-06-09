#!/usr/bin/env python3.2
import urllib.request
import string

import queue

def add_links(st,q):
  dat=st.split('\n')
	black=('feed','.','#')
	for s in dat:
		if 'http://www.geeksforgeeks.org/' in s:
			link=s.partition('href="http://www.geeksforgeeks.org/')
			l,p,link=link[2].partition('"')
			if 'feed' not in l and '.' not in l and '#' not in l and l != None:
				q.put('http://www.geeksforgeeks.org/'+l)
			

def format_string(data,name):
	dat=data.split('\n')
	b=False;
	r=''
	for s in dat :
		if '<p>' in s:
			b=True
		if b==True:
			r=r+'\n'+s
		if '<\p>' in s:
			b=False
			
	return r
   
def main():
	q=queue.Queue()
	url = 'http://www.geeksforgeeks.org/amazon-interview-set-33/'
	q.put(url)
	lst=[]
	while(not q.empty()):
		url=q.get()
		if url in lst:
			continue
		lst.append(url)
		request = urllib.request.Request(url)
		request.add_header("User-Agent", "My Crawler")
		opener = urllib.request.build_opener()
		f = opener.open(request)
		#f = urllib.request.urlopen(url)
		st = f.read().decode('utf-8');
		add_links(st,q)
		filename = url.partition('org/')
		filename,fil,fi = filename[2].partition('/')
		write_this = '<html> \n <head> ' + filename + ' \n <title>' +  filename +' </title>\n</head>\n <body>\n'
		st=write_this + format_string(st,url) + '</body>';
		fobj=open(filename,'w')
		fobj.write(st)
		fobj.close()
		print(filename+'\n')
	return 0

if __name__ == '__main__':
	main()
	
