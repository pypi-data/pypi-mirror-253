# -*- coding: utf-8 -*-
"""
check whether the VESTA file is written correctly
"""
from dspawpy.io.write import write_VESTA

write_VESTA(
    in_filename="rho.h5",
    data_type="rho",
    out_filename="rho.vasp",
    subtype=None,  # only for 'potential'
    format="VESTA",
)  # --> rho.vesta

write_VESTA(
    in_filename="rho.h5",
    data_type="rho",
    out_filename="rho.cube",
    subtype=None,  # only for 'potential'
    format="CUBE",
)  # --> rho.cube
