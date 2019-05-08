# K3G Music Inc
### K3G Music enterprises is planning a new music station which would enable listeners to listen to musicbased on how they feel. They plan to use Machine learning to classify songs. Acknowledging there arenew songs added to their catalog on a daily basis, they intend to build a machine learning basedclassifier service which would classify songs as (Happy/Sad). 
## Goal: Mood classifier for a top-k list 
        1. Retrieve the top k list from MusicMatch and present them with a happy/sad icon
        2. Use Flask to deploy the frontend.
        3. Use the modeling approach allocated to you to compute the scores

#### Claat Document : https://codelabs-preview.appspot.com/?file_id=18WLcxWBdVEqO-dMcvrffmENybG-OnntUDcsJ0fdQzKQ#3

#### Heroku Link : https://datadooclassifier.herokuapp.com/

#### Youtube Link : https://youtu.be/8qFAVImDW1A

## Steps : 

### 1. Read training and validation data : 
    https://raw.githubusercontent.com/rasbt/musicmood/master/dataset/training/train_lyrics_1000.csv
    https://github.com/rasbt/musicmood/blob/master/dataset/validation/valid_lyrics_200.csv
### 2. Perform Naive Bayes Data modelling along with Count and TFIDF vectorizer.
### 3. Calculate Accuracy , F1 score and Precision on training and valid lyrics
### 4. Scrape Data from https://www.musixmatch.com/explore
### 5. Predict mood of top-K songs using the Final classifier
### 6. Use Flask : a micro web framework written in Python to build the web application
### 7. Hosted the web app on Heroku

## Using the app:
    1. Go to the link : https://datadooclassifier.herokuapp.com/
    2. Enter the number of songs you want to predict and Click on Predict 
    3. A responsive page with all the songs with the mood prediction is displayed along with the probability
