#define N 10
#define SIMULATIONS 1024

//#define N 15
//#define SIMULATIONS 32768

// Delay values
#define T0 {7, 10, 3, 7, 12}
#define T1 {8, 9, 2, 4, 13}

// Random delay values
#define RANDOM_T
#define T_RAND_PARAM % 10 + 1
#define SEED 3

#define DEBUG
//#define DEBUG2

#ifdef DEBUG2
#define DEBUG
#endif

#define LOGFILE "log.txt"
