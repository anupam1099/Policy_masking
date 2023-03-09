from assets.constants import regex_ChassisMasked, regex_ChassisNotMasked, regex_EngineMasked, regex_EngineNotMasked, regex_Mobile, regex_Email, regex_EmailNotMasked, regex_MobileNotMasked
from assets.utils import use_regex


def applyRegex(text, unMaskedRegex, MaskedRegex, key):
    unMaskedText = use_regex(text, unMaskedRegex)
    maskedText = use_regex(text, MaskedRegex)
    response = {
        "masked": False,
        key: ""
    }
    if (unMaskedText != None):
        response[key] = text
    if (maskedText != None):
        response.update({'masked': True, key: text})
    return response


def maskedChecker(Input_List):
    # response build
    response = dict()
    Engine = {
        'masked': False,
        'EngineNo': ""
    }
    Chassis = {
        'masked': False,
        'ChassisNo': ""
    }
    Email = {
        'masked': False,
        'email': ""
    }
    Mobile = {
        'masked': False,
        'mobileNo': ""
    }
    for str in Input_List:
        str.strip(' ')

        # ENGINE
        if (Engine['EngineNo'] == ""):
            Engine = applyRegex(str, regex_EngineNotMasked,
                                regex_EngineMasked, "EngineNo")

        # CHASSIS
        if (Chassis['ChassisNo'] == ""):
            Chassis = applyRegex(str, regex_ChassisNotMasked,
                                 regex_ChassisMasked, "ChassisNo")

        # MOBILE
        if (Mobile['mobileNo'] == ""):
            Mobile = applyRegex(str, regex_MobileNotMasked,
                                regex_Mobile, "mobileNo")

        # EMAIL
        if (Email['email'] == ""):
            Email = applyRegex(str, regex_EmailNotMasked,
                               regex_Email, "email")

    # Build Respose
    response['Engine'] = Engine
    response['Chassis'] = Chassis
    response['Email'] = Email
    response['Mobile'] = Mobile
    return response
