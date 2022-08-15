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
