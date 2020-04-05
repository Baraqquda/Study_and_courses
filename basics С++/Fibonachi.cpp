#include <iostream>

using namespace std;

int main() {
    int a, i, k, c, n;
    i = 0;
    k = 1;
    c = 1;
    cin >> a;
    if (a == 1)
        cout << '1';
    else
    {
        a = a - 1;
        while (c <= a) {
            n = i + k;
            i = k;
            k = n;
            c = c + 1;
        }
        cout << n;
    }
    return 0;
}