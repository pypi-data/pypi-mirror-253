import pytest

from PourPy import parser

@pytest.fixture
def specie_fixture():
    return 'H|+1|,state=aq,dGf=0.0,dHf=1,Sm=12.345'
    

@pytest.fixture
def reaction_fixture():
    return '2H|+1| + 0.5e|-1| -> H2'


def test_parse_reaction(reaction_fixture):
    parsed_reaction = parser.DefaultParser.parse_reaction(reaction_fixture)
    assert parsed_reaction['H|+1|'] == 2.0 \
        and parsed_reaction['e|-1|'] == 0.5 \
        and parsed_reaction['H2'] == -1

def test_parse_specie(specie_fixture):
    name, prop = parser.DefaultParser.parse_specie(specie_fixture)
    check_name  = name == 'H|+1|'
    check_status  = prop['state'] == 'aq'

    assert check_name \
        and check_status \
        and float(prop['dGf']) == 0.0 \
        and float(prop['dHf']) == 1 \
        and float(prop['Sm']) == 12.345
