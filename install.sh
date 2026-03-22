#! /bin/sh

## To be used for: curl -fsSL https://install.ocl.nekernel.org | sh

git clone --recurse-submodules -j8 git@github.com:ocl-foss-org/ocl.git
cd ocl
cmake -B build
echo "INSTALLING THE OPEN C++ LIBRARIES..."
sudo cmake --install build