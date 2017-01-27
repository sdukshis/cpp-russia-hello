#ifndef HELLO_HELLO_H
#define HELLO_HELLO_H

#include <ostream>

namespace hello {
	inline namespace v1 {
		std::ostream& greet(std::ostream&);
	}
}
#endif