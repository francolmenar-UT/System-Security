#pragma once

#include <algorithm>
#include <array>
#include <vector>

namespace xorshift {

// Wrapper class for http://xoroshiro.di.unimi.it/xoroshiro128plus.c
    class Xoroshiro128 {
    private:
        std::array<uint64_t, 2> s;

        static inline uint64_t Rotl(const uint64_t x, int k) {
            return (x << k) | (x >> (64 - k));
        }

    public:
        explicit Xoroshiro128(std::array<uint64_t, 2> &seed) : s(seed) {}

        template<typename T>
        static Xoroshiro128 SeedFromRng(T &rng) {
            std::array<uint64_t, 2> a;
            std::generate(a.begin(), a.end(), [rng]() mutable { return rng.Next(); });
            return Xoroshiro128(a);
        }

        uint64_t Next(void) {
            const uint64_t s0 = s[0];
            uint64_t s1 = s[1];
            const uint64_t result = s0 + s1;

            s1 ^= s0;
            s[0] = Rotl(s0, 55) ^ s1 ^ (s1 << 14);  // a, b
            s[1] = Rotl(s1, 36);                    // c

            return result;
        }

        void Jump() {
            static const std::array<uint64_t, 2> JUMP = {0xbeac0467eba5facb,
                                                         0xd86b048b86aa9922};
            uint64_t s0 = 0;
            uint64_t s1 = 0;

            for (size_t i = 0; i < JUMP.size(); i++) {
                for (auto b = 0; b < 64; b++) {
                    if (JUMP[i] & 1ULL << b) {
                        s0 ^= s[0];
                        s1 ^= s[1];
                    }
                    Next();
                }
            }

            s[0] = s0;
            s[1] = s1;
        }

        static const size_t STATE_SIZE = 2;
    };
}
