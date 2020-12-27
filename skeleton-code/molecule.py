# Author John Landeholt [TA]

class syntax_error(Exception):
    """ Will only work when rest_of_q actually is a queue """
    def __init__(self, message, rest_of_q = None):
        self.message = message
        if rest_of_q:
            self.stack_trace = "".join(rest_of_q)
        else:
            self.stack_trace = rest_of_q

    def __str__(self):
        return f'{self.message} vid radslutet {self.stack_trace}'.strip()

    def __repr__(self):
        return self.__str__()

ATOMS = {'Ru': True, 'Re': True, 'Rf': True, 'Rg': True, 'Ra': True, 'Rb': True, 'Rn': True, 'Rh': True, 'Be': True, 'Ba': True, 'Bh': True, 'Bi': True, 'Bk': True, 'Br': True, 'H': True, 'P': True, 'Os': True, 'Es': True, 'Hg': True, 'Ge': True, 'Gd': True, 'Ga': True, 'Pr': True, 'Pt': True, 'Pu': True, 'C': True, 'Pb': True, 'Pa': True, 'Pd': True, 'Cd': True, 'Po': True, 'Pm': True, 'Hs': True, 'Ho': True, 'Hf': True, 'K': True, 'He': True, 'Md': True, 'Mg': True, 'Mo': True, 'Mn': True, 'O': True, 'Mt': True, 'S': True, 'W': True, 'Zn': True, 'Eu': True, 'Zr': True, 'Er': True, 'Ni': True, 'No': True, 'Na': True, 'Nb': True, 'Nd': True, 'Ne': True, 'Np': True, 'Fr': True, 'Fe': True, 'Fl': True, 'Fm': True, 'B': True, 'F': True, 'Sr': True, 'N': True, 'Kr': True, 'Si': True, 'Sn': True, 'Sm': True, 'V': True, 'Sc': True, 'Sb': True, 'Sg': True, 'Se': True, 'Co': True, 'Cn': True, 'Cm': True, 'Cl': True, 'Ca': True, 'Cf': True, 'Ce': True, 'Xe': True, 'Lu': True, 'Cs': True, 'Cr': True, 'Cu': True, 'La': True, 'Li': True, 'Lv': True, 'Tl': True, 'Tm': True, 'Lr': True, 'Th': True, 'Ti': True, 'Te': True, 'Tb': True, 'Tc': True, 'Ta': True, 'Yb': True, 'Db': True, 'Dy': True, 'Ds': True, 'I': True, 'U': True, 'Y': True, 'Ac': True, 'Ag': True, 'Ir': True, 'Am': True, 'Al': True, 'As': True, 'Ar': True, 'Au': True, 'At': True, 'In': True}

def atom(queue):
    """ <atom> must be a valid atom in the list ATOMS 
        Assumption: a atom is only 2 letters, where the first is capitalized
    """
    pass

def clause(queue):
    """ A clause must have a <mol> inside of it 
        Tip: count parenthesis or recurse
    """
    pass

def num(queue):
    """ <num> ::= > 1 
        Catch when first number is 0 or 1.
    """
    pass

def group(queue, inner_clause = False):
    """ <group> can either contain:
         a <atom>
         a <atom><num>
         a (<mol>)<num>
         
         Tip: check for incorrect group-starts.
    """
    pass

def mol(queue):
    """ <mol> can contains a <group> or <group><mol> """
    if not queue.empty:
        if group(queue):
            return mol(queue)
    return q.empty

def formula(f):
    """ Create queue of formula """
    try:
        queue = None
        if queue.empty: return 'Formeln är syntaktiskt korrekt'
        if mol(queue): return 'Formeln är syntaktiskt korrekt'
    except Exception as exc:
        return str(exc)