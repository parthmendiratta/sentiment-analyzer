import pandas as pd
import re
import string
import joblib
from functools import lru_cache

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

def clean_text(text):
    text=text.lower()
    text=re.sub(r"http\S+|www\S+","",text)
    text=re.sub(r"\d+","",text)
    text=text.translate(str.maketrans("","",string.punctuation))
    text=text.strip()
    return text

def train_and_save_model(
        dataset_path: str="IMDB_Dataset.csv",
        model_path: str="model.pkl",
        vectorizer_path: str="vectorizer.pkl"
):
  
    data=pd.read_csv(dataset_path)
    # print(data.describe())
    # print(data.info())
    # print(data.isnull().sum()) # gives how muh null values are in each column

    data['sentiment']=data['sentiment'].map({'positive':1,'negative':0})
    data['cleaned_review']=data['review'].apply(clean_text)

    print(data['sentiment'].value_counts())

    # Vectoriztion
    vectorizer=TfidfVectorizer(max_features=10000,
        stop_words='english',
        ngram_range=(1, 2))
    x=vectorizer.fit_transform(data['cleaned_review'])
    y=data['sentiment']

    # Train test split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    # Model Tuning
    model=LogisticRegression()
    model.fit(x_train,y_train)

    #Prediction
    y_predicted=model.predict(x_test)

    # Accuracy Score wth class weights
    print("Accuracy: ",accuracy_score(y_true=y_test,y_pred=y_predicted))
    print("Classification Report:\n",classification_report(y_test,y_predicted))
    print("Confusion Matrix\n",confusion_matrix(y_test,y_predicted))

    joblib.dump(model,model_path)
    joblib.dump(vectorizer,vectorizer_path)

@lru_cache(maxsize=1)
def _load_artifacts(model_path="model.pkl",vectorizer_path="vectorizer.pkl"):
    model=joblib.load(model_path)
    vectorizer=joblib.load(vectorizer_path)
    return model,vectorizer
def predict_sentiment(text):

    model,vectorizer=_load_artifacts()

    cleaned_text=clean_text(text)

    vectorized_text=vectorizer.transform([cleaned_text])

    prediction=model.predict(vectorized_text)[0]
    
    return "Positive" if prediction == 1 else "Negative"

if __name__=="__main__":
    train_and_save_model()