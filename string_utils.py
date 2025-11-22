def split_before_uppercases(formula):
    """Splits a chemical formula into parts whenever an uppercase letter appears."""
    parts = []
    current = ""

    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch

    if current:
        parts.append(current)

    return parts


def split_at_digit(element):
    """Splits 'H2' → ('H', 2) and 'O' → ('O', 1)."""
    name = ""
    number = ""

    for ch in element:
        if ch.isdigit():
            number += ch
        else:
            name += ch

    return name, int(number) if number else 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula and returns a dictionary of atom counts."""
    
    # Step 1: Initialize dictionary
    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        # Step 2: Update the dictionary
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: Return dictionary
    return atom_counts
