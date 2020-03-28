Define Search Terms and identify Datasource
Covid-19 outbreak terms
SARS-CoV-2  ,  Coronavirus  ,  COVID-19  ,   Quarantine  , self-isolating  , Stay at Home , Shelter in Place , Middle East Respiratory Syndrome , MERS-CoV , Severe Acute Respiratory Syndrome , SARS-CoV , community Spread , Public health emergency , outbreak , Epidemic , Droplet transmission , Home isolation , Viral shedding, novel coronavirus, Symptomatic

Covid-19 symptom terms
shortness of breath , sore throat , headache , respiratory virus , bronchoalveolar lavage fluid , ground glass opacities , Bluish lips or face, Real-Time RT-PCR Diagnostic Panel, myalgia, fever 100, fever 38C, rhinorrhea, dyspnea, Nausea

Covid-19 restriction terms
restrictions on movement,  highest-level travel advisories, travel ban , community mitigation measure

Covid-19 kits and medical facilities terms
Drive through testing , N95 respirator , Negative-pressure rooms , Ventilator , sanitizer with 60 percent alcohol , surgical face mask , Respiratory etiquette and hand hygiene , face masks , Environmental surface cleaning , Immune system boosters ,  interferons , filtering facepiece respirator , NIOSH-approved equipments 

Covid-19 mental anxiety terms

Collect the covid19 feeds
For example, 
(A) We can tap into the live tweeter feed and create a localtion-aware time-series based on above categories of terms
---------------------------------------------------
class TweetStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            json4 = convertTweetToJson4(status._json)
            if json4:
                timestr = time.strftime("%Y%m%d") + "-streamedCovidJson"
                filePath = "drive/My Drive/TweetStreams/"+timestr
                with open(filePath, 'a+') as f:
                    f.write(json4)
                    f.write("\n")
                    return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False
------------------------------------------------------------------------------------------------------------------------
Either directly specify the  covid19QueryTerms or specify different hashtags [#covid19]
tweetsStream = tweepy.Stream(auth = auth1, listener=TweetStreamListener())
tweetsStream.filter(track=covid19QueryTerms)
---------------------------------------------------------------------------------------------------------------
If someone running Collab Editor, then run this script in console so that collabpro doesn't time out
function ClickConnect(){
console.log("Working"); 
document.querySelector("colab-toolbar-button#connect-scrollbar").click() 
}
setInterval(ClickConnect,60000)

-----------------------------------------------------------------------------------------------------------------------
(B) Another way is to collect data in batches and wait for rate limits
def TweetBatchCollector():
    api = setup_twitter()
    if not os.path.exists('data_recent'):
        os.makedirs('covid19Terms')
    for queryTerm in queryTermList:
        filepath = 'covid19Terms/{}.json'.format(queryTerm)
        mode = 'a'
        if not os.path.exists(filepath):
            print(filepath)
            mode = 'w'
            with open(filepath, mode) as f:
                i = 0
                for tweet in limit_handled(tweepy.Cursor(api.search, q=query, lang='en', result_type='recent').items()):
                    f.write(json.dumps(tweet._json))
                    f.write('\n')
------------------------------------------------------------------------
We can apply cosine similarity between covidTerm and tweetText to find best matches

Transform Dataset
------------------
Find Geo-Locations
str(tweet['coordinates'][tweet['coordinates'].keys()[1]][1]) + ", " + str(tweet['coordinates'][tweet['coordinates'].keys()[1]][0])
str(tweet['place']['full_name'] + ", " + tweet['place']['country'])
tweet['user']['location']

Ref: http://www.mikaelbrunila.fi/2017/03/27/scraping-extracting-mapping-geodata-twitter/

Analyze Dataset
---------------
Map Geo Location


Featurize Dataset
-----------------

Apply Machine Learning Models
---
ToDo - Link to a simple Prediction Model and Anamoly detection service leveraging (timestamp, location, daily-moving-avg)
