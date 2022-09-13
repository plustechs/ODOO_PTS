import json
import requests


def ruc_fetch(ruc):
    _headers = {"Content-Type": "application/json",
                "Accept": "application/json", "Catch-Control": "no-cache"}
    _url_base = "http://35.90.30.141:8888/padron-sunat/ec/gebr/"
    _json_data = {}
    response = requests.post(
        _url_base+ruc, data=json.dumps(_json_data), headers=_headers)
    return response
