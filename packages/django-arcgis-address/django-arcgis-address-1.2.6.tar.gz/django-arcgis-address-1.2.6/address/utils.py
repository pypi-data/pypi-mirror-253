import requests
from django.conf import settings

components = [
    ("country", "Country"),
    ("country_code", "Country"),
    ("locality", "City"),
    ("sublocality", "Nbrhd"),
    ("postal_code", "Postal"),
    ("route", "StName"),
    ("street_number", "AddNum"),
    ("state", "Region"),
    ("district", "Subregion"),
    ("state_code", "RegionAbbr"),
    ("formatted", "LongLabel"),
    ("longitude", "X"),
    ("latitude", "Y"),
]
BATCH_SIZE = 50


def arcgis_to_address(arcgis_address):
    ad = dict([(c[0], arcgis_address["attributes"].get(c[1], "")) for c in components])
    return ad


def get_json_response(keyword, params):
    if keyword == "candidates":
        prefix = "-api"
        suffix = "findAddressCandidates"
    else:
        prefix = ""
        suffix = "geocodeAddresses"
    url = f"https://geocode{prefix}.arcgis.com/arcgis/rest/services/World/GeocodeServer/{suffix}"
    r = (
        requests.get(url, params=params)
        if keyword == "candidates"
        else requests.post(url, params=params)
    )
    r = r.json()
    if not keyword in r or len(r[keyword]) < 1:
        return False
    return r


def geocode_initialization(address_base):
    arcgis_params = {
        "outFields": ",".join([c[1] for c in components]),
        "f": "json",
        "token": settings.ARCGIS_SERVER_API_KEY,
    }
    if not address_base:
        return False
    if settings.ARCGIS_ADDRESS_CATEGORIES:
        arcgis_params["category"] = ",".join(settings.ARCGIS_ADDRESS_CATEGORIES)
    return arcgis_params


def geocode(raw):
    arcgis_params = geocode_initialization(raw)
    if not arcgis_params:
        return raw
    arcgis_params["singleLine"] = raw
    keyword = "candidates"
    json_response = get_json_response(keyword, arcgis_params)
    if not json_response:
        return raw
    arcgis_address = json_response[keyword][0]
    ad = arcgis_to_address(arcgis_address)
    ad["raw"] = raw
    return ad


# geocode addresses in chunks of BATCH_SIZE
def bulk_geocode(list_of_pks_and_raws):
    result = []
    all_successful = True
    for pos in range(0, len(list_of_pks_and_raws), BATCH_SIZE):
        temp_result, succesful = geocode_batch(
            list_of_pks_and_raws[pos : pos + BATCH_SIZE]
        )
        if not succesful:
            all_successful = False
            continue
        result = result + temp_result

    return result, all_successful


# geocode a list of up to BATCH_SIZE
def geocode_batch(list_of_pks_and_raws):
    arcgis_params = geocode_initialization(list_of_pks_and_raws)
    if not arcgis_params:
        return list_of_pks_and_raws, False

    records_list = []
    for pk, raw in list_of_pks_and_raws:
        temp_inner_dict = {"OBJECTID": pk, "SingleLine": raw}
        temp_outer_dict = {"attributes": temp_inner_dict}
        records_list.append(temp_outer_dict)
    arcgis_params["addresses"] = str({"records": records_list})

    keyword = "locations"
    json_response = get_json_response(keyword, arcgis_params)
    if not json_response:
        return list_of_pks_and_raws, False

    dict_of_pks_and_raws = dict(list_of_pks_and_raws)
    list_of_pk_and_addresses = []
    for arcgis_address in json_response[keyword]:
        address = arcgis_to_address(arcgis_address)
        pk = arcgis_address["attributes"].get("ResultID")
        address["raw"] = dict_of_pks_and_raws[pk]
        list_of_pk_and_addresses.append((pk, address))

    return list_of_pk_and_addresses, True
