# -*- coding: utf-8 -*-


class MegaException(Exception):
    pass
    
class MegaIncorrectPasswordExcetion(MegaException):
    """
    වැරදි මුරපදයක් හෝ විද්‍යුත් තැපෑලක් ලබා දී ඇත.
    """

class MegaRequestException(MegaException):
    """
    ඉල්ලීමේ දෝෂයක් තිබුණි.
    """
    pass
