# TEXT ENCRYPTOR
# Authors : Ala Fizal, Mohammed Aghil Puthiyottil

# 1. Get a text as input, for now it can be a sample text (Get a string)
plain_message = "how are you"
# 2. We will change it to something else in some-way
# which people cannot understand plainly

## 2.1 (Logic to convert)

make_into_dictionary={"a":"b","b":"a","c":"d","d":"c","e":"f","f":"e","g":"h","h":"g","i":"j","j":"i","k":"l",
                      "l":"k","m":"n","n":"m","o":"p","p":"o","q":"r","r":"q","s":"t","t":"s","u":"v","v":"u","w":"x","x":"w","y":"z","z":"y"}
for character in plain_message:
    for key, value in make_into_dictionary.items():
        if character == key:
            character = value 
        elif character == " ":
            character = " "
    print(character, end='')
 
## 2.2 (Convert plain_message to encrypted message using logic in #2.1)

# 3. print the encrypted text
