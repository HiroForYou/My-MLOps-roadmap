import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:mnist_flutter_app/dl_model/classifier.dart';
import 'dart:io';

class UploadImage extends StatefulWidget {
  @override
  _UploadImageState createState() => _UploadImageState();
}

class _UploadImageState extends State<UploadImage> {
  Classifier classifier = Classifier();
  final picker = ImagePicker();
  PickedFile image;
  int digit = -1;
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.black,
        child: Icon(Icons.camera_alt_outlined),
        onPressed: () async {
          image = await picker.getImage(source: ImageSource.gallery);
          digit = await classifier.classifyImage(image);
          setState(() {

          });
        },
      ),
      appBar: AppBar(
                    backgroundColor: Colors.redAccent,
                    title: Text("El mejor clasificador MNIST"),
                    ),
      body: Center(
        child: Column(
          children: [
            SizedBox(height: 40,),
            Text("La imagen se muestra abajo", style:
              TextStyle(fontSize: 20),),
            SizedBox(height: 10,),
            Container(
              height: 300,
              width: 300,
              decoration: BoxDecoration(
                color: Colors.white,
                border: Border.all(
                    color: Colors.redAccent,
                    width: 2.0 ),
                image: DecorationImage(
                  image: digit == -1 ?
                    AssetImage("assets/fondoCuadro.png") :
                    FileImage(File(image.path)),
                ),
              ),
            ),
            SizedBox(height: 45,),
            Text("Predicción actual: ", style:
              TextStyle(fontSize: 25, fontWeight: FontWeight.bold),),
            SizedBox(height: 20,),
            Text(
                digit == -1 ? "" : "$digit",
                style: TextStyle(fontSize: 50, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}