# Copyright (c) 2023, INRAE.
# Distributed under the terms of the GPL-3 Licence.
# The full licence is in the file LICENCE, distributed with this software.

cmake_minimum_required(VERSION 3.15)

project(
        EvalHyd
        LANGUAGES CXX
        VERSION 0.1.1
        DESCRIPTION "Utility to evaluate streamflow predictions"
)

# ------------------------------------------------------------------------------
# dependencies
# ------------------------------------------------------------------------------

find_package(xtl 0.7.5 REQUIRED)
message(STATUS "Found xtl: ${xtl_INCLUDE_DIRS}/xtl")

find_package(xtensor 0.24.7 REQUIRED)
message(STATUS "Found xtensor: ${xtensor_INCLUDE_DIRS}/xtensor")

# ------------------------------------------------------------------------------
# build
# ------------------------------------------------------------------------------

# define evalhyd library
add_library(
        evalhyd
        INTERFACE
)

add_library(EvalHyd::evalhyd ALIAS evalhyd)

set_target_properties(
        evalhyd
        PROPERTIES
                VISIBILITY_INLINES_HIDDEN ON
)

target_include_directories(
        evalhyd
        INTERFACE
                $<INSTALL_INTERFACE:include>
                $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(
        evalhyd
        INTERFACE
                xtensor
)

if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    target_compile_options(
            evalhyd
            INTERFACE
                "/bigobj"
    )
endif()

target_compile_features(
        evalhyd
        INTERFACE
                cxx_std_14
)

# test suite
OPTION(EVALHYD_BUILD_TEST "configure and compile tests" ON)

if(EVALHYD_BUILD_TEST)
    add_subdirectory(tests)
endif()

# ------------------------------------------------------------------------------
# installation
# ------------------------------------------------------------------------------

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

# install library file (.a/.so)
install(
        TARGETS evalhyd
        EXPORT evalhyd-targets
)

# install headers
install(
        DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/include/evalhyd"
        DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
        FILES_MATCHING PATTERN "*.hpp"
)

# generate target file
export(
        EXPORT evalhyd-targets
        FILE "${CMAKE_CURRENT_BINARY_DIR}/EvalHydTargets.cmake"
)

# install target file
install(
        EXPORT evalhyd-targets
        FILE "EvalHydTargets.cmake"
        NAMESPACE EvalHyd::
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/EvalHyd
)

# generate config file
configure_package_config_file(
        EvalHydConfig.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/EvalHydConfig.cmake"
        INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/EvalHyd
)
write_basic_package_version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/EvalHydConfigVersion.cmake"
        VERSION "${EvalHyd_VERSION}"
        COMPATIBILITY SameMinorVersion
)

# install files
install(
        FILES
            "${CMAKE_CURRENT_BINARY_DIR}/EvalHydConfig.cmake"
            "${CMAKE_CURRENT_BINARY_DIR}/EvalHydConfigVersion.cmake"
        DESTINATION
            "${CMAKE_INSTALL_LIBDIR}/cmake/EvalHyd"
)
