# personal notes


## running the local app

The `make test` tests fail, but the app works
The .cvs that is generated has the files in order.

So, to rename files we can parse it and proceed.


```csv
red,green,blue,hue,saturation,value,pixels_total,pixels_counted,pixels_pcnt,path
118,103,103,0.0,0.1271186440677966,118,65536,65525,100.0,assets/jpg/some.tiles/schnabel.computer_20220810-011052_16_64_8.004.png
172,123,115,0.023391812865497075,0.3313953488372093,172,65536,65526,100.0,assets/jpg/some.tiles/schnabel.computer_20220809-043209_12.59_64_64.003.png
84,78,77,0.02380952380952382,0.08333333333333333,84,65536,65536,100.0,assets/jpg/some.tiles/schnabel.computer_20220810-004959_16_64_16.002.png
```

## running the image-sort app

```
./imagesort.py print assets/jpg/some.tiles/ --threads 4 --ignore ignore-pixels-white.jpg > data.tiles.csv

./imagesort.py print /Users/michaelpaulukonis/Documents/images/schnabel.computer.tiles.upscaled/ --threads 4 --ignore ignore-pixels-white.jpg > upscaled.tiles.ignore.white.csv

./imagesort.py print /Users/michaelpaulukonis/Documents/images/babies.small/ --threads 4 > babies.csv
./imagesort.py print /Users/michaelpaulukonis/Documents/images/babies.small/ --threads 4 --key red > babies.red.csv
./imagesort.py print /Users/michaelpaulukonis/Documents/images/babies.small/ --threads 4 --key saturation > babies.sat.csv
./imagesort.py print /Users/michaelpaulukonis/Documents/images/babies.small/ --threads 4 --key blue > babies.blue.csv


./imagesort.py print /Users/michaelpaulukonis/Documents/images/babies.small/ --threads 4 --ignore ignore-pixels-white.jpg > babies.ignore.csv



./imagesort.py gif babies.csv --output babies.gif --csv -x 200 -y 200 --bar 60
./imagesort.py gif babies.red.csv --output babies.red.gif --csv -x 200 -y 200 --bar 60
./imagesort.py gif babies.blue.csv --output babies.blue.gif --csv -x 200 -y 200 --bar 60

./imagesort.py gif babies.sat.csv --output babies.sat.gif --csv -x 200 -y 200 --bar 60


./imagesort.py print /Users/michaelpaulukonis/projects/images/meat/meat.tiles --threads 4 > meat.csv
./imagesort.py print /Users/michaelpaulukonis/projects/images/meat/meat.tiles --threads 4 --key red > meat.red.csv

./imagesort.py print /Users/michaelpaulukonis/projects/images/meat/warhol.tiles --threads 4 > warhol.csv


./imagesort.py gif  meat.csv --output meat.gif --csv -x 200 -y 200 --bar 60
./imagesort.py gif  meat.red.csv --output meat.red.gif --csv -x 200 -y 200 --bar 60




./imagesort.py collage assets/jpg/some.tiles/ --output collage.tiles.jpg --threads 4


./imagesort.py gif assets/jpg/some.tiles/ --output image.tiles.gif --threads 4 -x 256 -y 256 --bar 0

./imagesort.py gif ~/Documents/images/schnabel.computer.tiles/ --output schnabel.sorted.gif --threads 4 -x 256 -y 256 --bar 0
```

## running the rename utility

I wrote this. Hah-hah-hah.

`./rename.py --input_csv ./upscaled.tiles.ignore.white.csv --output_path fresh`

`./rename.py --input_csv ./babies.csv --output_path /Users/michaelpaulukonis/Documents/images/babies.sorted/`


## opens a file in Chrome

`open -a "Google Chrome" image.tiles.gif`

ffmpeg -r 20 -f image2 -s 1024x1024 -pattern_type glob -i 'fresh/*.png' -vcodec libx264 -crf 17 -pix_fmt yuv420p schnabel.computer.sorted.fast.00.mp4

ffmpeg -i schnabel.computer.sorted.fast.00.mp4 -filter:v scale=720:-1 -c:a copy schnabel.computer.sorted.fast.720.mp4


## some Testing
 ./imagesort.py print /Users/michaelpaulukonis/projects/images/test --threads 4 --key value > test.csv
./rename.py --input_csv ./test.csv --output_path /Users/michaelpaulukonis/projects/images/test.sorted/


 ./imagesort.py print /Users/michaelpaulukonis/projects/images/test --threads 4 --key value > test3.csv

ffmpeg -r 20 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/test3.sorted/*.png' -vcodec libx264 -crf 17 -pix_fmt yuv420p test3.00.mp4
ffmpeg -r 20 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/test2.sorted/*.png' -vcodec libx264 -crf 17 -pix_fmt yuv420p test2.00.mp4
ffmpeg -r 20 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/meat/warhol.redux/*.png' -vcodec libx264 -crf 17 -pix_fmt yuv420p meat.redux.mp4

ffmpeg -r 30 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/meat/warhol.redux/*.png' -vcodec libx264 -crf 17 -filter:v scale=720:-1 -pix_fmt yuv420p meat.redux.30.720.mp4

ffmpeg -r 5 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/meat/warhol.redux/*.png' -vcodec libx264 -crf 17 -filter:v scale=720:-1 -pix_fmt yuv420p meat.redux.05.720.mp4


ffmpeg -r 30 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/meat/warhol.hilbert/*.png' -vcodec libx264 -crf 17 -filter:v scale=720:-1 -pix_fmt yuv420p meat.hilbert.30.720.mp4

ffmpeg -r 5 -f image2 -s 1024x1024 -pattern_type glob -i '/Users/michaelpaulukonis/projects/images/meat/warhol.hilbert/*.png' -vcodec libx264 -crf 17 -filter:v scale=720:-1 -pix_fmt yuv420p meat.hilbert.05.720.mp4


 ./imagesort.py print /Users/michaelpaulukonis/projects/images/meat/warhol.meat.upscaled --threads 4 --key value > meat.again.csv

 ./imagesort.py print /Users/michaelpaulukonis/projects/images/meat/warhol.meat.upscaled --threads 4 --key hilbert > meat.hilbert.csv


./rename.py --input_csv ./meat.again.csv --output_path /Users/michaelpaulukonis/projects/images/meat/warhol.redux

./rename.py --input_csv ./meat.hilbert.csv --output_path /Users/michaelpaulukonis/projects/images/meat/warhol.hilbert


montage -geometry +0+0 -tile 10x /Users/michaelpaulukonis/projects/images/insta/*.png montage.png

montage -geometry +0+0 -tile 8x /Users/michaelpaulukonis/projects/images/insta/*.png montage.08.png


/Users/michaelpaulukonis/projects/images/insta/

convert -crop 4096x4096 montage.08.png meats.%03d.png

mogrify montage.08.png  -resize 2048 montage.small.png

mogrify -resize 2048x2048 -format jpg /Users/michaelpaulukonis/projects/images/insta/montage.08.png 

mogrify -resize 2048x2048 -format jpg /Users/michaelpaulukonis/projects/images/insta/meats*.png



PEOPLE EXPECT YOU TO EAT PROTEIN AND YOU DO SO THEY WON’T TALK --ANDY WARHOL (IN THE FUTURE EVERYBODY WILL BE MEAT FOR FIFTEEN MINUTES)

These look more like Andy Warhol versions of anatomical diagrams (showing our best cuts of meat) than they look like Julian Schnabel versions of anatomical diagrams (showing our best cuts of meat). And I used a new sorting algorithm.

#color #colour #colors #artistsoninstagram #contemporaryart #digitalcollage #digitalcollageart #digitalart #capitalistneoexpressionism #techspressionism #repetition #neopop #aiassistedart #mindalle #meat #fakeandywarhol #andywarhol #andywarholquotes

import hilbert
colours.sort(key=lambda (r,g,b):hilbert.Hilbert_to_int([int(r*255),int(g*255),int(b*255)])    )