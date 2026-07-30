"""def changeads(num):
    b = bin(num)                      # converting int to num
    b= b[2:len(b)]                    # deleting the first 2 charcters of the binary number because they are python language specific and its not part of binary number.
    b1 = ""                           # new variable to store the new binary number 
    for bit in b :                    # Loop for iterating over the binary number and changing 1 to 0 and 0 to 1 
        if bit == '1' :               # if the bit is 1 then change it to 0
           b1 = b1+'0'
        else :                        # if it is 0 then change it to 1 
            b1 = b1+'1'
    sum1=0                            # new variable to  calculate the decimal number of then new binary number 
    for i in range (len(b1)):                                # iterating over new binary number 
          sum1= sum1 + ( int(b1[i]) *(2**(len(b1) -(i+1))))    # calculating the sum of bits in binary to convert it to decimal number 
    return sum1                                                # returning the decimal number of the new binary 
print(changeads(50))                                        # input num 


"""
"""better way1 """

def changeads(num):
    if num == 0:
        return 1 
    num_bits = num.bit_length()  # find the no of bits needed to represent num

    mask = (1 << num_bits) - 1     # create a mask of 1s of the same length as num

    return num ^ mask              # XOR the num with mask to flip all bits 

print(changeads(50))
    


"""
def changeads_string(num):
    b = bin(num)[2:]                                         # strip the '0b' prefix 
    flipped_b = b.translate(str.maketrans('01', '10'))        #use str.translate to flip 1s and 0s instantly 

    return int ( flipped_b,2)                                 # convert the bin string straight back to an integer using base 2 

    print(changeads_string(50))


"""