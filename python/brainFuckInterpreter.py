# https://www.codewars.com/kata/526156943dfe7ce06200063e

def jmp(pointer, code, data):
    if data != 0:
        return pointer + 1
    else:
        count = 1
        while count > 0:
            pointer += 1
            if code[pointer] == ']':
                count -= 1
            elif code[pointer] == '[':
                count += 1
    return pointer

def jmpBack(pointer, code, data):
    if data == 0:
        return pointer + 1
    else:
        count = 1
        while count > 0:
            pointer -= 1
            if code[pointer] == '[':
                count -= 1
            elif code[pointer] == ']':
                count += 1
    return pointer          

def brain_luck(code, program_input):
    memory = [0 for i in range(5000)]
    output = ""
    instrP = 0
    dataP = 0
    while (instrP < len(code)):
        instr = code[instrP]
        if instr == '>': dataP = dataP + 1 #% 5001
        elif instr == '<': dataP = dataP -1 #% 5001
        elif instr == '+': memory[dataP] = (memory[dataP] + 1)
        elif instr == '-': memory[dataP] = (memory[dataP] - 1)
        elif instr == '.': output += chr(memory[dataP])
        elif instr == ',':
            memory[dataP] = ord(program_input[0])
            program_input = program_input[1:]
        elif instr == '[': 
            instrP = jmp(instrP, code, memory[dataP])
            continue
        elif instr == ']':
            instrP = jmpBack(instrP, code, memory[dataP])
            continue
        instrP += 1
    return output