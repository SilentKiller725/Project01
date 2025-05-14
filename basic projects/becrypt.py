from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Example plaintext password
password = 'mysecretpassword'

# Hashing the password
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

print(hashed_password)