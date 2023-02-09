import sys

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/asset_loader'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    import AssetLoader
    from AssetLoader import *
    from utils import *

    unload_packages(silent=True, packages=["AssetLoader","Standin","Prefs"])
    app = AssetLoader()
    app.show()

