// SPDX-License-Identifier: BSL-1.0
// Copyright 2023-2026, Amlal El Mahrouss (amlal@nekernel.org)
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
// Official repository: https://git.ocl.nekernel.org/ocl

#ifndef OCL_HPP
#define OCL_HPP

// The version header of the OCL library.
#include <ocl/version.hpp>

// The mandatory OCL headers for standard use.
#include <ocl/alloc_op.hpp>
#include <ocl/crc_hash.hpp>
#include <ocl/option.hpp>
#include <ocl/equiv.hpp>
#include <ocl/print.hpp>
#include <ocl/smart_ptr.hpp>

// The FIX module
#ifdef OCL_FIX
# include <ocl/fix.hpp>
#endif

// The Text-processing module.
#ifdef OCL_TPROC
# include <ocl/tproc.hpp>
#endif

#endif // ifndef OCL_HPP
