import os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(root)

import Auto3D
from Auto3D.auto3D import options
from Auto3D.ASE.geometry import opt_geometry
path = os.path.join(root, "D:/Ph.D/Healy's Lab/20220927-145846-629666_linear_peptoid/linear_peptoid_out.sdf")
optimized = opt_geometry(path, model_name="AIMNET", opt_tol=0.002)
print(optimized)