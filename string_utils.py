from sympy import symbols, Eq, solve, Rational

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts

def balance_reaction(equation):
    reactants_str, products_str = equation.split("->")
    reactants = [r.strip() for r in reactants_str.split("+")]
    products = [p.strip() for p in products_str.split("+")]

    elements = set()
    for compound in reactants + products:
        elements.update(count_atoms_in_molecule(compound).keys())
    elements = list(elements)

    coeff_symbols = symbols(" ".join([f"a{i}" for i in range(len(reactants) + len(products))]))

    equations = []
    for elem in elements:
        lhs = sum(count_atoms_in_molecule(reactants[i]).get(elem, 0) * coeff_symbols[i] for i in range(len(reactants)))
        rhs = sum(count_atoms_in_molecule(products[i]).get(elem, 0) * coeff_symbols[len(reactants)+i] for i in range(len(products)))
        equations.append(Eq(lhs, rhs))

    equations.append(Eq(coeff_symbols[0], Rational(1,1)))

    solution = solve(equations, coeff_symbols)

    return [solution[s].simplify() for s in coeff_symbols]



