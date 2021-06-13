# av_gen
Little api to generate avatars from hash

https://av-gen.herokuapp.com/hash/40bce36cacc4b81585d1750df4d46ad6

## How it works?
To generate images, this API use Conway's Game of Life but with different rules.
For even iterations it has the basic rules, for odd - reversed.
Images are drawn by PIL.
Next it send bytes of image to io.buffer,read it and send it as response.

## Instalation
    $ pip3 install -r requirements.txt
    $ uvicorn main:app

## Dockerimage
    $ docker build -t av_gen .
    $ docker run -p 5000:5000 av_gen
