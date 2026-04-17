@echo off

## To be used for: curl -fsSL https://install.ocl.nekernel.org | sh

echo "==> WELCOME TO OPEN C++ LIBRARIES."
echo "==> INSTALLING OPEN C++ LIBRARIES..."

git clone --recurse-submodules -j8 https://github.com/ocl-foss/ocl.git

cd ocl
cmake -B build

echo "==> INSTALLING THE OPEN C++ LIBRARIES..."

cmake --install build

echo "==> WELCOME TO OPEN C++ LIBRARIES."
echo "==> THANK YOU FOR USING THE OCL!"
