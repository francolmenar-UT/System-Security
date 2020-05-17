#include <iostream>
#include <random>
#include <sstream>
#include <bitset>

#include "xoroshiro.hpp"
#include "config.hpp"

int main(int argc, char *argv[]) {
    int output_instances = std::stoi(argv[1]);
    int total_bit_length_C = std::stoi(argv[2]);
    // Calculates the amount of blocks needed rounding up the result
    int blocks = (total_bit_length_C / BLOCK_LENGTH) + (((total_bit_length_C < 0) ^ (BLOCK_LENGTH > 0)) && (total_bit_length_C % BLOCK_LENGTH));

    // Create the xoroshiro128+ Generator
    xoroshiro128plus_gen gen;

    // Random device created
    std::random_device dev{};

    // Seed created
    gen.seed([&dev]() { return dev(); });

    // Normalize the result to output just a bit - It is a bit random generator in this case
    std::uniform_real_distribution<> dist(0.0, 1.0);

    // Generate the random numbers
    for (int i = 0; i < output_instances; i++) {

        for (int j = 0; j < blocks; j++) {
            // If it is desired to output the total number just leave "gen()" alone

            uint64_t result = gen(); // Calculate the result of the algorithm

            std::bitset<BLOCK_LENGTH> result_bit(result); // Transform it to a bit string

            std::cout << result_bit; // Output the bit string
        }
        std::cout << std::endl; // End
    }
}


