def validate_uuid(uuid:'str') -> 'str':
    '''
    Функция для проверки валидности УИд.
    Присвоение УИд должно осуществляться в соответствии с приложением 2 к Положению Банка России от 11 мая 2021 года № 758-П 
    «О порядке формирования кредитной истории».
    '''
    import re
    ptrn = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-1[0-9a-fA-F]{3}-[89ab][0-9a-fA-F]{3}-[0-9a-fA-F]{12}-[0-9a-fA-F]'
    try:
        if len(uuid) == 38:
            if re.match(ptrn, uuid.strip().lower()) is not None:
                return 'OK: УИд валидный'
            else:
                return 'Error: УИд не валидный'
        else:
            return 'Error: Длина УИд не равна 38 символов'
    except TypeError:
        return 'Значение УИд может принимать только текстовый формат'