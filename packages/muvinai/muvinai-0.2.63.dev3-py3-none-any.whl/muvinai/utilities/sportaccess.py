# Crea o modifica usuarios en sportaccess
import requests
import json
from .init_creds import init_mongo, test
from datetime import datetime
from pymongo import ReturnDocument
from .format import fix_bad_characters
from muvinai.utilities.dates import today_argentina, arg_tz

db = init_mongo()

zonas = {
    "Elite": "-1",
    "Total": "1",
    "Plus": "2",
    "Local": "7"
}

sedes = {
    "CORP": "1",
    "ECOM": "900",
    "ALIA": "901",
    "WORK": "1010",
    "MUVI": "900"
}

all_clubes = db.club.find({"sportaccess_id": {"$exists": True}})


# sede_map = {c["sportaccess_id"]: c["name"] for c in all_clubes}
# additional_map = {
#    1: "Corporate",
#    900: "e-Commerce",
#    901: "Alianzas"
# }
# sede_map.update(additional_map)


def crear_usuario_sportclub(cliente: dict, payment_id: int = -1, nivel_de_acceso: str = 'buscar_plan') -> dict:
    """ Crear un usuario en la base de datos de Sportclub

    :param cliente: cliente de mongodb
    :type cliente: dict
    :param payment_id: id del pago de mercadopago
    :type payment_id: str
    :param nivel_de_acceso: nivel de acceso del plan
    :type nivel_de_acceso: str
    :return: los valores posibles son: Elite, Total, Plus, Local, Flex
    :rtype: dict
    """
    db = init_mongo()
    url = "https://apisami.sportclubaccess.com/2.0/socio?"

    plan = db.planes.find_one({"_id": cliente["active_plan_id"]})
    if nivel_de_acceso == 'buscar_plan':
        try:
            nivel_de_acceso = plan['nivel_de_acceso']
        except:
            nivel_de_acceso = 'Total'
    try:
        if plan["sede_local"] is None:
            sede_value = sedes[cliente["sportaccess_id"][0:4]]
        else:
            club = db.club.find_one({"_id": plan["sede_local"]})
            sede_value = club["sportaccess_id"]
    except:
        sede_value = "1"

    if payment_id == -1:
        try:
            payment_id = cliente['payment_ids'][-1]
        except:
            payment_id = 11

    for a in cliente["domicilio"]:
        if not a:
            cliente["domicilio"][a] = "n/a"

    if "nacimiento" not in cliente.keys():
        cliente["nacimiento"] = "22/02/2022"
    elif not cliente["nacimiento"] or cliente["nacimiento"] == "n/a":
        cliente["nacimiento"] = "22/02/2022"

    if "celular" not in cliente.keys():
        cliente["celular"] = "n/a"
    elif not cliente["celular"]:
        cliente["celular"] = "n/a"

    parameters = {
        "username": "3rdPty2902-8891-20",
        "password": "HWXSroa76FSI226JeEtOd9SqDoDXCkGtJyXTk2qEAN2HI34bOVe",
        "nro_socio": cliente["sportaccess_id"],
        "nombre": cliente["nombre"],
        "apellido": cliente["apellido"],
        "documento": cliente["documento"],
        "email": cliente["email"],
        "sexo": "X",
        "nacimiento": cliente["nacimiento"].replace("/", "-"),
        "celular": cliente["celular"],
        "calle": cliente["domicilio"]["calle"] if "calle" in cliente["domicilio"] else 'n/a',
        "numero": cliente["domicilio"]["altura"] if "altura" in cliente["domicilio"] else 'n/a',
        "localidad": cliente["domicilio"]["localidad"] if "localidad" in cliente["domicilio"] else 'n/a',
        "cp": cliente["domicilio"]["código postal"] if "código postal" in cliente["domicilio"] else 'n/a',
        "ciudad": cliente["domicilio"]["localidad"] if "localidad" in cliente["domicilio"] else 'n/a',
        "provincia": cliente["domicilio"]["provincia"] if "provincia" in cliente["domicilio"] else 'n/a',
        "nacionalidad": "Argentino",
        "sede": sede_value,
        "zona": "7" if nivel_de_acceso == "Flex" else zonas[nivel_de_acceso],
        "mp_payment_id": int(payment_id),
        "vigencia": cliente["fecha_vigencia"].strftime("%d-%m-%Y")

    }

    lista = [key + "=" + str(parameters[key]) for key in parameters.keys()]
    querystrings = "&".join(lista)
    if test:
        print("Se saltea el post a sportaccess por ser test.")
        return {"status": True, "message": "No se llamó al servicio por ser TEST."}
    r = requests.post(url + querystrings)
    response = r.json()
    if not response["status"]:
        print("Falló la creación de usuario en bd sporclub")
        print(response["message"])
    else:
        print("Usuario creado satisfactoriamente en bd sportclub")

    return response


def consulta_socio(documento: str) -> dict:
    """ Obtener un socio de la base de datos de sportclub
great
    :param documento: numero de documento del socio que buscado
    :type documento: str
    :return: respuesta de SpAccess (puede ser un socio o un mensaje de error)
    :rtype: dict
    """
    url = "https://apisami.sportclubaccess.com/2.0/members?Documento="
    r = requests.get(url + documento)
    r = r.json()
    try:  # Intento corregir los malos caracteres que puedan tener
        r['data']['Apellido'] = fix_bad_characters(r['data']['Apellido'])
        r['data']['Nombre'] = fix_bad_characters(r['data']['Nombre'])
        r['data']['Direccion'] = fix_bad_characters(r['data']['Direccion'])
    except:
        pass
    # Intenta pasar a datetime la fecha
    try:
        r['data']['Vigencia'] = datetime.strptime(r['data']['Vigencia'], '%d/%m/%Y')
        r['data']["FechaIngreso"] = datetime.strptime(r['data']["FechaIngreso"], '%d/%m/%Y')
    except:
        pass
    # Intenta convertir el apto medico
    try:
        r['data']['AptoMedico'] = datetime.strptime(r['data']['AptoMedico'], '%d/%m/%Y')
    except:
        pass
    return r


def consulta_socio_x_nro_socio(nro_socio: str) -> dict:
    """ Obtener un socio de la base de datos de sportclub

    :param documento: numero de documento del socio que buscado
    :type documento: str
    :return: respuesta de SpAccess (puede ser un socio o un mensaje de error)
    :rtype: dict
    """
    url = "https://apisami.sportclubaccess.com/2.0/members?NroSocio="
    r = requests.get(url + nro_socio)
    r = r.json()
    try:  # Intento corregir los malos caracteres que puedan tener
        r['data']['Apellido'] = fix_bad_characters(r['data']['Apellido'])
        r['data']['Nombre'] = fix_bad_characters(r['data']['Nombre'])
        r['data']['Direccion'] = fix_bad_characters(r['data']['Direccion'])
    except:
        pass
    try:  # Intenta pasar a datetime la fecha
        r['data']['Vigencia'] = datetime.strptime(r['data']['Vigencia'], '%d/%m/%Y')
        r['data']["FechaIngreso"] = datetime.strptime(r['data']["FechaIngreso"], '%d/%m/%Y')
    except:
        pass
    # Intenta convertir el apto medico
    try:
        r['data']['AptoMedico'] = datetime.strptime(r['data']['AptoMedico'], '%d/%m/%Y')
    except:
        pass
    return r


def create_external_user(data: dict) -> dict:
    """ Crear un cliente externo en mongodb

    :param data: datos del socio (estos datos se obtienen de la base de sportclub)
    :type data: dict
    :return: datos del socio con los que se guardo en mongodb
    :rtype: dict
    """

    inv_zonas = {a: b for b, a in zonas.items()}
    na = "Elite" if data["Documento"] in strelites else inv_zonas[str(data["Zona"])]

    nuevo_socio = {
        "sportaccess_id": data["NroSocio"],
        "nivel_de_acceso": na,
        "nombre": data["Nombre"],
        "apellido": data["Apellido"],
        "documento": data["Documento"],
        "email": data["Mail"],
        "domicilio": {
            "calle": data["Direccion"],
            "altura": data["Numero"],
            "apto_lote": data["Piso"],
            "localidad": data["Localidad"],
            "provincia": data["Provincia"],
            "código postal": data["CPostal"]
        },
        "celular": data["Movil"],
        "status": "externo",
        "fecha_vigencia": data["Vigencia"],
        "nacimiento": data["Nacimiento"],
        "last_subscription_date": data["FechaIngreso"],
        "sede": data["Sede"],
        "sede_sqlid": int(data["Sede-SqlId"]),
        "plan": data["Plan"],
        "active_plan_id": None,
        "apto_medico_externo": data["AptoMedico"],
        "brand_name": 'SportClub'
    }
    socio = db.clientes.update_one({"documento": data["Documento"], "sportaccess_id": {"$exists": True}},
                                   {"$set": nuevo_socio}, upsert=True)
    nuevo_socio["_id"] = socio.upserted_id
    return nuevo_socio


def cambio_de_plan(documento: str):
    """ Actualizar en mongodb y en SpAccess el plan del socio

    :param documento: numero de documento del socio al cual se le quiere cambiar el plan
    :type documento: str
    """
    db = init_mongo()
    cliente = db.clientes.find_one({"documento": documento})
    cliente["active_plan"] = "total-mensual"
    cliente["nivel_de_acceso"] = "Total"
    crear_usuario_sportclub(cliente, cliente["last_payment_id"], cliente["nivel_de_acceso"])
    db.clientes.update_one({"documento": documento}, {"$set": cliente})


def update_external_user(data: dict):
    """ Actualizar cliente externo

    :param data: datos que se van a actualizar (tienen que estar las keys: Documento, \
                    Zona, NroSocio, Nombre, Apellido, Documento, Mail, Direccion, Numero, Piso, Localidad,\
                    Provincia, CPostal, Movil, Vigencia, Nacimiento, FechaIngreso)
    :type data: dict
    """
    inv_zonas = {a: b for b, a in zonas.items()}
    na = "Elite" if data["Documento"] in strelites else inv_zonas[str(data["Zona"])]

    socio = {
        "sportaccess_id": data["NroSocio"],
        "nivel_de_acceso": na,
        "nombre": data["Nombre"],
        "apellido": data["Apellido"],
        "documento": data["Documento"],
        "email": data["Mail"],
        "domicilio": {
            "calle": data["Direccion"],
            "altura": data["Numero"],
            "apto_lote": data["Piso"],
            "localidad": data["Localidad"],
            "provincia": data["Provincia"],
            "código postal": data["CPostal"]
        },
        "celular": data["Movil"],
        "status": "externo",
        "fecha_vigencia": data["Vigencia"],
        "nacimiento": data["Nacimiento"],
        "last_subscription_date": data["FechaIngreso"],
        "sede": data["Sede"],
        "sede_sqlid": int(data["Sede-SqlId"]),
        "plan": data["Plan"],
        "active_plan_id": None,
        "apto_medico_externo": data["AptoMedico"],
        "brand_name": 'SportClub'
    }
    return db.clientes.find_one_and_update({"documento": data["Documento"], "brand_name": "SportClub"}, {"$set": socio},
                                           return_document=ReturnDocument.AFTER)


def resolve_external_status(documento):
    _client = db.clientes.find_one({"documento": documento, "brand_name": "SportClub", "email": {"$not": {"$regex": "@migracion"}}})
    if not _client or _client["status"] == "inactivo":
        r = consulta_socio(documento)
        try:
            if r["code"] == 404:
                return "*El DNI ingresado no se encuentra en nuestros registros. " \
                       "Por favor ingresá un DNI válido para continuar."
            elif r["code"] > 299:
                return r["message"]
            else:
                return create_external_user(r["data"])
        except:
            return "El servicio de SportAccess no retorna información válida para este documento."
    elif _client["status"] == "externo":
        r = consulta_socio(documento)
        try:
            if r["code"] == 404:
                return "*El DNI ingresado no se encuentra en nuestros registros. " \
                       "Por favor ingresá un DNI válido para continuar."
            elif r["code"] > 299:
                return r["message"]
            else:
                return update_external_user(r["data"])
        except:
            return "El servicio de SportAccess no retorna información válida para este documento."

    else:
        return _client


def consulta_socio_proclub(documento: str) -> dict:
    """ Obtener un socio de la base de datos de sportclub
great
    :param documento: numero de documento del socio que buscado
    :type documento: str
    :return: respuesta de ProClub (puede ser un socio o None)
    :rtype: dict
    """
    url = "https://apisocios.sportclub.com.ar/members?Documento="
    headers = {
        "x-api-key": "VHGFDn_2212FFF**/-FFFF",
        "Content-Type": "application/json"
    }
    try:
        r = requests.get(url + documento, headers=headers)
        r = r.json()
    except Exception as e:
        print('Se atrapo una excepcion llamando a proclub. ERROR:', str(e))
        return dict()

    try:
        int(r["code"])
    except ValueError:
        print('Error en consulta_socio_proclub. Status code invalido. Respuesta:', r)
        return dict()
    if r["code"] >= 400:
        print('Error en consulta_socio_proclub. status_code =', r["code"], 'Respuesta:', r)
        return dict()
    if not r["data"]:
        print('Error en consulta_socio_proclub. No hay data. status_code =', r["code"], 'Respuesta:', r)
        return dict()

    proclub = r["data"][0]
    if "CredencialSpice" in proclub.keys():
        spice = proclub["CredencialSpice"]
    else:
        spice = None

    sede_socio = db.club.find_one({"sportaccess_id": int(proclub["Sede-SqlId"])})
    if sede_socio:
        sede_id = sede_socio["_id"]
        sede_name = sede_socio["name"]
    else:
        sede_id = "n/a"
        sede_name = "n/a"

    na = proclub["nivel_acceso"].lower()
    fv = datetime.strptime(proclub['Vigencia'], '%d/%m/%Y').replace(tzinfo=arg_tz, hour=15)
    status = "activo" if fv > today_argentina() else "inactivo"

    deuda_promocion, deuda_arancel = 0, 0

    if "QntDeudaPromocion" in proclub.keys():
        deuda_promocion = proclub["QntDeudaPromocion"]
    if "QntDeudaArancel" in proclub.keys():
        deuda_arancel = proclub["QntDeudaArancel"]

    # Intentamos conversión a formato perfilsocio
    socio = {
        "_id": None,
        "status": status,
        "fecha_vigencia": fv,
        "last_subscription_date": datetime.strptime(proclub["FechaIngreso"], '%d/%m/%Y').replace(tzinfo=arg_tz, hour=15),
        "apto_medico": {
            "fecha_vigencia": datetime.strptime(proclub['AptoMedico'], '%d/%m/%Y').replace(tzinfo=arg_tz, hour=15)
        },
        "apellido": proclub["Apellido"],
        "documento": documento,
        "nombre": proclub["Nombre"],
        "email": proclub["Mail"],
        "plan_details": {
            "nivel_de_acceso": na,
            "name": proclub["Plan"],
            "merchant_id": None,
            "sede_local_name": sede_name if na == "local" else None,
            "sede_local": sede_id if na == "local" else None,
            "convenio": proclub["Convenio"],
            "vertical": "Corporativo" if proclub["Convenio"] else "otros"
        },
        "token_spice": spice,
        "seller_merchant": None,
        "externo": True,
        "terceros": proclub["Terceros"],
        "telefono": proclub.get("Telefono"),
        "sede_sqlid": proclub["Sede-SqlId"],
        "sede_socio_name": sede_name,
        "sede_socio": sede_id,
        "proclub_id": proclub["NroSocio"],
        "deuda_promocion": deuda_promocion,
        "deuda_arancel": deuda_arancel
    }

    return socio


def update_spice(nro_socio: str, spice) -> dict:
    """ Obtener un socio de la base de datos de sportclub
great
    :param documento: numero de documento del socio que buscado
    :type documento: str
    :return: respuesta de SpAccess (puede ser un socio o un mensaje de error)
    :rtype: dict
    """
    url = "https://apisocios.sportclub.com.ar/members?NroSocio="
    headers = {
        "x-api-key": "VHGFDn_2212FFF**/-FFFF",
        "Content-Type": "application/json"
    }
    body = {"Credencial_spice": spice}
    r = requests.put(url + nro_socio, headers=headers, data=json.dumps(body))
    return r


strelites = [
"17968603",
"25647644",
"18110621",
"44160654",
"28508245",
"20540023",
"29571882",
"17331567",
"24690984",
"29695864",
"32215977",
"16492982",
"17083952",
"37050158",
"94824571",
"14915216",
"14951519",
"39644268",
"27923183",
"42119189",
"20340280",
"11726199",
"28417781",
"26687480",
"24612588",
"25540482",
"28281063",
"12731772",
"16356582",
"22344506",
"17513343",
"28985800",
"22157614",
"17004744",
"30409905",
"17800734",
"16495297",
"30211271",
"32451066",
"22878693",
"21138738",
"20420715",
"20051366",
"21495716",
"12549464",
"21951202",
"44642281",
"37806138",
"28325919",
"21842834",
"10313318",
"94093103",
"42930040",
"43034077"]
