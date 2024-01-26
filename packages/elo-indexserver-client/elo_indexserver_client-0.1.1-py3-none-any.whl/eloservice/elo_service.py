import re
from enum import Flag

from attrs import define as define

from eloservice import internal_elo as intern
from eloclient import Client
from eloclient.api.ix_service_port_if import (ix_service_port_if_login, ix_service_port_if_checkin_sord_path,
                                              ix_service_port_if_create_sord, ix_service_port_if_checkout_doc_mask,
                                              ix_service_port_if_checkout_sord, ix_service_port_if_checkin_sord)
from eloclient.models import (BRequestIXServicePortIFLogin, BRequestIXServicePortIFCheckinSordPath,
                              BRequestIXServicePortIFCreateSord, BRequestIXServicePortIFCheckoutDocMask,
                              BRequestIXServicePortIFCheckoutSord, BRequestIXServicePortIFCheckinSord)
from eloclient.models import BResult100361105, BResult2054753789, BResult820228328, BResult5
from eloclient.models import DocMaskZ
from eloclient.models import client_info, EditInfoC, EditInfoZ
from eloclient.models import sord, Sord, SordZ, SordC, LockZ, LockC
from eloclient.types import Response


@define
class Cookie:
    """
    This class is for the cookies in the login process
    """
    key: str
    value: str


@define
class EloConnection:
    """
    This class is the result of the login process
    All needed parameter will be defined and filled during the login to the ELO IX server.
    """
    url: str
    user: str
    password: str
    ci: client_info.ClientInfo
    cookies: list[Cookie] = []


class EloBitSet_editZ(Flag):
    """
    This class is for the EditInfoZ bit set
    To get the needed information from the ELO IX server the needed bit is to set.
    """
    EMPTY = 0
    MASK_NAMES = 1
    PATH_NAMES = 2
    MARKER_NAMES = 4
    MASK = 16


class EloBitSet_sordZ(Flag):
    """
    This class is for the SordZ bit set
    To get the needed information from the ELO IX server the needed bit is to set.
    """
    EMPTY = 0
    SORD = 1

    # def elo_check_data():
    """
    This function checks the retrieved metadata from Weclapp
    :return: The information if the metadata is usable or not
    """


#     data = elo_get_data()
#
#     # Control if the invoice in ELO exists
#     if data['invoiceDate'] != data['createdDate']:  # get Date from ELO
#         logging.info('Dates are not equal --> Need a new version of the invoice')
#
#     else:
#         logging.info('No dates found --> Create new path and invoice')
#
#     # elo_set_folder_name(sordID="4358", folderName="TestFolder", eloConnection="")


def elo_login(url: str, user: str, password: str) -> EloConnection:
    """
    This function is for the connection with ELO responsible and returns the EloConnection class.
    :param url: The URL to the ELO IX server
    :param user: The user for the ELO IX server
    :param password: The password for the ELO IX server user
    :return: EloConnection class
    """
    client = Client(base_url=url,
                    httpx_args={"event_hooks": {"request": [intern._log_request], "response": [intern._log_response]}})

    with client as client:
        # It is important to set the clientInfo object with 'string' and 0 otherwise the login will fail
        clientInfo = client_info.ClientInfo(
            call_id="",
            country="AT",
            language="de",
            ticket="string",
            # format "GMT" + sign + hh + ":" + mm.
            time_zone="GMT+01:00",
            options=0
        )

        login = BRequestIXServicePortIFLogin(
            user_name=user,
            user_pwd=password,
            client_computer="",
            run_as_user="",
            ci=clientInfo
        )

        connection = ix_service_port_if_login.sync_detailed(client=client, json_body=login)
        # In case the request is not correctly formatted the ticket will be this string and not an actual ticket
        if connection.parsed.result.client_info.ticket == "de.elo.ix.client.ticket_from_cookie":
            raise Exception("Login failed - Ticket is not valid")

        # List of tuples
        headers: list[tuple] = connection.headers.raw
        cookies: list[Cookie] = []
        for header in headers:
            if str(header[0]) == "b'Set-Cookie'":
                header_content = str(header[1])
                index_splitter = header_content.find("=")
                header_key, header_value = (header_content[0:index_splitter], header_content[index_splitter + 1:])
                header_value = re.sub(pattern=";.*Path=\\/.*'", repl="", string=header_value)
                header_value = re.sub(pattern=";.*HttpOnly'", repl="", string=header_value)
                header_key = header_key.replace("b'", "")
                cookies.append(Cookie(key=header_key, value=header_value))

        # Swap cookies
        cookies[0], cookies[1] = cookies[1], cookies[0]

        return EloConnection(
            url=url,
            user=user,
            password=password,
            ci=connection.parsed.result.client_info,
            cookies=cookies
        )
    pass


def elo_checkin_sord_path(parent_id: str, path: str, elo_connection: EloConnection) -> Response[BResult100361105]:
    """
    This function creates new folder in ELO
    Depending on the given path it is possible to create 1 or multiple folders.
    :param parent_id: The parent ID from ELO (startpoint foldertree) = "1" (--> "TEST" folder in ELO)
    :param path: The path in ELO to the needed folder/ doc (e.g. = "/Alpha AG/Eingangsrechnungen/2023/November/20/)
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO IX server response of "CheckinSordPath" = the ID of the last created folder
    """
    client = intern._prepare_elo_client(elo_connection)
    sords = intern._split_path_elements(path)

    with client as client:
        body = BRequestIXServicePortIFCheckinSordPath(
            ci=elo_connection.ci,
            parent_id=parent_id,
            sords=sords,
            sord_z=SordZ(SordC().mb_all)
        )

        return ix_service_port_if_checkin_sord_path.sync_detailed(client=client, json_body=body)


def elo_get_all_masks(parent_id: str, mask_id: str, elo_connection: EloConnection) -> Response[BResult820228328]:
    """
    This function retrieves all saved masks from ELO IX server
    :param parent_id: The parent ID from ELO (startpoint foldertree) = "0" (--> root folder in ELO)
    :param mask_id: The mask ID in ELO (existing for all created masks in ELO) = "0" (--> mask "Freie Eingabe" = STD mask)
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO IX server response of "CreateSord" = all masks from ELO
    """
    client = intern._prepare_elo_client(elo_connection)

    editZ = EditInfoZ(EditInfoC().mb_mask_names)
    editZ.sord_z = SordZ()
    editZ.bset = EloBitSet_editZ.MASK_NAMES.value

    with client as client:
        body = BRequestIXServicePortIFCreateSord(
            ci=elo_connection.ci,
            parent_id=parent_id,
            mask_id=mask_id,
            edit_info_z=editZ
        )

        return ix_service_port_if_create_sord.sync_detailed(client=client, json_body=body)


# ELO filtering masks --> getting the mask lines of a specific mask
def elo_checkout_doc_mask_lines(mask_id, elo_connection: EloConnection) -> Response[BResult2054753789]:
    """
    This function retrieves all "doc mask lines" (= all defined form fields of the given mask)
    :param mask_id: The mask ID of the needed mask (look in ELO or use the mask name with "intern._get_the_mask_with_name")
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO IX server response of "CheckoutDocMask" = the form fields of the mask
    """
    client = intern._prepare_elo_client(elo_connection)

    with client as client:
        body = BRequestIXServicePortIFCheckoutDocMask(
            ci=elo_connection.ci,
            mask_id=mask_id,
            doc_mask_z=DocMaskZ(),
            lock_z=LockZ()
        )

        return ix_service_port_if_checkout_doc_mask.sync_detailed(client=client, json_body=body)


def elo_checkout_sord(object_id: int, elo_connection: EloConnection) -> Response[BResult820228328]:
    """
    This function retrieves a SORD object from ELO IX server
    :param object_id: The ID of the needed object in ELO (--> folder, doc)
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO IX server response of "CheckoutSord" = the sord object
    """
    client = intern._prepare_elo_client(elo_connection)

    editZ = EditInfoZ(EditInfoC().mb_sord)
    editZ.bset = EloBitSet_editZ.EMPTY.value
    editZ.sord_z = SordZ(SordC.mb_all)
    editZ.sord_z.bset = EloBitSet_sordZ.SORD.value
    lockZ = LockZ(LockC().yes)

    with client as client:
        body = BRequestIXServicePortIFCheckoutSord(
            ci=elo_connection.ci,
            obj_id=object_id,
            edit_info_z=editZ,
            lock_z=lockZ
        )

        return ix_service_port_if_checkout_sord.sync_detailed(client=client, json_body=body)


#  -> Response[BResult5]
# Matching metadata --> ELO doc mask lines with Weclapp metadata
def elo_matching_metadata(path: str, object_id: int, mask_id: int, doc_mask_lines: [], sord: Sord,
                          elo_connection: EloConnection) -> Response[BResult5]:
    """
    This function matches the metadata recieved from Weclapp with the needed information for the ELO mask
    :param path: The path in ELO to the needed folder/ doc (e.g. = "/Alpha AG/Eingangsrechnungen/2023/November/20/)
    :param object_id: The ID of the needed object in ELO (--> folder, doc)
    :param mask_id: The mask ID of the needed mask (look in ELO or use the mask name with "intern._get_the_mask_with_name")
    :param doc_mask_lines: The form fields from the needed mask
    :param sord: The needed sord object for matching the metadata
    :param elo_connection: The EloConnection class (filled by "elo_login")
    :return: The ELO IX server response of "CheckinSord" = the new sord object with matched form fields
    """
    client = intern._prepare_elo_client(elo_connection)

    # Matching data fields:
    doc_mask_lines[0].default_value = "Treskon GmbH"
    doc_mask_lines[1].default_value = "STANDARD_INVOICE"
    doc_mask_lines[2].default_value = "AR230442"
    doc_mask_lines[3].default_value = "4217"
    doc_mask_lines[4].default_value = "ELO Digital Office AT GmbH"
    doc_mask_lines[5].default_value = "Linz"
    doc_mask_lines[6].default_value = "AT"

    obj_keys: dict = {}
    for i in range(len(doc_mask_lines)):
        obj_keys[doc_mask_lines[i].key] = doc_mask_lines[i].default_value

    """
    docMaskZ = DocMaskZ(DocMaskC().mb_mask_lines)
    docMaskZ.bset = "1"
    unlockZ = LockZ(LockC().yes)
    # unlockZ.bset = "1"

    with (client as client):
        body = BRequestIXServicePortIFCheckinDocMask(
            ci = ci,
            doc_mask = doc_mask_lines,
            doc_mask_z = docMaskZ,
            unlock_z = unlockZ
        )

        return ix_service_port_if_checkin_doc_mask.sync_detailed(client=client, json_body=body)
    
    """

    sord.path = path
    # sord.id = folder_id
    sord.mask = mask_id
    # sord.mask_name = mask_name
    # sord.i_date_iso = datetime.now(tz = None)
    sord.i_date_iso = '14.11.2023, 15:15'
    # sord.obj_keys = obj_keys

    sordZ = SordZ(SordC().mb_all)
    # sordZ.bset = "1"

    # bset_sord
    # yes
    unlockZ = LockZ(LockC().no)

    with client as client:
        body = BRequestIXServicePortIFCheckinSord(
            ci=elo_connection.ci,
            sord=sord,
            sord_z=sordZ,
            unlock_z=unlockZ
        )

        return ix_service_port_if_checkin_sord.sync_detailed(client=client, json_body=body)

    """
    # Maske zuweisen in diesem Schritt!!

    fields[key, displayName] = ELO DOC MASK LINES:
    -------------------------------------------------------------
    0)  key[0] = 'COMPANY'          name[0] = 'Unternehmen'
    1)  key[1] = 'PURDOCTYPE'       name[1] = 'Dokumententyp'
    2)  key[2] = 'PURINVNO'         name[2] = 'Einkaufsrechnung'
    3)  key[3] = 'VENNO'            name[3] = 'Lieferantennummer'
    4)  key[4] = 'VENNAME'          name[4] = 'Lieferantenname'
    5)  key[5] = 'VENCITY'          name[5] = 'Lieferantenort'
    6)  key[6] = 'VENCOUNTRY'       name[6] = 'Lieferantenland'


    jsonStruct{var, value} = metadata WECLAPP:
    --------------------------------------------------------------
    0)  "invoiceAddress": {
            "company":              "Treskon GmbH",
        }
    1)  "purchaseInvoiceType":      "STANDARD_INVOICE",
    2)  "invoiceNumber":            "AR230442",
    3)  "supplierId":               "4217",
    4)  "company":                  "ELO Digital Office AT GmbH",
    5)  "city":                     "Linz",
    6)  "countryCode":              "AT",

    """
    return 0


# ELO create SORD --> new SORD object = TEST
def elo_create_sord(parent_id: str, mask_id: str, edit_info_z, elo_connection: EloConnection) -> Response[
    BResult820228328]:
    client = intern._prepare_elo_client(elo_connection)

    with client as client:
        body = BRequestIXServicePortIFCreateSord(
            ci=elo_connection.ci,
            parent_id=parent_id,
            mask_id=mask_id,
            edit_info_z=edit_info_z
        )

        return ix_service_port_if_create_sord.sync_detailed(client=client, json_body=body)


# ELO checkin SORD --> TEST
def elo_checkin_sord(path: str, maskId: str, elo_connection: EloConnection, ):
    client = intern._prepare_elo_client(elo_connection)
    sords = intern._split_path_elements(path)

    with client as client:
        body = BRequestIXServicePortIFCheckinSord(
            ci=elo_connection.ci,
            sord=sord,
            sord_z=SordZ(SordC().mb_all),
            unlock_z=LockZ(LockC().bset_sord)
        )

    return ix_service_port_if_checkin_sord.sync_detailed(client=client, json_body=body)
