#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, sum = 0;
    vector<int> list, new_list, index;

    for (int i = 0; i < 8; i++) {
        cin >> n;
        list.push_back(n);
    }

    new_list = list;

    sort(new_list.begin(), new_list.end());


    for (int i = 3; i < 8; i++) {
        sum += new_list[i];
        for (int j = 0; j < 8; j++) {
            if (list[j] == new_list[i]) index.push_back(j+1);
        }
    }

    cout << sum << endl;
    sort(index.begin(), index.end());
    for (auto& n : index)
        cout << n << " ";

    return 0;
}