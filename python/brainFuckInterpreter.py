# https://www.codewars.com/kata/526156943dfe7ce06200063e

# Handles the [ instruction
def jmp(pointer, code, data):
    if data != 0:                       # if data is not 0 don't jump
        return pointer + 1
    else:
        depth = 1
        while depth > 0:                # find matching ] to the current [
            pointer += 1
            if code[pointer] == ']':    # decrese bracket depth
                depth -= 1
            elif code[pointer] == '[':  # increse bracket depth
                depth += 1
    return pointer

# Handles the ] instruction. Works like jmp() but decrements the pointer
def jmpBack(pointer, code, data):
    if data == 0:
        return pointer + 1
    else:
        depth = 1
        while depth > 0:
            pointer -= 1
            if code[pointer] == '[':
                depth -= 1
            elif code[pointer] == ']':
                depth += 1
    return pointer          

def brain_luck(code, program_input):
    program_input += chr(0)
    memory = [0 for i in range(5000)]
    output = ""
    instrP = 0
    dataP = 0
    while (instrP < len(code)):
        instr = code[instrP]
        if instr == '>': dataP += 1                                     # increment data pointer
        elif instr == '<': dataP -= 1                                   # decrement data pointer 
        elif instr == '+': memory[dataP] = (memory[dataP] + 1) % 256    # increment data with 8-bit overflow
        elif instr == '-': memory[dataP] = (memory[dataP] - 1) % 256    # decrement data with 8-bit underflow
        elif instr == '.': output += chr(memory[dataP])                 # output current data byte
        elif instr == ',':                                              # if input is not empty: input byte -> memory[data pointer]
            if len(program_input) > 0:                                  # else: 0 -> memory[data pointer]
                memory[dataP] = ord(program_input[0])
                program_input = program_input[1:]
            else:
                memory[dataP] = 0
        elif instr == '[':                                              # jmp and jmpBack increments instruction pointer, continue
            instrP = jmp(instrP, code, memory[dataP])
            continue
        elif instr == ']':
            instrP = jmpBack(instrP, code, memory[dataP])
            continue
        instrP += 1                                                     # instruction handled, increment pointer
    output += chr(10)                                                   # add newline to end of output before returning
    return output