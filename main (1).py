import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
def main2():
    CBC()

# Cipher Block Chaining
def CBC():
    ciphert = "2f81131d1bf1284dc5b54e0c5c9aff545bd7ff8eb2364e9d7d806224117ac4fd18e89f1cad206f3778686f7e73717b8adbcedbc1704da1291abf6cd44dbb86da433305df3876390b3fc68b1a3cd6b3647f853ebc67a62785abfa3b1b1c0c50aac255967b03ba48eafddeb6b2b3ed973f6dc37cb08d173831ed852802b43d43c05a7d39d8620f9d80234b58c08fd6440586cb0cd85fbd6b1f84087c92b05d0eb063ceed0d6a5f307ec1387bd8594541d8499cc5d2f7703ccbc520034df53a5f1052e794464aef722bf0e71177f3e12183618413f7cc6911ecf707d3a985db1b90"
    cipherArray = bytearray.fromhex(ciphert)
    # print(cipherArray)

    original = "proj5_ciphertext.txt"
    deciphered = "proj5_deciphered.txt"
    with open("proj5_ciphertext.txt", 'rb') as f:
        content = f.read()

    # print ciphertext
    # print(content)
    # final size = length of the ciphertext
    fsz = len(cipherArray)
    # print("size of bytearray: ", fsz)
    # Given Key (32 bytes)
    # key as hex string
    hexkey: str = "ec58dfa74641af52ad0d16e77d576623"
    # convert to byte array
    givenkey = bytearray.fromhex(hexkey)



    # IV as hex string

    hexIV: str = "5468617473206d79204b756e67204675"
    # convert to byte array
    givenIV = bytearray.fromhex(hexIV)

    # Opening all files
    encrypted_file = open(original, "rb")
    decrypted_file = open(deciphered, "wb")
    i = fsz
    j = 1
    #decrypt loop similar to CBC as well
    while (i > 0):
        cipher = AES.new(givenkey, AES.MODE_CBC, givenIV)
        #last block  first

        #read in a block of 32 bytes
        blockValues = cipherArray[i-64: i]
        # print("block values: ", blockValues)
        decrypted_blockValues = cipher.decrypt(blockValues)

        # convert bytes back to hex string
        decrypted_file.write((decrypted_blockValues))
        # increment to next block
        i = i - 64
        #print("\n\nblock " , j , ", reading 32 bytes starting at byte(" ,i,") ", blockValues)
        # print("Decrypted block values: ")
        #print("decrypted text in block ", j, " reading bytes ", i-64, " - ", i, ": " )
        print(decrypted_blockValues)
        j = j + 1




    print("\n\n", original, "was decrypted correctly using Cipher Block Chaining Mode")
    encrypted_file.close()
    decrypted_file.close()


main2()
