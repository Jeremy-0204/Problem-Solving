#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    int N, num;
    int count = 0;
    cin >> N;

    vector<int> plug;

    for (int i = 0; i < N; i++) {
        cin >> num;
        plug.push_back(num);
    }
    int sum_of_elems = 0;


    for (auto& n : plug)
        sum_of_elems += n;

    sum_of_elems -= N-1;

    cout << sum_of_elems;



    return 0;
}