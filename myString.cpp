#include <iostream>
#include <string>
using namespace std;

int main() {
  int x = 3;
  int y = 4;
  string myStr = "This string";

  cout << (x < y);
  cout << endl;
  myStr.append(" is testing...  ");
  cout << myStr << endl;
  return 0;
}
