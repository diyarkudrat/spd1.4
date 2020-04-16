def score(word):

    points_list = [
        ("A, E, I, O, U, L, N, R, S, T", 1),
        ("D, G", 2),
        ("B, C, M, P", 3),
        ("F, H, V, W, Y", 4),
        ("K", 5),
        ("J, X", 8),
        ("Q, Z", 10)]
    
    total_score_dict = {}
    for letters, val in points_list:
        for letter in letters.split(", "):
            total_score_dict[letter] = val
    
    score = 0
    for letter in word.upper():
        score += total_score_dict[letter]

    return score
