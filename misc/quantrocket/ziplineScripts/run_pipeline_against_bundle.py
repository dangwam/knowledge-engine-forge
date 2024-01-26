# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:21:05 2023

@author: MAYANK DANGWAL
"""

"""
below code will list the asset that is registered with the bundle
"""
from zipline.data import bundles
bundle = bundles.load('csvdir_equities')
a = bundle.asset_finder.retrieve_all(bundle.asset_finder.sids)
print(a)

