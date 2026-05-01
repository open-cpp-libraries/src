from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class oclRecipe(ConanFile):
    name = "Open C++ Libraries."
    version = "1.63.4"

    # Optional metadata
    license = "BSL-1.0"
    author = "Amlal El Mahrouss amlal@nekernel.org"
    url = "https://git.ocl.nekernel.org/ocl"
    description = "The Open C++ Libraries.org super-project."
    topics = ("c++17", "libraries", "cpp")

    exports_sources = "CMakeLists.txt", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        self.package(self)

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ocl"]



