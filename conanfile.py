from conans import ConanFile, CMake, tools
import shutil
import os


class NlohmannjsonConan(ConanFile):
    name = "nlohmann-json"
    version = "3.6.1"
    license = "MIT"
    url = "https://github.com/darcamo/conan-nlohmann_json"
    description = "JSON for Modern C++"
    no_copy_source = True
    homepage = "https://github.com/nlohmann/json#examples"
    # No settings/options are necessary, this is header only

    def source(self):
        tools.get("https://github.com/nlohmann/json/archive/v{0}.zip".format(self.version))
        shutil.move("json-{0}".format(self.version), "sources")

    def build(self):
        os.mkdir("build")
        cmake = CMake(self)
        cmake.configure(source_folder="sources", build_folder="build")
        cmake.build()
        cmake.install()
