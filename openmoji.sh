#!/usr/bin/env bash

set -e

FONT_NAME=AppleColorEmoji@2x
NAME=openmoji
ASSETS=../$NAME/color/svg
MAX_SIZE=96
[[ $1 == 'HD' ]] && HD=true || HD=false

[[ $HD = true ]] && MAX_SIZE=160

rm -rf $NAME/images
mkdir -p $NAME/images/160 $NAME/images/96 $NAME/images/64 $NAME/images/48 $NAME/images/40 $NAME/images/32 $NAME/images/20

cd $NAME-extra
rm -rf svgs images
mkdir -p svgs images/160 images/96 images/64 images/48 images/40 images/32 images/20
python3 gen-couple-heart.py
python3 gen-couple-kiss.py
python3 gen-couple-stand.py
python3 gen-handshake.py

echo "Converting SVGs into PNGs..."
for svg in $(find ./svgs -type f -name '*.svg')
do
    fname=$(basename $svg)
    rsvg-convert -a -h $MAX_SIZE $svg -o images/$MAX_SIZE/${fname/.svg/.png} &
done
wait

cd ..

for svg in $(find $ASSETS -type f -name '*.svg')
do
    fname=$(basename $svg)
    rsvg-convert -a -h $MAX_SIZE $svg -o $NAME/images/$MAX_SIZE/${fname/.svg/.png} &
done
wait

echo "Resizing and optimizing PNGs..."
./resize.sh $NAME $HD false false true
./resize.sh $NAME-extra $HD false false true

if [[ $HD = true ]]; then
    IN_FONT_NAME=AppleColorEmoji-HD
    OUT_FONT_NAME=$NAME-HD.ttc
else
    IN_FONT_NAME=$FONT_NAME
    OUT_FONT_NAME=$NAME.ttc
fi

python3 $NAME.py $HD apple/${IN_FONT_NAME}_00.ttf &
python3 $NAME.py $HD apple/${IN_FONT_NAME}_01.ttf &
wait

otf2otc $NAME/${IN_FONT_NAME}_00.ttf $NAME/${IN_FONT_NAME}_01.ttf -o $NAME/$OUT_FONT_NAME

echo "Output file at $NAME/$OUT_FONT_NAME"
