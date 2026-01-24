// Copyright 2023-2025, Amlal El Mahrouss (amlal@nekernel.org)
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
// Official repository: https://github.com/ocl-org/ocl

#ifndef OCL_HPP
#define OCL_HPP

// Version header
#include <ocl/version.hpp>

// Mandatory core headers.
#include <ocl/allocator_op.hpp>
#include <ocl/crc_hash.hpp>
#include <ocl/option.hpp>
#include <ocl/equiv.hpp>
#include <ocl/print.hpp>
#include <ocl/smart_ptr.hpp>

#ifdef OCL_FIX

# include <ocl/fix.hpp>

#endif

#ifdef OCL_TPROC

# include <ocl/tproc.hpp>

#endif

#endif // ifndef OCL_HPP
