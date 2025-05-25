class EncryptedPassword:
    def __init__(self, password):
        self.password = password
        self.alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.crypted_password = ""
        self.decrypted_password = ""

    def encrypt(self):
        for char in self.password:
            if char.isupper():
                index = self.alphabet.find(char)
                if index < 13:
                    value = index + 13
                else:
                    value = index - 13
                self.crypted_password += self.alphabet[value]
            elif char.islower():
                lower_case = self.alphabet.lower()
                index = lower_case.find(char)
                if index < 13:
                    value = index + 13
                else:
                    value = index - 13
                self.crypted_password += lower_case[value]
            else:
                self.crypted_password += char

        return self.crypted_password

    def decrypt(self):
        for char in self.password:
            if char.isupper():
                index = self.alphabet.find(char)
                if index < 13:
                    value = 13 + index
                else:
                    value =  index - 13
                self.crypted_password += self.alphabet[value]
            elif char.islower():
                lower_case = self.alphabet.lower()
                index = lower_case.find(char)
                if index < 13:
                    value = 13 + index
                else:
                    value =  index - 13 
                self.crypted_password += lower_case[value]
            else:
                self.crypted_password += char

        return self.crypted_password



