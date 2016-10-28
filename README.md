# simplepad
Simple Padding module for python
functions:

sim_pad(MESSAGE, PAD_TO_MULT)
pads with spaces and returns string,so it can be divided exactly by a certain amount
MESSAGE=the string you want to pad
PAD_TO_MULT=the number that the string must be divisible by

sim_pad_with_char(MESSAGE, PAD_TO_MULT, CHAR_TO_PAD_WITH)
pads a string so it can be divided exactly by a number but with a choosen charcater
also returns both the padded string and value of how many characters it has paded by, needed for unpadding
returns two values in a tuple
MESSAGE=the string you want to pad
PAD_TO_MULT=the number that the string must be divisible by
CHAR_TO_PAD_WITH=the character that you want to pad with

sim_pad_with_amount(MESSAGE, CHAR_TO_PAD_WITH, PAD_AMOUNT)
pads a string with a certain character and certain amount
MESSAGE=the string you want to pad
CHAR_TO_PAD_WITH=the character that you want to pad with
PAD_AMOUNT=the number of characters to pad with

sim_unpad(PADDED_MES)
unpads a padded string that has been padded by sim_pad
PADDED_MES=message that has been padded with the sim_pad function

sim_unpad_with_char(PADDED_MES, PAD_AMOUNT)
unpads a string that is padded with a certain character or amount of characters
requires how many extra characters the string has been padded with
PADDED_MES=message that has been padded with the sim_pad function
PAD_AMOUNT=the number of characters the string was padded with
