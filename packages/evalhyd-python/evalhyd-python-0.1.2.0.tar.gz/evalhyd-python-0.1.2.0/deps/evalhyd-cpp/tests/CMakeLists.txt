# Copyright (c) 2023, INRAE.
# Distributed under the terms of the GPL-3 Licence.
# The full licence is in the file LICENCE, distributed with this software.

cmake_minimum_required(VERSION 3.15)

# ------------------------------------------------------------------------------
# dependencies
# ------------------------------------------------------------------------------
find_package(GTest REQUIRED)

# ------------------------------------------------------------------------------
# build
# ------------------------------------------------------------------------------
add_executable(
        evalhyd_tests
        test_determinist.cpp
        test_probabilist.cpp
        test_uncertainty.cpp
)

OPTION(EVALHYD_TESTING_OS "OS system used to run tests")

if(CMAKE_HOST_APPLE)
    target_compile_definitions(evalhyd_tests PRIVATE EVALHYD_TESTING_OS MACOS)
    message(STATUS "Found supported OS to run tests: APPLE")
elseif(CMAKE_HOST_WIN32)
    target_compile_definitions(evalhyd_tests PRIVATE EVALHYD_TESTING_OS WINDOWS)
    message(STATUS "Found supported OS to run tests: WIN32")
elseif(CMAKE_HOST_UNIX)
    target_compile_definitions(evalhyd_tests PRIVATE EVALHYD_TESTING_OS LINUX)
    message(STATUS "Found supported OS to run tests: UNIX")
else()
    message(SEND_ERROR "OS not supported to run tests")
endif()

set_target_properties(
        evalhyd_tests
        PROPERTIES
                VISIBILITY_INLINES_HIDDEN ON
)

target_include_directories(
        evalhyd_tests
        PRIVATE
                ${CMAKE_SOURCE_DIR}/include/evalhyd
)

target_compile_definitions(
        evalhyd_tests
        PRIVATE
                EVALHYD_DATA_DIR="${CMAKE_CURRENT_SOURCE_DIR}"
)

target_link_libraries(
        evalhyd_tests
        PRIVATE
                EvalHyd::evalhyd
                GTest::GTest
                GTest::Main
)
