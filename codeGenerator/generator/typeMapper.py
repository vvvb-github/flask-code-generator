mapping_table = {
    0: 'Numeric',
    1: 'SmallInteger',
    2: 'Integer',
    3: 'Integer',
    4: 'Float',
    5: 'Float',
    6: 'null',
    7: 'TIMESTAMP',
    8: 'Integer',
    9: 'BigInteger',
    10: 'Date',
    11: 'Time',
    12: 'DateTime',
    13: None,
    14: None,
    15: 'String',
    16: None,
    245: None,
    246: None,
    247: None,
    248: None,
    249: 'Text',
    250: 'Text',
    251: 'Text',
    252: 'Text',
    253: 'String',
    254: 'String',
    255: None
}


def typeMapping(fields):
    result = []
    for field in fields:
        result.append((field[0], mapping_table[field[1]]))
    return result
