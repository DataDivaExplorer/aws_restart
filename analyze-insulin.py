mystring="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
counter=0
for i in mystring:
    counter+=1
print(counter)
substring_1_24 = mystring[:24]
print("characters 1-24:", substring_1_24)
print("Length of the substring:", len(substring_1_24))

substring_25_54 = mystring[24:54]
print("characters 25-54:", substring_25_54)
print("Length of the substring:", len(substring_25_54))

substring_55_89 = mystring[54:89]
print("characters 55-89:", substring_55_89)
print("Length of the substring:", len(substring_55_89))

substring_90_110 = mystring[89:110]
print("characters 90-110:", substring_90_110)
print("Length of the substring:", len(substring_90_110))
