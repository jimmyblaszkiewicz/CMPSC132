#Lab #4
#Due Date: 09/14/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program myself using only the class materials             
#
########################################

def encrypt(message, key):
    """
        Takes a string and an integer an returns the encrypted message using the Caesar cipher method 
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'Invalid input'
        >>> encrypt('Hello',3.5)
        'Invalid input'
        >>> encrypt(5.6,3.15)
        'Invalid input'
    """
    # --- YOU CODE STARTS HERE
    
    # make sure that message and key are the right type ie str and int respectively
    if type(message) != str or type(key) != int:
        return ('Invalid input')

    encrypted = ""
    index = 0

    # walk through each character in the message
    for character in message:
        if ord(character) in range(65, 91):
            # it is a capital letter
            index = 65
        elif ord(character) in range(97, 123):
            # it is a lowercase letter
            index = 97
        else:
            # if not a capital / lowercase letter, just add to final message
            encrypted += character
            continue

        # subtract the 'index' from the ord(character) so that A or a = 0
        # add the key and mod 26 so that 'Z' shifted 1 is 'A' not '['
        # the mod 'wraps' the shift around the alphabet
        # and the index maintains the letter's case
        encrypted += chr(((ord(character) - index + key) % 26) + index)
        
    return encrypted  


def decrypt(message, key):
    """
        Takes a string and an integer an returns the decrypted message using the Caesar cipher method 
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'Invalid input'
        >>> decrypt('Hello',3.5)
        'Invalid input'
        >>> decrypt(5.6,3.15)
        'Invalid input'
    """

    # --- YOU CODE STARTS HERE
    # adding this test comment
    # make sure that message and key are the right type ie str and int respectively
    if type(message) != str or type(key) != int:
        return ('Invalid input')

    #decrypting a caesar cipher is equivalent to encrypting 
    #it how ever many more times than the key it takes to get to 26    
    return encrypt(message, 26-(key%26))

    # ---  CODE ENDS HERE




