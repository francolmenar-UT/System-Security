#define N 10
#define SIMULATIONS 1024

//#define N 15
//#define SIMULATIONS 32768

// Random delay values
#define RANDOM_T
#define T_RAND_PARAM % 10 + 1
#define SEED 42

#define DEBUG
//#define DEBUG2

#ifdef DEBUG2
#define DEBUG
#endif

#define LOGFILE "log.txt"

// If set log the challenge
//#define LOG_CHALLENGE
// How many bit to print per line if the challenge is not printed
#define BIT_PER_LINE 5242880

// Number of arbiter puf to combile
#define PUF_NUM 25
