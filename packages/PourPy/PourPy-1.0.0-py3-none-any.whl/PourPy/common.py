from enum import Enum, unique, Flag

class State(Enum):
    aqueous = 'aq'
    solid = 's'
    gaseous = 'g'
    liquid = 'l'
    electron = 'e'

class Constants(float, Flag):
    GAS = 8.31446262
    FARADAY = 96485.3321
    STANDARD_TEMPERATURE = 298.15
    STANDARD_PRESSURE = 1.0


class Defaults(object):
    activity = 1.00
    maximum_electrode_potential = 2.0
    minimum_electrode_potenital = -2.0
    maximum_pH_value = 14.0
    minimum_pH_value = 0.
    pressure = 1.
    temperature = 298.15
    reference_electrode_abbreviation = "SHE"
    reference_potential_difference = 0.0
    reference_electrodes = {"SHE": 0.000, "SCE":0.241, "CSE":0.314, "SCE":0.197}
