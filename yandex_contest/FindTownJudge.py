class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        votes = {}
        voters = []
        for i in trust:
            if i[1] not in votes:
                votes[i[1]] = 1
            else:
                votes[i[1]] = votes[i[1]]+1
            voters.append(i[0])
        judge = sorted(votes.items(), key=lambda x: -x[1])
        if judge[0][1] == n-1 and judge[0][0] not in voters:
            return judge[0][0]
        return -1
