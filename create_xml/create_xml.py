

import numpy as np

import pandas as pd
from astropy.table import Table, join, hstack
from astropy.io import ascii, fits




data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers/cats'

version = '0.2'
# version = '0.07.2'

field = '1'

cat_name = f'CEERS_NIRCam{field}_v{version}'

filename = f'{data_dir}/{cat_name}_photom.fits'
hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()
photom = Table(rows = data, names = data.columns.names)

filename = f'{data_dir}/{cat_name}_zphot.fits'
hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()
zphot = Table(rows = data, names = data.columns.names)

combined = photom
combined['ZA'] = zphot['ZA'][0]

# combined = join(photom, zphot, join_type = 'cartesian')
# combined = hstack([photom, zphot])




combined = combined[:10]

print(combined.colnames)



names = [name for name in combined.colnames if len(combined[name].shape) <= 1]
combined_df = combined[names].to_pandas()


xml = combined_df.to_xml(parser = 'etree')

with open(f'../data/{cat_name}.xml', 'w') as f:
    f.writelines(xml)
