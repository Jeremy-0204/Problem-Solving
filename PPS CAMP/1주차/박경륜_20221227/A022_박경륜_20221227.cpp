#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, N, sumY = 0, sumM = 0, resultY = 0, resultM = 0;
    cin >> N;
    vector<int> time;

    for (int i = 0; i < N; i++) {
        cin >> n;
        time.push_back(n);
    }

    for (int i = 0; i < N; i++) {
        // ¿µ½Ä
        if (time[i] / 29 >= 1 && time[i] % 29 >= 1) resultY = time[i] / 30 * 10 + 10;
        else if (time[i] / 29 >= 1 && time[i] % 29 == 0) resultY = time[i] / 30 * 10;
        else if (time[i] / 29 < 1) resultY = 10;

        if (time[i] / 59 >= 1 && time[i] % 59 >= 1) resultM = time[i] / 60 * 15 + 15;
        else if (time[i] / 59 >= 1 && time[i] % 59 == 0) resultM = time[i] / 60 * 15;
        else if (time[i] / 59 < 1) resultM = 15;

        sumY += resultY;
        sumM += resultM;
    }

    if (sumY < sumM) cout << "Y" << " " << sumY;
    else if (sumY == sumM) cout << "Y" << " " << "M" << " " << sumY;
    else cout << "M" << " " << sumM;

    return 0;
}