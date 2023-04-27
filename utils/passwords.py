import bcrypt

salt = bcrypt.gensalt()


def encrypt(password: str) -> str:
    return str(bcrypt.hashpw(bytes(password, 'utf-8'), salt))
