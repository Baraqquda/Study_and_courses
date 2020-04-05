#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double a, s = 0, i = 0;
    while (a != 0) {
        cin >> a;
        if (a == 0)break;
        s = s + 1;
        i = i + a;
    }
    cout << fixed << setprecision(11);
    cout << double(i) / s;


    return 0;
}