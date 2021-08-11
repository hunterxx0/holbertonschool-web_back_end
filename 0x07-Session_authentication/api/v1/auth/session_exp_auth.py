#!/usr/bin/env python3
"""
Auth class for the API
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class
    """

    def __init__(self):
        """
        """
        sDur = getenv('SESSION_DURATION')
        try:
            session_duration = int(sDur)
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """
        Creates a Session ID for a user
        """
        sID = super().create_session(user_id)
        if not sID:
            return None
        sDict = {"user_id": user_id,
                 "created_at": datetime.now()}
        self.user_id_by_session_id[sID] = sDict
        return sID

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID
        """
        if not session_id or session_id not in self.user_id_by_session_id:
            return None
        sDict = self.user_id_by_session_id.get(session_id)
        if not sDict:
            return None
        if self.session_duration <= 0:
            return sDict.get('user_id')
        creatd = sDict.get('created_at')
        if not creatd:
            return None
        time = creatd + timedelta(seconds=self.session_duration)
        if time < datetime.now():
            return None
        return sDict.get('user_id')
