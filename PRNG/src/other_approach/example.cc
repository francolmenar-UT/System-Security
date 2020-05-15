#include <algorithm>
#include <chrono>
#include <iostream>
#include <iterator>
#include <vector>

#include "xorshift.hpp"

namespace xs = xorshift;

int main() {
    auto now = []() {
        return std::chrono::system_clock::now().time_since_epoch().count();
    };

    // xoroshiro128
    std::array<uint64_t, 2> state1;
    state1[0] = now();
    state1[1] = now();
    xs::Xoroshiro128 xoro(state1);
    std::vector<uint64_t> v(20);
    std::cout << "Xoroshiro128: " << xoro.Next() << std::endl;

    return 0;
}
