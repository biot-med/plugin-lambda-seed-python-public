# The script create a zip file to upload as a BioT plugin.
# Assumptions 
# 1. The handler function is in the index.py (its zipped specifically)
# 2. The venv directory is called seedenv (seedenv/lib/python3.11/site-packages is zipped specifically)
# 3. Some dependencies are NOT zipped - base things like pip

import os
import shutil
import traceback
from shutil import copytree, ignore_patterns

dist_path = "../dist"

try: 

    print("Copy dependencies")

    copytree(
        './seedenv/lib/python3.11/site-packages', 
        dist_path, 
        symlinks=True, 
        ignore=ignore_patterns("pip", 'pkg_resources', 'setuptools', '_distutils_hack', 'distutils-precedence.pth',
                               '*.dist-info'))
    
    print("Copy all src")

    copytree('./src', dist_path + "/src", symlinks=True)

    print("Copy index.py file")

    shutil.copyfile("./index.py", dist_path + "/index.py")

    # Installed Python dependencies must be included inside the packed zipped plugin.
    # All the dependencies need to be installed localy in the "./package" folder so the script could pack them properly.
    # if os.path.exists('../package'):
    #     copy_tree('../package', dist_path)  

    print("Zip")

    shutil.make_archive("plugin", 'zip', dist_path)

    shutil.rmtree(dist_path)


except Exception:
    shutil.rmtree(dist_path)
    print("packing plugin failed with error: ", traceback.format_exc())

