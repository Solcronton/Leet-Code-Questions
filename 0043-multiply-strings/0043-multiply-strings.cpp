class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.size();
        int m = num2.size();

        if (num1 == "0" || num2 == "0")
            return "0";

        string s(n + m, '0');

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                int n1 = num1[i] - '0';
                int n2 = num2[j] - '0';

                int k = n1 * n2 + (s[i + j + 1] - '0');

                s[i + j + 1] = (k % 10) + '0';
                s[i + j] += k / 10;
            }
        }

        int i = 0;
        while (i < s.size() && s[i] == '0')
            i++;

        return s.substr(i);
    }
};