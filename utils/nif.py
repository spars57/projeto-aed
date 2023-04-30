def validate_nif(nif: int) -> bool:
    try:
        nif = [int(v) for v in str(nif)]

        if not len(nif) == 9:
            return False

        if nif[0] not in [1, 2, 3, 5, 6, 8]:
            return False

        if f"{nif[1]}{nif[2]}" in [45, 70, 71, 72, 77, 79, 90, 91, 98, 99] == False:
            return False

        total = nif[0] * 9 + nif[1] * 8 + nif[2] * 7 + nif[3] * 6 + nif[4] * 5 + nif[5] * 4 + nif[6] * 3 + nif[7] * 2

        return nif[8] == total % 11 == 1 or 0 if total % 11 == 0 else 11 - total % 11
    except IndexError:
        return False
