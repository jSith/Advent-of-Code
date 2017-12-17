import utility
import re


class Program(object):

    def __init__(self, name, weight, above_programs):
        self.name = name
        self.weight = weight
        self.above_programs = above_programs
        self.below_programs = []


def parse_tower(string):
    programs = []
    for line in string:
        name = re.findall('[a-z]* \(', line)
        name = re.sub(' \(', '', name[0])
        weight = re.findall('\([0-9]*\)', line)
        weight = int(re.sub('\(|\)', '', weight[0]))
        above_programs = re.findall('->.*', line)
        if len(above_programs) > 0:
            above_programs = re.sub('-> ', '', above_programs[0])
            above_programs = above_programs.split(', ')
        else:
            above_programs = []
        if name is not None:
            programs.append(Program(name, weight, above_programs))
    return programs


def get_bottom_programs(tower):
    for below_program in tower:
        for above_program in below_program.above_programs:
            tower = add_below_program(tower, above_program, below_program)
    return tower


def trace_tower(data):
    tower = get_bottom_programs(parse_tower(data))
    for program in tower:
        if len(program.below_programs) == 0:
            return program.name



def add_below_program(tower, above, below):
    for program in tower:
        if program.name == above:
            if below not in program.below_programs:
                program.below_programs.append(below)
            return tower

def main():
    print(trace_tower(utility.read_by_line('input7.txt')))


if __name__ == '__main__':
    main()