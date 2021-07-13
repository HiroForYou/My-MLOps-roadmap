import 'package:flutter/material.dart';
import 'package:mnist_flutter_app/dl_model/classifier.dart';

class DrawPage extends StatefulWidget {
  @override
  _DrawPageState createState() => _DrawPageState();
}

class _DrawPageState extends State<DrawPage> {
  Classifier classifier = Classifier();
  List<Offset> points = List<Offset>();
  int digit = -1;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.black,
        child: Icon(Icons.close),
        onPressed: () {
          points.clear();
          digit = -1;
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
            Text("Dibuja un dígito en el cuadro", style:
              TextStyle(fontSize: 20),),
            SizedBox(height: 10,),
            Container(
              height: 304,
              width: 304,
              decoration: BoxDecoration(
                color: Colors.white,
                border: Border.all(
                    color: Colors.redAccent,
                    width: 2.0 ),

                ),
              child: GestureDetector(
                onPanUpdate: (DragUpdateDetails details) {
                  Offset localPosition = details.localPosition;
                  setState(() {
                    if (localPosition.dx >= 0 &&
                        localPosition.dx <= 300 &&
                        localPosition.dy >= 0 &&
                        localPosition.dy <= 300){
                      points.add(localPosition);
                    }

                  });
                },
                onPanEnd: (DragEndDetails details) async {
                  points.add(null);
                  digit = await classifier.classifyDrawing(points);
                  setState(() {

                  });
                },
                child: CustomPaint(
                  painter: Painter(points: points)
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

class Painter extends CustomPainter {
  final List<Offset> points;
  Painter({this.points});

  final Paint paintDetails = Paint()
    ..style = PaintingStyle.stroke
    ..strokeWidth = 4.0
    ..color = Colors.black;

  @override
  void paint(Canvas canvas, Size size) {
    for (int i = 0; i < points.length - 1; i++) {
      if (points[i] != null && points[i+1] != null) {
        canvas.drawLine(points[i], points[i+1], paintDetails);
      }
    }
  }

  @override
  bool shouldRepaint(Painter oldDelegale) {
    return true;
  }

}
