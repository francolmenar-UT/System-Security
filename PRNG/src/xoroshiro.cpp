#include "xoroshiro.hpp"

xoroshiro128plus_gen::result_type
xoroshiro128plus_gen::operator()() {
    // Copying state to operate with it
    const uint64_t s0 = state[0];
    uint64_t s1 = state[1];

    // Sum of the states
    const uint64_t result = s0 + s1;

    s1 ^= s0;

    // Update the states
    state[0] = rotl(s0, gen_a) ^ s1 ^ (s1 << gen_b);
    state[1] = rotl(s1, gen_c);

    return result;
}

void xoroshiro128plus_gen::seed(std::function<uint32_t(void)> f) {
    uint64_t x_0 = f();
    uint64_t x_1 = f();
    state[0] = (x_0 << 32) | x_1;
    x_0 = f();
    x_1 = f();
    state[1] = (x_0 << 32) | x_1;
}

void xoroshiro128plus_gen::seed(const std::array<uint32_t, 4> &a) {
    state[0] = ((uint64_t) a[0] << 32) | (uint64_t) a[1];
    state[1] = ((uint64_t) a[2] << 32) | (uint64_t) a[3];
}

