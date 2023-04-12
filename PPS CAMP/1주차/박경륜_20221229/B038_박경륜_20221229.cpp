#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, N, L;
    cin >> N >> L;

    int init = L;

    vector<int> list;

    for (int i = 0; i < N; i++) {
        cin >> n;
        list.push_back(n);
    }
    sort(list.begin(), list.end());
    
    for (int i = 0; i < N; i++) {
        if (init < list[0]) {
            break;
        }

        if (L >= list[i]) {
            L++;
        }

        else {
            break;
        }
    }

    cout << L;
    return 0;
}
