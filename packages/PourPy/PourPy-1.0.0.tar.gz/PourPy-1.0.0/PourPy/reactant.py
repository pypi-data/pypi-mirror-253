#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:57:37 2023

@author: anjakorber
"""

import numpy as np
import re
from .common import State

class Reactant:
    """Reactant class that defines an ion, compound or electron including all required thermodynamic and molecular parameters.
    """
    def __init__(self, formula, state, dGf, dHf, Sm, elements):
        """Constructor method for Reactant class.

        :param formula: Chemical formula of the reactant, e.g. H2O.
        :param state: State of the reactant (l, s, g, aq, or e).
        :param dGf: Standard Gibbs free energy of formation in joules per mole.
        :param dHf: Standard enthalpy of formation in joules per mole.
        :param Sm: Standard molar entropy in joules per mole per degree kelvin.
        """
        self.formula = self._get_formula(formula)
        self.state = self._get_state(state)
        self.charge = self._get_charge()
        self.atoms = self._get_atoms(elements)
        self.MW = self._get_molecular_weight(elements)
        self.dGf = dGf
        self.dHf = dHf
        self.Sm = Sm
        
        self.initialize()

    def __str__(self):
        padding = 8
        return f"{self.formula:8}\t{self.dGf:8}\t{self.dHf:8}\t{self.Sm:8}"

    def initialize(self):
        """Initialize additional properties of the Reactant.

        :return: None
        :rtype: None
        """
        self.reactant_string = self._get_reactant_string()
        self.intersectionsX = []
        self.intersectionsY = []


    def _get_formula(self, formula):
        """Validate and returns user-input chemical formula of the reactant.

        :param formula: The chemical formula to validate.
        :return: Validated chemical formula.
        """
        while len(formula) < 0 or not re.match("^[A-Za-z0-9-+\(\)\(|)]*$", formula):
            formula = input(formula, " is not a valid formula.\
                            \nThe formula must only contain numbers,\
                                letters, + and - .\
                            \nValid formula: ")
        return formula


    def _get_state(self, state):
        """Validates and returns the user-input physical state of the reactant.

        :param state: The physical state to validate.
        :return: Validated physical state.
        """

        states = [State.liquid.value, State.solid.value, State.gaseous.value, State.aqueous.value, State.electron.value]
        while not(state in states):
            state = input(state, " is not a valid state.\
                          \nThe physical state must be either liquid (l),\
                              solid (s), gaseous (g)\
                          \naqueous (aq) or that of an electron (e).\
                          \nValid state: ")
        return state
    
    def _get_charge(self):
        """Validates and returns the user-input charge of the reactant.

        :return: The charge of the reactant, 0 if not present.
        """
        if '|' not in self.formula:
            return 0
        else:
            h = 0
            for j in range(len(self.formula)-2,0, -1):
                if self.formula[j] == "|":
                    h = j
                    break
                
            return int(self.formula[h+1:-1])
    
    def _get_atoms(self, elements):
        """Retrieves a dictionary of atoms in the reactant.

        :return: A dictionary containing atom symbols as keys and their counts as values.
        """

        atoms = {}
        open_brackets = ["(", "[", "{"]
        close_brackets = ["}", "]", ")"]

        i = 0        
        while i < len(self.formula) and self.formula[i] != "|":
            if self.formula[i].isalpha():
                if (i+1 < len(self.formula) and self.formula[i+1].islower()):
                    el = self.formula[i:i+2]
                    i += 1
                else:
                    el = self.formula[i]
            else:
                i += 1
                continue
            if (el not in elements.keys()):
                print("Element {} not found in dict".format(el))
                return 0
    
            j = i+1
            while j < len(self.formula) and self.formula[j].isdecimal():
                j += 1
    
            if (i+1 == j):
                nel = 1
            else:
                nel = int(self.formula[i+1:j])
            i = j-1
    
            brac_level = 0
            for m in self.formula[:i]:
                if (m in open_brackets):
                    brac_level += 1
                if (m in close_brackets):
                    brac_level -= 1
    
            multf = 1
            for b in range(brac_level, 0, -1):
                b_current = b
                for m in range(i, len(self.formula)):
                    if (self.formula[m] in open_brackets):
                        b_current += 1
                        m
                        break
                    if self.formula[m] in close_brackets:
                        b_current -= 1
                        if (b_current == b-1):
                            k = m+1
                            while k < len(self.formula) and self.formula[k].isdecimal():
                                k += 1
                            if (k == m+1):
                                multf *= 1
                            else:
                                multf *= int(self.formula[m+1:k])
                            m = k-1
                            break
    
            if (el not in atoms):
                atoms[el] = multf*nel
            else:
                atoms[el] += multf*nel
            i += 1
        return atoms
    
    
    def _get_molecular_weight(self, elements):
        """Calculates the molecular weight of the reactant.

        :return: The molecular weight of the reactant in grams per mole.
        """
        mass = 0.0
        for i in self.atoms:
            mass += self.atoms[i]*elements[i]
        return mass
    
    
    def _get_super_string(self, x):
        """Converts numeric characters in the formula of the reactant to Unicode superscript characters.

        :param x: The input string to convert.
        :return: The input string with numeric characters replaced by super-script characters.
        """
        normal = "0123456789+-"
        super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)

    def _get_sub_string(self, x):
        """Converts numeric characters in the formula of the reactant to Unicode subscript characters.

        :param x: The input string to convert.
        :return: The input string with numeric characters replaced by sub-script characters.
        """
        normal = "0123456789+-"
        sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋"
        res = x.maketrans(''.join(normal), ''.join(sub_s))
        return x.translate(res)


    def _get_reactant_string(self):
        """Creates a formatted string representing the reactant formula.

        :return: Formatted string representation of the reactant, including subscripts for number of atoms and superscripts for charge.
        """
        # Split reactant into formula and charge
        stop = 0
        if '|' not in self.formula:
            formula = self.formula
            charge = ''
        else:
            for i in range(len(self.formula)-2,0,-1):
                if self.formula[i] == "|":
                    stop = i
                    break
            charge = self.formula[stop+1:-1]
            formula = self.formula[0:stop]
        
        # Get subscript numbers for formula
        new_formula = ""
        for i in formula:
            if i.isnumeric():
                new_formula += self._get_sub_string(i)
            else:
                new_formula += i
        
        return new_formula + self._get_super_string(charge)
        
