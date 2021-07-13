import requests

URL = "http://127.0.0.1:5050/predict"
TEST_AUDIO_FILE_PATH = "prueba_me/down.wav"

if __name__ == "__main__":

    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")} 
    response = requests.post(URL, files=values)
    data = response.json()

    print(f"La palabra predicha es: {data['keyword']}")