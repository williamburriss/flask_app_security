from password_utils import __hash_password_custom__, __gen_salt_custom__, Secured_Password, __gen_login_token__, secure_password, validate_password, validate_login_token
from session_utils import decode_dict, encode_dict
import time

def test___hash_password_custom__():
    hashed = __hash_password_custom__("password", "salt")
    if hashed != "7a37b85c8918eac19a9089c0fa5a2ab4dce3f90528dcdeec108b23ddf3607b99":
        raise Exception("__hash_password_custom__ test failed")
test___hash_password_custom__()

def test___gen_salt_custom__():
    salt = __gen_salt_custom__(10)
    salt2 = __gen_salt_custom__(10)
    failed = len(salt) != 8 and len(salt2) != 10
    if failed:
        raise Exception("__gen_salt_custom__ test failed")
test___gen_salt_custom__()

def test_secured_password():
    failed = False
    secured_password = Secured_Password("password_hash", "salt", "login_token")
    as_string = secured_password.to_string()
    failed = failed or as_string != "password_hash-salt-login_token"

    new_secured_password = Secured_Password.from_string("password_hash-salt-login_token")
    failed = failed or new_secured_password.login_token != "login_token"
    failed = failed or new_secured_password.salt != "salt"
    failed = failed or new_secured_password.password_hash != "password_hash"

    if failed:
        raise Exception("Secured_Password test failed")
test_secured_password()

def test_secure_password():
    failed = False
    secured_password = secure_password("password")
    string = secured_password.to_string()
    failed = failed or not secured_password.__equals__(Secured_Password.from_string(string))

    if failed:
        raise Exception("secure_password test failed")
test_secure_password()

def test_validate_password():
    failed = False
    secured_password = secure_password("password")
    string = secured_password.to_string()
    failed = failed or not validate_password("password", secured_password)
    failed = failed or not validate_password("password", string)

    failed = failed or validate_password("password wrong", secured_password)
    failed = failed or validate_password("password wrong", string)

    if failed:
        raise Exception("validate_password test failed")
test_validate_password()

def test_validate_login_token():
    failed = False
    secured_password = secure_password("password")
    token = secured_password.login_token
    string = secured_password.to_string()

    failed = failed or not validate_login_token(token, secured_password)
    failed = failed or not validate_login_token(token, string)
    failed = failed or validate_login_token("invalid token", secured_password)
    failed = failed or validate_login_token("invalid token", string)

    if failed:
        raise Exception("validate_login_token test failed")
test_validate_login_token()

def test_encode_decode_dict():
    failed = False
    secret_key = "my_secret_key"
    test_dict = {
        "username": "my_username",
        "email": "myemail@test.com",
        "user_id": 123456789
    }
    encoded_dict = encode_dict(test_dict, secret_key)
    decoded_dict = decode_dict(encoded_dict, secret_key)
    failed == failed or (decoded_dict != test_dict)

    decoded_dict_wrong_key = decode_dict(encoded_dict, "wrong_key")
    failed = failed or (decoded_dict_wrong_key is not None)

    if failed:
        raise Exception("encode_decode_dict test failed")
test_encode_decode_dict()

def test_timed_encode():
    failed = False
    secret_key = "my_secret_key"
    test_dict = {
        "username": "my_username",
        "email": "myemail@test.com",
        "user_id": 123456789
    }
    t = 2 * 1000
    encoded_dict = encode_dict(test_dict, secret_key, t)
    decoded_dict = decode_dict(encoded_dict, secret_key)

    failed == failed or (decoded_dict != test_dict)

    time.sleep(2.1)

    decoded_dict_2 = decode_dict(encoded_dict, secret_key)

    failed == failed or (decoded_dict_2 is not None)

    if failed:
        raise Exception("timed_encode test failed")
test_timed_encode()


print("All tests passed")