from collections import Counter

def never_decrease(password_candidate):
    password_candidate_str = str(password_candidate)
    return ''.join(sorted(password_candidate_str)) == password_candidate_str

def adjacent_are_the_same(password_candidate):
    password_candidate_str = str(password_candidate)
    return len(set(password_candidate_str)) <= 5

def adjacent_are_the_same_p2(password_candidate):
    password_candidate_str = str(password_candidate)
    return 2 in Counter(password_candidate_str).values()

if __name__ == '__main__':
    input_range = range(359282, 820402)
    possible_password = []

    for password_candidate in input_range:
        if never_decrease(password_candidate) and adjacent_are_the_same(password_candidate):
            possible_password.append(password_candidate)
    part1 = len(possible_password)

    possible_password = []
    for password_candidate in input_range:
        if never_decrease(password_candidate) and adjacent_are_the_same_p2(password_candidate):
            possible_password.append(password_candidate)    
    part2 = len(possible_password)
    
    print(part1)
    print(part2)

