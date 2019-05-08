# cs1-us-banks-fintech-hiring-trends

## Cleaning Data:
1. Merge all the PDF sources - It can be done using the tika-python library                             
   1) Installation(with pip)- pip install tika                                      
   2) Installation(without pip) - python setup.py build, python setup.py install
2. Remove Special characters - 
    It can be done using the regular expression library in python - re is regular expression library  
3. Remove Stopwords -                            
    1)Stopwords are the English words which does not add much meaning to a sentence.                      
    They can safely be ignored without sacrificing the meaning of the sentence. For example, the words like the, he, have etc.        
    Such words are already captured this in corpus named corpus. We first download it to our python environment             
    2)Used word list - https://www.ranks.nl/stopwords to remove data              
    3)And also used NLTK - Natural Language Toolkit - pip install nltk
    4)Clean lower cases 
## Extracting keywords and building list using following approches: 
### Wordcount
    1) Used NLP library and collections to generate wordcount for bigram
    2) Convert text file into list
    3) create function to clean text , Lowercases, takes out punct and short strings
    4) create function to Lemmatize like remove plurals(creates, plays)- it will save- create and play
    5) Count bigram frequencies and convert it into dictionary 
    6) Count the word and bigram frequencies 
    7) Take output into text format  
    8) Convert list into dataframe using Pandas - installation--> conda install pip  and  pip install django
    9) Convert Dataframe into csv
## Contributor
   Yashashri Shiral, Yash Lekhwani
  
