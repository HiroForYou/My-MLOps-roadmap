import 'package:flutter/material.dart';
import 'package:mnist_flutter_app/pages/drawing_page.dart';
import 'package:mnist_flutter_app/pages/upload_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Home(),
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int currentIndex = 0;
  List tabs = [
    UploadImage(),
    DrawPage(),

  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: tabs[currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        selectedFontSize: 14.0,
        unselectedFontSize: 14.0,
        selectedItemColor: Colors.redAccent,
        unselectedItemColor: Colors.grey[400],
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.image),
              label: "Image"
          ),
          BottomNavigationBarItem(
              icon: Icon(Icons.album),
              label: "Draw"
          )
        ],
        onTap: (index) {
          setState(() {
            currentIndex = index;
          });
        },
      ),
    );
  }
}
