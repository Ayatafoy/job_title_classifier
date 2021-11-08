FROM python:3.7

RUN python -m pip install flask flask-cors gunicorn numpy tensorflow nltk
RUN python -m pip install -U scikit-learn
WORKDIR /app

ADD classifier_app.py classifier_app.py
ADD tokenizer.pickle tokenizer.pickle
ADD encoder.pickle encoder.pickle
ADD model.h5 model.h5

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "classifier_app:app" ]

