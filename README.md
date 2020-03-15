# Img2xlsx

This is a proof-of-concept of a simple program that transform an image to an spreadsheet.

Each pixel is will be placed in a cell. The cell background will be filled with a solid color representing the pixel color (RGB)

# How to use it
There are two ways to use the program. One is sending a post requet to the endpoint https://img2xlsx.herokuapp.com/
The body should containg the base64 of the image. Since thius is a free node, you may find some problems with the file size. Only small images will be converted

The second way is cloning this repository and starting the server yourself.
You should install the requirements:
``` bash
pip install -r requirements.txt
```

and then start the server:
``` bash
flask run
```

after that, send a post request to 127.0.0.1:5000 with your base64 image