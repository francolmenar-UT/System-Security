cmake_minimum_required(VERSION 3.0)
project(PRNG)

## file globbing ##

file(GLOB_RECURSE sources src/*.cpp src/*.h)

## target definitions ##

add_executable(prng ${sources})

# Compiler flags.
target_compile_options(prng PUBLIC -std=c++1y -Wall)

## dependencies ##
target_link_libraries(prng PUBLIC
        ${Boost_LIBRARIES}
        )

## packaging ##

# All install commands get the same destination. this allows us to use paths
# relative to the executable.
install(TARGETS prng DESTINATION example_destination)

# Create the package

set(CPACK_PACKAGE_NAME "MyExample")
set(CPACK_PACKAGE_VERSION "1.0.0")

# Do not split the program up into several incomplete pieces.
set(CPACK_MONOLITHIC_INSTALL 1)

include(CPack)
