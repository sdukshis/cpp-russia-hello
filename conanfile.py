from conans import ConanFile, CMake

class HelloConan(ConanFile):
    description = "Demo package"
    license = "https://github.com/sdukshis/conan-librabbitmq/blob/master/LICENSE"
    url = "https://github.com/sdukshis/cpp-russia-hello"
    name = "hello"
    version = "0.1"
    exports = "include/*", "src/*", "CMakeLists.txt"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        self.run('cmake "{}" {}'.format(self.source_folder,
                                        cmake.command_line))
        self.run('cmake --build . {}'.format(cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["hello"]

