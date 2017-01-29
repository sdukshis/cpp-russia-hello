#include <sstream>

#include <gtest/gtest.h>

#include <hello/hello.h>

using namespace hello;

TEST(hello, hello) {
	std::stringstream ss;

	greet(ss);

	ASSERT_EQ("Hello, world", ss.str());
}
