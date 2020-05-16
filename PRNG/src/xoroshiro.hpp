#ifndef AJC_HGUARD_XOROSHIRO128PLUS
#define AJC_HGUARD_XOROSHIRO128PLUS

#include <random>
#include <array>

struct xoroshiro128plus_gen {
private:
    // State: Two unsigned long long int variables
    uint64_t state[2];

    /**
     * It performs a Left sift of x by k OR Right sift of x by (k - 1)
     *
     * @param x: uint64_t to be left rotated, it will be state[0] or state[1]
     * @param k: input parameter to operate with (gen_a, gen_b or gen_c)
     */
    static inline uint64_t rotl(const uint64_t x, int k) {
        // Left sift of x by k OR Right sift of x by (k - 1)
        return (x << k) | (x >> (64 - k));
    }


public:
    using result_type = uint64_t;

    constexpr static result_type min() { return 0; }

    constexpr static result_type max() { return -1; }

    result_type operator()();

    void seed(std::function<uint32_t(void)>);

    void seed(const std::array<uint32_t, 4> &);
};

#endif
