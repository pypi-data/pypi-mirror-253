#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:50:23 2023

@author: fabioenricofurcas
"""

import numpy as np
import json
import warnings
from .reaction import Reaction, Reactant
from .database import element_list
from .common import Constants, State, Defaults

from functools import singledispatchmethod



class System:
    """System class that contains all required physiochemical parameters, elements and reacion constituents nessecary to create a pourbaix diagram.
    """
    def __init__(self, filename=None):
        """Constructor method for the System class.

        :param filename: Optional filename to read various system parameters from.
        :type filename: str
        """
        if filename != None:
            self.read_parameters_from_file(filename)

        self.reactions              = list()
        self.elements               = dict()
        self.temperature            = Defaults.temperature
        self.pressure               = Defaults.pressure
        self.pHmin                  = Defaults.minimum_pH_value
        self.pHmax                  = Defaults.maximum_pH_value
        self.Emin                   = Defaults.minimum_electrode_potenital
        self.Emax                   = Defaults.maximum_electrode_potential
        self.reference_electrode    = Defaults.reference_electrode_abbreviation, Defaults.reference_potential_difference


    def set_database(self, database):
        self.db = database
    
    def __str__(self):
        """Generate a string of the System object containing all chemical reactions, its temperature and pressure.

        :return: String representation of the System.
        :rtype: str
        """

        padding = 8
        print(f"{'System':{'-'}{'^'}{64}}")
        print(f'Temperature : {self.temperature}, Pressure : {self.pressure}')
        print(f"{'':{'-'}{'^'}{64}}")      

        for reaction in self.reactions:
            print(f"\t{reaction}")
        return  f"{'':{'-'}{'^'}{64}}"


    def initialize(self):
        """Initialize all chemical reactions included in the system using its current physiochemical parameters.

        :return: None
        :rtype: None
        """
        for reaction in self.reactions:
            reaction.initialize()

    def write_parameters_to_file(self, filename):
        """Writes a dictionary of standard system parameters and physical constants into a JSON file.

        :param filename: Name of the JSON file to write parameters to.
        :type filename: str
        :param R: Ideal gas constant R = 8.31446262 J/mol/K.
        :type R: float
        :param F: Faraday constant F = 96485.3321 A*s/mol.
        :type F: float
        :param T0: Standard temperature T0 = 298.15 degree Kelvin.
        :type T0: float
        :param P0: Standard pressure P0 = 1.00 bar.
        :type P0: float
        :param Reference_abbreviation: Abbreviation of the reference electrode.
        :type Reference_abbreviation: str
        :param dE: Potential difference of the reference electrode in volts vs. the standard hydrogen electrode.
        :type dE: float
        :param T: Temperature in degree Kelvin.
        :type T: float
        :param P: Pressure in bar.
        :type P: float
        :param pHmin: Minimum pH of the diagram.
        :type pHmin: float
        :param pHmax: Maximum pH of the diagram.
        :type pHmax: float
        :param Emin: Minimum potential of the diagram in volts vs. SHE.
        :type Emin: float
        :param Emax: Maximum potential of the diagram in volts vs. SHE.
        :type Emax: float 
        """
        parameter_dictionary = {
            "constants":[
                {
                    "R": Constants.GAS.value, 
                    "F": Constants.FARADAY.value,
                    "T0": Constants.STANDARD_TEMPERATURE.value,
                    "P0": Constants.STANDARD_PRESSURE.value,
                }
            ],
            "reference":[
                {
                    "Reference_abbreviation": self.reference_abbreviation,
                    "dE": self.deltaE
                }
            ],
            "variables":[
                {
                    "T": self.temperature,
                    "P": self.pressure,
                    "pHmin": self.pHmin,
                    "pHmax": self.pHmax,
                    "Emin": self.Emin,
                    "Emax": self.Emax
                }
            ]
        }
        
        json_string = json.dumps(parameter_dictionary, indent=2)
        with open(filename, 'w') as f:
            f.write(json_string)
    
    def read_parameters_from_file(self, filename):
        """Reads system parameters from a JSON file.

        :param filename: Name of the JSON file to read parameters from.
        :type filename: str
        :return: None
        :rtype: None
        """
        with open(filename, 'r') as f:
            json_object = json.loads(f.read())
        self.temperature  = json_object['variables'][0]['T']
        self.pressure     = json_object['variables'][0]['P']
        self.pHs          = (json_object['variables'][0]['pHmin'], 
                             json_object['variables'][0]['pHmax'])
        self.electrode_potentials = (json_object['variables'][0]['Emin'], 
                                     json_object['variables'][0]['Emax'])
        self.reference_electrode = (json_object['reference'][0]['Reference_abbreviation'],  json_object['reference'][0]['dE'])

    @property
    def temperature(self):
        """Get the system temperature.

        :return: Temperature in degrees Kelvin.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, value : float):
        """Validates the user-input temperature. If input is numerical
        and greater than 0, `298.15` otherwise.
        
        :param value: Temperature in degrees Kelvin.
        :type value: float
        :return: None
        :rtype: None
        """

        if not isinstance(value, (int,float)):
            warnings.warn(f'System temperature provided not a numerical input. It will be reset to {Defaults.temperature} K.')
            self._temperature = Defaults.temperature
        elif value < 0:
            warnings.warn(f'System temperature provided is less than 0 K. It will be reset to {Defaults.temperature} K.')
            self._temperature = Defaults.temperature
        else:
            self._temperature = value

    @property
    def pressure(self):
        """Get the system pressure.

        :return: Pressure in bar.
        :rtype: float
        """
        return self._pressure

    @pressure.setter
    def pressure(self, value : float):
        """Validates the user-input pressure. If input is numerical and
        greater than 0, `1.00` otherwise.

        :param value: Pressure in bar.
        :type value: float
        :return: None
        :rtype: None
        """
        if not isinstance(value, (int,float)):
            warnings.warn(f'System pressure provided not a numerical input. It will be reset to {Defaults.pressure} bar.')
            self._pressure = Defaults.pressure
        elif value < 0:
            warnings.warn(f'System temperature provided is less than 0 bar. It will be reset to {Defaults.pressure} bar.')
            self._pressure = Defaults.pressure
        else:
            self._pressure = value

    @property
    def pHs(self):
        """Get the system pH range.

        :return: A tuple containing the minimum and maximum pH values.
        :rtype: tuple
        """
        return (self._pHmin, self._pHmax)

    @pHs.setter
    def pHs(self, value : tuple):
        """Set the system pH range and automatically check which value is the lower one an which one corresponds to the upper limit.

        :param value: A tuple containing the minimum and maximum pH values.
        :type value: tuple
        :return: None
        :rtype: None
        """
        self.pHmin = min(value)
        self.pHmax = max(value)
        
    @property
    def pHmin(self):
        """Get the minimum pH value of the system.

        :return: Minimum pH value.
        :rtype: float
        """
        return self._pHmin

    @pHmin.setter
    def pHmin(self, value):
        """Validates the user-input lower pH limit. If input is
        numerical, `0.00` otherwise

        :param value: Minimum pH value.
        :type value: float
        :return: None
        :rtype: None
        """
        if not isinstance(value, (int,float)):
            warnings.warn(f'Lower pH limit provided not a numerical input. It will be reset to {Defaults.minimum_pH_value}')
            self._pHmin = Defaults.minimum_pH_value
        else:
            self._pHmin = value

    @property
    def pHmax(self):
        """Get the maximum pH value of the system.

        :return: Maximum pH value.
        :rtype: float
        """
        return self._pHmax

    @pHmax.setter
    def pHmax(self, value : float):
        """Validates the user-input upper pH limit. If input is
        numerical, `14.00` otherwise.

        :param value: Maximum pH value.
        :type value: float
        :return: None
        :rtype: None
        """
        if not isinstance(value, (int,float)):
            warnings.warn('Upper pH limit provided not a numerical input. It will be reset to {Defaults.maximum_pH_value}')
            self._pHmax = Defaults.maximum_pH_value
        else:
            self._pHmax = value

    @property
    def electrode_potentials(self):
        """Get the electrode potential range of the system and automatically check which value is the lower one an which one corresponds to the upper limit.

        :return: A tuple containing the minimum and maximum electrode potentials.
        :rtype: tuple
        """
        return (self._Emin, self._Emax)

    @electrode_potentials.setter
    def electrode_potentials(self, value : tuple):
        """Set the electrode potential range of the system.

        :param value: A tuple containing the minimum and maximum electrode potentials.
        :type value: tuple
        :return: None
        :rtype: None
        """
        self.Emin = min(value)
        self.Emax = max(value)

    @property
    def Emin(self):
        """Get the minimum electrode potential value of the system.

        :return: Minimum electrode potential value in volts vs. SHE.
        :rtype: float
        """
        return self._Emin

    @Emin.setter
    def Emin(self, value : float):
        """Validates the user-input lower potential limit.  If input
        is numerical, `-2.00` otherwise.

        :param value: Minimum electrode potential value in volts vs. SHE.
        :type value: float
        :return: None
        :rtype: None
        """
        if not isinstance(value, (int,float)):
            warnings.warn(f'Lower potential limit provided not a numerical input. It will be reset to {Defaults.minimum_electrode_potenital}')
            self._Emin = Defaults.minimum_electrode_potenital
        else:
            self._Emin = value
            

    @property
    def Emax(self):
        """Get the maximum electrode potential value of the system.

        :return: Maximum electrode potential value in volts vs. SHE.
        :rtype: float
        """
        return self._Emax

    @Emax.setter
    def Emax(self, value : float):
        """Validates the user-input upper potential limit. If input is
        numericla, `2.00` otherwise.

        :param value: Maximum electrode potential value in volts vs. SHE.
        :type value: float
        :return: None
        :rtype: None
        """
        if not isinstance(value, (int,float)):
            warnings.warn(f'Upper potential limit provided not a numerical input. It will be reset to {Defaults.maximum_electrode_potential}')
            self._Emax = Defaults.maximum_electrode_potential
        else:
            self._Emax = value

    @property
    def reference_electrode(self):
        """Get the reference electrode information.

        :return: A tuple containing the reference electrode abbreviation and potential difference.
        :rtype: tuple
        """
        return (self.reference_abbreviation, self.deltaE)

    @reference_electrode.setter
    def reference_electrode(self, value : tuple):
        """Validates the user-input reference electrode information.

        :param value: A tuple containing the reference electrode abbreviation and potential difference.
        :type value: tuple
        :return: None
        :rtype: None
        """
        abbreviation, dE = value
        self._reference_abbreviation = abbreviation
        if abbreviation in Defaults.reference_electrodes.keys():
            self._deltaE = Defaults.reference_electrodes[abbreviation]
        else:
            self._deltaE = dE
    
    @property
    def reference_abbreviation(self):
        """Get the abbreviation of the reference electrode.

        :return: Abbreviation of the reference electrode.
        :rtype: str
        """
        return self._reference_abbreviation

    @property
    def deltaE(self):
        """Get the potential difference of the reference electrode in volts vs. the standard hydrogen electrode.

        :return: Potential difference in volts.
        :rtype: float
        """
        return self._deltaE
    
    def add_elements(self, elements : list):
        """Adds elements to the chemical system.

        :param elements: List of chemical elements in the system.
        :type elements: list
        """
        self._get_elements(elements)


    @singledispatchmethod
    def add_reactions(self, reactions):
        raise NotImplementedError("The reactions type can be either list of dict() or string")

    @add_reactions.register(list)
    def _(self, reactions : list):
        """Adds reactions to the chemical system.

        :param reactions: List of chemical reactions in the system.
        :type reactions: list
        """
        self._get_reactions(reactions)
        
    @add_reactions.register(tuple)
    def _(self, reactions : tuple):
        reactions = self.db.add_reactions(reactions)
        self._get_reactions(reactions)

    def read_reactions_from_file(self, filename : str):
        """Reads the reactions from a file and adds reactions to the
        chemical system

        :param filename: filename with reactions
        :type filename: str
        """
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        self.add_reactions(tuple(lines))

    def set_aqueous_activity(self, element : str, activity : float):

        """Modifies the aqueous activity of singular elements previously defined to be included in the chemical system.

        :param element: Chemical element in the system.
        :type element: str
        :param activity: Chemical activity of `element`.
        :type activity: float
        """
        self._set_aqueous_activity(element, activity)
    
    def _get_elements(self, elements):
        """Validates the user-input list of chemical elements and updates the dictionary in system_parameters.json to include a dictionary of elements together with their aqueous activities.

        :param elements: List of chemical elements in the system.
        :type elements: list
        :raises ValueError: Error raised if the list of elements provided contains entries that are not in `element_list` of know and supported elements.
        :return: Dictionary of validated elements as keys and standard aqueous activities as values.
        :rtype: dict
        """
        for i in elements:
            try:
                i in element_list
            except ValueError:
                print(f"Chemical element '{i}' is not in the list of elements added to the reactive system.")
            
        # Adding the elements hydrogen (H) and oxygen (O) to element_list since they always have to be present to generate an aqueous Pourbaix diagram.
        elements.append("H")
        elements.append("O")
        for i in set(elements):
            self.elements.update({i: Defaults.activity})

    def construct_reactions_from_reactants(self, reactants : dict):
        """Validates the user-input reactants and constructs reactions from reactants from a dictionary containing the reactants and their corresponding activities.

        :param reactants: A dictionary of reactants (species) as keys and their corresponding activities as values.
        :type reactants: dict
        :return: A Reaction object created based on the provided reactants and activities.
        :rtype: Reaction
        :raises ValueError: If any reactant contains elements not yet added to the system.
        """
        constituent_dict = {}
        for j in reactants.keys():
            for k in j.atoms.keys():
                if k != "e" and k not in self.elements:
                    raise ValueError("Reactions added to the system feature elements that are not yet added to the system yet. Please add them using add_elements().")
            if j.state == State.aqueous.value:
                component_activity = [Defaults.activity]    
                for k in j.atoms.keys():
                    if k != "H" or k != "O" or k != "e":
                        component_activity.append(self.elements[k])
                activity = min(component_activity)
            else:
                activity = Defaults.activity
            constituent_dict.update({j: [reactants[j], activity] })

        return Reaction(constituent_dict, self)

    def _get_reactions(self, reactions):
        """Validates the user-input list of chemical reactions to appear on the Pourbaix diagram.

        :param reactions: List of chemical reactions in the system.
        :type reactions: list
        :raises ValueError: Error raised if list entries are not in the form of a dictionary. Further error validation upon creating the reaction() object from each entry provided.
        :return: List of chemical reaction objects featuring the systems potential and pH limits as well as the temperature and pressure.
        :rtype: list
        """
        for i in reactions:
            if type(i) != dict:
                raise ValueError("Reactions added to the system must be a dictionary of the reactants, their stoichiometric coefficients and activities.")
            constituent_dict = {}
            for j in i.keys():
                for k in j.atoms.keys():
                    if k != "e" and k not in self.elements:
                        raise ValueError("Reactions added to the system feature elements that are not yet added to the system yet. Please add them using add_elements().")
                if j.state == State.aqueous.value:
                    component_activity = [Defaults.activity]    
                    for k in j.atoms.keys():
                        if k != "H" or k != "O" or k != "e":
                            component_activity.append(self.elements[k])
                        activity = min(component_activity)
                else:
                    activity = Defaults.activity
                
                constituent_dict.update({j:[i[j], activity]})

            new_reaction = Reaction(constituent_dict, self)
            self.reactions.append(new_reaction)


    def _set_aqueous_activity(self, element : str, activity : float) -> dict:
        """Validates the user-input element and corresponding chemical activity and updates the dictionary in system_parameters.json.

        :param element: Chemical element whose activity is modified.
        :type element: str
        :param activity: Chemical activity of the element.
        :type activity: float
        :raises ValueError: Error raised if element provided is not part of the chemical system.
        :return: Dictionary of elements as keys and updated standard aqueous activities as values.
        :rtype: dict
        """
        
        if element not in self.elements:
            raise ValueError("Chemical element provided not is the list of chemical elements in the system.")
        if not isinstance(activity,(int,float)):
            warnings.warn(f'Chemical activity provided is not numerical. It will be reset to {Defaults.activity}')
            activity = Defaults.activity
        if activity < 0:
            warnings.warn(f'Chemical activity provided is negative. It will be reset to {Defaults.activity}')
            activity = Defaults.activity
        self.elements.update({element: activity})
