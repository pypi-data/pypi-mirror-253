class Levenshtein:

    def distance(self, s0, s1):

        dp = [[0] * (len(s1) + 1) for _ in range(len(s0) + 1)]

        for i in range(len(s0) + 1):
            dp[i][0] = i
        for j in range(len(s1) + 1):
            dp[0][j] = j

        for i in range(1, len(s0) + 1):
            for j in range(1, len(s1) + 1):
                cost = 0 if s0[i - 1] == s1[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1,
                            dp[i][j - 1] + 1,
                            dp[i - 1][j - 1] + cost)

        return dp[len(s0)][len(s1)]


if __name__ == "__main__":
    d = Levenshtein()
    print(d.distance("Hi", "Hello"))
