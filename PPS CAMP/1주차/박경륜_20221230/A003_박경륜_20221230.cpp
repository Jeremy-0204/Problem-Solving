#include <algorithm>

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int last = digits.size() - 1; // get last index
        int carry = 0; // declare initial carry

        digits[last] += 1; // Plus One

        if (digits[last] > 9) { // Check if last index gets bigger then 9
            reverse(digits.begin(), digits.end()); // reverse the vector for easier calculation

            for(int i = 0; i <= last; i++){
                digits[i] += carry; // add carry with ith number
                carry = 0; // reset carry since we used it
                if(digits[i] > 9){ // if another bigger then 9 happens
                    carry = digits[i] / 10; // recalculate carry
                    digits[i] %= 10; // set ith number again
                }
            }

            
            if (carry > 0 && digits[last] == 0) { 
                // if carry is still one and last index is 0, it meeans we need to push carry into vector
                digits.push_back(carry);
            }
            reverse(digits.begin(), digits.end()); // reverse into original vector
        }
        return digits;
    }
};