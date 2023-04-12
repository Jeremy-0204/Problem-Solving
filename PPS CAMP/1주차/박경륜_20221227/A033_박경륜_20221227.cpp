#include <iostream>
using namespace std;

int main() {
    int total = 0 , max = 0, index = 0;

    for (int i = 1; i <= 5; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        total = a + b + c + d;

        if (max <= total) {
            max = total;
            index = i;
        }
    }

    cout << index <<  " " << max;


    return 0;
}