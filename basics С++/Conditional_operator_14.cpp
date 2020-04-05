#include <iostream>

using namespace std;

int main() {
    int n, m, x, y, k, l, u, i;
    cin >> n >> m >> x >> y;
    if (n > m) {
        k = n;
        n = m;
        m = k;
    }
    if ((n - x < x) && (n - x < m - y) && (n - x < y)) {
        cout << n - x;
    }
    else if ((x < n - x) && (x < m - y) && (x < y)) {
        cout << x;
    }
    else if ((m - y < x) && (m - y < y) && (m - y < n - x)) {
        cout << m - y;
    }
    else {
        cout << y;
    }
    return 0;
}