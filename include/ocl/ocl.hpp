#ifndef __OCL_HPP
#define __OCL_HPP

#include <ocl/allocator_op.hpp>
#include <ocl/crc_hash.hpp>
#include <ocl/option.hpp>
#include <ocl/is_same.hpp>
#include <ocl/print.hpp>
#include <ocl/smart_ptr.hpp>
#include <ocl/tracked_ptr.hpp>
#include <ocl/unique_socket.hpp>

#ifdef __OCL_FIX

# include <ocl/fix/parser.hpp>
# include <ocl/fix/checksum.hpp>

#endif

#endif // ifndef __OCL_HPP