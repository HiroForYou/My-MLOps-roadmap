## Instrucciones

> crearemos el init.sh con los comandos que se ejecutará en el servidor de amazon

> abrimos AWS, en EC2 dashboard
    le damos a "Launch instance"-> ubuntu -> review and launch -> "create a new key pair"
    -> configuramos el nombre de la máquina y descargamos la clave -> "launch instance"
    -> "view instances"

> el key descargado lo movemos a la carpeta 7 AWS y abrimos terminal 
```bash
chmod 400 speech_recognition.pem
scp -i speech_recognition.pem -r server/ ubuntu@<< PUBLIC DNS COPIADO DE AWS>>:~     ///con ese comando subimos el contenido de la carpeta server
```

> desde el mismo terminar, ahora nos logearemos
```bash
ssh -i speech_recognition.pem ubuntu@<< PUBLIC DNS COPIADO DE AWS>>
cd server/
chmod +x init.sh  //para hacer el ejecutable
./init.sh             // con eso se ejecuta todo lo que queriamos instalar y correr
```

> ahora configuramos el firewall, en AWS en la opción de Security groups->launch-wizard-9

    -> clic en el security group ID-> se abrirá una ventana con "Inbound rules" -> "edit inbound rules"
    -> add rule->seleccionamos HTTP -> en la opcion de custom le damos a "Anywhere" -> save rules


> mientras el terminal sigue cargando el contenedor, modificamos el client.py, el http se reemplaza  con wl IPv4 Public IP de AWS. Para esto el docker ya se estaría ejecutando
    -> corremos  el client.py y ya!!




























