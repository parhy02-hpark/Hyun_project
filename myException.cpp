#include <iostream>
using namespace std;

int main() {
  try {
    int age = 18;
    if (age >= 18) {
      cout << "Access granted... ";
    } else {
      throw(age);
    }
  }
  catch (int myNum) {
    cout << "Access denied... \n";
    cout << "Age is: " << myNum << endl;
  }
  return 0;
}
