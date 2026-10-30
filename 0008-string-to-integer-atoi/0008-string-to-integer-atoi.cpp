class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();
        long long num = 0;
        int sign = 1;

        // Skip leading spaces
        while (i < n && s[i] == ' ') {
            i++;
        }

        // Check sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            if (s[i] == '-') sign = -1;
            i++;
        }

        // Convert digits
        while (i < n && s[i] >= '0' && s[i] <= '9') {
            num = num * 10 + (s[i] - '0');

            if (sign * num >= INT_MAX) return INT_MAX;
            if (sign * num <= INT_MIN) return INT_MIN;

            i++;
        }

        return sign * num;
    }
};
