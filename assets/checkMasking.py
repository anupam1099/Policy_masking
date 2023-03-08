import re
from assets.config import regex_ChassisMasked, regex_ChassisNotMasked, regex_EngineMasked, regex_EngineNotMasked


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

    for str in Input_List:
        str.strip(' ')
        EngineNo = use_regex(str, regex_EngineNotMasked)
        ChassisNo = use_regex(str, regex_ChassisNotMasked)
        maskedEngineNo = use_regex(str, regex_EngineMasked)
        maskedChassisNo = use_regex(str, regex_ChassisMasked)
        if (EngineNo != None):
            Engine['EngineNo'] = str
        if (ChassisNo != None):
            Chassis['ChassisNo'] = str
        if (maskedEngineNo != None):
            Engine.update({'masked': True, "EngineNo": str})
        if (maskedChassisNo != None):
            Chassis.update({'masked': True, "ChassisNo": str})

    response['Engine'] = Engine
    response['Chassis'] = Chassis
    return response
