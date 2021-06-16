def handleQuoutes():
    inputsDir = 'corpus'
    outputDir = 'new_output'
    txtVi = "vi-unicode.txt"
    txtBana = "bana-vni2unicode.txt"
    txtViFile = open(inputsDir + '/' + txtVi, encoding='utf-8', errors='ignore').read()
    txtBanaFile = open(inputsDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()

    txtViFile = txtViFile.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("\n ", "\n")
    txtBanaFile = txtBanaFile.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("\n ", "\n")
    with open(outputDir + '/lang-vi-radio.txt', 'w', encoding='utf-8') as f:
        f.write(txtViFile)
    with open(outputDir + '/bana-vni2unicode.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaFile)


def transform2Kriem():
    radioContentMap = {
        'pôlok': 'pơlĕi',
        'pôloêk': 'pơlĕi',
        'pôtaêm': 'pơtăm',
        'uê': 'ŭ',
        ' huyeân': ' huên',
        ' Huyeân': ' Huên',
        '\nHuyeân': '\nHuên',
        'tröêk': 'trưk',
        'adring': 'adrĭng',
        'ñe hôyoh': 'đe hơ\'yoh',
        'Ñôêng roêng': 'Đưng rŏng',
        'ñôêng roêng': 'đưng rŏng',
        'xaõ': 'sa',
        'aõit': 'axit',
        'tơpalh': 'tơblah',
        'eÊâ': 'ê̆',
        'ø': '',
        'aï': 'a',
        'eã': 'ê',
        'uõ': 'ŭ',
        'uù': 'u',
        'oei': 'uĕi',
        'ôi': 'ơĭ',
        'ôêi': 'ơĭ',
        'ÔÊi': 'Ơĭ',
        'Ôêi': 'Ơĭ',
        'aê': 'ă',
        'ôê': 'ơ̆',
        'ñ': 'đ',
        'Ñ': 'Đ',
        'Uê': 'Ŭ',
        'ei': 'ĕi',
        'eêi': 'ĕi',
        'oê': 'ŏ',
        'iê': 'ĭ',
        'eâ': 'ê',
        'eä': 'ê',
        'ô': 'ơ',
        'Ô': 'Ơ',
        'oâ': 'ô',
        'öê': 'ư',
        'eê': 'ê',
        'ö': 'ư',
        'aâ': 'â',
        # 'i': 'ĭ',
    }

    inputDir = 'new_output'
    outputDir = 'new_output'
    txtBana = 'lang-bana-radio.txt'
    txtBanaContent = open(inputDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()
    txtBanaTransformed = txtBanaContent
    for key, value in radioContentMap.items():
        print(key, '->', value)
        txtBanaTransformed = txtBanaTransformed.replace(key, value)


    contentSpecialMap = {
        'đi đăng': 'đĭ đăng',
        'Bi thư': 'Bĭ thư',
        'bi thư': 'bĭ thư',
        'trŭng': 'jrŭ',
        'đuoÊâi': 'đuôĭ',
        # 'đuôÊi': 'đuôĭ',
        # 'kruôÊi': 'kruôĭ',
        'ôÊih': 'ôih',
        'ôÊi ': 'uôĭ ',
        'kruôi': 'kruôĭ',
        'đuôi': 'đuôĭ',
        'oêng': 'weng',
        'oeng': 'weng',
        'ksôÊ': 'ksô',
        'caùch mang': 'cach mang',
        'chpuôih': 'chơpuih',
        'd/c': 'đ/c',
        'ji ': 'jĭ ',
        'ji,': 'jĭ,',
        'ji\n': 'jĭ\n',
        'kjung': 'kơjung',
        'adrêÊch': 'adrêch',
        '\'bôÊ': '\'bŏ',
        ' xa ': ' sa ',
        'Xa ': 'Sa ',
        'xa,': 'Sa,',
        ' xa\n': ' sa\n',
        ' xa:': ' sa:',
        ' xa;': ' sa;',
        '(xa ': '(sa ',
        ' xa.': ' sa.',
        ' xa…': ' sa…',
        'jêÊ': 'jê̆',
        'ksoÊâ': 'ksô',
        'alêÊ': 'alê̆',
        'amnê': 'amrĕ',
        ' ngam ': ' \'ngam ',
        ' ngam\n': ' \'ngam\n',
        ' ngam,': ' \'ngam,',
        'cuû caûi': '\'bum cai',
        'lyê': 'ly',
        'AÙN1': 'ANS1',
        'hoù,': 'hoa,',
        'ù': '',
        'Sơùnư': 'Sơn',
        'yok': '\'yŏk',
        'Bơghê': 'Bơgê',
        'bơghê': 'bơgê',
        'Nghò': 'Nghi',
        'kuyet': 'kuyêt',
        'nghi quyêt': 'nghi kuyêt',
        'truy quyet': 'truy quet',
        'Quyêt': 'Kuyêt',
        'quêt': 'quet',
        ' yŏk': ' \'yŏk',
        'nnghê': 'nghê',
        '\nNăr': '\n\'Năr',
    }

    for key, value in contentSpecialMap.items():
        print(key, '->', value)
        txtBanaTransformed = txtBanaTransformed.replace(key, value)

    with open(outputDir + '/lang-radio-new.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaTransformed)


def transform2KriemNew():
    contentMap = {
        'liêt sit': 'liet si',
        'đi đăng': 'đĭ đăng',
        'Điê đăng': 'Đĭ đăng',
        'điê đăng': 'đĭ đăng',
        'điê ': 'đĭ ',
        'điêê': 'đĭ',
        'ơêi': 'ơĭ',
        'ơê': 'ơ̆',
        'ƠÊi': 'Ơĭ',
        ' ơi': ' ơĭ',
        'Ơi': 'Ơĭ',
        'chiênh': 'chĭnh',
        'Adriêng': 'Adrĭng',
        'adriêng': 'adrĭng',
        'kiêa': 'kĭa',
        'jiê': 'jĭ',
        'biê ': 'bĭ ',
        'eê': 'ĕ',
        'eÊâ': 'ê̆',
        'êÊ': 'ê̆',
        'EÊ': 'Ĕ',
        'uê': 'ŭ',
        'UÊ': 'Ŭ',
        'ưê': 'ư̆',
        'oÊâ': 'ô̆',
        ' yoêk': ' \'yŏk',
        'oê': 'ŏ',
        'ôê': 'ô̆',
        'ôÊ': 'ô̆',
        'ÁN1': 'ANS1',
        'oeng': 'weng',
        'ôÊih': 'ôih',
        'uôÊi ': 'uôĭ ',
        'kruôi': 'kruôĭ',
        'đuôi': 'đuôĭ',
        'bone': 'bơne',
        'Dơno': 'Dơnŏ',
        'dơno': 'dơnŏ',
        'dơ no': 'dơnŏ',
        'Dơ no': 'Dơ nŏ',
        'nghiê ': 'nghĭ ',
        # 'ksôÊ': 'ksô̆',
        'Ahrei': 'Ahrĕi',
        'tổng': 'tông',
        'tơdrogn': 'tơdrong',
        'Nghị': 'Nghi',
        'Việt': 'Viêt',
        'kơdriêng': 'kơdrĭng',
        'nôngnghiêp': 'nông nghiêp',
        '\n ': '\n',
        'miê': 'mĭ',
        '  ': ' ',
        '...': '.',
        'jởẳ': 'jơh',
        'ahrei': 'ahrĕi',
        'kruô̆i': 'kruôĭ',
        'alê ': 'alê̆ ',
        'Alê ': 'Alê̆ ',
        'đuô̆i': 'đuôĭ',
        'xã': 'xa',
        'huyện': 'huyên'
    }
    inputDir = 'new_output'
    outputDir = 'new_output'
    txtBana = 'bana-vni2unicode.txt'
    txtBanaContent = open(inputDir + '/' + txtBana, encoding='utf-8', errors='ignore').read()
    txtBanaTransformed = txtBanaContent
    for key, value in contentMap.items():
        print(key, '->', value)
        txtBanaTransformed = txtBanaTransformed.replace(key, value)

    with open(outputDir + '/bana-vni2unicode-new.txt', 'w', encoding='utf-8') as f:
        f.write(txtBanaTransformed)

# transform2Kriem()
transform2KriemNew()
# handleQuoutes()