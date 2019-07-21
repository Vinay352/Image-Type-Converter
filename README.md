# Image-Type-Converter
This program converts all images within a folder/dataset, which might be of different image formats, to JPEG (default) images with .jpg extension.

This program uses command line arguments. The program asks the user to input the path to the folder in which the images he/she wants to convert to JPEG (.jpg) image format are stored. Then the program automatically converts all those images in the folder defined by the user's input path to .jpg extensions. The name of the images are numbers ranging from 0 to (number of images in the folder - 1).

## Input:
>> python imagesToJPG.py -i (path to the folder whose images' type you want to convert)

### Motivation:
The reason behind why I wrote this program is because I was working with tensorflow image classification which required JPEG, PNG or GIF file formats as input. My dataset had a mix of these file formats + other file formats as well because of which my program failed everytime. My dataset contained 3500 images approximately. To save the trouble of opening every single image one by one and converting them to some specific format, I wrote this code to automates this tedious task for me.

<b>NOTE:-</b> 
  - The new images are saved in the directory where this program is saved.
  - Keep this python program file and the folder which contains the images in a separate directory so that all the new images will be saved in that separate directory and hence will be easy to locate.
