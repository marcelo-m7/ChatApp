import ossecret_key = os.getenv("MY_APP_SECRET_KEY")

import osfrom flet.security import encrypt, decryptsecret_key = os.getenv("MY_APP_SECRET_KEY")plain_text = "This is a secret message!"encrypted_data = encrypt(plain_text, secret_key)

import osfrom flet.security import encrypt, decryptsecret_key = os.getenv("MY_APP_SECRET_KEY")encrypted_data = "601llp2zpPp4QjBWe2cOwGdBQUFBQUJqTTFJbmgyWU5jblVp..."plain_text = decrypt(encrypted_data, secret_key)print(plain_text)

