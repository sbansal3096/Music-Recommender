import os, fnmatch
import difflib

def find(pattern):
    result = []
    path='/home/shubham/Documents/projects/MUSIC/party'
    for root, dirs, files in os.walk(path):
        for name in files:
            d = difflib.SequenceMatcher(None,name, pattern).ratio()
            if d>=0.3:
                result.append(os.path.splitext(name)[0])

    path='/home/shubham/Documents/projects/MUSIC/romance'
    for root, dirs, files in os.walk(path):
        for name in files:
            d = difflib.SequenceMatcher(None,name, pattern).ratio()
            if d>=0.3:
                result.append(os.path.splitext(name)[0])
            #print(name)
    return result[:10]

#print(find('dil'))