import mediapipe as mp
import cv2
import csv 
import os
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

#load in data

print("loading data up into a dataframe")

df = pd.read_csv('jab_cross_coords.csv')

X = df.drop('class', axis=1) #here we drop the class column so we are extracting our feautures i.e the coordinates to the keypoints
y = df['class'] # the target values we want to identify / match with X

print("done loading data into dataframe. now begenning training of pipeline")


X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.35, random_state=1234)

'''
Think of a pipeline as a streamlined way to setup all the preproccessing of data
that has be done before being fed to any specifed model

the actual pipeline varible is a dictionary where the abbriviations are keys that point
to the models themselves.

So in this case each model first normalizees the data(standardscalar) then passes it to its respective model 

'''

pipelines = {

    'lr':make_pipeline(StandardScaler(), LogisticRegression(max_iter=550)),
    'rc':make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf':make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb':make_pipeline(StandardScaler(), GradientBoostingClassifier()),
    
}

''' Here we cycle through all the possible models we have and go through their indavidual pipelines'''

fit_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fit_models[algo] = model

print("now testing models")

for algo, model in fit_models.items():
    yhat = model.predict(X_test)
    print(algo, accuracy_score(y_test, yhat))

with open('jab_cross_model.pkl', 'wb') as f:
    pickle.dump(fit_models['rf'], f)