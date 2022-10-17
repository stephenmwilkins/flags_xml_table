

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



data_dir = '/Users/stephenwilkins/Dropbox/Research/data/images/jwst/ceers/cats'

version = '0.2'
# version = '0.07.2'

field = '1'

cat_name = f'CEERS_NIRCam{field}_v{version}'

filename = f'{data_dir}/{cat_name}_photom.fits'
hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()
photom = Table(data = data, names = data.columns.names)

filename = f'{data_dir}/{cat_name}_pz.fits'
hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()
pz = Table(data = data, names = data.columns.names)


for i, photom_ in enumerate(photom[:10]):

    id = photom_['ID']

    fig = plt.figure(figsize = (3.5, 1.5))

    left  = 0.2
    width = 0.75
    height = 0.6
    bottom = 0.25

    ax = fig.add_axes((left, bottom, width, height))

    ax.plot(pz['ZGRID'][0], pz['PZ'][0][i], lw=1, c='k')

    #
    #
    # ax.set_ylim([0., 1.2*np.max(np.array(list(fnu.values())))])
    #
    #
    # ax.set_xlim([0.4, 4.7])
    ax.set_ylabel(r'$\rm P(z) $')
    ax.set_xlabel(r'$\rm z $')

    fig.savefig(f'../images/{version}_{field}/pz_{id}.png')
