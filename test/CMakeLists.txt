cmake_minimum_required(VERSION 2.8.7)

project(test_hello CXX)

set(${PROJECT_NAME}_SRC
	test_hello.cpp
)

add_executable(${PROJECT_NAME} ${${PROJECT_NAME}_SRC})

target_link_libraries(${PROJECT_NAME}
	hello
	${CONAN_LIBS}
)

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)

add_test(NAME ${PROJECT_NAME}
		 COMMAND ${PROJECT_NAME})
