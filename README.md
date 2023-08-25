# flask_app_security

Created by William Burriss

## password_utils

#### Secured_Password

```
(class) Secured_Password
```

#### gen_login_token(length)

```
(function) def gen_login_token(length: int = 32) -> str
```

Creates a token to be stored on the client side to validate login.
This should be used instead of storing the users password directly
on the client side.

#### gen_salt_custom(length)

```
(function) def gen_salt_custom(length: int = 8) -> str
```

Creates a string of random letters and numbers provided a string
length. By default the string will have a length of 8 if no length
is provided.

#### hash_password_custom(password, salt)

```
(function) def hash_password_custom(
    password: str,
    salt: str
) -> str
```

Creates a sha256 hash given a password string and a string of salt.