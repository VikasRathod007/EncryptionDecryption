Val = {
    "A": 0.1,
    "B": 0.2,
    "C": 0.3,
    "D": 0.4,
    "E": 0.5,
    "F": 0.6,
    "G": 0.7,
    "H": 0.8,
    "I": 0.9,
    "J": 0.01,
    "K": 0.02,
    "L": 0.03,
    "N": 0.05,
    "O": 0.06,
    "P": 0.07,
    "Q": 0.08,
    "M": 0.04,
    "R": 0.09,
    "S": 0.001,
    "T": 0.002,
    "U": 0.003,
    "V": 0.004,
    "W": 0.005,
    "X": 0.006,
    "Y": 0.007,
    "Z": 0.008,
    " ": 0.009,
}


def Encryption(EachAlpha, Key):
    Encrypted_Message = []
    for x in EachAlpha:
        if x in Val:
            index = (list(Val.keys()).index(x) + Key) % len(Val)
            Encrypted_Message.append(Val[list(Val.keys())[index]])
        else:
            Encrypted_Message.append(x)
    print(Encrypted_Message)


def Decryption(Encrypted_Message, Key):
    Decrypted_Message = []
    Encrypted_Words = Encrypted_Message.split(", ")
    for word in Encrypted_Words:
        if word.isdigit() == False:
            index = (list(Val.values()).index(float(word))) - Key % len(Val)
            Decrypted_Message.append(list(Val.keys())[index])
        else:
            Decrypted_Message.append(word)
    decrypted_text = "".join(Decrypted_Message)
    print(decrypted_text)


while True:
    WhatToDo = input(
        """which operation would you like to perform?
    01:Encryption
    02:Decryption
    """
    )
    if WhatToDo == "exit":
        print("Exiting...")
        break

    print(WhatToDo)
    if WhatToDo.lower() == "encryption":
        Message = input("Enter message to be Encrypted:").upper()
        Key = int(input("Enter a key:"))
        EachAlpha = [x for x in Message]
        Encryption(EachAlpha, Key)
    elif WhatToDo.lower() == "decryption":
        Message = input("Enter Encrypted Message:")
        Key = int(input("Enter a key:"))
        Decryption(Message, Key)
        # print(Message)

    else:
        print("Please Enter valid method.")
