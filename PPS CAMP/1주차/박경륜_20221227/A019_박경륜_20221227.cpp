#include <iostream>
#include <string>

using namespace std;

int main() {
    int a, b, c;
    int count = 0;
    cin >> a;
    cin >> b;
    cin >> c;

    int total = a * b * c;
    string str = to_string(total);

    for (int i = 0; i <= 9; i++) {
        for(int j = 0; j < str.length(); j++)
            if ((char)(i + 48) == str[j]) count++;
        cout << count << endl;
        count = 0;
    }


    return 0;
}