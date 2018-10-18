def tempF(temp):
    ftemp = float(temp) * 9/5 + 32
    return ftemp

def tempC(temp):
    ctemp = (float(temp) - 32) * 5/9
    return ctemp 

print(tempF(37))
print(tempC(72))

