Q_table = {
    (0,0): {0: -5.2, 1: -3.1, 2: -4.0, 3: -2.5},
    (1,0): {0: -4.1, 1: -2.3, 2: -5.0, 3: -1.8},
    (2,0): {0: 1.5, 1: 3.2, 2: 2.1, 3: 0.9},
}

policy = {
    state: max(Q_table[state], key=lambda a: Q_table[state][a])
    for state in Q_table
}

print(policy)