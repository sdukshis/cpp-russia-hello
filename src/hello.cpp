#include <hello/hello.h>

std::ostream& hello::greet(std::ostream& stream) {
	return stream << "Hello, world";
}
