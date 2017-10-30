import string

with open('get_flag.txt') as f:
    lines = f.readlines()

lines = lines[1:]

elems = []
output = ""
wciecie = ""
for line in lines:
    if line == '\n':
        continue
    line = line.strip().split()
    while line[1][0] not in string.ascii_uppercase:
        line = line[1:]
    if len(line) == 4:
        del line[2]
    line = line[1:]
    if line[0] == "LOAD_CONST":
        elems.append( line[1])
    elif line[0] == "STORE_FAST":
        output += wciecie + line[1] + "=" + elems[-1] + "\n"
        wciecie = ""
        print(output.split("\n")[-2])
        elems=elems[:-1]
    elif line[0] == "LOAD_FAST":
        elems.append(line[1])
    elif line[0] == "INPLACE_ADD":
        val = elems[-2] + "+" + elems[-1]
        elems = elems[:-2]
        elems.append(val)
    elif line[0] == "LOAD_CONST":
        elems.append(line[1])
    elif line[0] == "JUMP_FORWARD":
        output += "else:\n"
        wciecie = "    "
    elif line[0] == "POP_JUMP_IF_FALSE":
        output += "if " + elems[-1] + ":\n"
        print(output.split("\n")[-2]) 
        wciecie = "    "
        elems = elems[:-1]
    elif line[0] == "COMPARE_OP":
        val = elems[-2] + line[1][1:-1] + elems[-1]
        elems = elems[:-2]
        elems.append(val)
    elif line[0] == "INPLACE_SUBTRACT":
        val = elems[-2] + "-" + elems[-1]
        elems = elems[:-2]   
        elems.append(val)
    else:
        print (line[0])
        output += "#" + line[0] + "\n"
output
print(output)
with open("output.py", 'w') as f:
    f.write(output)

