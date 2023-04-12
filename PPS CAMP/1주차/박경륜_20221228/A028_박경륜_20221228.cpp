#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

int main() {
    string num1, num2, answer;
    int sum, carry = 0, remain;
    cin >> num1 >> num2;

    reverse(num1.begin(), num1.end());
    reverse(num2.begin(), num2.end());

    int dif = num1.size() - num2.size();

    for (int i = 0; i < abs(dif); i++) {
        if (dif < 0) num1 = num1 + "0";
        else if (dif > 0) num2 = num2 + "0";
    }

    for (int i = 0; i < num1.size(); i++) {
        sum = int(num1[i] - '0') + int(num2[i] - '0') + carry;
        remain = sum % 10;
        carry = sum / 10;

        answer = answer + char(remain + 48);
    }

    if(carry > 0)   answer = answer + char(carry + 48);

    reverse(answer.begin(), answer.end());
    cout << answer << endl;

    return 0;
}