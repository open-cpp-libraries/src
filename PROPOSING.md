# Proposing New Libraries:

## Abstract

OCL proposals can be done at the following address: [contact@nekernel.org](contact@nekernel.org).

### Note

Freestanding targets are defined using the `OCL_FREESTANDING` macro.

- Verified: Freestanding verified.
- Half-Verified: Some components have been freestanding verified.
- Unverified: Library is not freestanding.

## Acceptance Criterias:

### I: The library must be based on `OCL.Core` (Half-Verified)

### II: The Library must follow a specific structure. (Verified)

```
.github/
include/ocl/<library_name>/detail
include/ocl/<library_name>
test/
example/
.clang-format
.editorconfig
LICENSE
```

### III: The Library must be able to be compiled as header-only, and targeting C++20 or higher. (Verified)

### IV: The Library must include unit tests using a known framework. (GTest, Boost.Test, Catch2). (Unverified)

### V: The Library must contain a Free Software License, such as, the BSD, or BSL license.
