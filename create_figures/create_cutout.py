

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.style.use('http://stephenwilkins.co.uk/matplotlibrc.txt')

import pandas as pd
from astropy.table import Table
from astropy.io import ascii, fits
from synthesizer.filters import SVOFilterCollection
import pysep.sep as sep
import pysep.utils
import pysep.plots.image
import pysep.analyse


data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers'
version = '0.2'
field = '1'

# --- open photometry catalogue

cat_name = f'CEERS_NIRCam{field}_v{version}'
filename = f'{data_dir}/cats/{cat_name}_photom.fits'

hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()
photom = Table(rows = data, names = data.columns.names)

# --- open image

data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers/images'
filename = f'{data_dir}/ceers_nircam{field}_f200w_v{version}_i2d.fits'

# --- create the Image object. The Image object contains the science and weight arrays and can be easily masked
img = pysep.utils.ImageFromMultiFITS(filename)
# img.measure_background_map()


filters = []
# filters += [f'HST/ACS_WFC.{f}' for f in ['F606W', 'F814W']]
# filters += [f'HST/WFC3_IR.{f}' for f in ['F105W', 'F125W', 'F160W']]
filters += [f'JWST/NIRCam.{f}' for f in ['F115W','F150W', 'F200W','F277W','F356W','F410M','F444W']]


for row in photom[:10]:

    id = row['ID']
    x = row['X']
    y = row['Y']

    # x = img.data.shape[0] - x
    # y = img.data.shape[1] - y

    # --- make a new image from a cutout of another image
    cutout = img.make_cutout(y, x, 100)

    fig, ax = pysep.plots.image.make_image_plot(cutout.data) # --- plot the cutout science image # TODO: add better scaling

    fn = f'../images/{version}_{field}/cutout_{id}.png'
    print(fn)
    fig.savefig(fn)
