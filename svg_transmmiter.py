import math
import os
from pathlib import Path
import re
import xml.etree.ElementTree as ET

BASE_DIR = PROGRAM_DIR = Path(__file__).resolve().parent
SVG_DIR = os.path.join(BASE_DIR, 'svgs')
OUTPUT_DIR = os.path.join(os.path.join(BASE_DIR, 'lib'),'outputs')

def is_svg_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    return file_extension == ".svg"

def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_svg_file(file_path):
                file_list.append(file_path)
    return file_list

def svg_to_flutter_path(svg_path_data, path_name):
    commands = ""
    svg_path_data = svg_path_data.replace('-', ' -')  # 用空格替换所有的负号
    parts = re.findall(r'([A-Za-z]|-?\d+\.?\d*(?:e[-+]?\d+)?)', svg_path_data)
    # print('parts = ',parts)
    i = 0
    x = 0
    y = 0
    while i < len(parts):
        command = parts[i]
        i += 1
        if command == 'M' or command == 'D':
            x = float(parts[i])
            y = float(parts[i + 1])
            commands += f'    {path_name}.moveTo(' + parts[i] + ', ' + parts[i + 1] + ');\n'
            i += 2
        elif command == 'm':
            x += float(parts[i])
            y += float(parts[i + 1])
            commands += f'    {path_name}.relativeMoveTo(' + str(x) + ', ' + str(y) + ');\n'
            i += 2
        elif command == 'L':
            x = float(parts[i])
            y = float(parts[i + 1])
            commands += f'    {path_name}.lineTo(' + parts[i] + ', ' + parts[i + 1] + ');\n'
            i += 2
        elif command == 'l':
            x += float(parts[i])
            y += float(parts[i + 1])
            commands += f'    {path_name}.relativeLineTo(' + str(x) + ', ' + str(y) + ');\n'
            i += 2
        elif command == 'H':
            x = float(parts[i])
            commands += f'    {path_name}.lineTo(' + parts[i] + ', ' + str(y) + ');\n'
            i += 1
        elif command == 'h':
            x += float(parts[i])
            commands += f'    {path_name}.relativeLineTo(' + str(x) + ', 0);\n'
            i += 1
        elif command == 'V':
            y = float(parts[i])
            commands += f'    {path_name}.lineTo(' + str(x) + ', ' + parts[i] + ');\n'
            i += 1
        elif command == 'v':
            y += float(parts[i])
            commands += f'    {path_name}.relativeLineTo(0, ' + str(y) + ');\n'
            i += 1
        elif command == 'C':
            x = float(parts[i + 4])
            y = float(parts[i + 5])
            commands += f'    {path_name}.cubicTo(' + ', '.join(parts[i:i + 6]) + ');\n'
            i += 6
        elif command == 'c':
            commands += f'    {path_name}.relativeCubicTo(' + ', '.join([str(x + float(part)) for part in parts[i:i + 6]]) + ');\n'
            x += float(parts[i + 4])
            y += float(parts[i + 5])
            i += 6
        elif command == 'S':
            x = float(parts[i + 2])
            y = float(parts[i + 3])
            commands += f'    {path_name}.cubicTo(' + ', '.join(parts[i:i + 4]) + ');\n'
            i += 4
        elif command == 's':
            commands += f'    {path_name}.relativeCubicTo(' + ', '.join([str(x + float(part)) for part in parts[i:i + 4]]) + ');\n'
            x += float(parts[i + 2])
            y += float(parts[i + 3])
            i += 4
        elif command == 'Q':
            x = float(parts[i + 2])
            y = float(parts[i + 3])
            commands += f'    {path_name}.quadraticBezierTo(' + ', '.join(parts[i:i + 4]) + ');\n'
            i += 4
        elif command == 'q':
            commands += f'    {path_name}.relativeQuadraticBezierTo(' + ', '.join([str(x + float(part)) for part in parts[i:i + 4]]) + ');\n'
            x += float(parts[i + 2])
            y += float(parts[i + 3])
            i += 4
        elif command == 'A':
            rx = float(parts[i])
            ry = float(parts[i + 1])
            rotation = float(parts[i + 2])
            large_arc_flag = int(parts[i + 3])
            sweep_flag = int(parts[i + 4])
            x = float(parts[i + 5])
            y = float(parts[i + 6])
            rect_left = x - rx
            rect_top = y - ry
            rect_right = x + rx
            rect_bottom = y + ry
            sweep_angle = math.degrees(math.acos(1 - 2 * (1 - large_arc_flag)))
            if sweep_flag == 0:
                sweep_angle = -sweep_angle
            commands += f'    {path_name}.arcTo(Rect.fromLTRB({rect_left}, {rect_top}, {rect_right}, {rect_bottom}), {rotation}, {sweep_angle}, false);\n'
            i += 7
        elif command == 'a':
            rx = float(parts[i])
            ry = float(parts[i + 1])
            rotation = float(parts[i + 2])
            large_arc_flag = int(parts[i + 3])
            sweep_flag = int(parts[i + 4])
            x += float(parts[i + 5])
            y += float(parts[i + 6])
            rect_left = x - rx
            rect_top = y - ry
            rect_right = x + rx
            rect_bottom = y + ry
            sweep_angle = math.degrees(math.acos(1 - 2 * (1 - large_arc_flag)))
            if sweep_flag == 0:
                sweep_angle = -sweep_angle
            commands += f'    {path_name}.arcTo(Rect.fromLTRB({rect_left}, {rect_top}, {rect_right}, {rect_bottom}), {rotation}, {sweep_angle}, false);\n'
            i += 7
        elif command == 'Z' or command == 'z':
            commands += f'    {path_name}.close();\n'
        else:
            print(f"Unknown command: {command}")

    return commands

def write_text_to_file(text, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse(file):
    tree = ET.parse(file)
    root = tree.getroot()

    fill_colors = []
    paths = []

    for i, path in enumerate(root.iter('{http://www.w3.org/2000/svg}path')):
        svg_path_data = path.get('d')
        fill_color = path.get('fill', '#000000').lstrip('#')  # 提取颜色属性，如果不存在则默认为黑色
        fill_colors.append(fill_color)
        flutter_path_commands = svg_to_flutter_path(svg_path_data, f'path{i}')
        paths.append(flutter_path_commands)
    return fill_colors, paths

files = get_all_files(SVG_DIR)

def str_begin(title='MySvg'):
    return f'''import 'package:flutter/material.dart';

class {title.title()}Icon extends StatelessWidget {{

  final double width;
  final double height;

  const {title.title()}Icon({{
    super.key,
    this.width = 20,
    this.height = 20,
  }});

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(),
      body: CustomPaint(
        size: Size(width, height),
        painter: {title.title()}IconPainter(),
      ),
    );
  }}
}}

class {title.title()}IconPainter extends CustomPainter {{
  @override
  void paint(Canvas canvas, Size size) {{
'''

str_end = '''
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
'''

def convert_one_file(file):
    print(f'Current file is: {file}')
    fill_colors, paths = parse(file)
    print('File has been parsed.')
    
    # 为每个部分应用不同的颜色
    path_commands = []
    for i, path in enumerate(paths):
        color_hex = fill_colors[i].lstrip('#') if i < len(fill_colors) else '000000'
        path_commands.append(f'''    final paint{i} = Paint()
      ..color = const Color(0xFF{color_hex})
      ..style = PaintingStyle.fill
      ..strokeWidth = 1;

    var path{i} = Path();
{path}
    canvas.drawPath(path{i}, paint{i});\n''')
    file_base_name = os.path.splitext(os.path.basename(file))[0]
    # 写入生成的Flutter代码
    write_text_to_file(str_begin(file_base_name.replace('_','')) + '\n'.join(path_commands) + str_end, os.path.join(OUTPUT_DIR, file_base_name + '.dart'))

for file in files:
    try:
        convert_one_file(file)
    except Exception as E:
        print(E)
print('All done')

