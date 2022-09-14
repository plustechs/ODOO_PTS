# -*- coding: utf-8 -*-
# import json (use)
# result = request_model_from_dict(json.loads(json_string)) (load)

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Data:
    ruc: str
    nombre_razon_social: str
    estado_contribuyente: str
    condicion_domicilio: str
    ubigeo: str
    tipo_via: str
    nombre_via: str
    codigo_zona: str
    tipo_zona: str
    numero: str
    interior: str
    lote: str
    departamento: str
    manzana: str
    kilometro: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        ruc = str(obj.get("ruc"))
        nombre_razon_social = str(obj.get("nombreRazonSocial"))
        estado_contribuyente = str(obj.get("estadoContribuyente"))
        condicion_domicilio = str(obj.get("condicionDomicilio"))
        ubigeo = str(obj.get("ubigeo"))
        tipo_via = str(obj.get("tipoVia"))
        nombre_via = str(obj.get("nombreVia"))
        codigo_zona = str(obj.get("codigoZona"))
        tipo_zona = str(obj.get("tipoZona"))
        numero = str(obj.get("numero"))
        interior = str(obj.get("interior"))
        lote = str(obj.get("lote"))
        departamento = str(obj.get("departamento"))
        manzana = str(obj.get("manzana"))
        kilometro = str(obj.get("kilometro"))
        return Data(ruc, nombre_razon_social, estado_contribuyente, condicion_domicilio, ubigeo, tipo_via, nombre_via, codigo_zona, tipo_zona, numero, interior, lote, departamento, manzana, kilometro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ruc"] = str(self.ruc)
        result["nombreRazonSocial"] = str(self.nombre_razon_social)
        result["estadoContribuyente"] = str(self.estado_contribuyente)
        result["condicionDomicilio"] = str(self.condicion_domicilio)
        result["ubigeo"] = str(self.ubigeo)
        result["tipoVia"] = str(self.tipo_via)
        result["nombreVia"] = str(self.nombre_via)
        result["codigoZona"] = str(self.codigo_zona)
        result["tipoZona"] = str(self.tipo_zona)
        result["numero"] = str(self.numero)
        result["interior"] = str(self.interior)
        result["lote"] = str(self.lote)
        result["departamento"] = str(self.departamento)
        result["manzana"] = str(self.manzana)
        result["kilometro"] = str(self.kilometro)
        return result


@dataclass
class RequestModel:
    response_code: int
    error_list: List[Any]
    data: Data
    message_errors: str

    @staticmethod
    def from_dict(obj: Any) -> 'RequestModel':
        assert isinstance(obj, dict)
        response_code = int(str(obj.get("responseCode")))
        error_list = from_list(lambda x: x, obj.get("errorList"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        message_errors = str(obj.get("messageErrors"))
        return RequestModel(response_code, error_list, data, message_errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseCode"] = str(self.response_code)
        result["errorList"] = from_list(lambda x: x, self.error_list)
        result["data"] = from_union(
            [lambda x: to_class(Data, x), from_none], self.data)
        result["messageErrors"] = str(self.message_errors)
        return result


def request_model_from_dict(s: Any) -> RequestModel:
    return RequestModel.from_dict(s)


def request_model_to_dict(x: RequestModel) -> Any:
    return to_class(RequestModel, x)
