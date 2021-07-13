from tensorflow import keras
import librosa
import numpy as np
import os


MODEL_PATH = f"{os.getcwd()}/../2 Implementing the model TF/modelo.h5"
NUM_SAMPLES_2_CONSIDER = 22050  # 1 seg


class _Keyword_Spotting_Service:

    model = None
    _mapping = [
        "down",
        "go",
        "left",
        "no",
        "off",
        "on",
        "right",
        "stop",
        "up",
        "yes"
    ]
    _instance = None

    def predict(self, file_path):

        # extraemos MFCCs
        MFCCs = self.preprocess(file_path)  # (# segmentos, # coeficientes)

        # convertimos el array MFCCs 2d a 4d  -> (# ejemplos, # segmentos, # coeficientes, # canales)
        MFCCs = MFCCs[np.newaxis, ..., np.newaxis]
        

        # hacemos las predicciones
        predictions = self.model.predict(MFCCs)  # [ [ 0.1, 0.6, 0.1, ...] ]
        
        predicted_keyword = self._mapping[np.argmax(predictions)]

        return predicted_keyword


    def preprocess(self, file_path, n_mfcc=13, n_fft=2048, hop_length=512):
        
        # cargamos el archivo de audio
        signal, sr= librosa.load(file_path)

        # nos aseguramos de la longitud de audio sea consistente
        if len(signal) >= NUM_SAMPLES_2_CONSIDER:
            signal = signal[:NUM_SAMPLES_2_CONSIDER]

             # extraemos los MFCCs
            MFCCs = librosa.feature.mfcc(signal, sr, n_mfcc=n_mfcc, n_fft=n_fft, 
                                        hop_length=hop_length)

        return MFCCs.T

def Keyword_Spotting_Service():

    # Nos aseguramos que solo tenemos una instancia de KSS
    if _Keyword_Spotting_Service._instance is None:

        _Keyword_Spotting_Service._instance = _Keyword_Spotting_Service()
        _Keyword_Spotting_Service.model = keras.models.load_model(MODEL_PATH)
    
    return _Keyword_Spotting_Service._instance


if __name__ == "__main__": 
    kss = Keyword_Spotting_Service()


    audios = [obj for obj in os.listdir(f"{os.getcwd()}/prueba_me/") if os.path.isfile(f"{os.getcwd()}/prueba_me/" + obj)]
    recog = []
    coincidencias = 0

    print("\n---------------------PREDICCIONES---------------------------\n")
    for i, audio in enumerate(audios):

        recog.append(kss.predict(f"{os.getcwd()}/prueba_me/" + audio))
        print(f"Palabra detectada: {recog[i]}, Palabra verdadera: {os.path.splitext(audio)[0]}") 

        if recog[i] == os.path.splitext(audio)[0]:
            coincidencias+=1

    print(f"\nCoincidencias: {coincidencias}/{len(audios)}")
        

    