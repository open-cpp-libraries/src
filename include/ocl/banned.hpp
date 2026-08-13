// SPDX-License-Identifier: BSL-1.0
// Copyright 2026, Amlal El Mahrouss (amlal@nekernel.org)
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
// Official repository: https://github.com/ocl-foss-org/ocl

#ifndef OCL_VERSION_BANNED_HPP
#define OCL_VERSION_BANNED_HPP

// This idea comes from: https://github.com/git/git/blob/master/banned.h

#define OCL_BANNED(FUNC) sorry_##FUNC##_is_a_banned_function

#undef strcpy
#define strcpy OCL_BANNED(strcpy)

#undef strcat
#define strcat OCL_BANNED(strcat)

#undef memset
#define memset OCL_BANNED(memset)

#undef memcpy
#define memcpy OCL_BANNED(memcpy)

/// More unsafe C functions are welcome by submission.

#endif
