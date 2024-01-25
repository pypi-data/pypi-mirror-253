# -*- coding: utf-8 -*-
from dspawpy.io.structure import _from_pdb
from dspawpy.io.write import to_file

ss = _from_pdb("ala_phe_ala.pdb")
print(len(ss))
print(ss[0])
to_file(ss[0], "POSCAR")
