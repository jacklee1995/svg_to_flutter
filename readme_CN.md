# SVG TO Flutter Canvas

Author: 李俊才

Email：291148484@163.com

License: [MIT](./LICENSE)

## 功能

简介：该项目是一个代码生成器，用于将SVG文件转换为Flutter绘图代码，使用前请确保你的电脑上安装了Python环境。

## 用法

svg的源文件放在 svgs/ 目录中。运行 run.bat 后，将生成与之对应的Flutter代码。

## 备注

当前对于部分SVG命令尚未实现 Flutter 中的绘图方式，这导致一个现象是复杂的SVG可以生成看起来差不多的图片，而简单的图形更多情况下无法支持。

如下面这张图，完全是基于生成的Fluutter绘图代码绘制的：

![alt text](image.png)