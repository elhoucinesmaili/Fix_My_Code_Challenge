#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hashed in MD5
    """

    def __init__(self):
        """
        Initialize a new user with a unique `id`.
        """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """
        Password getter.
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - Set to `None` if `pwd` is not a valid string.
        - Hash `pwd` in MD5 before assigning to `__password`.
        """
        if isinstance(pwd, str):
            self.__password = hashlib.md5(pwd.encode()).hexdigest()
        else:
            self.__password = None

    def is_valid_password(self, pwd):
        """
        Check if the provided password matches the stored hash.
        - Returns `False` for invalid inputs or mismatches.
        """
        if not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Test User")

    # Test unique id
    user_1 = User()
    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    # Test password hashing
    test_password = "myPassword"
    user_1.password = test_password
    assert user_1.password != test_password, "User.password should be hashed"

    # Default password behavior
    assert user_2.password is None, "User.password should be None by default"
    user_2.password = None
    assert user_2.password is None, "User.password should remain None if set to None"
    user_2.password = 89
    assert user_2.password is None, "User.password should be None if set to a non-string"

    # Test password validation
    assert user_1.is_valid_password(test_password), "Valid password check failed"
    assert not user_1.is_valid_password("Fakepwd"), "Invalid password check failed"
    assert not user_1.is_valid_password(None), "None password check failed"
    assert not user_1.is_valid_password(89), "Non-string password check failed"
    assert not user_2.is_valid_password("No pwd"), "Check failed for user with no password set"

    print("All tests passed!")
