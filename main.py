import importlib
from common import utils

utils.unload_packages(silent=True, package="asset_loader")
importlib.import_module("asset_loader")
from asset_loader.AssetLoader import AssetLoader
try:
    app.close()
except:
    pass
app = AssetLoader()
app.show()

