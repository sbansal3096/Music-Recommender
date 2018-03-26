from PIL import Image
import os
from subprocess import run, PIPE
import pickle
import os.path


DEFAULT_IMG_SIZE = 256
DATA_DIR = '../data/party/'
genre='party'






def delete_file(file_path):
    os.remove(file_path)



def get_spect_dims(input_img):
	img_width, img_height = input_img.size
	return img_width, img_height

def get_num_slices(img_width):
    n_slices = img_width // 256
    return n_slices

def get_slice_dims(input_img):
    img_width, img_height = get_spect_dims(input_img)
    num_slices = get_num_slices(img_width)
    unused_size = img_width - (num_slices * DEFAULT_IMG_SIZE)
    start_px = 0 + unused_size
    image_dims = []
    for i in range(num_slices):
        img_width = DEFAULT_IMG_SIZE
        image_dims.append((start_px, start_px + DEFAULT_IMG_SIZE))
        start_px += DEFAULT_IMG_SIZE
    return image_dims

def slice_spect(input_file):
    input_file_cleaned = input_file.replace('.png','')
    img = Image.open(input_file)
    dims = get_slice_dims(img)
    counter = 0
    for dim in dims:
        counter_formatted = str(counter).zfill(3)
        img_name = '{}_{}.png'.format(input_file_cleaned, counter_formatted)
        start_width = dim[0]
        end_width = dim[1]
        sliced_img = img.crop((start_width, 0, end_width, DEFAULT_IMG_SIZE))
        sliced_img.save(DATA_DIR + img_name)
        counter += 1
    delete_file(input_file)

#img=Image.open('O_Saiyyan.png')
#print(get_spect_dims(img))
def tospect(input_file,id):
	name=genre+'_'+str(id)+'.png'
	command="sox "+input_file+" -n trim 10 180 spectrogram -Y 300 -X 50 -m -r -o "+name
	os.system(command)
	return name

def towav(input_file):
	name=input_file.replace('.mp3','.wav')
	command="ffmpeg -i "+input_file+" "+name
	os.system(command)
	os.remove(input_file)
	return name

def tomono(input_file):
	
	temp='tmp.wav'
	command="sox "+input_file+" "+temp+" remix 1,2"
	os.system(command)
	if os.path.isfile(temp):
		os.remove(input_file)
		os.rename(temp,input_file)
	

filelist=os.listdir('.')
filelist.remove('preprocess.py')
filelist.sort()
songlist=[]



i=0
for file in filelist:
	print(file)

	filename=towav(file)
	tomono(filename)
	spect=tospect(filename,i)
	img=Image.open(spect)
	w,h=get_spect_dims(img)
	n=get_num_slices(w)
	if(n==35):
		slice_spect(spect)
		name=filename.replace('.wav','')
		songlist.append(name)
		i=i+1
	else:
		os.remove(filename)



with open("party_list", "wb") as d:
	pickle.dump(songlist, d)





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