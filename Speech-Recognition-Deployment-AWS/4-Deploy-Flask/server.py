from flask import Flask, request, jsonify
import random
import os
from keyword_spotting_service import Keyword_Spotting_Service

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():

    # obtenemos el archivo de audio y lo guardamos
    audio_file = request.files["file"]
    file_name = str(random.randint(0, 100000))
    audio_file.save(file_name)

    # llamamos a el servicio keyword_spotting_service
    kss = Keyword_Spotting_Service()

    # hacemos la predicción
    predicted_keyword = kss.predict(file_name)

    # removemos el archivo de audio del directorio temporal
    os.remove(file_name)

    # devolvemos la predicción en formato json
    data = {'keyword': predicted_keyword}

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False)