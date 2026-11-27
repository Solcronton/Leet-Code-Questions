
class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();

        vector<int> values(n, 1);

        // Calculate free copies
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && items[j][0] % items[i][0] == 0) {
                    values[i]++;
                }
            }
        }

        vector<pair<int, int>> arr;

        for (int i = 0; i < n; i++) {
            arr.push_back({items[i][1], values[i]});
        }

        sort(arr.rbegin(), arr.rend());

        vector<int> dp(budget + 1, -1);
        dp[0] = 0;

        int ans = 0;

        for (auto [price, value] : arr) {

            for (int c = 0; c + price <= budget; c++) {
                if (dp[c] != -1) {
                    int total = dp[c] + value
                              + (budget - price - c) / price;

                    ans = max(ans, total);
                }
            }

            for (int c = budget; c >= price; c--) {
                if (dp[c - price] != -1) {
                    dp[c] = max(dp[c],
                                dp[c - price] + value);
                }
            }
        }

        return ans;
    }
};
