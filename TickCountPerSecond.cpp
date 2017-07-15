using namespace std;

// tic is called to start timer
void tic(double &t)
{
  t = (double)getTickCount();
}

// toc is called to end timer
double toc(double &t)
{
  return ((double)getTickCount() - t)/getTickFrequency();
}
