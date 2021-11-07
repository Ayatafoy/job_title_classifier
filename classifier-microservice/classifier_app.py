from flask import Flask, jsonify, request
from tensorflow import keras
import numpy as np
from flask_cors import CORS
import tensorflow as tf
import image

app = Flask(__name__)
global default_graph
default_graph = tf.compat.v1.get_default_graph()

with default_graph.as_default():
    model = keras.models.load_model('model.h5', compile=False)

# Cross Origin Resource Sharing (CORS) handling
CORS(app, resources={'/image': {"origins": "http://localhost:8080"}})


@app.route('/image', methods=['POST'])
def image_post_request():  
    x = image.convert(request.json['image'])
    with default_graph.as_default():
        y = model.predict(x.reshape((1, 28, 28, 1))).reshape((10,))
    n = int(np.argmax(y, axis=0))
    y = [float(i) for i in y]

    return jsonify({'result': y, 'digit': n})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
