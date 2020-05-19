#include <fstream>

#include "config.hpp"

#ifdef DEBUG
#include <iostream>
#endif

#ifdef RANDOM_T
#include <cstdlib>
#include <ctime>
#endif


// Get the value of the i-th bit of C
int get_C(int C, int i) {
  int mask = 1 << i;

  return (C & mask) >> i;
}

int simulate(int** T, int**M, int challenge) {
  // Initialize the first 2 values to 0
  M[0][0] = M [1][0] = 0;

  // Iterate over all the multiplexer couples
  for (int i = 1; i < N+1; i++) {
    // For each multiplexer in the couple
    for (int j = 0; j < 2; j++) {
      // if get_C returns 0 keep on the same line, otherwise change
      int c = (j + get_C(challenge, i)) % 2;

      // The timing of this multiplexer is the activation time of the previous
      // multiplexer plus its delay time
      M[j][i] = M[c][i-1] + T[c][i-1];
    }
  }

  // Compute the final output as the fastest signal
  int output = M[0][N] < M[1][N] ? 0 : 1;

  #ifdef DEBUG2
  // Output the matrix
  std::cout << "Challenge bits:" << std::endl;
  for (int i = 0; i < N; i++) {
    std::cout << get_C(challenge, i) << "\t";
  }

  std::cout << std::endl << "M:";
  for (int j = 0; j < N; j++) std::cout <<"\t";
  std::cout <<"Arbiter:" << std::endl;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < N+1; j++) {
      std::cout << M[i][j] << "\t";
    }
    std::cout << std::endl;
  }
  std::cout << "Output: " << output << std::endl;
  #endif

  return output;
}

int main(int argc, char const *argv[]) {
  #ifdef RANDOM_T
  srand(SEED);
  #endif
  // Delay matrices
  int*** Ts = new int**[PUF_NUM];
  for (int p = 0; p < PUF_NUM; p++) {
    Ts[p] = new int*[2];
    Ts[p][0] = new int[N];
    Ts[p][1] = new int[N];

    #ifdef RANDOM_T
    for (int i = 0; i<2; i++)
    for (int j = 0; j < N; j++)
    Ts[p][i][j] = rand() T_RAND_PARAM;
    #endif

    #ifdef DEBUG
    std::cout << "Delay matrix T" << p << ":" << std::endl;
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < N; j++) {
        std::cout << Ts[p][i][j] << "\t";
      }
      std::cout << std::endl;
    }
    #endif
  }


  int*** Ms = new int** [PUF_NUM];
  for (int p = 0; p < PUF_NUM; p++) {
    // Create a new timing matrix. The +1 is for the final arbiter value
    Ms[p] = new int*[2];
    Ms[p][0] = new int[N+1];
    Ms[p][1] = new int[N+1];
  }


  // The challenge can be just an int, then each bit is considered as 1 or 0.
  // This way it's easier to generate multiple values
  int challenge = 42;

  std::ofstream out (LOGFILE);

  // Run each simulation
  for (int s = 0; s < SIMULATIONS; s++) {
    challenge = s;
    int output = simulate(Ts[0], Ms[0], challenge);
    for (int p = 1; p < PUF_NUM; p++){
      int tmp =simulate(Ts[p], Ms[p], challenge);
      output = output ^ tmp;
    }

    #ifdef LOG_CHALLENGE
    out << "(";
    for (int i = 0; i < N-1; i++)
      out << get_C(challenge, i) << ", ";
    out << get_C(challenge, N-1) << ")" << "|";
    #endif
    out << output;
    #ifdef LOG_CHALLENGE
    out << std::endl;
    #endif
    #ifndef LOG_CHALLENGE
    if (  (s+1) % BIT_PER_LINE == 0)
      out << std::endl;
    #endif
  }

  return 0;
}
