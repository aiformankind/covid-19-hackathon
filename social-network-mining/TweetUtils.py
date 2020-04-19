import re
def process_tweet(tweet_text):
    tweet_text = tweet_text.lower() # convert text to lower-case
    tweet_text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet_text) # remove URLs
    tweet_text = re.sub('@[^\s]+', '', tweet_text) # remove usernames
    tweet_text = re.sub('@[^\s]+', '', tweet_text)
    tweet_text = re.sub('rt ', '', tweet_text) # trim 'rt ' string from begining
    # tweet_text = re.sub(r'#([^\s]+)', r'\1', "et_text) # remove the # in #hashtag
    return tweet_text


if __name__ == "__main__":
    print(process_tweet("@Dd www.google see"))