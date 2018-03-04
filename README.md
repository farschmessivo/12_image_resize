# Image Resizer

The module re-sizes given picture by scale or height and width or only by height or width (second argument is adjusted 
proportionally). 

# How it works

The program takes such arguments:
```
--height -he height

--width -w width

--scale -s scale

--input -i  [file.png]

--output -o path to directory/file for output 
```

# Example input

```
$ python3 image_resize.py zen.png --height 500 --width 400 --output  --input zen_resize.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)