name = "Cultist"
owner = "Nadiah"

# open with a secret handshake, cooperate with fellow cultists, defect against all others

def play(p1_moves, p2_moves, T, R, P, S, delta):

    secret_handshake = [False, False, True]
    n = len(secret_handshake)

    idx = len(p2_moves)

    if idx == 0:

        # first move is first handshake move
        return secret_handshake[idx]

    elif 0 < idx < n:

        # check the partner has done the handshake correctly so far
        if all([a == b for a, b in zip(p2_moves, secret_handshake)]):

            # do the handshake
            return secret_handshake[idx]

        else:

            # if they've made a wrong move, defect
            return False

    else:

        # after that, check for the handshake and verify that all moves after were cooperate
        if all([a == b for a, b in zip(p2_moves, secret_handshake)]) and all(p2_moves[n:]):

            # cooperate with fellow cultist
            return True

        else:

            # defect against all others
            return False

