#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    return max(a_dictionary.items(), key=lambda n: n[1])[0]
