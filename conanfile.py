from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class oclRecipe(ConanFile):
    name = "Open C++ Libraries."
    version = "1.62.0"

    # Optional metadata
    license = "BSL-1.0"
    author = "Amlal El Mahrouss amlal@nekernel.org"
    url = "https://git.ocl.nekernel.org/src"
    description = "The Open C++ Libraries super-project."
    topics = ("c++17", "libraries", "cpp")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "CMakeLists.txt", "libs/*", "include/*"

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
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ocl"]



