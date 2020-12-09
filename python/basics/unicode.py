with open(r'c:\tmp\x_2sup', 'w', encoding='utf-8') as fout:
    # write unicode string x² in text mode encoding to utf-8 byte string
    fout.write('x²')
    # hexdump of that file is 78c2 b2

with open(r'c:\tmp\x_2sup.bin', 'wb') as fout:
    # write unicode glyph Ĕ in binary mode encoding to utf-8 byte string
    fout.write('\u0114'.encode('utf-8'))
    # hexdump of that file is c494
