from flask import Flask, jsonify, request
from tensorflow import keras
from flask_cors import CORS
import os
from keras.preprocessing import sequence
import pickle
import string
import sklearn
from sklearn.preprocessing import LabelBinarizer
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('stopwords')



def remove_punctuation(text):
    punctuationfree = "".join([i for i in text if i not in string.punctuation])
    return punctuationfree


def lemmatizer(text):
    if len(text.split(' ')) == 1:
        text = [text]
    else:
        text = text.split(' ')
    lemm_text = " ".join([wordnet_lemmatizer.lemmatize(word) for word in text])
    return lemm_text


def remove_stopwords(text):
    if len(text.split(' ')) == 1:
        text = [text]
    else:
        text = text.split(' ')

    output = [i for i in text if i not in stopwords.words('english')]
    output = " ".join(output)

    return output


def preprocess_str(text):
    text = text.strip()
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = lemmatizer(text)
    return text

wordnet_lemmatizer = WordNetLemmatizer()
cwd = os.getcwd()
app = Flask(__name__)
# global default_graph
# default_graph = tf.compat.v1.get_default_graph()

# with default_graph.as_default():
model = keras.models.load_model('model.h5', compile=False)

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('encoder.pickle', 'rb') as handle:
    encoder = pickle.load(handle)

# Cross Origin Resource Sharing (CORS) handling
CORS(app, resources={'/classify': {"origins": "http://localhost:8080"}})

INTERN_SYNONYMS = [
    "intern",
    "apprentice",
    "probationer",
    "student",
    "novice",
    "learner",
    "beginner"
]

JUNIOR_SYNONYMS = [
    "junior",
    "subordinate",
    "secondary",
    "inferior",
]

MIDDLE_SYNONYMS = [
    "middle"
]

SENIOR_SYNONYMS = [
    "senior",
    "superior"
]

LEAD_SYNONYMS = [
    "lead",
    "head of",
    "principal",
    "distinguished",
    "staff"
]

EXECUTIVES_SYNONYMS = [
    "executive",
    "vp of",
    "chief",
    "ceo",
    "cto",
    "cdo"
]


def get_grades(titles):
    grades = []
    for title in titles:
        flag = False
        for syn in INTERN_SYNONYMS:
            if syn in title:
                grades.append("intern")
                flag = True
                break
        for syn in JUNIOR_SYNONYMS:
            if syn in title:
                grades.append("junior")
                flag = True
                break
        for syn in JUNIOR_SYNONYMS:
            if syn in title:
                grades.append("senior")
                flag = True
                break
        for syn in LEAD_SYNONYMS:
            if syn in title:
                grades.append("lead")
                flag = True
                break
        for syn in EXECUTIVES_SYNONYMS:
            if syn in title:
                grades.append("executive")
                flag = True
                break
        if "middle" in title or flag == False:
            grades.append("middle")

        return grades


@app.route('/classify', methods=['POST'])
def classify_title():
    titles = request.json['text']
    titles = [preprocess_str(x) for x in titles]
    sequences = tokenizer.texts_to_sequences(titles)
    x = sequence.pad_sequences(sequences, maxlen=32, padding='post')
    # with default_graph.as_default():
    predictions = model.predict(x)
    specializations = encoder.inverse_transform(predictions)
    specializations = list(specializations)
    grades = get_grades(titles)
    return jsonify({'titles': titles, 'specializations': specializations, 'grades': grades})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
