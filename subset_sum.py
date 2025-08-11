"""
Given a possibly empty list of strictly positive numbers and a non-negative target number, return either a subset of the list summing to the target, or null or a similar empty value if no such subset exists.

The subset must consist of unique ( by index ) list elements.
If a particular value occurs more than once in the input list, you can use it up to as many times as it occurs.
The empty subset sums to 0.
If multiple valid subsets exist, return any one of them.

The target will never be much bigger than the sum of the input list, and often quite a bit smaller.

"""
def subset_sum(xs, target):
    memo = {}
    def dfs(i, t):
        if t == 0:
            return []
        if i >= len(xs) or t < 0:
            return None
        if (i, t) in memo:
            return memo[(i, t)]
        with_curr = dfs(i + 1, t - xs[i])
        if with_curr is not None:
            memo[(i, t)] = [xs[i]] + with_curr
            return memo[(i, t)]
        without_curr = dfs(i + 1, t)
        memo[(i, t)] = without_curr
        return without_curr
    return dfs(0, target)
