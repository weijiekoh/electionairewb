"""
Lays out each party's positions on policies.
"""

"""
parties:
    0: All India Trinamool Congress
    1: Bharatiya Janata Party
    2: Indian National Congress
    3: Communist Party of India (Marxist)
"""

party_positions = {
    0:{ #AITC
        0:0,
        1:4,
        2:[0, 4, 0, 0, 0],
        3:[4, 4, 4, 2, -4, 0],
        4:[4, 4, 4, 0],
        5:[0, 4, 4, 4],
        6:[4, 2, 4, 0],
        7:[4, 0, 4, 0],
        8:[4, 4, 4, 4, 4],
        9:[4, 4, 4 ,2],
        10:[0, 0, 4, 4],
    },

    1:{ #BJP
        0:0,
        1:2,
        2:[4, 2, 4, 0, 2],
        3:[4, 4, 2, 4, 4, 2,],
        4:[4, 4, 1, 2,],
        5:[0, 4, 4, 4,],
        6:[4, 4, 4, 0,],
        7:[0, 0, 4, 0,],
        8:[4, 4, 2, 2, 4,],
        9:[2, 0, 4, 0,],
        10:[4, 4, 0, 0,],
    },

    2:{ #INC
        0:4,
        1:0,
        2:[4, 0, 4, 4, 0,],
        3:[4, 4, 4, 4, 4, 4,],
        4:[0, 0, 4, 2],
        5:[0, 4, 0, 4,],
        6:[4, 2, 4, 0,],
        7:[4, 0, 4, 0,],
        8:[0, 0, 4, 2, 2,],
        9:[4, 4, 2, 4,],
        10:[0, 0, 0, 0,],
    },

    3:{ #CPIM

        0:4,
        1:4,
        2:[0, 4, 0, 0, 4,],
        3:[2, 0, 2, 0, 4, 2,],
        4:[4, 0, 4, 4,],
        5:[4, 2, 4, 0,],
        6:[4, 0, 2, 0,],
        7:[4, 4, 4, 0,],
        8:[0, 0, 2, 0, 0,],
        9:[4, 4, 0, 4,],
        10:[-4, 0, 4, 4,],
    },
}
