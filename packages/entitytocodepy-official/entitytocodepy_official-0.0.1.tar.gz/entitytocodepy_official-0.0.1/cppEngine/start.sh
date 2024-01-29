rm -rf build
mkdir build
cd build 
cmake ..
cd ..
cmake --build build/ -j4
build/omanyte
