def integerToRoman(num):
    
    charDict = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

    intArray = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    index=-1
    roman=""
    
    while num > 0:
        charCount = num//intArray[index]
        roman+=charDict[intArray[index]]*charCount
        num-=charCount*intArray[index]
        index-=1
    return roman

print(integerToRoman(1994))