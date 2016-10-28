#Author: CuriousTeenager
#Thought I would create a simple padding module and algorithm for people who came across the same problems i have when encrypting data

#pads with spaces and returns string,so it can be divided exactly by a certain amount
def sim_pad(MESSAGE, PAD_TO_MULT):
    MESSAGE = MESSAGE + "1" 
    pad = (((len(MESSAGE)/PAD_TO_MULT)+1)*PAD_TO_MULT)-len(MESSAGE)
    for i in range(pad):
        MESSAGE = MESSAGE + " "
    return MESSAGE

#pads a string so it can be divided exactly by a number but with a choosen charcater
#also returns both the padded string and value of how many characters it has paded by, needed for unpadding
#returns two values in a tuple
def sim_pad_with_char(MESSAGE, PAD_TO_MULT, CHAR_TO_PAD_WITH):
    if len(CHAR_TO_PAD_WITH)== 1:
        pad = (((len(MESSAGE)/PAD_TO_MULT)+1)*PAD_TO_MULT)-len(MESSAGE)
        for i in range(pad):
            MESSAGE = MESSAGE + CHAR_TO_PAD_WITH
        return (MESSAGE, pad)
    else:
        raise ValueError('ValueError: legnth of CHAR_TO_PAD_WITH must only be 1')

#pads a string with a certain character and certain amount
def sim_pad_with_amount(MESSAGE, CHAR_TO_PAD_WITH, PAD_AMOUNT):
    for i in range(PAD_AMOUNT):
        MESSAGE = MESSAGE + CHAR_TO_PAD_WITH
    return (MESSAGE)

#unpads a padded string
def sim_unpad(PADDED_MES):
    PADDED_MES = PADDED_MES.rstrip()[:-1]
    return PADDED_MES


#unpads a string that is padded with a certain character
#requires how many extra characters the string has been padded with
def sim_unpad_with_char(PADDED_MES, PAD_AMOUNT):
    PAD_AMOUNT = PAD_AMOUNT*-1
    PADDED_MES = PADDED_MES[:PAD_AMOUNT]
    return PADDED_MES

#unpad a string based on the amount it was padded by
def sim_unpad_with_amount(PADDED_MES, PAD_AMOUNT):
    PAD_AMOUNT = PAD_AMOUNT*-1
    PADDED_MES = PADDED_MES[:PAD_AMOUNT]
    return PADDED_MES
    



