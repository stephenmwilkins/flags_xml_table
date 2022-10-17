

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
# photom = ascii.read(filename)
# print(photom.colnames)



hdul = fits.open(filename)
data = hdul[1].data # assuming the first extension is a table
hdul.close()

data10 = data[:10]


photom = Table(rows = data10, names = data10.columns.names)


filters = []
filters += [f'HST/ACS_WFC.{f}' for f in ['F606W', 'F814W']]
filters += [f'HST/WFC3_IR.{f}' for f in ['F105W', 'F125W', 'F160W']]
filters += [f'JWST/NIRCam.{f}' for f in ['F115W','F150W', 'F200W','F277W','F356W','F410M','F444W']]

fc = SVOFilterCollection(filters)

for row in photom:

    print(row.colnames)

    id = row['ID']

    fig = plt.figure(figsize = (3.5, 1.5))

    left  = 0.2
    width = 0.75
    height = 0.6
    bottom = 0.25


    ax = fig.add_axes((left, bottom, width, height))

    fnu = {}
    fnu_err = {}

    for f in filters:

        wv = fc.filter[f].pivwv()/1E4

        f_ = f.split('.')[-1][:-1]

        fnu[f] = row[f_]
        fnu_err[f] = row['D'+f_]

        if fnu != 0.0:
            # ax.scatter(wv, fnu)
            ax.errorbar(wv, fnu[f], yerr = fnu_err[f], fmt = 'o', c = 'k', ms = 2, lw=1)




    ax.set_ylim([0., 1.2*np.max(np.array(list(fnu.values())))])


    ax.set_xlim([0.4, 4.7])
    ax.set_ylabel(r'$\rm f_{\nu}/nJy $')
    ax.set_xlabel(r'$\rm \lambda/\mu m$')

    fig.savefig(f'../images/{version}_{field}/sed_{id}.png')
