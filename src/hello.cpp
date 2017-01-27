#include <hello/hello.h>

std::ostream& hello::v1::greet(std::ostream& stream) {
	return stream << "Hello, world";
}
