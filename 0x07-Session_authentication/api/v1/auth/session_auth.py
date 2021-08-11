#!/usr/bin/env python3
"""
Auth class for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user
        """
        if not user_id or type(user_id) != str:
            return None
        sessionId = str(uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if not session_id or type(session_id) != str:
            return None
        session = self.user_id_by_session_id.get(session_id)
        if not session:
            return None
        return session

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        sID = self.session_cookie(request)
        if not sID:
            return None
        uID = self.user_id_by_session_id.get(sID)
        return User.get(uID)
