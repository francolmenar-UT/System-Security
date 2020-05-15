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
      int c = get_C(challenge, i) == 0 ? j : (j + 1) % 2;

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
  // Delay matrix
  int** T = new int*[2];
  T[0] = new int[N] T0;
  T[1] = new int[N] T1;

  #ifdef RANDOM_T
  srand(time(NULL));
  for (int i = 0; i<2; i++)
    for (int j = 0; j < N; j++)
      T[i][j] = rand() T_RAND_PARAM;
  #endif

  #ifdef DEBUG
  std::cout << "Delay matrix T:" << std::endl;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < N; j++) {
      std::cout << T[i][j] << "\t";
    }
    std::cout << std::endl;
  }
  #endif


  // Create a new timing matrix. The +1 is for the final arbiter value
  int** M = new int*[2];
  M[0] = new int[N+1];
  M[1] = new int[N+1];

  // The challenge can be just an int, then each bit is considered as 1 or 0.
  // This way it's easier to generate multiple values
  int challenge = 42;

  std::ofstream out (LOGFILE);

  // Run each simulation
  for (int s = 0; s < SIMULATIONS; s++) {
    challenge = s;
    int output = simulate(T, M, challenge);

    out << "(";
    for (int i = 0; i < N-1; i++)
      out << get_C(challenge, i) << ", ";
    out << get_C(challenge, N-1) << ")"
        << "|" << output << std::endl;
  }

  return 0;
}
