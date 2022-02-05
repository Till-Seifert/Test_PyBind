cmake_minimum_required(VERSION 3.22.1)

project("HelloWorld")

add_executable("${PROJECT_NAME}" "HelloWorld.cpp")

install(TARGETS "${PROJECT_NAME}" DESTINATION bin)