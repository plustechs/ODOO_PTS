# -*- coding: utf-8 -*-
# import json (use)
# result = request_model_from_dict(json.loads(json_string)) (load)

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Data:
    ubigeo: Optional[int] = None
    ruc: Optional[int] = None
    nombre_razon_social: Optional[str] = None
    estado_contribuyente: Optional[str] = None
    condicion_domicilio: Optional[str] = None
    tipo_via: Optional[str] = None
    nombre_via: Optional[str] = None
    codigo_zona: Optional[str] = None
    tipo_zona: Optional[str] = None
    numero: Optional[str] = None
    interior: Optional[str] = None
    lote: Optional[str] = None
    departamento: Optional[str] = None
    manzana: Optional[str] = None
    kilometro: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        ubigeo = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("ubigeo"))
        ruc = from_union([from_int, from_none], obj.get("ruc"))
        nombre_razon_social = from_union(
            [from_str, from_none], obj.get("nombreRazonSocial"))
        estado_contribuyente = from_union(
            [from_str, from_none], obj.get("estadoContribuyente"))
        condicion_domicilio = from_union(
            [from_str, from_none], obj.get("condicionDomicilio"))
        tipo_via = from_union([from_str, from_none], obj.get("tipoVia"))
        nombre_via = from_union([from_str, from_none], obj.get("nombreVia"))
        codigo_zona = from_union([from_str, from_none], obj.get("codigoZona"))
        tipo_zona = from_union([from_str, from_none], obj.get("tipoZona"))
        numero = from_union([from_str, from_none], obj.get("numero"))
        interior = from_union([from_str, from_none], obj.get("interior"))
        lote = from_union([from_str, from_none], obj.get("lote"))
        departamento = from_union(
            [from_str, from_none], obj.get("departamento"))
        manzana = from_union([from_str, from_none], obj.get("manzana"))
        kilometro = from_union([from_str, from_none], obj.get("kilometro"))
        return Data(ubigeo, ruc, nombre_razon_social, estado_contribuyente, condicion_domicilio, tipo_via, nombre_via, codigo_zona, tipo_zona, numero, interior, lote, departamento, manzana, kilometro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ubigeo"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.ubigeo)
        result["ruc"] = from_union([from_int, from_none], self.ruc)
        result["nombreRazonSocial"] = from_union(
            [from_str, from_none], self.nombre_razon_social)
        result["estadoContribuyente"] = from_union(
            [from_str, from_none], self.estado_contribuyente)
        result["condicionDomicilio"] = from_union(
            [from_str, from_none], self.condicion_domicilio)
        result["tipoVia"] = from_union([from_str, from_none], self.tipo_via)
        result["nombreVia"] = from_union(
            [from_str, from_none], self.nombre_via)
        result["codigoZona"] = from_union(
            [from_str, from_none], self.codigo_zona)
        result["tipoZona"] = from_union([from_str, from_none], self.tipo_zona)
        result["numero"] = from_union([from_str, from_none], self.numero)
        result["interior"] = from_union([from_str, from_none], self.interior)
        result["lote"] = from_union([from_str, from_none], self.lote)
        result["departamento"] = from_union(
            [from_str, from_none], self.departamento)
        result["manzana"] = from_union([from_str, from_none], self.manzana)
        result["kilometro"] = from_union([from_str, from_none], self.kilometro)
        return result


@dataclass
class ErrorList:
    error_code: Optional[str] = None
    error_message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorList':
        assert isinstance(obj, dict)
        error_code = from_union([from_str, from_none], obj.get("errorCode"))
        error_message = from_union(
            [from_str, from_none], obj.get("errorMessage"))
        return ErrorList(error_code, error_message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["errorCode"] = from_union(
            [from_str, from_none], self.error_code)
        result["errorMessage"] = from_union(
            [from_str, from_none], self.error_message)
        return result


@dataclass
class RequestModel:
    response_code: Optional[int] = None
    error_list: Optional[List[ErrorList]] = None
    datalist: Optional[List[Data]] = None
    data: Optional[Data] = None
    message_errors: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RequestModel':
        assert isinstance(obj, dict)  # check if obj is a json dict
        response_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("responseCode"))
        error_list = from_union([lambda x: from_list(
            ErrorList.from_dict, x), from_none], obj.get("errorList"))
        datalist = from_union([lambda x: from_list(
            Data.from_dict, x), from_none], obj.get("datalist"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        message_errors = from_union(
            [from_str, from_none], obj.get("messageErrors"))
        return RequestModel(response_code, error_list, datalist, data, message_errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["responseCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.response_code)
        result["errorList"] = from_union([lambda x: from_list(
            lambda x: to_class(ErrorList, x), x), from_none], self.error_list)
        result["datalist"] = from_union([lambda x: from_list(
            lambda x: to_class(Data, x), x), from_none], self.datalist)
        result["data"] = from_union(
            [lambda x: to_class(Data, x), from_none], self.data)
        result["messageErrors"] = from_union(
            [from_str, from_none], self.message_errors)
        return result


def request_model_from_dict(s: Any) -> RequestModel:
    return RequestModel.from_dict(s)
