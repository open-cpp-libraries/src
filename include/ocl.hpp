/*
 * File: ocl.hpp
 * Purpose: Open C++ Libraries.
 * Author: Amlal El Mahrouss (amlal@nekernel.org)
 * Copyright 2025, Amlal El Mahrouss, licensed under the Boost Software License.
 */

#ifndef __OCL_HPP
#define __OCL_HPP

// Mandatory core headers.
#include <ocl/allocator_op.hpp>
#include <ocl/crc_hash.hpp>
#include <ocl/option.hpp>
#include <ocl/equiv.hpp>
#include <ocl/print.hpp>
#include <ocl/smart_ptr.hpp>

#ifdef __OCL_FIX

# include <ocl/fix/parser.hpp>
# include <ocl/fix/checksum.hpp>

#endif

#endif // ifndef __OCL_HPP
