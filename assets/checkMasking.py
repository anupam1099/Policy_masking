import re
from assets.constants import regex_ChassisMasked, regex_ChassisNotMasked, regex_EngineMasked, regex_EngineNotMasked, regex_Mobile, regex_Email, regex_EmailNotMasked, regex_MobileNotMasked


def use_regex(input_text, regex):
    return re.match(regex, input_text)


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
        EngineNo = use_regex(str, regex_EngineNotMasked)
        maskedEngineNo = use_regex(str, regex_EngineMasked)
        if (EngineNo != None):
            Engine['EngineNo'] = str
        if (maskedEngineNo != None):
            Engine.update({'masked': True, "EngineNo": str})

        # CHASSIS
        ChassisNo = use_regex(str, regex_ChassisNotMasked)
        maskedChassisNo = use_regex(str, regex_ChassisMasked)
        if (ChassisNo != None):
            Chassis['ChassisNo'] = str
        if (maskedChassisNo != None):
            Chassis.update({'masked': True, "ChassisNo": str})

        # MOBILE
        MobileNo = use_regex(str, regex_MobileNotMasked)
        maskedMobileNo = use_regex(str, regex_Mobile)
        if (MobileNo != None):
            Mobile['mobileNo'] = str
        if (maskedMobileNo != None):
            Mobile.update({'masked': True, "mobileNo": str})

        # EMAIL
        email = use_regex(str, regex_EmailNotMasked)
        maskedEmail = use_regex(str, regex_Email)
        if (email != None and Email['email'] == ""):
            Email['email'] = str
        if (maskedEmail != None and Email['email'] == ""):
            Email.update({'masked': True, "email": str})

    # Build Respose
    response['Engine'] = Engine
    response['Chassis'] = Chassis
    response['Email'] = Email
    response['Mobile'] = Mobile
    return response
