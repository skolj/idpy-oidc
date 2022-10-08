import copy
from typing import Optional
from typing import Union
from urllib.parse import quote_plus

from cryptojwt import KeyJar
from cryptojwt.key_jar import init_key_jar
from idpyoidc.configure import Configuration

from idpyoidc.impexp import ImpExp


def add_issuer(conf, issuer):
    res = {}
    for key, val in conf.items():
        if key == "abstract_storage_cls":
            res[key] = val
        else:
            _val = copy.copy(val)
            _val["issuer"] = quote_plus(issuer)
            res[key] = _val
    return res


class OidcContext(ImpExp):
    parameter = {"issuer": None}

    def __init__(self, config=None, entity_id=""):
        ImpExp.__init__(self)
        self.entity_id = entity_id or config.get('client_id')
