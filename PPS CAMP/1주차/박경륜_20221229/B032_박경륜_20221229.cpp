#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T, n;
    vector<int> list;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> n;
        list.push_back(n);
    }

    sort(list.begin(), list.end(), greater<int>());

    for (int i = 0; i < T; i++) {
        list[i] += i + 1;
    }

    cout << *max_element(list.begin(), list.end()) + 1 << " ";

    return 0;
}