#! /bin/sh

## To be used for: curl -fsSL https://install.ocl.nekernel.org | sh

echo "==> WELCOME TO OPEN C++ LIBRARIES."
echo "==> INSTALLING OPEN C++ LIBRARIES..."

sudo apt update
sudo apt install build-essential cmake libboost-dev

git clone --recurse-submodules -j8 https://github.com/ocl-foss/ocl.git
cd ocl
cmake -B build
echo "==> INSTALLING THE OPEN C++ LIBRARIES..."
sudo cmake --install build

echo "==> WELCOME TO NE.APP OPEN C++ LIBRARIES."
echo "==> THANK YOU FOR USING THE OCL!"
