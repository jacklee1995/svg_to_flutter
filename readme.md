# SVG TO Flutter Canvas

Author: Juncai Li (jcLee95)

Email: 291148484@163.com

License: [MIT](./LICENSE)

## Functionality

Introduction: This project is a code generator designed to convert SVG files into Flutter drawing code. Make sure you have Python installed on your computer before using it.

## Usage

Place the SVG source files in the svgs/ directory. After running run.bat, corresponding Flutter code will be generated.

## Remarks

At present, some SVG commands have not been implemented in the drawing method of Flutter, which results in a phenomenon where complex SVGs can generate images that look similar, while simple shapes are often not supported.

For example, the image below is entirely drawn based on the generated Flutter drawing code:

![alt text](image.png)