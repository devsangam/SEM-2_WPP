def all_decodings(s):
    def backtrack(idx, path_str, path_nums):
        if idx == len(s):
            results.append((path_str, path_nums.copy()))
            return
        if s[idx] != '0': 
            num = int(s[idx])
            backtrack(idx+1, path_str + chr(ord('A') + num - 1),
                      path_nums + [num])
        if idx+1 < len(s):
            num = int(s[idx:idx+2])
            if 10 <= num <= 26:
                backtrack(idx+2, path_str + chr(ord('A') + num - 1),
                          path_nums + [num])

    results = []
    backtrack(0, "", [])
    return results
message=input("Eeter message:\t")
for decoded, grouping in all_decodings(message):
    print(f"{decoded}\twith grouping {grouping}")
