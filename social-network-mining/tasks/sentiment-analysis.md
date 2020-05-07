Description
--
Covid19 mental anxiety terms, spread of negativity, corrective measures by sending back positive message , trends over time , geo-location analysis

Implementation Approaches
--
Approach-1
1) Data Collection : Extract the tweets from the Twitter Ids
- POC
  - captured live streams
  - Hydrator tool to store tweets in google drive
- Alpha
  - store large dataset in google cloud storage
  - use google Dataproc cluster / Colab notebook for crunching big data 

2) Data Analysis : Find the topic and analyze the terms
- POC
  - Find mental anxiety terms 
  - Word Cloud
  - Google NLP for topic modeling for detecting Org / Place / other Business Entities
  - Spacy UMLS for disease and drugs name detection
- Alpha
  - apply SparkNLP / spacy on the spark dataframe

Approach-2
