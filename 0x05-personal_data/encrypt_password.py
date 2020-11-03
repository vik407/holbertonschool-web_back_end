#!/usr/bin/env python3
""" 5. Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Salted pass generation
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
