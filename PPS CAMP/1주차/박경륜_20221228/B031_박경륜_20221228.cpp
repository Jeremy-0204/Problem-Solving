#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a, b, N, h, close;
    int min = 1000;

    cin >> a >> b;
    cin >> N;

    vector<int> star;

    for (int i = 0; i < N; i++) {
        cin >> h;
        star.push_back(h);

        int num = abs(b - h);

        if (min >= num) {
            min = num;
            close = h;
        }
    }

    int num1 = abs(b - a);
    int num2 = abs(b - close);

    if (num1 <= num2) cout << num1;
    else if (a == b) cout << 0;
    else cout << num2 + 1;

    return 0;
}