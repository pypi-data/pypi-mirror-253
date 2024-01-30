from abc import ABC, abstractmethod
from .reactant import Reactant
from .common import State

class Parser(ABC):
    @abstractmethod
    def parse_reactions(self):
        pass

    @abstractmethod
    def parse_species(self):
        pass
    
    @abstractmethod
    def parse_elements(self):
        pass


class DefaultParser(Parser):
    @staticmethod
    def parse_reactions(reactions : tuple):
        """
        Parses several reactions given as tuple

        :param reactions: reactions to be parsed, each entry of a tuple is a reaction string
        :type reactions: tuple

        :return : reactions as list, each entry is a dict containing reactants
        :rtype : list
        """

        reactions_list = []
        for i in reactions:
            reac = DefaultParser.parse_reaction(i)

            temp = dict()
            for key, value in reac.items():
                temp[key] = value
            reactions_list.append(temp)

        return reactions_list

    @staticmethod
    def parse_reaction(reaction : str):
        """
        Parse a reaction from its string representation

        :param reaction: reaction to be parsed
        :type reaction: str

        :return : reactants as dict
        :rtype : dict
        """

        components = reaction.strip().split('->')
        lhs = components[0]
        rhs = components[1]
        lhs_split = lhs.split(' + ')
        rhs_split = rhs.split(' + ')

        reactants = dict()
        for i in lhs_split:
            i = i.strip()
            formula = i.lstrip('0123456789.- ')
            start_index = len(i) - len(formula)

            if start_index == 0:
                reactants[i.strip()] = 1.0
            else:
                reactants[i[start_index:].strip()] = float(i[:start_index])

        for i in rhs_split:
            i = i.strip()
            formula = i.lstrip('0123456789.- ')
            start_index = len(i) - len(formula)

            if start_index == 0:
                reactants[i.strip()] = -1.0
            else:
                reactants[i[start_index:].strip()] = -float(i[:start_index])

        return reactants

    @staticmethod
    def parse_species(species : tuple, elements : dict):
        species_list = []
        for specie in species:
            name, prop = DefaultParser.parse_specie(specie)
            species_list.append(Reactant(name,
                                         state=str(prop['state']),
                                         dGf=float(prop['dGf']),
                                         dHf=float(prop['dHf']),
                                         Sm=float(prop['Sm']),
                                         elements=elements))
        return species_list

    @staticmethod
    def parse_specie(specie : str):
        """
        Parse a specie and its chemical props from its string representation

        :param specie: specie_name,state,dGf,dHf,Sm as string
        :type specie: str

        :return : name of the specie, properties as dictionary
        :rtype : tuple
        """

        components = specie.strip().split(',')
        prop = dict()
        for comp in components[1:]:
            split = comp.split('=')
            prop[split[0].strip()] = split[1].strip()

        return (components[0].strip(), prop)

    @staticmethod
    def parse_elements():
        elements = {'e': 0, 'La': 0, 'H': 1.0079, 'Xe': 131.3,
            'He': 4.0026, 'Li': 6.941, 'Rf': 265.0, 'B': 10.81,
            'Db': 268.0, 'Fe': 55.847, 'Sg': 271.0, 'Bh': 272.0,
            'F': 18.998, 'Ag': 107.87, 'Mt': 276.0, 'Na': 22.99,
            'Mg': 24.305, 'Cs': 132.91, 'Al': 26.982, 'Zr': 91.224,
            'Si': 28.086, 'P': 30.974, 'S': 32.06, 'Cl': 35.453,
            'Ar': 39.948, 'Ca': 40.08, 'N': 14.007, 'Sc': 44.955912,
            'Hf': 178.49, 'Ti': 47.9, 'Hg': 200.59, 'V': 50.941,
            'Cr': 51.996, 'Ta': 180.95, 'O': 15.999, 'Mn': 54.938,
            'Be': 9.0122, 'Ba': 137.33, 'Co': 58.933, 'Fr': 223.0,
            'Os': 190.2, 'Cu': 63.546, 'Ir': 192.22, 'Zn': 65.38,
            'Pt': 195.09, 'Au': 196.97, 'Ga': 69.72, 'Ge': 72.59,
            'C': 12.011, 'As': 74.922, 'W': 183.84, 'Tl': 204.37,
            'Bi': 206.98, 'Br': 79.904, 'Rn': 222.0, 'At': 210.0,
            'Kr': 83.8, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906,
            'Pb': 207.2, 'Nb': 92.906, 'Ni': 58.71, 'Ne': 20.179,
            'Mo': 95.94, 'Tc': 97.0, 'Ra': 226.03, 'Ac': 227.0,
            'Ru': 102.91, 'Po': 209.0, 'Re': 128.207, 'Pd': 106.4,
            'K': 39.096, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.69,
            'Sb': 121.75, 'Se': 78.96, 'I': 126.9, 'Te': 127.6}

        return elements
