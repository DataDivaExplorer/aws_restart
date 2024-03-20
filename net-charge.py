# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
# Create a new dictionary pKR
pKR = {}

# Fill the dictionary with key-value pairs
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

print(pKR)

y_count = float(insulin.count("y"))
c_count = float(insulin.count("c"))
k_count = float(insulin.count("k"))
h_count = float(insulin.count("h"))
r_count = float(insulin.count("r"))
d_count = float(insulin.count("d"))
e_count = float(insulin.count("e"))


seqCount = {'y': y_count, 'c': c_count, 'k': k_count, 'h': h_count, 'r': r_count, 'd': d_count, 'e': e_count}

print(seqCount)


# Initialize pH variable to zero
pH = 0

# Create the while loop
while (pH <= 14):
    # Define the netCharge formula
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    
    # Print the pH and netCharge with formatting
    print('{0:.2f}'.format(pH), netCharge)
    
    # Increment pH by 1
    pH += 1