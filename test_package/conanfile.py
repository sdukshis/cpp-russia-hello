from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "demo")

class HelloReuseConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = ("hello/0.1@%s/%s" % (username, channel),
                "gtest/1.8.0@lasote/stable")
    generators = "cmake"
    default_options = "gtest:shared=False"

    def build(self):
        # For following issue https://github.com/conan-io/conan/issues/475
        if (self.settings.compiler == "Visual Studio" and
            self.settings.build_type == "Debug" and
                not self.settings.compiler.runtime.value.endswith("d")):
            self.settings.compiler.runtime.value += "d"

        cmake = CMake(self)
        self.run('cmake "%s" %s' % (self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        # equal to ./bin/greet, but portable win: .\bin\greet
        self.run(os.sep.join([".","bin", "test_hello"]))
