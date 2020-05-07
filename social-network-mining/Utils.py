""" 
Helper function for File, List and String

"""
import os
import json
import pandas as pd
import glob
import time
from multiprocessing import Pool
from timeit import default_timer as timer
from tqdm import trange


def get_words_from_file(file_path):
    words = []
    with open(file_path) as fo:
        for word in fo:
            words.append(word.strip())
    return set(words)


def has_word_in_text(sentence, match_words):
    return any(word.lower() in sentence.lower().split() for word in match_words)


def filter_tweet_data(json_file_path, filter_keys = None):
    if os.path.exists(os.path.abspath(json_file_path)) is False:
        raise("Not valid fiel path, please check")
        os.sys.exit(0)
    data = []
    
    with open(json_file_path, encoding='utf-8-sig') as f:
        for line in f:
            d = json.loads(line)
            filter_data = {}
            if filter_keys is not None:
                filter_data = { k:v for k,v in d.items() if k in filter_keys}
            else:
                filter_data = d
            data.append(filter_data)
        return json.dumps(data)

# Get start and end batch from list of indexes 
def get_batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield ndx,min(ndx + n, l)

def read_json_data(json_gz_files):
    # When I supplied 400 JSON gz file to read, machine was going out of memory
    # Lets do by batch by batch. There could be some better way.

    BATCH_SIZE = 50
    for i,b in enumerate(get_batch(range(0, len(json_gz_files)), BATCH_SIZE)):
        start = b[0]
        end = b[1]
        df = pd.concat((pd.read_json(f, compression="gzip", lines=True) for f in json_gz_files[start: end]),  ignore_index=True)
        columns_to_keep = ['created_at', 'full_text', 'geo','coordinates', 'place', 'contributors', 'lang']
        df = df[columns_to_keep]
        print(f"Writing pickle file : {i}")
        df.to_pickle("./df_pkl_" + str(i) + ".pkl")
        del df

def read_json_gz_data_multiprocessing(json_file):
    return pd.read_json(json_file, compression="gzip", lines=True)

def get_files_list(json_gz_folder):
    json_gz_files = glob.glob(json_gz_folder +"/*.jsonl.gz")
    return json_gz_files

def validate_pkl(pkl_file):
    df = pd.read_pickle(pkl_file)
    print(len(df))
    print(df.iloc[0])

# create one pickle file out of multiple pickle files 
def combine_multiple_pickle(pickle_file_list, target_pickle_file):
    df = pd.concat([pd.read_pickle(f) for f in  pickle_file_list], ignore_index=True)
    df.to_pickle(target_pickle_file)


if __name__ == "__main__":
    HYDRATED_TWEET_GZ_FOLDER  = "./data/COVID-19-TweetIDs/2020-04/"
    COMBINED_PICKLE_FILE =  "COMBINED_PICKLE"
    ALL_PICKLE_FILES_EXPRESSION =  "./*.pkl"

    json_gz_files = get_files_list(HYDRATED_TWEET_GZ_FOLDER)
    df = read_json_data(json_gz_files[:11])

    # clean_up_tweet_df(df)
    
    # pickle_files = glob.glob(ALL_PICKLE_FILES_EXPRESSION)
    # combine_multiple_pickle(pickle_files, COMBINED_PICKLE_FILE)