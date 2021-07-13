

<p align="center">
    <br>
    <img src="./../assets/portada.jpeg"/>
    </a>
    <br>
</p>

<h2 align="center">
<p>Creación y despliegue en AWS de un modelo de reconocimiento de voz</p>
</h2>

Para este proyecto me basé en el repositorio de [Valerio Velardo](https://www.youtube.com/channel/UCZPFjMe1uRSirmSpznqvJfQ). Puede encontrar un explicación resumidar en la siguiente [presentacion](./presentacion.pdf).

### Dataset
Para entrenar el modelo se necesitan muchos datos, y en especial para el problema en cuestión, usaremos [este](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html) dataset de Google que pesa apróximadamente 2GB.


### Instalación
En algunas carpetas puede encontrar un archivo `requirements.txt` que debe instalar con `pip`. Un requisito necesario para ejecutar el modelo en la nube, es que usted necesita todo en Ubuntu (o alguna distribución Linux), debido a la compatibilidad de `uWSGI`.

Hay otras dependecias que debe instalar de forma separada, en primer lugar esta `ffmpeg`, luego siga los siguientes comandos:

```bash
conda install -c conda-forge librosa
conda install ffmpeg -c conda-forge
pip install numba==0.48  // instalar con pip 9
conda install -c conda-forge uwsgi
```
