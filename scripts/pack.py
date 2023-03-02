import os
import shutil
import traceback
from distutils.dir_util import copy_tree

dist_path = "../dist"

try: 
    if not os.path.exists(dist_path):
        os.makedirs(dist_path + "./src")

    copy_tree('../src', dist_path + "./src")
    shutil.copyfile("../index.py", dist_path + "/index.py")

    # Installed Python dependencies must be included inside the packed zipped plugin.
    # All the dependencies need to be installed localy in the "./package" folder so the script could pack them properly.
    if os.path.exists('../package'):
        copy_tree('../package', dist_path)  

    shutil.make_archive("plugin", 'zip', dist_path)
    shutil.rmtree(dist_path)

except Exception:
    shutil.rmtree(dist_path)
    print("packing plugin failed with error: ", traceback.format_exc())

