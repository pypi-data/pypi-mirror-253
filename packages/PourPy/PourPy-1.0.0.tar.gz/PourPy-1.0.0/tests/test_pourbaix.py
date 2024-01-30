import pytest

from PourPy import PourbaixDiagram, System, Database

species = ('H|+1|,      state=aq,   dGf=0,              dHf=0,              Sm=0',
           'H2,         state=g,    dGf=0,              dHf=0,              Sm=0',
           'e|-1|,      state=e,    dGf=0,              dHf=0,              Sm=0',
           'H2O,        state=l,    dGf=-2.37140E+05,   dHf=-2.85830E+05,   Sm=69.95',
           'O2,         state=g,    dGf=0,              dHf=0,              Sm=205.137',
           'Fe,         state=s,    dGf=0,              dHf=0,              Sm=27.1',
           'Fe(OH)2,    state=s,    dGf=-494.89E+03,    dHf=-583.4E+03,     Sm=84.0',
           'Fe2O3,      state=s,    dGf=-744.45E+03,    dHf=-826.3E+03,     Sm=87.4',
           'Fe3O4,      state=s,    dGf=-1012.72E+03,   dHf=-1115.8E+03,    Sm=145.9',
           'Fe|+2|,     state=aq,   dGf=-91504,         dHf=-92257,         Sm=-105.855',
           'Fe|+3|,     state=aq,   dGf=-16.23E+03,     dHf=-50.1E+03,      Sm=-282.4',
           'FeOH|+1|,   state=aq,   dGf=-274.00E+03,    dHf=-321.50E+03,    Sm=-29.6',
           'CO2,        state=aq,   dGf=-385.970e+03,   dHf=-413.260e+03,   Sm=119.360',
           'HCO3|-1|,   state=aq,   dGf=-586.845e+03,   dHf=-689.930e+03,   Sm=98.400',
           'CO3|-2|,    state=aq,   dGf=-527.900e+03,   dHf=-675.230e+03,   Sm=50.000',
           'FeCO3,      state=s,    dGf=-679.557e+03,   dHf=-752.609e+03,   Sm=95.537'
           )


reactions = ('2H|+1| + 2e|-1| -> H2',
             'O2 + 4H|+1| + 4e|-1| -> 2H2O',
             'Fe -> Fe|+2| + 2e|-1|',
             'Fe|+2| -> Fe|+3| + e|-1|',
             'Fe|+2| + 2H2O -> Fe(OH)2 + 2H|+1|',
             '3Fe|+2| + 4H2O -> Fe3O4 + 8H|+1| + 2e|-1|',
             'Fe + 2H2O -> Fe(OH)2 + 2H|+1| + 2e|-1|',
             '3Fe(OH)2 -> Fe3O4 + 2H2O + 2H|+1| + 2e|-1|',
             '2Fe3O4 + H2O -> 3Fe2O3 + 2H|+1| + 2e|-1|',
             'Fe|+3| + 1.5H2O -> 0.5Fe2O3 + 3H|+1|',
             'Fe|+2| + 1.5H2O -> 0.5Fe2O3 + 3H|+1| + e|-1|'
             )


@pytest.fixture
def chemical_system():
    db = Database.from_default(species)
    system = System()
    system.set_database(db)

    system.temperature = 298.15
    system.pressure = 1
    system.pHs = (5, 14)
    system.electrode_potentials = (-2, 2)
    system.reference_electrode = ("SHE",1.0)

    system.add_elements(["O","H","Fe","C"])
    system.set_aqueous_activity("Fe", 1e-5)
    system.set_aqueous_activity("C", 1e-3)

    system.add_reactions(reactions)


    return system

def test_unique_const(chemical_system):
    diagram = PourbaixDiagram(chemical_system)
    uniqueConst = diagram._get_unique_constitutents()

    '''for constituent, associated_reactions in uniqueConst.items():
        print(constituent.formula)
        for reac in associated_reactions:
            print(reac)'''
        
            
def test_intersection(chemical_system):
    diagram = PourbaixDiagram(chemical_system)
    uniqueConst = diagram._get_unique_constitutents()
    diagram._compute_intersections(uniqueConst)
    
    '''for constituent, associated_reactions in uniqueConst.items():
        print(constituent.formula)
        for j in associated_reactions:
            print(j)
            for ii in j.intersections:
                print(ii)'''

    diagram._compute_boundary_lines(chemical_system)
