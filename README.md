# flask_app_security

Created by William Burriss

## password_utils

#### Secured_Password

```
(class) Secured_Password
```

Secures a users password, see ```__init__``` below

#### Secured_Password()

```
(method) def __init__(
    self: Self@Secured_Password,
    password_hash: Any,
    salt: Any,
    login_token: Any
) -> None
```

Creates instance of secured password.
Secured_Password contains 3 fields:
    - password_hash
    - salt
    - login_tokena

#### secured_password_instance.to_string()

```
(method) def to_string(self: Self@Secured_Password) -> str
```

Creates a string that can be stored in a database (or elsewhere).
This string can later be used to create another
instance of Secured_Password using its static
from_string() method.

#### Secured_Password.from_string()
```
@staticmethod
(method) def from_string(string: str) -> Secured_Password
```

Creates a Secured_Password instance from a string.
Used to convert the string returned by this class'
to_string() method back into a Secured_Password.

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