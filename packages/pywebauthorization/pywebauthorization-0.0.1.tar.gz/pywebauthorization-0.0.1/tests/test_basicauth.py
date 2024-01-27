import pytest
import base64
from hashlib import sha3_512
from pywebauthorization.basicauth import encode, decode, verify, BasicAuthError


@pytest.mark.describe("Test the pywebauthorization.encode")
def test_basic_auth_encode_good_user_password():
    # Test 1 - basicauth.encode with good user/password
    username = 'test'
    password = 'password'
    encoded_auth = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
    expected = f"Basic {encoded_auth}"
    actual = encode(username, password)
    assert actual == expected


@pytest.mark.describe("Test the pywebauthorization.encode using use_hashed_password=True")
def test_basic_auth_encode_good_user_password_with_use_hashed_password():
    # Test 1 - basicauth.encode with good user/password
    username = 'test'
    password = 'password'
    sha3512_writer = sha3_512()
    sha3512_writer.update(password.encode('utf-8'))
    encoded_auth = base64.b64encode(f"{username}:{sha3512_writer.hexdigest()}".encode('utf-8')).decode('utf-8')
    expected = f"Basic {encoded_auth}"
    actual = encode(username, sha3512_writer.hexdigest())
    assert actual == expected


@pytest.mark.describe("Test the pywebauthorization with bad username")
def test_basicauth_encode_bad_username():
    # Test 2 - basicauth.encode with bad user
    username = ''
    password = 'test'
    try:
        encode(username, password)
        pytest.fail()
    except BasicAuthError:
        assert 1 == 1


@pytest.mark.describe("Test the pywebauthorization with bad password")
def test_basicauth_encode_bad_password():
    # Test 2 - basicauth.encode with bad user
    username = 'test'
    password = ''
    try:
        encode(username, password)
        pytest.fail()
    except BasicAuthError:
        assert 1 == 1


@pytest.mark.describe("Test the pywebauthorization.decode good authorization string")
def test_basic_auth_decode_good_auth_string():
    expected = {'user': 'test', 'password': 'password'}
    # Build the authorization string
    authorization = encode(expected.get('user'), expected.get('password'))
    # Validate the authorization string is valid
    if not authorization:
        pytest.fail()
    # Build the decoded string
    actual = decode(authorization=authorization)
    # Validate that all keys match the expected keys decoded
    for k in expected:
        assert actual[k] == expected[k]


@pytest.mark.describe("Test the pywebauthorization.decode bad authorization string")
def test_basic_auth_decode_bad_auth_string():
    expected = {'user': 'test', 'password': 'password'}
    authorization = encode(expected.get('user'), expected.get('password'))
    # validate the authorization string was built
    if not authorization:
        pytest.fail()

    # Convert to lower case
    try:
        decode(authorization=authorization.lower())
        pytest.fail()
    except BasicAuthError:
        assert 1 == 1


@pytest.mark.description("Test the pywebauthorization.verify with good authorization string")
def test_basic_auth_verify_good_authorization_string():
    expected = True
    authorization = 'Basic dGVzdDpwYXNzd29yZA=='
    user = {'user': 'test', 'password': 'password'}
    actual = verify(authorization=authorization, user=user)
    assert actual == expected
