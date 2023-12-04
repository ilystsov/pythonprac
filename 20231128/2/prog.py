import sys
from collections import defaultdict
import math
listing = [' '.join(line.strip().split()) for line in sys.stdin.read().split('\n')]
listing = [x for x in listing if x]
instructions = []
used_labels = set()
possible_labels = {}
for i in range(len(listing)):
    instruction = listing[i].split()
    if instruction[0][-1] == ':':
        possible_labels[instruction[0][:-1]] = len(instructions)
        instruction = instruction[1:]
    match instruction:
        case ['stop']:
            instructions.append(instruction)
        case ['store', value, variable]:
            instructions.append(instruction)
        case  ['add' | 'sub' | 'div' | 'mul' as op, operand1, operand2, storage]:
            instructions.append(instruction)
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as cmp, operand1, operand2, label]:
            instructions.append(instruction)
            used_labels.add(label)
        case ['out', name]:
            instructions.append(instruction)
        case _:
            pass 

if not used_labels.issubset(possible_labels.keys()):
    exit(0)

variables = defaultdict(int)  
i = 0
while i < len(instructions):
    match instructions[i]:
        case ['stop']:
            exit(0)
        case ['store', value, variable]:
            try:
                value = float(value)
            except ValueError:
                value = 0
            variables[variable] = value
        case ['add' | 'sub' | 'div' | 'mul' as op, operand1, operand2, storage]:
            try:
                match op:
                    case 'add':
                        variables[storage] = variables[operand1] + variables[operand2]
                    case 'sub':
                        variables[storage] = variables[operand1] - variables[operand2]
                    case 'div':
                        variables[storage] = variables[operand1] / variables[operand2]
                    case 'mul':
                        variables[storage] = variables[operand1] * variables[operand2]
            except Exception:
                variables[storage] = math.inf
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as cmp, operand1, operand2, label]:
            match cmp:
                case 'ifeq':
                    res = variables[operand1] == variables[operand2]
                case 'ifne':
                    res = variables[operand1] != variables[operand2]
                case 'ifgt':
                    res = variables[operand1] > variables[operand2]
                case 'ifge':
                    res = variables[operand1] >= variables[operand2]
                case 'iflt':
                    res = variables[operand1] < variables[operand2]
                case 'ifle':
                    res = variables[operand1] <= variables[operand2]
            if res: 
                i = possible_labels[label] - 1
        case ['out', name]:
            print(variables[name])
    i += 1
