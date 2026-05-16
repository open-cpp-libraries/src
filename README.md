
![GitHub Stars](https://img.shields.io/github/stars/ocl-foss-org/ocl?style=for-the-badge)

## Quick Install

> [!NOTE]
> On Windows, you will need to use the setup link at:
> `curl -fsSL http://setup.ocl.nekernel.org`.

Install the OCL using the following link:

```sh
curl -fsSL http://install.ocl.nekernel.org | sh
```

## Primers

The primers are available at:

- https://primer.ocl.nekernel.org

## Abstract

Ne.app OCL provides free header-only C++ libraries for usage in C++ software development.

Modules include, a `core` library containing algorithms and containers for C++20 or later.

These libraries were built on top of the Boost C++ libraries and C++ SL.

## Using OCL

This is taken from the FIX module, and will be used here as an example of usage of the OCL.

```cpp
int main(int argc, char** argv)
{
	ocl::fix::visitor	   basic_visitor;
	ocl::fix::range_buffer fix = basic_visitor.visit(default_fix);

	ocl::io::enable_stdio_sync(false);

	ocl::io::print(":key=35\n");
	ocl::io::print(":value=", fix["35"], "\n");
}
```

The OCL are mostly headers only (except OCL.FIX as of 2026), so no compilation step is needed. And is C++17 or later.

## Community

Join the ne.app [discord](https://discord.gg/uD76Qweght), we're quite active there and open for contributors!

## Getting Started

Documentation can be found at: [https://docs.ocl.nekernel.org](https://docs.ocl.nekernel.org).

##### Copyright (c) 2023-2026 Amlal El Mahrouss & OCL Authors, Licensed under the BSL 1.0.
