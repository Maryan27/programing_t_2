def rabin_karp(haystack, needle, q):
    text = len(haystack)
    pattern = len(needle)
    d = 10
    hash_haystack = 0
    hash_needle = 0
    h = d**(pattern-1) % q  
    
    for i in range(pattern):
        hash_needle = (d * hash_needle + ord(needle[i])) % q
        hash_haystack = (d * hash_haystack + ord(haystack[i])) % q

    for i in range(text - pattern + 1):
        if hash_haystack == hash_needle:
            if haystack[i:i+pattern] == needle:
                return i  
        if i < text - pattern:
            hash_haystack = (d * (hash_haystack - ord(haystack[i]) * h) + ord(haystack[i + pattern])) % q
    return -1
