import os


class Standin:
    def __init__(self, standin):
        self.__standin = standin
        self.__object_name = ""
        self.__standin_name = ""
        self.__versions = {}
        self.__active_variant = ""
        self.__active_version = None
        self.parse()

    def parse(self):
        # object name
        standin_trsf = self.__standin.getParent()
        trsf_name = standin_trsf.name()
        self.__object_name = trsf_name.strip("|")

        # standin name
        standin_file_path = self.__standin.dso.get()
        standin_file_name_ext = os.path.basename(standin_file_path)
        standin_file_name = os.path.splitext(standin_file_name_ext)[0]
        self.__standin_name = standin_file_name.strip("_" + standin_file_name.split('_')[-1])

        # active variant and version
        path_version_dir = os.path.dirname(standin_file_path)
        path_variant_dir = os.path.dirname(path_version_dir)
        variant = os.path.basename(path_variant_dir)
        self.__active_variant = variant.split('_')[-1]
        self.__active_version = os.path.basename(path_version_dir)

        # variants and versions
        self.__versions.clear()
        path_asset_dir = os.path.dirname(path_variant_dir)
        for variant in os.listdir(path_asset_dir):
            variant_dir = path_asset_dir + "/" + variant
            if os.path.isdir(variant_dir):
                self.__versions[variant.split('_')[-1]] = []
                for version in os.listdir(variant_dir):
                    version_dir = variant_dir + "/" + version
                    if os.path.isdir(version_dir):
                        self.__versions[variant.split('_')[-1]].append((version,version_dir))

        for variant in self.__versions.keys():
            self.__versions[variant] = sorted(self.__versions[variant], reverse=True)

    def get_object_name(self):
        return self.__object_name

    def get_standin_name(self):
        return self.__standin_name

    def get_active_variant(self):
        return self.__active_variant

    def get_active_version(self):
        return self.__active_version

    def get_versions(self):
        return self.__versions

    def last_version(self):
        return self.__versions[self.__active_variant][0][0]

    def is_up_to_date(self):
        return self.last_version() == self.__active_version
