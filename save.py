import os
from mutagen.mp3 import MP3

filelist=os.listdir('party')


for f in filelist:
	print(f)
	#audio=MP3("romance/"+f)

	if os.path.getsize('party/'+f)/1000000 >8 :
		os.remove('party/'+f)
		print('deleted')

