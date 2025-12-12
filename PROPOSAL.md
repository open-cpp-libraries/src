# Proposing New Libraries:

## Abstract

OCL proposals can be done at the following address: [contact@nekernel.org](contact@nekernel.org).

## Acceptance Criterias:

### I: The library must be based on `OCL.Core`.

### II: The Library must follow the following structure:

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

### III: The Library must be able to be compiled as header-only, and targeting C++20 or higher.

### IV: The Library must include unit tests using a known framework. (GTest, Boost.Test, Catch2).

### V: The Library must contain a Free Software License, like the BSD, or BSL license.