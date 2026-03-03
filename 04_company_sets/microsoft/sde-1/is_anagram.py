def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    track = {}
    for chr in s:
        track[chr] = track.get(chr, 0) + 1
    
    for chr in t:
        if chr not in track:
            return False
        track[chr] -= 1
        if track[chr] < 0:
            return False
    
