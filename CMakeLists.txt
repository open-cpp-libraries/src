# // ============================================================= //
# // Open C++ Libraries.
# // Copyright (C) 2025-2026, Amlal El Mahrouss and OCL Authors, licensed under BSL-1.0 license.
# // ============================================================= //

cmake_minimum_required(VERSION 3.30)

project(OCL)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if (NOT DEFINED OCL_NO_INSTALL)
include(install_ocl.cmake)
endif ()
