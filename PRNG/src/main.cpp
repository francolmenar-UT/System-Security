#include <iostream>
#include <random>
#include <sstream>
#include <bitset>


#include "xoroshiro.hpp"

using namespace std;

const int output_instances = 1; // Amount of random numbers generated
const int bit_number = 50; // Length of the bit string output

int main(void) {
    // Create the xoroshiro128+ Generator
    xoroshiro128plus_gen gen;

    // Random device created
    random_device dev{};

    // Seed created
    gen.seed([&dev]() { return dev(); });

    // Normalize the result to output just a bit - It is a bit random generator in this case
    uniform_real_distribution<> dist(0.0, 1.0);

    // Generate the random numbers
    for (int i = 0; i < output_instances; i++) {
        // If it is desired to output the total number just leave "gen()" alone

        uint64_t result = gen(); // Calculate the result of the algorithm

        bitset<bit_number> result_bit (result); // Transform it to a bit string

        cout << result_bit << endl; // Output the bit string
    }
}


