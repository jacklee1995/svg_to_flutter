import 'package:flutter/material.dart';

class PianoIcon extends StatelessWidget {
  final double width;
  final double height;

  const PianoIcon({
    super.key,
    this.width = 20,
    this.height = 20,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: CustomPaint(
        size: Size(width, height),
        painter: PianoIconPainter(),
      ),
    );
  }
}

class PianoIconPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint0 = Paint()
      ..color = const Color(0xFF231815)
      ..style = PaintingStyle.fill
      ..strokeWidth = 1;

    var path0 = Path();
    path0.moveTo(1788.416, 1.706667);
    path0.lineTo(1788.416, 0);
    path0.relativeLineTo(1649.8346669999999, 0);
    path0.relativeLineTo(0, 1.706667);
    path0.relativeLineTo(1615.7013329999997, 0);
    path0.lineTo(1615.7013329999997, 0);
    path0.relativeLineTo(1476.6079999999997, 0);
    path0.relativeLineTo(0, 1.706667);
    path0.relativeLineTo(1442.4746669999997, 0);
    path0.lineTo(1442.4746669999997, 0);
    path0.relativeLineTo(1303.3813329999998, 0);
    path0.relativeLineTo(0, 1.706667);
    path0.lineTo(1095.509333, 1.706667);
    path0.lineTo(1095.509333, 0);
    path0.relativeLineTo(956.928, 0);
    path0.relativeLineTo(0, 1.706667);
    path0.relativeLineTo(907.776, 0);
    path0.lineTo(907.776, 0);
    path0.relativeLineTo(769.194667, 0);
    path0.relativeLineTo(0, 1.706667);
    path0.lineTo(0, 1.706667);
    path0.lineTo(0.0, 1024);
    path0.relativeLineTo(1901.568, 0);
    path0.lineTo(1901.568, 1.706667);
    path0.close();
    path0.relativeMoveTo(1762.986667, 18.773333);
    path0.relativeLineTo(0, 610.304);
    path0.relativeLineTo(1826.3039999999999, 0);
    path0.lineTo(1826.3039999999999, 1006.933333);
    path0.relativeLineTo(1672.704, 0);
    path0.lineTo(1672.704, 610.304);
    path0.relativeLineTo(1729.024, 0);
    path0.lineTo(1729.024, 18.773333);
    path0.close();
    path0.relativeMoveTo(1555.797333, 18.773333);
    path0.relativeLineTo(0, 610.304);
    path0.relativeLineTo(1620.992, 0);
    path0.lineTo(1620.992, 1006.933333);
    path0.relativeLineTo(1467.392, 0);
    path0.lineTo(1467.392, 610.304);
    path0.relativeLineTo(1521.664, 0);
    path0.lineTo(1521.664, 18.773333);
    path0.close();
    path0.relativeMoveTo(1415.68, 610.304);
    path0.lineTo(1415.68, 1006.933333);
    path0.relativeLineTo(1262.0800000000002, 0);
    path0.lineTo(1262.0800000000002, 18.773333);
    path0.relativeLineTo(1349.1200000000001, 0);
    path0.relativeLineTo(0, 610.304);
    path0.close();
    path0.moveTo(1199.274667, 18.773333);
    path0.lineTo(1199.274667, 1006.933333);
    path0.relativeLineTo(1045.674667, 0);
    path0.lineTo(1045.674667, 610.304);
    path0.relativeLineTo(1096.874667, 0);
    path0.lineTo(1096.874667, 18.773333);
    path0.close();
    path0.relativeMoveTo(854.528, 18.773333);
    path0.relativeLineTo(0, 610.304);
    path0.relativeLineTo(925.525333, 0);
    path0.lineTo(925.525333, 1006.933333);
    path0.relativeLineTo(771.925333, 0);
    path0.lineTo(771.925333, 610.304);
    path0.relativeLineTo(806.058667, 0);
    path0.lineTo(806.058667, 18.773333);
    path0.close();
    path0.relativeMoveTo(705.706667, 610.304);
    path0.lineTo(705.706667, 1006.933333);
    path0.relativeLineTo(552.106667, 0);
    path0.lineTo(552.106667, 18.773333);
    path0.relativeLineTo(619.008, 0);
    path0.relativeLineTo(0, 610.304);
    path0.close();
    path0.relativeMoveTo(-1.1946669999999813, 620.373333);
    path0.lineTo(-1.1946669999999813, 18.773333);
    path0.relativeLineTo(26.62400000000002, 0);
    path0.relativeLineTo(0, 620.373333);
    path0.relativeLineTo(105.13066700000002, 0);
    path0.lineTo(105.13066700000002, 1006.933333);
    path0.lineTo(187.733333, 1006.933333);
    path0.lineTo(187.733333, 620.373333);
    path0.close();
    path0.relativeMoveTo(311.12533299999996, 620.373333);
    path0.relativeLineTo(354.13333299999994, 0);
    path0.lineTo(354.13333299999994, 18.773333);
    path0.relativeLineTo(388.2666669999999, 0);
    path0.relativeLineTo(0, 620.373333);
    path0.relativeLineTo(464.89599999999996, 0);
    path0.lineTo(464.89599999999996, 1006.933333);
    path0.relativeLineTo(311.29599999999994, 0);
    path0.close();
    path0.relativeMoveTo(481.9626669999999, 1006.933333);
    path0.relativeLineTo(526.6773339999999, 0);
    path0.lineTo(526.6773339999999, 18.773333);
    path0.relativeLineTo(636.0746669999999, 0);
    path0.lineTo(636.0746669999999, 1006.933333);
    path0.relativeLineTo(482.47466699999984, 0);
    path0.close();
    path0.moveTo(17.066667, 18.773333);
    path0.relativeLineTo(97.792, 0);
    path0.relativeLineTo(0, 620.373333);
    path0.lineTo(170.666667, 620.373333);
    path0.lineTo(170.666667, 1006.933333);
    path0.lineTo(17.066667, 1006.933333);
    path0.close();
    path0.moveTo(1884.501333, 1006.933333);
    path0.relativeLineTo(1730.901333, 0);
    path0.lineTo(1730.901333, 610.304);
    path0.relativeLineTo(1789.098667, 0);
    path0.lineTo(1789.098667, 18.773333);
    path0.relativeLineTo(1885.184, 0);
    path0.close();

    canvas.drawPath(path0, paint0);
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
