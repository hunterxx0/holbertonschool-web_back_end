#!/usr/bin/env python3
"""
Auth class for the API
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """
        Creates a Session ID for a user
        """
        sID = super().create_session(user_id)
        if not sID:
            return None
        dt = {'user_id': user_id, 'session_id': sID}
        uSes = UserSession(**dt)
        uSes.save()
        UserSession.save_to_file()
        return sID

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID
        """
        if not session_id:
            return None
        UserSession.load_from_file()
        uSes = UserSession.search(
            {'session_id': session_id}
        )
        if not uSes:
            return None
        uSes = uSes[0]
        time = uSes.created_at + timedelta(seconds=self.session_duration)
        if time < datetime.now():
            return None
        return uSes.user_id

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        """
        sID = self.session_cookie(request)
        if not sID:
            return False
        uID = self.user_id_for_session_id(sID)
        if not uID:
            return False

        ids = UserSession.search({'session_id': sID})
        if not ids:
            return False
        ids = ids[0]
        try:
            ids.remove()
            UserSession.save_to_file()
        except Exception:
            return False
        return True
