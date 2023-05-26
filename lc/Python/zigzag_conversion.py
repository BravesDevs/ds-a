def convert(s: str, numRows: int) -> str:
    charDict = {i:"" for i in range(1,numRows+1)}
    row=1
    flow=1
    for i in range(1,len(s)+1):
        row = row+1 if row==0 else row
        charDict[row]+=s[i-1]
        if(row == numRows):
            flow*=-1
        if(row==1 and i > numRows):
            flow*=-1
        row+=flow
    return "".join(charDict.values())

print(convert("PAYPALISHIRING",3))