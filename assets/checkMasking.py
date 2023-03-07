import re


def use_regex(input_text, regex):
    return re.match(regex, input_text)


def maskedChecker(Input_List):
    # masked regex
    regex_EngineMasked = "X{9}[0-9]{5}"
    regex_ChassisMasked = "X{11}[0-9]{5}"

    # unmasked regex
    regex_EngineNotMasked = "[A-Z]{2}[0-9]{2}[A-Z]{5}[0-9]{5}"
    regex_ChassisNotMasked = "[(A-H|J-N|P|R-Z|0-9)]{17}"

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
