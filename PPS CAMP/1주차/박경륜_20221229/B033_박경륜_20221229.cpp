#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, a = 300, b = 60, c = 10;
    vector<int> list;

    cin >> T;

    if (T % c != 0) list.push_back(-1);

    else {
        while (T != 0) {
            list.push_back(T / a);
            T -= a * (T / a);

            list.push_back(T / b);
            T -= b * (T / b);

            list.push_back(T / c);
            T -= c * (T / c);
        }
    }

    for (auto& n : list)
        cout << n << " ";

    return 0;
}