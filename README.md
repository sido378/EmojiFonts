# EmojiFonts

Python scripts to backport Apple Color Emoji font.

# Prerequisites

- [Python 3.7 or later](http://www.python.org/download/)
- [pip](https://pip.pypa.io/en/stable/)
- [fonttools](https://github.com/fonttools/fonttools) (`pip3 install fonttools`)
- (Optional) [Pillow](https://pillow.readthedocs.io/en/stable/) (`python3 -m pip install --upgrade Pillow`)

# Prerequisites (Theming)

- [getfonts](https://github.com/DavidBarts/getfonts) (for `getfonts`, `getfontname` and `stripttc`)
- [ImageMagick](https://imagemagick.org/index.php) (`brew install freetype imagemagick`)
- [Wand](https://pypi.org/project/Wand/) (`pip3 install Wand`)
- [librsvg](https://wiki.gnome.org/Projects/LibRsvg) (`brew install librsvg`)

# Before anything

- Copy `Apple Color Emoji.ttc` from `/System/Library/Fonts` of your macOS instance to the root of this repository and rename it to `AppleColorEmoji@2x.ttc`.

# Optimizing font for iOS 13-

1. Execute `get-fonts.sh`
2. Once finished, you will get `AppleColorEmoji@2x-out.ttc` that's compatible with iOS 13 and below and `AppleColorEmoji@2x.ttf` that's compatible with iOS 9 and below.

# Scripts

EmojiFonts modifies two font tables; `hmtx` and `sbix`.

`shift-multi.py` resizes and shifts the multi-skinned emojis that pair up as one, including couples and handshake, to have them displayed on iOS 13 and below correctly where there is no render logic to automatically place the pair close together.

`remove-strikes.py` removes supposedly least used strikes (image data) from `sbix` table. By default, emoji images come in certain dimensions from `20x20` to `160x160`. If images are uncompressed (macOS, for example), the total font size exceeds 100 MB which is not suitable for storing in GitHub repository.

`strip.py` strips PNG metadata out of emoji images using Python PIL Fork (Pillow). This is the case for older macOS emoji font where Apple simply did not optimize the PNGs and made the font size so big. You may comment out the execution of this script in `get-fonts.sh` if you are working on a recent emoji font.

`extractor.py` extracts PNG emoji images from the font - and opens up the possibility to theme the emoji font!

`otf2otc.py` combines TTF (True Type Font) fonts into a single TTC (True Type Collection) font. Fron iOS 10, Apple Color Emoji is built as TTC.

# Theming

## Twemoji

1. Clone [twemoji](https://github.com/twitter/twemoji) and place it alongside this project.
2. Execute `generate-twemoji-png.sh` to convert their emoji SVGs into compatible PNGs.
3. Execute `twemoji.sh` to create iOS-compatible Twemoji font, output at `twemoji/twemoji.ttc`.

## Noto Emoji

1. Clone [noto-emoji](https://github.com/googlefonts/noto-emoji) and place it alongside this project.
2. Execute `noto-emoji.sh` to create iOS-compatible Noto Color Emoji font, output at `noto-emoji/noto-emoji.ttc`.