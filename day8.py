import re
import utility


class Instruction(object):

    def __init__(self, operation_register, operation, operation_amount, condition_register, condition, condition_amount):
        self.operation_register = operation_register
        self.operation = operation
        self.operation_amount = operation_amount
        self.condition_register = condition_register
        self.condition = condition
        self.condition_amount = condition_amount

    def to_string(self):
        return self.operation_register + ' ' + self.operation + ' ' + str(self.operation_amount) + ' if ' + self.condition_register + ' ' + str(self.condition) + ' ' + str(self.condition_amount)


def parse_instructions(data):
    instructions = []
    registers = []
    for line in data:
        operation_register = re.findall('.* dec|.* inc', line)
        operation_register = re.sub(' dec| inc', '', operation_register[0])
        if operation_register not in registers:
            registers.append(operation_register)
        operation = re.findall('inc|dec', line)[0]
        operation_amount = re.findall('-[0-9]* if|[0-9]* if', line)
        operation_amount = int(re.sub(' if', '', operation_amount[0]))
        condition_register = re.findall('if [a-z]*', line)
        condition_register = re.sub('if ', '', condition_register[0])
        if condition_register not in registers:
            registers.append(condition_register)
        condition = line.split('if')[1]
        condition_op = re.findall('>=|>|==|!=|<=|<', condition)[0]
        condition_amount = re.findall(' [0-9]*|-[0-9]*', condition)
        condition_amount = int(condition_amount[len(condition_amount)-1])
        if operation_register is not None:
            instructions.append(Instruction(operation_register, operation, operation_amount, condition_register, condition_op, condition_amount))
    return registers, instructions


def max_register(data):
    info = parse_instructions(data)
    registers = info[0]
    instructions = info[1]
    register_values = {}
    maximum = float('-Inf')

    for register in registers:
        register_values[register] = 0

    for instruction in instructions:
        operation_register = instruction.operation_register
        amount = instruction.operation_amount
        register_value = register_values[operation_register]
        if condition_holds(instruction, register_values):
            if instruction.operation == 'dec':
                register_values[operation_register] = register_value - amount
            else:
                register_values[operation_register] = register_value + amount

    return max(register_values.values())


def condition_holds(instruction, registers):
    a = registers[instruction.condition_register]
    b = instruction.condition_amount
    if instruction.condition == '>':
        return a > b
    elif instruction.condition == '>=':
        return a >= b
    elif instruction.condition == '==':
        return a == b
    elif instruction.condition == '!=':
        return a != b
    elif instruction.condition == '<=':
        return a <= b
    elif instruction.condition == '<':
        return a < b


def main():
    print(max_register(utility.read_by_line('input8.txt')))


if __name__ == '__main__':
    main()