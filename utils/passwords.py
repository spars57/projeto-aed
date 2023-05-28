import bcrypt

salt = b'$2b$12$KgoByXTnp0hVy2DR1l17He'


def encrypt(password: str) -> str:
    return str(bcrypt.hashpw(bytes(password, 'utf-8'), salt))
