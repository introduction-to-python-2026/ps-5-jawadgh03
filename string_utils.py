def split_before_uppercases(formula):
    if len(formula) == 0:
        return []
    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula


def split_at_digit(element):
    name = ""
    number = ""
    for ch in element:
        if ch.isdigit():
            number += ch
        else:
            name += ch
    return name, int(number) if number else 1


def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts
