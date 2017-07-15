#include <opencv2/opencv.hpp>

void complicatedThreshold(Pixel &pixel)
{
  // Do something fancy.
}

struct Operator
{
  void operator ()(Pixel &pixel, const int * position) const
  {
    // Perform a simple threshold operation
   	complicatedThreshold(pixel);
  }
};

// >>>>>>>>>>>> Slightly faster than C++11 lambda
for (int n = 0; n < numTrials; n++)
{
  image2.forEach<Pixel>(Operator());
}

// C++11 lambda>
#if __cplusplus >= 201103L || (__cplusplus < 200000 && __cplusplus > 199711L)
  
  for (int n = 0; n < numTrials; n++)
  {
    // Parallel execution using C++11 lambda.
    image3.forEach<Pixel>
    (
      [](Pixel &pixel, const int * position) -> void
      {
        complicatedThreshold(pixel);
      }
     );
  }

#endif
