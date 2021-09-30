from string import ascii_uppercase, ascii_lowercase

class Cipher:
    """Class which have functions The Keyword encoding and decoding for latin alphabet"""
    def __init__(self, keyword_alph):
        self.keyword_alph = "".join(list(dict.fromkeys(("".join(list(dict.fromkeys(keyword_alph))) + ascii_lowercase))))

    def encode(self, text):
        code = []
        cipher = ""
        for char in text:
            if char in ascii_lowercase:
                code.append(str(ascii_lowercase.find(char)))
            elif char in ascii_uppercase:
                code.append(str(ascii_uppercase.find(char))+".")
            else:
                code.append(char)

        for index in range(0, len(code)):
            if code[index].isnumeric():
                cipher += self.keyword_alph[int(code[index])]
            else:
                if len(code[index]) == 2:
                    code[index] = code[index][0]
                    cipher += self.keyword_alph[int(code[index])].upper()
                else:
                    cipher += code[index]
        print(cipher)

    def decode(self, text):
        code = []
        cipher = ""
        for char in text:
            if char in self.keyword_alph:
                code.append(str(self.keyword_alph.find(char)))
            elif char in self.keyword_alph.upper():
                code.append(str(self.keyword_alph.find(char.lower())) + ".")
            else:
                code.append(char)

        for index in range(0, len(code)):
            if code[index].isnumeric():
                cipher += ascii_lowercase[int(code[index])]
            else:
                if len(code[index]) == 2:
                    code[index] = code[index][0]
                    cipher += ascii_uppercase[int(code[index])].upper()
                elif len(code[index]) == 3:
                    code[index] = code[index][:2]
                    cipher += ascii_uppercase[int(code[index])].upper()
                else:
                    cipher += code[index]
        print(cipher)


cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")