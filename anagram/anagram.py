def detect_anagrams(word, candidates):
    check_list = []
    for candidate in candidates:
        if is_anagram(word, candidate):
            check_list.append(candidate)
    return check_list

def is_anagram(word, candidate):
    if word.lower() != candidate.lower() and sorted(word.lower()) == sorted(candidate.lower()):
        return True
    else:
        return False
    




        
