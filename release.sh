#!/usr/bin/env bash

set -e

rm -rf release
mkdir -p release

ln apple/AppleColorEmoji-HD.ttc release/AppleColorEmoji-HD.ttc
ln apple/AppleColorEmoji-LQ.ttc release/AppleColorEmoji-LQ.ttc
ln blobmoji/blobmoji.ttc release/blobmoji.ttc
ln facebook/facebook.ttc release/facebook.ttc
ln fluentui/fluentui-Color.ttc release/fluentui-Color.ttc
ln fluentui/fluentui-Flat.ttc release/fluentui-Flat.ttc
ln joypixels/joypixels.ttc release/joypixels.ttc
ln joypixels/joypixels-Decal.ttc release/joypixels-Decal.ttc
ln noto-emoji/noto-emoji.ttc release/noto-emoji.ttc
ln noto-emoji/noto-emoji-HD.ttc release/noto-emoji-HD.ttc
ln oneui/oneui.ttc release/oneui.ttc
ln openmoji/openmoji.ttc release/openmoji.ttc
ln openmoji/openmoji-HD.ttc release/openmoji-HD.ttc
ln twemoji/twemoji.ttc release/twemoji.ttc
ln twemoji/twemoji-HD.ttc release/twemoji-HD.ttc
ln whatsapp/whatsapp.ttc release/whatsapp.ttc
