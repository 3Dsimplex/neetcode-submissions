#include <cctype>
class Solution {
public:
    bool isNotAlphanumeric(char letter) {
        if (('A' <= letter) and (letter <= 'Z')) return false;
        if (('a' <= letter) and (letter <= 'z')) return false;
        if (('0' <= letter) and (letter <= '9')) return false;
        return true;
    }

    bool isPalindrome(string s) {
        bool ans = true;
        int left = 0; int right = s.size() - 1;
        while (left < right){
            if (isNotAlphanumeric(s[left])) {
                left++;
                continue;
            }
            if (isNotAlphanumeric(s[right])) {
                right --;
                continue;
            }
            if (tolower(s[left]) != tolower(s[right])) ans = false;
            left++; right--;
        }
        return ans;
    }
};
