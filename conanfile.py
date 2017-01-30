from conans import ConanFile, CMake

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    exports = "include/*", "src/*", "CMakeLists.txt"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "{}" {}'.format(self.conanfile_directory,
                                        cmake.command_line))
        self.run('cmake --build . {}'.format(cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["hello"]

