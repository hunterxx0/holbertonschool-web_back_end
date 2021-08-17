#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    Takes in a string and returns salted hash bytes.
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Return a string representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Takes in a string and returns salted hash bytes.
        """
        u = None
        try:
            u = self._db.find_user_by(email=email)
        except Exception:
            pass
        if u:
            raise ValueError("User {} already exists".format(email))
        else:
            u = self._db.add_user(email, _hash_password(password))
            return u

    def valid_login(self, email: str, password: str) -> bool:
        """
        checks if Password is valid
        """
        try:
            u = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), u.hashed_password)

    def create_session(self, email: str) -> str:
        """
        Gives a user a the session ID
        """
        try:
            u = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(u.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Find user by session ID
        """
        try:
            u = self._db.find_user_by(session_id=session_id)
            return u
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys user's session
        """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Returns the reset password token
        """
        try:
            u = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(u.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update password
        """
        try:
            u = self._db.find_user_by(reset_token=reset_token)
            hpass = _hash_password(password)
            self._db.update_user(u.id,
                                 hashed_password=hpass,
                                 reset_token=None)
            return None
        except NoResultFound:
            raise ValueError
