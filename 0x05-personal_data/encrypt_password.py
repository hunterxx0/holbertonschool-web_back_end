#!/usr/bin/env python3
"""
Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string.
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that the provided password matches the hashed password.
    """
    return bcrypt.checkpw(str.encode(password), hashed_password)
