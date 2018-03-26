from PIL import Image
import os
from subprocess import run, PIPE
import pickle






def towav(input_file):
    name=input_file.replace('.wav','.mp3')
    command="ffmpeg -i "+input_file+" "+name
    os.system(command)
    os.remove(input_file)
    #return name

filelist=os.listdir('romance')
filelist.sort()

for i,file in enumerate(filelist):
    print(file)
    name="romance/"+file
    towav(name)













'''
os.system("ffmpeg -i Subhanallah.mp3 Subhanallah.wav")
os.system("sox Subhanallah.wav tmp.wav remix 1,2")
set_to_mono('Subhanallah.wav')
#os.system("ffmpeg -i Subhanallah.mp3 Subhanallah.wav")
os.system("sox Subhanallah.wav -n trim 20 180 spectrogram -Y 300 -X 50 -m -r -o Subhanallah.png")
slice_spect('Subhanallah.png')

#w,h=get_spect_dims(img)
#print(get_num_slices(w))
img=Image.open('Subhanallah.png')
#print(get_spect_dims(img))
w,h=get_spect_dims(img)
print(get_num_slices(w))

'''