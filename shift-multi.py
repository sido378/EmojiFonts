import sys
import xml.etree.ElementTree as ET

data = ET.parse(sys.argv[1]).getroot()

# For iOS 13 and below only!
overrides = {
    "silhouette.u1F468.u1F48B.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F468.u1F48B.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1F468.u2764.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F468.u2764.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1F469.u1F48B.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F469.u1F48B.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1F469.u2764.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F469.u2764.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1F9D1.u1F48B.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F9D1.u1F48B.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1F9D1.u2764.L": { "width": "400", "lsb": "0" },
    "silhouette.u1F9D1.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.0.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.0.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.0.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.0.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.1.L": { "width": "400", "lsb": "0" },
    "u1F468.1.R": { "width": "400", "lsb": "-400" },
    "u1F468.1.RA": { "width": "400", "lsb": "-400" },
    "u1F468.1.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.1.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.1.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.1.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.2.L": { "width": "400", "lsb": "0" },
    "u1F468.2.R": { "width": "400", "lsb": "-400" },
    "u1F468.2.RA": { "width": "400", "lsb": "-400" },
    "u1F468.2.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.2.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.2.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.2.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.3.L": { "width": "400", "lsb": "0" },
    "u1F468.3.R": { "width": "400", "lsb": "-400" },
    "u1F468.3.RA": { "width": "400", "lsb": "-400" },
    "u1F468.3.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.3.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.3.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.3.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.4.L": { "width": "400", "lsb": "0" },
    "u1F468.4.R": { "width": "400", "lsb": "-400" },
    "u1F468.4.RA": { "width": "400", "lsb": "-400" },
    "u1F468.4.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.4.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.4.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.4.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F468.5.L": { "width": "400", "lsb": "0" },
    "u1F468.5.R": { "width": "400", "lsb": "-400" },
    "u1F468.5.RA": { "width": "400", "lsb": "-400" },
    "u1F468.5.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F468.5.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F468.5.u2764.L": { "width": "400", "lsb": "0" },
    "u1F468.5.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.0.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.0.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.0.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.0.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.1.L": { "width": "400", "lsb": "0" },
    "u1F469.1.R": { "width": "400", "lsb": "-400" },
    "u1F469.1.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.1.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.1.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.1.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.2.L": { "width": "400", "lsb": "0" },
    "u1F469.2.R": { "width": "400", "lsb": "-400" },
    "u1F469.2.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.2.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.2.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.2.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.3.L": { "width": "400", "lsb": "0" },
    "u1F469.3.R": { "width": "400", "lsb": "-400" },
    "u1F469.3.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.3.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.3.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.3.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.4.L": { "width": "400", "lsb": "0" },
    "u1F469.4.R": { "width": "400", "lsb": "-400" },
    "u1F469.4.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.4.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.4.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.4.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F469.5.L": { "width": "400", "lsb": "0" },
    "u1F469.5.R": { "width": "400", "lsb": "-400" },
    "u1F469.5.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F469.5.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F469.5.u2764.L": { "width": "400", "lsb": "0" },
    "u1F469.5.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.0.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.0.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.0.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.0.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.1.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.1.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.1.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.1.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.2.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.2.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.2.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.2.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.3.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.3.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.3.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.3.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.4.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.4.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.4.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.4.u2764.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.5.u1F48B.L": { "width": "400", "lsb": "0" },
    "u1F9D1.5.u1F48B.R": { "width": "400", "lsb": "-400" },
    "u1F9D1.5.u2764.L": { "width": "400", "lsb": "0" },
    "u1F9D1.5.u2764.R": { "width": "400", "lsb": "-400" },
    "silhouette.u1FAF1.L": { "width": "400", "lsb": "0" },
    "silhouette.u1FAF2.R": { "width": "400", "lsb": "-400" },
    "u1FAF1.0.L": { "width": "400", "lsb": "0" },
    "u1FAF1.1.L": { "width": "400", "lsb": "0" },
    "u1FAF1.2.L": { "width": "400", "lsb": "0" },
    "u1FAF1.3.L": { "width": "400", "lsb": "0" },
    "u1FAF1.4.L": { "width": "400", "lsb": "0" },
    "u1FAF1.5.L": { "width": "400", "lsb": "0" },
    "u1FAF2.0.R": { "width": "400", "lsb": "-400" },
    "u1FAF2.1.R": { "width": "400", "lsb": "-400" },
    "u1FAF2.2.R": { "width": "400", "lsb": "-400" },
    "u1FAF2.3.R": { "width": "400", "lsb": "-400" },
    "u1FAF2.4.R": { "width": "400", "lsb": "-400" },
    "u1FAF2.5.R": { "width": "400", "lsb": "-400" }
}

sbix = data.find('hmtx')
for mtx in data.iter('mtx'):
    name = mtx.attrib['name']
    if name in overrides:
        override = overrides[name]
        mtx.set('width', override['width'])
        mtx.set('lsb', override['lsb'])

output = ET.ElementTree(data)
output.write(sys.argv[1], encoding='utf-8')