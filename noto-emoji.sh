#!/usr/bin/env bash

set -e

FONT_NAME=AppleColorEmoji@2x
NAME=noto-emoji
ASSETS=../$NAME/png/128
FLAG_ASSETS=../$NAME/third_party/region-flags/png
MAX_SIZE=96

rm -rf $NAME
mkdir -p $NAME/images/96 $NAME/images/64 $NAME/images/48 $NAME/images/40 $NAME/images/32 $NAME/images/20

echo "Copying and resizing PNGs..."
cp -r $ASSETS/ $NAME/images/$MAX_SIZE
cp -r $FLAG_ASSETS/ $NAME/images/$MAX_SIZE
mogrify -resize 96x96 $NAME/images/$MAX_SIZE/*.png
mogrify -resize 64x64 -path $NAME/images/64 $NAME/images/96/*.png
mogrify -resize 48x48 -path $NAME/images/48 $NAME/images/64/*.png
mogrify -resize 40x40 -path $NAME/images/40 $NAME/images/48/*.png
mogrify -resize 32x32 -path $NAME/images/32 $NAME/images/40/*.png
mogrify -resize 20x20 -path $NAME/images/20 $NAME/images/32/*.png

echo "Converting SVGs into PNGs..."
cd ${NAME}-extra
rm -rf svgs images
mkdir -p svgs images/96 images/64 images/48 images/40 images/32 images/20
python3 gen-couple-heart.py
python3 gen-couple-kiss.py
python3 gen-couple-stand.py
python3 gen-handshake.py
for svg in $(find ./svgs -type f -name '*.svg')
do
    fname=$(basename $svg)
    rsvg-convert -a -h $MAX_SIZE $svg -o images/$MAX_SIZE/${fname/.svg/.png}
done

mogrify -resize 64x64 -path images/64 images/96/*.png
mogrify -resize 48x48 -path images/48 images/64/*.png
mogrify -resize 40x40 -path images/40 images/48/*.png
mogrify -resize 32x32 -path images/32 images/40/*.png
mogrify -resize 20x20 -path images/20 images/32/*.png

cd ..

echo "Optimizing PNGs using pngquant..."
pngquant -f --ext .png $NAME/images/96/*.png
pngquant -f --ext .png $NAME/images/64/*.png
pngquant -f --ext .png $NAME/images/48/*.png
pngquant -f --ext .png $NAME/images/40/*.png
pngquant -f --ext .png $NAME/images/32/*.png
pngquant -f --ext .png $NAME/images/20/*.png
pngquant -f --ext .png ${NAME}-extra/images/*/*.png

python3 $NAME.py common/${FONT_NAME}_00.ttf
python3 $NAME.py common/${FONT_NAME}_01.ttf

python3 otf2otc.py $NAME/${FONT_NAME}_00.ttf $NAME/${FONT_NAME}_01.ttf -o $NAME/$NAME.ttc

echo "Output file at $NAME/$NAME.ttc"
