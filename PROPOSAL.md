# Proposing New Libraries:

## Abstract

Proposals can be done at [contact@nekernel.org](contact@nekernel.org). 
The library must be based on `OCL.Core` and must respect the following criteras:

## The Library must follow this structure:

```
.github/
examples/
include/ocl/<library_name>/detail
include/ocl/<library_name>
tests/
.clang-format
.editorconfig
LICENSE
```

## The Library must be able to be compiled as header-only, and targeting C++20 or higher.

## The Library must include unit tests using a known framework. (GTest, Boost.Test, Catch2).

## The Library must contain a Free Software License, like the BSD, or BSL license.