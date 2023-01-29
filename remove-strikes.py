import sys
import xml.etree.ElementTree as ET

# input: font sbix ttx
data = ET.parse(sys.argv[1]).getroot()

used_strikes = ['40', '64', '96', '160']
sbix = data.find('sbix')
to_remove = []
for strike in data.iter('strike'):
    ppem = strike.find('ppem')
    value = ppem.attrib['value']
    # possible values (macOS): 20, 26, 32, 40, 48, 52, 64, 96, 160
    # possible values (iOS): 40, 64, 96, 160
    if value not in used_strikes:
        print(f'Removing strike {value}x{value}...')
        to_remove.append(strike)

for strike in to_remove:
    sbix.remove(strike)

output = ET.ElementTree(data)
output.write(sys.argv[1], encoding='utf-8')
