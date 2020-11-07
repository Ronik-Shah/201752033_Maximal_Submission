def lengthOfLongestSubstring(s: str) -> int:
    l, res = 0, 0
    map_arr = {}
    for r in range(len(s)):
        if s[r] in map_arr:
            l = max(l, map_arr[s[r]] + 1)
        map_arr[s[r]] = r
        res = max(res, r - l + 1)
    return res


def main():
    s = input("Input a string:")
    print(lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
