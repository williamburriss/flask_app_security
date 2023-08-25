# flask_app_security

Created by William Burriss


# flask_app_security.password_utils

## secure_password

```
(function) def secure_password(password: str) -> Secured_Password
```

Secures a password by generating a random string of "salt"
and then hashing the password+salt. This is done to prevent
duplicate passwords from having the same hash. A login_token
is also generated. This should be stored !!SECURELY!! on the
client side for the use of remembering the user. 

Example:
```
from flask_app_security.password_utils import secure_password

password = "my_password"
secured_password_string = secure_password(password).to_string()
```

## validate_password

```
(function) def validate_password(
    password: str,
    _secured_password: Any
) -> (bool | Any)
```

Takes a plain text password and a Secured_Password and returns
if the password is correct.

Note: the Secured_Password can either be an instance of
Secured_Password OR it can be the string returned from
Secured_Password's to_string() method

Example:
```
secured_password = secure_password("password")
string = secured_password.to_string()
validate_password("password", secured_password) # True
validate_password("password", string) # True

validate_password("password wrong", secured_password) # False
validate_password("password wrong", string) # False
```