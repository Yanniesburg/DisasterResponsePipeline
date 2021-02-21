import sys
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 
from nltk.stem import WordNetLemmatizer

import re 
from nltk import word_tokenize 
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


def load_data(database_filepath):
    """
    Load data from database
    Input: 
    database_filepath (string): file path of the database 

    Output:
    X (matrix): X for training model 
    y (matrix): y for taining model 
    """

    path_str = 'sqlite:///' + database_filepath
    table_name = engine.table_names()
    engine = create_engine(path_str)
    df = pd.read_sql_table(table_name, con = engine)
    X = df.iloc[:,1].values
    y = df.iloc[:,5:-1].values
    return X,y


def tokenize(text):
    """
    tokenize input text
    Input: 
    text (str): text to be tokenized 
    Output:
    clean_tokens(): results 
    """
    # sentence tokenize 
    sentences = sent_tokenize(text)
    
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for sent_ in sentences:
        # normalization 
        text = re.sub(r"[^a-zA-Z0-9]", " ", sent_.lower())
        # tokenize 
        words = word_tokenize(text)
        # remove stop words 
        words = [word for word in words if not word in stop_words]
        # lemmatization
        for word in words:
            clean_tok = lemmatizer.lemmatize(word).lower().strip()
            clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    

    return cv_model


def evaluate_model(model, X_test, Y_test, category_names):
    pass


def save_model(model, model_filepath):
    pass


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()