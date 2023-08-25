# flask_app_security

Created by William Burriss

### Dependencies

    - joserfc


# - password_utils -
#### module: flask_app_security.password_utils

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
from flask_app_security.password_utils import secure_password, validate_password

secured_password = secure_password("password")
string = secured_password.to_string()

validate_password("password", secured_password) # True
validate_password("password", string) # True

validate_password("password wrong", secured_password) # False
validate_password("password wrong", string) # False
```

## validate_login_token

```
(function) def validate_login_token(
    login_token: str,
    _secured_password: Any
) -> (bool | Any)
```

Takes a plain login_token and a Secured_Password and returns
if the login_token is correct.

Note: the Secured_Password can either be an instance of
Secured_Password OR it can be the string returned from
Secured_Password's to_string() method

Example:
```
from flask_app_security.password_utils import secure_password, validate_login_token

secured_password = secure_password("password")
token = secured_password.login_token
string = secured_password.to_string()

validate_login_token(token, secured_password) # True
validate_login_token(token, string) # True

validate_login_token("invalid token", secured_password) # False
validate_login_token("invalid token", string) # False
```

## Secured_Password


```
(class) Secured_Password
```

* ```(method) def __init__(self: Self@Secured_Password, password_hash: Any, salt: Any, login_token: Any) -> None```

Constructor

* ```(method) def to_string(self: Self@Secured_Password) -> str```

Creates a string that can be stored in a database.
This string can later be used to create another
instance of Secured_Password using its static
from_string() method.

* ```(staticmethod) def from_string(string: str) -> Secured_Password```

Creates a Secured_Password instance from a string.
Used to convert the string returned by this class'
to_string() method back into a Secured_Password.

# - session_utils -
#### module: flask_app_security.session_utils

## encode_dict

```
(function) def encode_dict(
    d: dict,
    secret_key: str,
    valid_time_ms: float = -1
) -> str
```

Encodes a python dictionary provided a secret key used to
encode. Takes optional parameter for creating a timed
encode. Meaning the encoded dict will have an expiriation.
This is done by passing the time in ms as the third 
parameter. If no 3rd parameter or -1 is passed, no time
will be set and the encoded dict will not expire.

Example:
```
from flask_app_security.session_utils import encode_dict

secret_key = "my_secret_key"
test_dict = {
    "username": "my_username",
    "email": "myemail@test.com",
    "user_id": 123456789
}

encoded_dict = encode_dict(test_dict, secret_key)

valid_until = 10 * 1000 # 10 seconds (as ms)

encoded_dict_timed = encode_dict(test_dict, secret_key, valid_until)
```

## decode_dict

```
(function) def decode_dict(
    string: str,
    secret_key: str
) -> dict
```

Decodes dict. Works with both timed and non-timed encodes.
Returns None if expired or if invalid secret_key is given.  

Example:
```
from flask_app_security.session_utils import encode_dict, decode_dict

secret_key = "my_secret_key"
test_dict = {
    "username": "my_username",
    "email": "myemail@test.com",
    "user_id": 123456789
}

t = 2 * 1000 # 2 seconds (as ms)

encoded_dict = encode_dict(test_dict, secret_key, t)
decoded_dict = decode_dict(encoded_dict, secret_key) # {"username": "my_username", "email": "myemail@test.com", "user_id": 123456789}
decoded_dict = decode_dict(encoded_dict, "incorrect_secret_key") # None

time.sleep(2.1) # sleeps for 2 seconds, so that the encoded dict will have expired

decoded_dict = decode_dict(encoded_dict, secret_key) # None
```