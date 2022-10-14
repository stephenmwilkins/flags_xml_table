

import numpy as np

import pandas as pd
from astropy.table import Table
from astropy.io import ascii



# data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers/cats'
#
# version = '0.2'
# version = '0.07.2'
#
# field = '2'
#
# filename = f'{data_dir}/CEERS_NIRCam{field}_v{version}_photom.fits'
# photom = ascii.read(filename)
# print(photom.colnames)
#
#
# photom_df = photom.to_pandas()


photom_df = pd.DataFrame({'shape': ['square', 'circle', 'triangle'],
                    'degrees': [360, 360, 180],
                    'sides': [4, np.nan, 3]})


xml = photom_df.to_xml(parser = 'etree')

with open('../data/test.xml', 'w') as f:
    f.writelines(xml)
