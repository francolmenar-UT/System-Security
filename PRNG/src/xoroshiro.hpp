#ifndef AJC_HGUARD_XOROSHIRO128PLUS
#define AJC_HGUARD_XOROSHIRO128PLUS

#include <random>
#include <array>

/**** Parameters used in the Algorithm. Defined by the specification ***/
extern int gen_a = 24;
extern int gen_b = 16;
extern int gen_c = 37;

struct xoroshiro128plus_gen {
private:
    // State: Two unsigned long long int variables
    uint64_t state[2];

    /**
     * Function to rotate to the left the "x" variable by "k"
     *
     * @param x: uint64_t to be left rotated, it will be state[0] or state[1]
     * @param k: input parameter to operate with (gen_a, gen_b or gen_c)
     */
    static inline uint64_t rotl(const uint64_t x, int k) {
        return (x << k) | (x >> (64 - k));
    }


public:
    using result_type = uint64_t;

    result_type operator()();

    void seed(std::function<uint32_t(void)>);

    void seed(const std::array<uint32_t, 4> &);
};

#endif
