import librosa
import os
import json

DATASET_PATH = "dataset"
JSON_PATH = "data.json"
SAMPLES_TO_CONSIDER = 22050 # 1 segundo de sonido

def prepare_dataset(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512):  

    # creamos un diccionario de datos
    data = {
        "mapping": [],
        "labels": [],
        "MFCCs": [],
        "files": []
    }

    # bucle sobre todos los subdirectorios
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # tenemos que asegurarnos de que no estamos a nivel de raiz
        if dirpath is not dataset_path:

            # actualizamos mappings
            category = dirpath.split("/")[-1]  # dataset/down -> [dataset, down]
            data["mapping"].append(category)
            print(f"\nProcesando {category}")

            # bucle sobre todos los filenames y extraemos los MFCCs
            for f in filenames:

                # obtenemos la ruta de archivo
                file_path = os.path.join(dirpath, f)

                # cargamos el archivo de audio
                signal, sr = librosa.load(file_path)

                # nos aseguramos que el audio es de al menos 1 segundo
                if len(signal) >= SAMPLES_TO_CONSIDER:
                    
                    # forzamos a que nuestro archivo de audio sea de 1 seg
                    signal= signal[:SAMPLES_TO_CONSIDER]

                    # extraemos los MFCCs
                    MFCCs = librosa.feature.mfcc(signal, sr, n_mfcc=n_mfcc, n_fft=n_fft, 
                                                hop_length=hop_length)
                    
                    # almacenamos los datos
                    data["labels"].append(i-1)
                    data["MFCCs"].append(MFCCs.T.tolist())
                    data["files"].append(file_path)
                    print(f"{file_path}: {i-1}")
    
    # almacenamos en los archivos json
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)

if __name__ == "__main__":
    prepare_dataset(DATASET_PATH, JSON_PATH)

