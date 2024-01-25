project(Collision LANGUAGES CXX)
cmake_minimum_required(VERSION 3.15...3.27)
find_package(Python 3.9
    COMPONENTS Interpreter Development.Module REQUIRED
    OPTIONAL_COMPONENTS Development.SABIModule
)

find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(collision STABLE_ABI Collision/Collision.cpp)
install(TARGETS collision LIBRARY DESTINATION collision)