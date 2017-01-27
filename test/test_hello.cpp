#include <sstream>
#include <cassert>
#include <iostream>

#include <hello/hello.h>

using namespace hello;

void test_hello() {
	std::stringstream ss;

	greet(ss);

	assert(ss.str() == "Hello, world");
}

int main() {
	std::cout << "test_hello...";
	test_hello();
	std::cout << "OK\n";
}