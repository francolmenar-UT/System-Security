rm -rf cmake-build-debug
mkdir cmake-build-debug/

cd cmake-build-debug/
cmake ..

cd ../src/python/
python cli.py run -m

python3 cli.py run -m