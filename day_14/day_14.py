from collections import defaultdict
from functools import reduce

def parse_reaction(line):
    elements = line.split(" ")
    elements.remove("=>")
    elements = [e.strip(" ,") for e in elements]
    return elements

def add_to_reactions(reactions, line):
    reactants = {}
    
    reactants = [[line[i+1],int(line[i])] for i in range(0, len(line)-2, 2)]
    amount, product = line[-2:]
    reactions[product] = [int(amount)] + reactants

    return reactions


def parse_reactions(lines):
    reaction_lines = map(parse_reaction, lines)

    reactions = reduce(add_to_reactions, reaction_lines, {})
    
    return reactions