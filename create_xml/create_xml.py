

import numpy as np

import pandas as pd
from astropy.table import Table
from astropy.io import ascii, fits




data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers/cats'

version = '0.2'
version = '0.07.2'

field = '2'

cat_name = f'CEERS_NIRCam{field}_v{version}'
filename = f'{data_dir}/{cat_name}_photom.fits'
# photom = ascii.read(filename)
# print(photom.colnames)



hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()

data10 = data[:10]

print(data10)

photom = Table(rows = data10, names = data10.columns.names)

names = [name for name in photom.colnames if len(photom[name].shape) <= 1]
photom_df = photom[names].to_pandas()


xml = photom_df.to_xml(parser = 'etree')

with open(f'../data/{cat_name}.xml', 'w') as f:
    f.writelines(xml)
