#include <iostream>
#include <random>

#include "xoroshiro.hpp"

const int output_instances = 20; // Amount of random numbers generated

int main(void) {
    // Create the xoroshiro128+ Generator
    xoroshiro128plus_gen gen;

    // Random device created
    std::random_device dev{};

    // Seed created
    gen.seed([&dev]() { return dev(); });

    // Normalize the result to output just a bit - It is a bit random generator in this case
    std::uniform_real_distribution<> dist(0.0, 1.0);

    // Generate the random numbers
    for (int i = 0; i < output_instances; i++)
        // If it is desired to output the total number just leave "gen()" alone
        std::cout << dist(gen) << std::endl;
}


