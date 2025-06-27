#include <iostream>
using namespace std;

void divide(int x,int y) {
  float result;
  try {
    if (y != 0) {
      result = x / y;
      cout << "The result is: " << result << "\n";
    }
    else {
      throw (y);
    }
  }
  catch (int myErr) {
    cout << "DividebyZero error and y value is " << myErr << "\n";
  }

}

int main() {
  int a = 6;
  int b = 0;
  divide(a,b);
  return 0;
}

