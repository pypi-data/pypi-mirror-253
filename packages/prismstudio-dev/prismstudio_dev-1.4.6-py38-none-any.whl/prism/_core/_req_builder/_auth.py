import re
import requests
import hashlib
import json
import uuid

import prism
from ..._common.config import *
from ..._utils.exceptions import PrismValueError
from ..._utils import _validate_args, _create_token, get, _delete_token, post
from ..._common import const

__all__ = ['login', 'change_password', 'logout']


@_validate_args
def login(username: str = '', password: str = '', credential_file: str = ''):
    """
    Log in to PrismStudio.

    Parameters
    ----------
        username : str, default ''
            A string representing the username of the user.
        password : str, default ''
            A string representing the password of the user.
        credential_file : str, default ''
            | Provide credential text files.
            | The first line of the file should be username and the second line should be password.
            | Please provide either valid credential file or username and password pair.

    Returns
    -------
        str
            A string with a success message if the login is successful, or **None** if the login fails.
    """
    if not(bool(username or password) ^ bool(credential_file)):
        print("Please provide valid credential!")
        print("You are only allowed to enter a pair of username and password or a credential file with txt extension.")
        return
    if bool(credential_file) & (not(credential_file[-4:] == ".txt")):
        print("Please enter a valid file path. Only txt file is allowed!")
        return
    if password:
        password = hashlib.sha512(password.encode())
        password = password.hexdigest()
    if credential_file:
        try:
            with open(credential_file, 'r') as f:
                username = f.readline().strip()
                password = f.readline().strip()
        except:
            print("Please check credential file path!")
            return
    query = {'username': username, 'password': password}
    req_id = str(uuid.uuid4())[:8]
    headers = {"client": "python", 'requestid': req_id}
    res = requests.post(url=URL_LOGIN, data=query, headers=headers)

    if res.ok:
        _create_token(res)
        smattributes = get(f'{URL_SM}/attributes')
        const.SMValues = {a['attributerepr']: a['attribute'] for a in smattributes}
        const.PreferenceType = get(f'{URL_PREFERENCES}/types')
        const.CategoryComponent = get(URL_CATEGORYCOMPONENTS)
        const.FunctionComponents = get(URL_FUNCTIONCOMPONENTS)
        const.DataComponents = get(URL_DATACOMPONENTS)
        prism.username = username
        result = f'Login success! Welcome {username}'
    else:
        _delete_token()
        print(f"\033[91mLogin Failed\033[0m: {json.loads(res.content).get('message', None)}")
        return

    return result


def logout():
    """
    Log out from PrismStudio.

    Returns
    -------
        str
            A string with a logout message.
    """
    _delete_token()
    prism.username = None
    return 'Logout success!'


def change_password(new_password: str):
    """
    Change password for current user. It requires user to login to the service again with new password.

    Parameters
    ----------
    new_password : str, default ''
        | A new password for current user.
        | Password is minimum 8 characters and must contain at least one uppercase letter, one lowercase letter, one number and one special character.

    Returns
    -------
        str
            A string with a success message if password changing is successful.
    """
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    p = re.compile(regex)
    if not p.match(new_password):
        raise PrismValueError("Password is minimum 8 characters and must contain at least one uppercase letter, one lowercase letter, one number and one special character.")

    password = hashlib.sha512(new_password.encode())
    password = password.hexdigest()
    query = {'username': prism.username, 'password': password}

    # res = requests.post(url=URL_PASSWORD, headers=headers, json=query)
    res = post(url=URL_PASSWORD, params={}, body=query)
    if res.get('status', None) == 'success':
        _delete_token()
        prism.username = None
        return "Password changed successfully! Please login again using new password!"
    return "Failed to get response"

