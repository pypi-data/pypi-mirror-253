import base64
import logging

from eloclient import Client
from eloclient.models import Sord


"""
 --------------------------------------------------------------
      ELO client - tools and help functions 
 --------------------------------------------------------------    
"""


def _log_request(request):
    """
    This help function logs the requests
    :param request: See "elo_login"
    :return: NOTHING
    """
    logging.debug(f"Request event hook: {request.method} {request.url} - Waiting for response")
    logging.debug(f"Request headers {request.headers}")
    logging.debug(f"Request detail {request.content}")


def _log_response(response):
    """
    This help function logs the responses
    :param response: See "elo_login"
    :return: NOTHING
    """
    request = response.request
    logging.debug(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")


def _split_path_elements(path) -> list[Sord]:
    """
    This help function splits a path in subparts and return the splitte parts
    :param path: A path with "/" separator (e.g. = "/Alpha AG/Eingangsrechnungen/2023/November/20/)
    :return: The subparts of the path = path slices
    """
    path_elements = path.split("/")
    sords = []

    for path_element in path_elements:
        if path_element == "":
            continue
        sord = Sord()
        sord.name = path_element
        sords.append(sord)

    return sords


def _gen_http_basic_hash(user, pw) -> str:
    """
    This help function encode and decode the user and password to base 64 (UTF-8)
    :param user: The user for the ELO IX server
    :param pw: The password for the ELO IX server user
    :return: The encoded and decoded user and password
    """
    return base64.b64encode((user + ":" + pw).encode("utf-8")).decode("utf-8")


def _prepare_elo_client(elo_connection) -> Client:
    """
    This help function prepares the ELO client and returns the client
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO client, ready to work
    """
    client = Client(base_url=elo_connection.url, httpx_args={"event_hooks": {"request": [_log_request], "response": [_log_response]}})
    client = client.with_cookies({"JSESSIONID": elo_connection.ci.ticket + ".ELO-DESKTOP-E6H3J7R-1"})
    client = client.with_headers({
        "Authorization": "Basic " + _gen_http_basic_hash(elo_connection.user, elo_connection.password)
    })

    return client


"""
 --------------------------------------------------------------
      Filtering mask - help functions
 --------------------------------------------------------------    
    1) Types --> Array of masks
    2) By name or id --> The one needed mask
    
"""


def _get_folder_masks(all_masks: []) -> []:
    """
    First function for point 1:

    This function retrieve all masks for folders (folder bit = TRUE)
    :param all_masks: All masks founded on ELO IX server
    :return: All folder masks = Array
    """
    folder_masks: [] = [
        fm for fm in all_masks
        if fm.folder_mask
    ]

    return folder_masks


def _get_document_masks(all_masks: []) -> []:
    """
    This function retrieve all masks for documents (document bit = TRUE)
    :param all_masks: All masks founded on ELO IX server
    :return: All document masks = Array
    """
    document_masks: [] = [
        dm for dm in all_masks
        if dm.document_mask
    ]

    return document_masks


def _get_search_masks(all_masks: []) -> []:
    """
    This function retrieve all masks for searches (search bit = TRUE)
    :param all_masks: All masks founded on ELO IX server
    :return: All search masks = Array
    """
    search_masks: [] = [
        sm for sm in all_masks
        if sm.search_mask
    ]

    return search_masks


def _get_barcode_masks(all_masks: []) -> []:
    """
    Last function for point 1:

    This function retrieve all masks for barcodes (barcode bit = TRUE)
    :param all_masks: All masks founded on ELO IX server
    :return: All barcode masks = Array
    """
    barcode_masks: [] = [
        bm for bm in all_masks
        if bm.barcode_mask
    ]

    return barcode_masks


def _get_the_mask_with_name(all_masks: [], mask_name: str) -> []:
    """
    First function for point 2:

    This function retrieve the mask witch matches with the given name and returns it
    :param all_masks: All masks founded on ELO IX server
    :param mask_name: The needed mask name (= e.g. "Einkaufsrechnungsakte")
    :return: The mask object with the given name = 1 mask object
    """
    mask: [] = [
        m for m in all_masks
        if m.name == mask_name
    ]

    return mask


# Filtering masks --> getting the one and only mask over the id
def _get_the_mask_with_id(all_masks: [], mask_id: int) -> []:
    """
    Last function for point 2:

    This function retrieve the mask witch matches with the given ID and returns it
    :param all_masks: All masks founded on ELO IX server
    :param mask_id: The needed mask ID (= e.g. 76)
    :return: The mask object with the given ID = 1 mask object
    """
    mask: [] = [
        m for m in all_masks
        if m.id == mask_id
    ]

    return mask
