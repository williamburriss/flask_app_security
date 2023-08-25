# flask_app_security

Created by William Burriss

## password_utils

#### hash_password_custom(password, salt)

```
(function) def hash_password_custom(
    password: str,
    salt: str
) -> str
```

Creates a sha256 hash given a password string and a string of salt.