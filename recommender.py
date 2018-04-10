import os
import glob
import numpy as np
import pickle as pkl
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def ret_name(st):

    np_arrays = np.load('finaldata.npy')
    with open('finaldata.pkl', 'rb') as handle:
        song_ids = pkl.load(handle)

    np_arrays.shape
    len(song_ids)
    cs = cosine_similarity(np_arrays)
    dists = pd.DataFrame(cs, columns=song_ids)
    dists.index = dists.columns
    #dists.head()
    import pickle
    with open('romance_list', 'rb') as f:
        romance = pkl.load(f)

    romance=romance[:100]

    import pickle
    with open('party_list', 'rb') as f:
        party = pkl.load(f)

    party=party[:100]
    data=romance+party

    selected_song_id = st

    recommendations = dists[str(selected_song_id)].sort_values(ascending=False).reset_index()
    list=[]
    for i in range(0,10):
        list.append(data[int(recommendations['index'][i])])
    return list


def ret_id(st):

    np_arrays = np.load('finaldata.npy')
    with open('finaldata.pkl', 'rb') as handle:
        song_ids = pkl.load(handle)

    np_arrays.shape
    len(song_ids)
    cs = cosine_similarity(np_arrays)
    dists = pd.DataFrame(cs, columns=song_ids)
    dists.index = dists.columns
    #dists.head()
    import pickle
    with open('romance_list', 'rb') as f:
        romance = pkl.load(f)

    romance=romance[:100]

    import pickle
    with open('party_list', 'rb') as f:
        party = pkl.load(f)

    party=party[:100]
    data=romance+party

    selected_song_id = st

    recommendations = dists[str(selected_song_id)].sort_values(ascending=False).reset_index()
    list=[]
    for i in range(0,10):
        list.append(int(recommendations['index'][i]))
    return list

def ret_id1(sn):
    np_arrays = np.load('finaldata.npy')
    with open('finaldata.pkl', 'rb') as handle:
        song_ids = pkl.load(handle)

    np_arrays.shape
    len(song_ids)
    cs = cosine_similarity(np_arrays)
    dists = pd.DataFrame(cs, columns=song_ids)
    dists.index = dists.columns
    #dists.head()
    import pickle
    with open('romance_list', 'rb') as f:
        romance = pkl.load(f)

    romance=romance[:100]

    import pickle
    with open('party_list', 'rb') as f:
        party = pkl.load(f)

    party=party[:100]
    data=romance+party
    
    for i in range(200):  
        if data[i]==sn:
            return i

    return -1