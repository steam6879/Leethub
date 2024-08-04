from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        visited = [False] * len(accounts)
        m = defaultdict(list)
        ans = []

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                m[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return None

            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)

                for neighbor in m[email]:
                    dfs(neighbor, emails)

        for i, account in enumerate(accounts):
            if visited[i]:
                continue

            name, emails = account[0], set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))

        return ans
