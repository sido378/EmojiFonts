import os
import sys

sys.path.append('..')
from shared import *

# input: font ttf

ttf = sys.argv[1]

f = ttLib.TTFont(ttf)

def whatsapp_name(name: str):
    tokens = name.split('_')
    n = []
    for t in tokens:
        if t[0] == 'u':
            t = t[1:] # strip u prefix
        n.append(t)
    result = '_'.join(n)
    return 'u' + result

prepare_strikes(f)
for ppem, strike in f['sbix'].strikes.items():
    print(f'Reading strike of size {ppem}x{ppem}')
    for name, glyph in strike.glyphs.items():
        if glyph.graphicType != 'png ':
            continue
        name = base_norm_name(name)
        if base_is_whitelist(name):
            continue
        name = norm_fam(name)
        name = norm_dual(name)
        if name is None:
            continue
        name = base_norm_variants(name)
        name = base_norm_special(name)
        if name in u15_1 or name.endswith('_200d_27a1'):
            m_print(f'{name} is missing')
            continue
        o_name = name
        name = whatsapp_name(name)
        path = f'images/{ppem}/emoji_{name}.png'
        if not os.path.exists(path) or o_name.startswith('1f491') or o_name.startswith('1f48f'):
            name = name[1:] if name[0] == 'u' else name
            path = f'extra/images/{ppem}/{name}.png'
        glyph.imageData = get_image_data(path)

if not os.path.exists('../.test'):
    print('Saving changes...')
    ttf = ttf.replace('../apple/', '')
    f.save(ttf)
