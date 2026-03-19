#! /bin/sh

## To be used for: curl -fsSL https://install.ocl.nekernel.org | sh

ARCH=x64
PROFILE=debug

git clone --recurse-submodules -j8 git@github.com:ocl-foss-org/ocl.git
cd ocl
./updater.sh
