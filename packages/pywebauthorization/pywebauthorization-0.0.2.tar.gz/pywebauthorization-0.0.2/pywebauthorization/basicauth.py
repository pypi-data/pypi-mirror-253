from base64 import b64encode, b64decode
from hashlib import sha3_512


# Exception Handlers
class BasicAuthError(BaseException):
    def __init__(self, reason: str):
        super(BasicAuthError, self).__init__(f"Basic Authorization Error: {reason}")


# Methods
def encode(user: str, password: str, use_hashed_password: bool = False) -> str:
    """
    Encode the user and password into Base64 encoded Basic Authorization token
    :param user: (str) The username of the user
    :param password: (str) The password of the user
    :param use_hashed_password: (bool) Flag to indicate password is hashed using SHA3-512 algorithm
    :return: (str | None) The base64 encoded Basic Authorization string
    """
    # Prepare the user_name
    user_name = user

    # Validate the user parameter
    if not user_name:
        raise BasicAuthError('The user parameter was not valid')

    # Prepare the user_password
    user_password = password

    # Validate the password parameter
    if not user_password:
        raise BasicAuthError('The password parameter was not valid')

    # If the flag use_hashed_password then create a SHA3-512 hashed password
    if use_hashed_password:
        try:
            hash_writer = sha3_512()
            encoded_user_password = user_password.encode('utf-8')
            hash_writer.update(encoded_user_password)
            user_password = hash_writer.hexdigest()
        except TypeError as e:
            raise BasicAuthError(f'{e}') from e

    try:
        # Encode the authorization string to byte stream
        encoded_auth = f'{user_name}:{user_password}'.encode('utf-8')

        # Get the Base64 encoded token
        token = b64encode(encoded_auth).decode('utf-8')

    except (TypeError, ValueError, UnicodeEncodeError) as e:
        raise BasicAuthError(f'{e}') from e

    # Validate the token
    if not token:
        raise BasicAuthError('The creation of basic authorization token failed')

    # Return the Basic Authorization String
    return f"Basic {token}"


def decode(authorization: str) -> dict:
    """
    Decode the Basic Authorization string
    :param authorization: Basic Authorization string
    :return: (dict | None)
    """

    # Validate the basic authorization string starts correct prefix
    if not authorization.startswith('Basic'):
        raise BasicAuthError('Invalid basic authorization string')

    # Parse the basic authorization string
    basic_auth_token = authorization.replace('Basic', '').strip()

    # Validate the parsed basic authorization string
    if not basic_auth_token:
        raise BasicAuthError('Invalid basic authorization token')

    # Decode the basic authorization string
    try:
        # Decode the basic authorization string
        basic_auth_bytes = b64decode(basic_auth_token.encode('utf-8'))

        # Decode the basic authorization bytes stream
        basic_auth_string = basic_auth_bytes.decode('utf-8')

        # split the basic authorization string into array
        user_data = basic_auth_string.split(":")

    except (TypeError, ValueError) as e:
        raise BasicAuthError(f'{e}') from e

    # Validate the username
    user_name = user_data[0]
    if not user_name:
        raise BasicAuthError('Invalid basic authorization user')

    # Validate the user password
    user_password = user_data[1]
    if not user_password:
        raise BasicAuthError('Invalid basic authorization password')

    # Build the user data
    user = {'user': user_data[0], 'password': user_data[1]}

    # Return the user dict
    return user


def verify(authorization: str, user: dict, use_hashed_password: bool = False) -> bool:

    # Validate the authorization parameter (str)
    if not authorization:
        # Return failure
        return False

    # Validate the authorization parameter (dict)
    if not user:
        # Return failure
        return False

    # Get the user_name (no empty user_name)
    user_name = user.get('user')

    # Validate the user_name
    if not user_name:
        # Return failure
        return False

    # Get the user_password (no empty user_password)
    user_password = user.get('password')

    # Validate the user_password
    if not user_password:
        # Return failure
        return False

    # Encode the user_name and user_password
    verify_auth = encode(user=user_name, password=user_password, use_hashed_password=use_hashed_password)

    # Validate the verify authorization string
    if not verify_auth:
        # Return failure
        return False

    # Verify the basic authorization string
    # matches the client verified authorization string
    if authorization != verify_auth:
        # Return failure
        return False

    # Return success
    return True


# Explicit Exports
__all__ = ["encode", "decode", "verify", "BasicAuthError"]
