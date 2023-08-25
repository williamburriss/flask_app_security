# flask_app_security

Created by William Burriss

# password_utils

### secure_password

```
(function) def secure_password(password: str) -> Secured_Password
```

Secures a password by generating a random string of "salt"
and then hashing the password+salt. This is done to prevent
duplicate passwords from having the same hash. A login_token
is also generated. This should be stored !!SECURELY!! on the
client side for the use of remembering the user. 