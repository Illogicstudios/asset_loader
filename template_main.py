import sys

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/template'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    # TODO import and start right tool
    import AssetLoader
    from AssetLoader import *
    from utils import *
    from Prefs import *

    unload_packages(silent=True, packages=["MayaTool","Standin","Prefs"])
    app = AssetLoader()
    app.show()

