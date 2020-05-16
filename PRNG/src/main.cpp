#include <iostream>
#include <random>
#include <sstream>
#include <bitset>

#include "xoroshiro.hpp"
#include "config.hpp"

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
    for (int i = 0; i < OUTPUT_INSTANCES; i++) {
        // If it is desired to output the total number just leave "gen()" alone

        uint64_t result = gen(); // Calculate the result of the algorithm

        std::bitset <BIT_LENGTH> result_bit(result); // Transform it to a bit string

        std::cout << result_bit << std::endl; // Output the bit string
    }
}


