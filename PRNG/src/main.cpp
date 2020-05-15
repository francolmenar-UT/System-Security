#include <iostream>
#include <random>

#include "xoroshiro.hpp"

int main(void) {
    // Create the xoroshiro128+ Generator
    xoroshiro128plus_gen gen;

    // Random device created
    std::random_device dev{};

    // Using xoroshiro128+ generator seed
    gen.seed([&dev]() { return dev(); });

    std::uniform_real_distribution<> dist(0.0, 1.0);

    for (int i = 0; i < 20; i++)
        std::cout << dist(gen) << std::endl;
}


