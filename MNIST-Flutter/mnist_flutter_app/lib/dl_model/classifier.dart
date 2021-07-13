import 'dart:ffi';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite_flutter/tflite_flutter.dart';
import 'dart:io' as io;
import 'package:image/image.dart' as img;
import 'dart:ui' as ui;

class Classifier {
  Classifier();

  classifyImage(PickedFile image) async {
    var file = io.File(image.path);
    img.Image imageTemp = img.decodeImage(file.readAsBytesSync());
    img.Image resizedImg = img.copyResize(imageTemp,
                                          height: 28, width: 28);
    var imgBytes = resizedImg.getBytes();
    var imgAsList = imgBytes.buffer.asUint8List();

    return getPred(imgAsList);

  }

  classifyDrawing(List<Offset> points) async{
    final picture = toPicture(points);
    final image = await picture.toImage(28, 28);
    ByteData imgBytes = await image.toByteData();
    var imgAsList = imgBytes.buffer.asUint8List();

    return getPred(imgAsList);
  }

  Future<int> getPred(Uint8List imgAsList) async {
    List resultBytes = List(28*28);  // [] reemplazó a List(28*28)

    for(int i = 0, index = 0; i < imgAsList.lengthInBytes; i+=4, index++){
      final r = imgAsList[i];
      final g = imgAsList[i+1];
      final b = imgAsList[i+2];

      resultBytes[index] = ( (r+g+b)/3.0 ) / 255.0;
    }

    var input = resultBytes.reshape([1, 28, 28, 1]);
    var output = List(1*10).reshape([1, 10]);

    InterpreterOptions interpreterOptions =  InterpreterOptions();

    try{
      Interpreter interpreter = await Interpreter.fromAsset(
        "model.tflite",
        options: interpreterOptions
      );
      interpreter.run(input, output);
    } catch(e){
      print("Error cargando el modelo o ejecuntándolo");
    }

    double highestProb = 0;
    int digitPred;
    for (int i =0; i < output[0].length; i++){
      if (output[0][i] > highestProb){
        digitPred = i;
        highestProb = output[0][i];
      }
    }

    return digitPred;
  }
}

ui.Picture toPicture(List<Offset> points) {
  // Obtain a Picture from a List of points
  // This Picture can then be converted to something
  // we can send to our model. Seems unnecessary to draw twice,
  // but couldn't find a way to record while using CustomPainter,
  // this is a future improvement to make.

  final _whitePaint = Paint()
    ..strokeCap = StrokeCap.round
    ..color = Colors.white
    ..strokeWidth = 16.0;

  final _bgPaint = Paint()..color = Colors.black;
  final _canvasCullRect = Rect.fromPoints(Offset(0, 0),
      Offset(28.0, 28.0));
  final recorder = ui.PictureRecorder();
  final canvas = Canvas(recorder, _canvasCullRect)
    ..scale(28 / 300);

  canvas.drawRect(Rect.fromLTWH(0, 0, 28, 28), _bgPaint);

  for (int i = 0; i < points.length - 1; i++) {
    if (points[i] != null && points[i + 1] != null) {
      canvas.drawLine(points[i], points[i + 1], _whitePaint);
    }
  }

  return recorder.endRecording();
}








