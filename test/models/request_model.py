# -*- coding: utf-8 -*-
# import json (use)
# result = request_model_from_dict(json.loads(json_string)) (load)

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(str(x), str)
    return str(x)


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
        ruc = from_str(obj.get("ruc"))
        nombre_razon_social = from_str(obj.get("nombreRazonSocial"))
        estado_contribuyente = from_str(obj.get("estadoContribuyente"))
        condicion_domicilio = from_str(obj.get("condicionDomicilio"))
        ubigeo = from_str(obj.get("ubigeo"))
        tipo_via = from_str(obj.get("tipoVia"))
        nombre_via = from_str(obj.get("nombreVia"))
        codigo_zona = from_str(obj.get("codigoZona"))
        tipo_zona = from_str(obj.get("tipoZona"))
        numero = from_str(obj.get("numero"))
        interior = from_str(obj.get("interior"))
        lote = from_str(obj.get("lote"))
        departamento = from_str(obj.get("departamento"))
        manzana = from_str(obj.get("manzana"))
        kilometro = from_str(obj.get("kilometro"))
        return Data(ruc, nombre_razon_social, estado_contribuyente, condicion_domicilio, ubigeo, tipo_via, nombre_via, codigo_zona, tipo_zona, numero, interior, lote, departamento, manzana, kilometro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ruc"] = from_str(self.ruc)
        result["nombreRazonSocial"] = from_str(self.nombre_razon_social)
        result["estadoContribuyente"] = from_str(self.estado_contribuyente)
        result["condicionDomicilio"] = from_str(self.condicion_domicilio)
        result["ubigeo"] = from_str(self.ubigeo)
        result["tipoVia"] = from_str(self.tipo_via)
        result["nombreVia"] = from_str(self.nombre_via)
        result["codigoZona"] = from_str(self.codigo_zona)
        result["tipoZona"] = from_str(self.tipo_zona)
        result["numero"] = from_str(self.numero)
        result["interior"] = from_str(self.interior)
        result["lote"] = from_str(self.lote)
        result["departamento"] = from_str(self.departamento)
        result["manzana"] = from_str(self.manzana)
        result["kilometro"] = from_str(self.kilometro)
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
        response_code = int(from_str(obj.get("responseCode")))
        error_list = from_list(lambda x: x, obj.get("errorList"))
        data = Data.from_dict(obj.get("data"))
        message_errors = from_str(obj.get("messageErrors"))
        return RequestModel(response_code, error_list, data, message_errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseCode"] = from_str(str(self.response_code))
        result["errorList"] = from_list(lambda x: x, self.error_list)
        result["data"] = to_class(Data, self.data)
        result["messageErrors"] = from_str(self.message_errors)
        return result


def request_model_from_dict(s: Any) -> RequestModel:
    return RequestModel.from_dict(s)


def request_model_to_dict(x: RequestModel) -> Any:
    return to_class(RequestModel, x)
