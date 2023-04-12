#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, h, target, end, start = 0, count = 0, sum = 2000000;
    cin >> N;

    vector<int> list;

    for (int i = 0; i < N; i++) {
        cin >> h;
        list.push_back(h);
    }
    end = N - 1;
    sort(list.begin(), list.end());
    cin >> target;

    while (end > start) {
        sum = list[start] + list[end];
        if (sum == target) count++;
        else if (sum < target) {
            start += 1;
            continue;
        }
        else if (sum > target) {
            end -= 1;
            continue;
        }
        start += 1;
        end -= 1;
    }

    cout << count;
    return 0;
}