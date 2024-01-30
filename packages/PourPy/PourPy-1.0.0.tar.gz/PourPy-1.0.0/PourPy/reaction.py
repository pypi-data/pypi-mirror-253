#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:00:38 2023

@author: anjakorber
"""

import numpy as np
import json
from .reactant import Reactant
from .common import Constants, Defaults

class Reaction(object):
    """Reaction class featuring all reaction-specific parameters of the (electro)chemical reactions to be included in the Pourbaix diagram.
    """
    def __init__(self, constituents, system):
        """Constructor method for Reaction class.

        :param constituents: A dictionary of reactants as keys and their corresponding stoichiometric coefficients and activities as values.
        :type constituents: dict
        :param system: The chemical system to which this reaction belongs.
        :type system: System
        """
        self.constituents = constituents
        self.system = system
        self.initialize()
        
    def __str__(self):
        """Return the string representation of the reaction, where all reactants appear on the left hand side and all products appear on the right of the reacton arrow.

        :return: A string representation of the reaction, e.g., 'H2O ⇄ H2 + 0.5*O2'.
        :rtype: str
        """
        return self.reaction_string


    def initialize(self):
        """Initialize the Reaction object by calculating various reaction-specific properties.

        :return: None
        :rtype: None
        """
        for const in self.constituents:
            const.initialize()

        self.reaction_string = self._get_reaction_string()
        self.echem_reaction = self._get_echem_reaction()
        self.pH_reaction = self._get_pH_reaction()
        self.Hlimit = self._get_Hlimit()
        self.pourbaix_line = self._get_pourbaixLine()
        self.intersections = []
        self.lineBoundary = []
        self.intersecReac = []


    def _get_reaction_string(self):
        """Create the string representation of the reaction, where all reactants appear on the left hand side and all products appear on the right of the reacton arrow.

        Returns the string representation of the reaction, e.g., 'H2O ⇄ H2 + O2'.

        :return: A string representation of the reaction.
        :rtype: str
        """
        arrow = ' ⇄ '
        reactantStr = ''
        productStr = ''
        for i in self.constituents:
            stoicCoeff = str(abs(self.constituents[i][0]))
            if stoicCoeff == '1':
                stoicCoeff = ''
            if self.constituents[i][0] < 0:
                reactantStr += stoicCoeff + i.reactant_string + ' + '
            else:
                productStr += stoicCoeff + i.reactant_string + ' + '
        reactantStr = reactantStr[0:-3]
        productStr = productStr[0:-3]
        return reactantStr + arrow + productStr

    def _get_echem_reaction(self):
        """Checks if the reaction is an electrochemical reaction, i.e. whether it contains electrons, and returns True if it's electrochemical, otherwise returns False.

        :return: True if the reaction is electrochemical, False otherwise.
        :rtype: bool
        """

        for i in self.constituents:
            if i.formula == 'e|-1|':
                return True
        return False


    def _get_pH_reaction(self):
        """Checks if the reaction is a pH-dependent reaction, i.e. whether it contains protons, and returns True if it's pH-dependent, otherwise returns False.

        :return: True if the reaction is pH-dependent, False otherwise.
        :rtype: bool
        """

        for i in self.constituents:
            if i.formula == 'H|+1|': 
                return True
        return False

    @property
    def dGr(self) -> float:
        """Calculate the standard Gibbs free energy change of the reaction from the standard molar Gibbs free energies of all reation costituents.

        :return: The standard Gibbs free energy change of the reaction in joules per mole.
        :rtype: float
        """
        dGr = 0.0
        for i in self.constituents:
            dGr += self.constituents[i][0]*i.dGf
        return dGr
    
    @property
    def dHr(self) -> float:
        """Calculate the standard enthalpy change of the reaction from the standard molar enthalpies of all reation costituents.

        :return: The standard enthalpy change of the reaction in joules per mole.
        :rtype: float
        """
        dHr = 0.0
        for i in self.constituents:
            dHr += self.constituents[i][0]*i.dHf
        return dHr

    @property
    def dSr(self) -> float:
        """Calculate the standard entropy change of the reaction from the standard Gibbs free energy and enthalpy.

        :return: The standard entropy change of the reaction in joules per mole per degrees kelvin.
        :rtype: float
        """

        return (self.dHr - self.dGr)/Constants.STANDARD_TEMPERATURE.value

    @property
    def K(self):
        """Calculate the equilibrium constant for the reaction from its standard Gibbs free energy.

        :return: The equilibrium constant K for the reaction.
        :rtype: float
        """
    
        return np.exp(-1*self.dGr/Constants.GAS.value/self.system.temperature)

    @property
    def E0(self):
        """Calculate the standard electrode potential for the reaction in volts vs. SHE from its standard Gibbs gree energy.

        :return: The standard electrode potential E0 for the electrochemical reaction in volts vs. SHE, or 0 if the reaction is not an electrochemical reaction.
        :rtype: float
        """
        if not self.echem_reaction:
            return 0
        for i in self.constituents:
            if i.formula == 'e|-1|':
                return self.dGr/self.constituents[i][0]/Constants.FARADAY.value

    @property
    def nElectrons(self):
        """Retrieve the number of electrons involved in the reaction.

        :return: The number of electrons involved in the electrochemical reaction, or 0 if the reaction is not an electrochemical reaction.
        :rtype: float
        """
        if not self.echem_reaction:
            return 0
        for i in self.constituents:
            if i.formula == 'e|-1|':
                return self.constituents[i][0]

    @property
    def nProtons(self):
        """Retrieve the number of protons involved in the reaction.

        :return: The number of protons involved in the pH-dependent reaction, or 0 if the reaction is not pH-dependent.
        :rtype: float
        """
        if not self.pH_reaction:
            return 0
        for i in self.constituents:
            if i.formula == 'H|+1|':
                return self.constituents[i][0]
                
            
    def _get_Hlimit(self):
        """Retrieve the range of H+ activities corresponding to the pH limits of the Pourbaix diagram.

        :return: An array of H+ activities. 
        :rtype: numpy.ndarray
        """
        return 10**(-np.linspace(self.system.pHmin, self.system.pHmax, 2))
        
    @property
    def Q(self) -> float:
        """Calculate the reaction quotient Q for the reaction.

        :return: The reaction quotient Q for the reaction.
        :rtype: float
        """
        Q = 1.
        for i in self.constituents:
            Q *= self.constituents[i][1]**self.constituents[i][0]
        return Q

    @property
    def rQ(self) -> float:
        """Calculate the reduced reaction quotient rQ excluding the activity contribution of protons.

        :return: The reduced reaction quotient rQ for the reaction.
        :rtype: float
        """
        rQ = 1.
        for i in self.constituents:
            if i.formula != 'H|+1|':
                rQ *= self.constituents[i][1]**self.constituents[i][0]
        return rQ

    @property
    def QpH(self) -> list:
        """Calculate reaction quotient of the reaction at different H+ activities.

        :return: A list of reaction quotients at different H+ ion concentrations.
        :rtype: list
        """
        Q = []
        for i in range(len(self.Hlimit)):
            for j, value in self.constituents.items():
                if j.formula == 'H|+1|':
                    value[1] = self.Hlimit[i]
            Q.append(self.Q)
        return Q

    def _get_pourbaixLine(self):
        """Calculate the Pourbaix line formulated by the reaction.

        :return: A list of coordinates defining the Pourbaix line, depending on whether the reaction is potential- and/or pH-dependent.
        :rtype: list
        :raises ValueError: If the reaction is neither potential- nor pH-dependent.
        """
        if not(self.echem_reaction or self.pH_reaction):
            raise ValueError("The reaction is neither pH nor potential\
                             dependent and cannot be drawn.")
        elif self.echem_reaction and self.pH_reaction:
            E = self.E0 + (Constants.GAS.value*self.system.temperature/Constants.FARADAY.value/self.nElectrons)*np.log(self.QpH)
            return [self.system.pHmin, E[0], self.system.pHmax, E[-1]]
        elif self.pH_reaction:
            pH = -np.log10((self.K/self.rQ)**(1./self.nProtons))
            if pH < self.system.pHmin or pH > self.system.pHmax:
                return None
            return [pH, self.system.Emax, pH, self.system.Emin]
        elif self.echem_reaction:
            E = self.E0 + (Constants.GAS.value*self.system.temperature/Constants.FARADAY.value/self.nElectrons)*np.log(self.Q)
            return [self.system.pHmin, E, self.system.pHmax, E]
            
    def _sanity_check(self):
        """Perform a sanity check on the total charge and atom balance of all species in the reaction.

        :return: A message indicating whether charge and atom balances are correct or if there's a warning.
        :rtype: str
        """
        charge_balance = 0
        for i in self.constituents:
            charge_balance += i.charge * self.constituents[i][0]
         
        balanced_atoms = {}
        for i in self.constituents:
            for j in i.atoms:
                if j not in balanced_atoms:
                    balanced_atoms[j] = i.atoms[j]*self.constituents[i][0]
                else:
                    balanced_atoms[j] += i.atoms[j]*self.constituents[i][0]
        atom_balance = 0
        for h in balanced_atoms:
            if h != 'e': # !!!! somethings off, should be e|-1|, doesnt work
                atom_balance += balanced_atoms[h]
        if charge_balance == 0 and atom_balance == 0:
            return 'Both the charge and the atoms are balanced.'
        elif charge_balance == 0:
            return 'WARNING: The atoms are not balanced.' 
        elif atom_balance == 0:
            return 'WARNING: The charge of the constituents is not balanced.'
        else:
            return 'WARNING: Neither the charge nor the atoms are balanced.'
        
    
    def _balanced_charge(self):
        """Check if the reaction is charge-balanced.

        :return: True if the reaction's charge is balanced, False otherwise.
        :rtype: bool
        """
        balance = 0
        for i in self.constituents:
            balance += i.charge * self.constituents[i][0]
        return balance == 0
    
    
    def _balanced_atoms(self):
        """Check if the reaction has balanced numbers of atoms of each chemical element.

        :return: True if the reaction's atoms are balanced, False otherwise.
        :rtype: bool
        """
        balanced_atoms = {}
        for i in self.constituents:
            for j in i.atoms:
                if j not in balanced_atoms:
                    balanced_atoms[j] = i.atoms[j]*self.constituents[i][0]
                else:
                    balanced_atoms[j] += i.atoms[j]*self.constituents[i][0]
        balance = 0
        for h in balanced_atoms:
            if h != 'e|-1|':
                balance += balanced_atoms[h]
        return balance == 0
        
        
        
                
        
        
