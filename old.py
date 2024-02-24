import os
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_DIR = PROGRAM_DIR = Path(__file__).resolve().parent
SVG_DIR = os.path.join(BASE_DIR, 'svgs')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')

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

def svg_to_flutter_path(svg_path_data, fill_colors, path_name):
    commands = ""
    parts = svg_path_data.split()
    i = 0
    while i < len(parts):
        command = parts[i]
        i += 1
        if command == 'M':
            commands += f'    {path_name}.moveTo(' + parts[i] + ', ' + parts[i + 1] + ');\n'
            i += 2
        elif command == 'L':
            commands += f'    {path_name}.lineTo(' + parts[i] + ', ' + parts[i + 1] + ');\n'
            i += 2
        elif command == 'C':
            commands += f'    {path_name}.cubicTo(' + ', '.join(parts[i:i + 6]) + ');\n'
            i += 6
        elif command == 'Z':
            commands += f'    {path_name}.close();\n'
        elif command == 'fill':
            fill_color = parts[i].strip()
            fill_colors.append(fill_color)
        else:
            pass

    return fill_colors, commands

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
        _, flutter_path_commands = svg_to_flutter_path(svg_path_data, fill_colors, f'path{i}')
        paths.append(flutter_path_commands)
    return fill_colors, paths

files = get_all_files(SVG_DIR)

str_begin = '''import 'package:flutter/material.dart';

class MySVGIcon extends StatelessWidget {

  final double width;
  final double height;

  const MySVGIcon({
    super.key,
    this.width = 20,
    this.height = 20,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomPaint(
        size: const Size(width, height),
        painter: MySVGIconPainter(),
      ),
    );
  }
}

class MySVGIconPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
'''

str_end = '''
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
'''

for file in files:
    print(f'Current file is: {file}')
    fill_colors, paths = parse(file)
    print('File has been parsed.')
    
    # 为每个部分应用不同的颜色
    path_commands = []
    for i, path in enumerate(paths):
        color_hex = fill_colors[i].lstrip('#') if i < len(fill_colors) else '000000'
        path_commands.append(f'''    final paint{i} = Paint()
      ..color = Color(0xFF{color_hex})
      ..style = PaintingStyle.fill
      ..strokeWidth = 1;

    var path{i} = Path();
{path}
    canvas.drawPath(path{i}, paint{i});\n''')

    # 写入生成的Flutter代码
    write_text_to_file(str_begin + '\n'.join(path_commands) + str_end, os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(file))[0] + '.dart'))

print('All done')