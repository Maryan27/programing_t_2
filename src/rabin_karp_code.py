def rabin_karp(haystack, needle, q):
    n = len(haystack)
    m = len(needle)
    d = 10
    hash_haystack = 0
    hash_needle = 0
    h = d**(m-1) % q  
    
    for i in range(m):
        hash_needle = (d * hash_needle + ord(needle[i])) % q
        hash_haystack = (d * hash_haystack + ord(haystack[i])) % q

    for i in range(n - m + 1):
        if hash_haystack == hash_needle:
            result = True
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    result = False
                    break
            if result:
                return i  
        if i < n - m:
            hash_haystack = (d * (hash_haystack - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
    return -1  
