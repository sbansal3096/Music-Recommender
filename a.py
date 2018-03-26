import requests as req 

from bs4 import BeautifulSoup 
import os
import os.path
import shutil
try:
	r1=req.get("https://gaana.com/playlist/gaana-dj-best-of-badshah")
	c1=r1.content

	soup1=BeautifulSoup(c1,"html.parser")
	F1=soup1.find_all("a",{"class":"sng_c "})
	#print(F1)
	namelist=[]
	#count=0
	for i in F1:
		print (i.text)
		x=i.text
		l=x.split()
		name=""
		url="https://www.youtube.com/results?search_query="
		for j in l:
			url=url+j+"+"
			name=name+j+"_"
		#print(":",url)
		url=url[:-1]
		name=name[:-1]
		namelist.append(name)
		#print(url,name)
		r2=req.get(url)
		c2=r2.content
		soup2=BeautifulSoup(c2,"html.parser")
		#F2=soup2.find_all("a",{"class":"yt-simple-endpoint"})
		#print(F2[0]['href'])
		#print(F2)
		
		#F2 = soup2.find_all('a',href=True)
		#print(link[40]['href'])
		F2 =soup2.findAll(attrs={'class':'yt-uix-tile-link'})
			

		
		link="https://www.youtube.com"+F2[0]['href']
		command="youtube-dl --extract-audio --audio-format mp3 "+link+" -o "+name+".mp3"
		os.system(command)

		

		#count=count+1
except req.exceptions.RequestException as e: 
    print (e)

'''
for n in namelist:
	if os.path.isfile(n):
		n=n+".mp3"
		src = n
		dst = 'data/romance/{}'.format(n)
		shutil.move(src, dst)


filelist=os.listdir('.')
for f in filelist:
	os.remove(f)

'''
