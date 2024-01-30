 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:01:46 2023

@author: anjakorber
"""

# Handhabung für H+ und e-?
# jeweils H|+1| und e|-1?|


import numpy as np
import warnings
import math
import random

from .reaction import Reaction
from .parser import DefaultParser
from .common import Defaults

# Bokeh Moduls
from bokeh import io, plotting, models, layouts
from bokeh.palettes import Set3_12 as palette
from colorsys import rgb_to_hsv, hsv_to_rgb
import itertools

# Matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import shapely 


class PourbaixDiagram(object): 
    """
    PourbaixDiagram class that defines and plots a Pourbaix diagram.

    :param reactive_system: The reactive system for which the diagram is constructed.
    :type reactive_system: ReactiveSystem

    :param HER: Hydrogen Evolution Reaction.
    :type HER: Reaction, optional

    :param OER: Oxygen Evolution Reaction.
    :type OER: Reaction, optional
    """

    def __init__(self, reactive_system, line_inspection=False, HER=False, OER=False):
        """
        Initialize the PourbaixDiagram class with the given user-defined reactive system and reactions.

        :param reactive_system: The reactive system for which the diagram is constructed.
        :type reactive_system: ReactiveSystem

        :param HER: The hydrogen evolution reaction (HER).
        :type HER: Reaction, optional

        :param OER: The oxygen evolution reaction (OER).
        :type OER: Reaction, optional
        """
        self.system = reactive_system
        self.inspectorMode = line_inspection
        if HER is True:
            self.HER    =  [self.system.pHmin, 0.000 - 0.059*self.system.pHmin, self.system.pHmax, 0.000 - 0.059*self.system.pHmax]
        else:
            self.HER    =  None
        if OER is True:
            self.OER    =  [self.system.pHmin, 1.23 - 0.059*self.system.pHmin, self.system.pHmax, 1.23 - 0.059*self.system.pHmax]
        else:
            self.OER    =  None
        self.stable_regions = dict()        
    
    def solve(self):
        """
        Solve the Pourbaix diagram by computing the intersections of all Nernst equation reaction lines and the regions of stability enclosed between the lines.
        """
        self.system.initialize()
        if self.inspectorMode is False:
            self._compute_intersections(self._get_unique_constitutents())
            self._compute_boundary_lines(self.system)
            self._construct_stability_regions()
        
    def show(self, backend='bokeh', plot_regions=False, labelling=True):
        """
        Plots the Pourbaix diagram using the specified plotting backend.

        :param backend: The plotting backend to use (either 'bokeh' or 'matplotlib').
        :type backend: str

        :raises RuntimeError: If the specified backend is invalid.
        """
        if backend == 'bokeh':
            io.show(self._get_bokeh_plot(plot_regions, labelling))
        elif backend == 'matplotlib':
            self._get_matplotlib_plot(plot_regions, labelling)
        else:
            raise RuntimeError('Invalid backend. Please specify either "bokeh" or "matplotlib".')

    def _get_unique_constitutents(self):
        """
        Get a dictionary of unique constituents in the included in the reactive system.
        Species H+, e-, H2O(l), O2(g) and H2(g) are automatically excluded, as these species are unique constituents of the aqueous solvent bound by the HER and OER by default.
 
        :return: A dictionary of unique constituents.
        :rtype: dict
        """
        if len(self.system.reactions) < 1:
            raise ValueError("The physical system provided has no reactions to be plotted.")

        unique_constituents = dict()
        exclude = ['H|+1|', 'e|-1|', 'H2O', 'O2', 'H2', 'HCO3|-1|']

        for reaction in self.system.reactions:
            if reaction.pourbaix_line is None:
                continue

            for constituent in reaction.constituents:
                if constituent.formula not in exclude and constituent not in unique_constituents:
                    associated_reactions = []
                    for k in self.system.reactions:
                        if constituent in k.constituents and k.pourbaix_line is not None:
                            associated_reactions.append(k)

                    # only include constituents with two valid reactions
                    if len(associated_reactions) > 1:
                        unique_constituents.update({constituent: associated_reactions})

        return unique_constituents

    @staticmethod
    def _compute_intersections(unique_constituents : dict):
        """
        Compute intersections between the reactions marking the stablity region of each unique constituent.

        :param unique_constituents: A dictionary of unique constituents.
        :type unique_constituents: dict
        """

        tolerance = 1e-5
        for i in unique_constituents:
            if len(unique_constituents[i]) == 1:
                continue
            for j in unique_constituents[i]:
                for k in unique_constituents[i]:
                    if j != k:
                        [x1, y1, x2, y2] = j.pourbaix_line
                        [x3, y3, x4, y4] = k.pourbaix_line
                        if j.echem_reaction and j.pH_reaction and k.echem_reaction and k.pH_reaction:
                            k1 = (y2-y1)/(x2-x1)
                            d1 = y1 - k1*x1
                            k3 = (y4-y3)/(x4-x3)
                            d3 = y3 - k3*x3
                            if abs(k1 - k3) > tolerance:
                                x = (d3-d1)/(k1-k3)
                                j.intersections.append([x, k1*x + d1])
                                j.intersecReac.append(k)
                        elif j.echem_reaction and j.pH_reaction and k.pH_reaction:
                            k1 = (y2-y1)/(x2-x1)
                            d1 = y1 - k1*x1
                            j.intersections.append([x3, k1*x3+d1])
                            j.intersecReac.append(k)
                        elif j.pH_reaction and k.echem_reaction and k.pH_reaction:
                            k3 = (y4-y3)/(x4-x3)
                            d3 = y3 - k3*x3
                            j.intersections.append([x1, k3*x1+d3])
                            j.intersecReac.append(k)
                        elif j.echem_reaction and j.pH_reaction and k.echem_reaction:
                            k1 = (y2-y1)/(x2-x1)
                            d1 = y1 - k1*x1
                            j.intersections.append([(y3-d1)/k1, y3])
                            j.intersecReac.append(k)
                        elif j.echem_reaction and k.echem_reaction and k.pH_reaction:
                            k3 = (y4-y3)/(x4-x3)
                            d3 = y3 - k3*x3
                            j.intersections.append([(y1-d3)/k3, y1])
                            j.intersecReac.append(k)
                        elif j.echem_reaction and k.pH_reaction:
                            j.intersections.append([x3, y1])
                            j.intersecReac.append(k)
                        elif j.pH_reaction and k.echem_reaction:
                            j.intersections.append([x1, y3])
                            j.intersecReac.append(k)
        
    @staticmethod
    def _compute_boundary_lines(system):
        """
        Compute the boundary lines that actually enclose the stability region of each unique constituent.

        :param system: The reactive system.
        :type system: ReactiveSystem
        """
        tolerance = 1e-4
        for i in system.reactions:
            
            if i.pourbaix_line is None:
                continue
            
            a = i.intersections
            b = i.intersecReac

            i.intersections = []
            i.intersecReac = []
            j = 0
            while j < len(a):
                k = j+1
                while k < len(a):
                    if abs(a[j][0]-a[k][0]) < tolerance and abs(a[j][1]-a[k][1]) < tolerance:
                        i.intersections.append(a[j])
                        i.intersecReac.append(b[j])
                        a = [x for x in a if a[j] != x]
                        b = [x for x in b if b[j] != x]
                        j = 0
                        k = 0
                    k += 1
                j += 1

    
                
            if len(i.intersections) == 1:
                dummyReaction = i.intersecReac[0]
                VZReactant = 0
                VZe = 0
                VZH = 0
                for j in i.constituents:
                    for k in dummyReaction.constituents:
                        if j == k and j.formula not in ['H|+1|', 'e|-1|', 'H2O', 'O2', 'H2', 'HCO3|-1|']:
                            VZReactant = dummyReaction.constituents[k][0]
                        if k.formula == 'e|-1|':
                            VZe = dummyReaction.constituents[k][0]
                        if k.formula == 'H|+1|':
                            VZH = dummyReaction.constituents[k][0]
                            
                            
                if dummyReaction.pH_reaction and dummyReaction.echem_reaction:
                    if i.pH_reaction and i.echem_reaction:
                        [x1, y1, x2, y2] = dummyReaction.pourbaix_line
                        [x3, y3, x4, y4] = i.pourbaix_line
                        k1 = (y2-y1)/(x2-x1)
                        k3 = (y4-y3)/(x4-x3)
                    if (VZReactant < 0 and VZe < 0) or (VZReactant > 0 and VZe > 0):
                        if i.pH_reaction and i.echem_reaction:
                            if k1 < k3:
                                i.intersections.append(i.pourbaix_line[2:4])
                            else:
                                i.intersections.append(i.pourbaix_line[0:2])
                        elif i.pH_reaction:
                            i.intersections.append(i.pourbaix_line[0:2])
                        elif i.echem_reaction:
                            i.intersections.append(i.pourbaix_line[2:4])
                    elif (VZReactant < 0 and VZe > 0) or (VZReactant > 0 and VZe < 0):
                        if i.pH_reaction and i.echem_reaction:
                            if k1 < k3:
                                i.intersections.append(i.pourbaix_line[0:2])
                            elif k1 > k3:
                                i.intersections.append(i.pourbaix_line[2:4])
                        elif i.pH_reaction:
                            i.intersections.append(i.pourbaix_line[2:4])
                        elif i.echem_reaction:
                            i.intersections.append(i.pourbaix_line[0:2])
                            
                            
                elif dummyReaction.pH_reaction:
                    if (VZReactant < 0 and VZH < 0) or (VZReactant > 0 and VZH > 0):
                        i.intersections.append(i.pourbaix_line[2:4])
                    elif (VZReactant < 0 and VZH > 0) or (VZReactant > 0 and VZH < 0):
                        i.intersections.append(i.pourbaix_line[0:2])
                        
                        
                elif dummyReaction.echem_reaction:
                    if (VZReactant < 0 and VZe < 0) or (VZReactant > 0 and VZe > 0):
                        i.intersections.append(i.pourbaix_line[0:2])
                    elif (VZReactant < 0 and VZe > 0) or (VZReactant > 0 and VZe < 0):
                        i.intersections.append(i.pourbaix_line[2:4])

    def _construct_stability_regions(self):
        """
        Construct stability regions on the Pourbaix diagram.

        This method calculates stability regions for different constituents on the Pourbaix diagram
        and adds corner points where the computed intersection points are on the boundary of the diagram.

        :return: None
        :rtype: None
        """
        unique_constituents = self._get_unique_constitutents()
        for i in unique_constituents:
            for j in self.system.reactions:
                if i in j.constituents:
                    for k in j.intersections:
                        if k[0] not in i.intersectionsX or k[1] not in i.intersectionsY:
                            i.intersectionsX.append(k[0])
                            i.intersectionsY.append(k[1])
                        if k[0] in i.intersectionsX and k[1] in i.intersectionsY and i.intersectionsX.index(k[0]) == i.intersectionsY.index(k[1]):
                            pass
                        else:
                            i.intersectionsX.append(k[0])
                            i.intersectionsY.append(k[1])

            try:
                x_avg = sum(i.intersectionsX)/len(i.intersectionsX)
                y_avg = sum(i.intersectionsY)/len(i.intersectionsY)
            except ZeroDivisionError as e:
                x_avg = 0
                y_avg = 0

            # Adding corner points where needed:
            min_pH = self.system.pHmin
            max_pH = self.system.pHmax

            if min_pH in i.intersectionsX:
                indices = []
                for idx, value in enumerate(i.intersectionsX):
                    if value == min_pH:
                        indices.append(idx)
                if self.system.Emax in i.intersectionsY and len(indices) < 3:
                    i.intersectionsX.append(min_pH)
                    i.intersectionsY.append(self.system.Emax)
                elif self.system.Emin in i.intersectionsY and len(indices) < 3:
                    i.intersectionsX.append(min_pH)
                    i.intersectionsY.append(self.system.Emin)
                elif self.system.Emin not in i.intersectionsY and self.system.Emax not in i.intersectionsY and len(indices) < 3:
                    del1 = abs(self.system.Emin - y_avg) 
                    del2 = abs(self.system.Emax - y_avg)
                    if del2 > del1:
                        i.intersectionsX.append(min_pH)
                        i.intersectionsY.append(self.system.Emin)
                    else:
                        i.intersectionsX.append(min_pH)
                        i.intersectionsY.append(self.system.Emax)

            if max_pH in i.intersectionsX:
                if self.system.Emax in i.intersectionsY:
                    i.intersectionsX.append(max_pH)
                    i.intersectionsY.append(self.system.Emax)
                if self.system.Emin in i.intersectionsY:
                    i.intersectionsX.append(max_pH)
                    i.intersectionsY.append(self.system.Emin)

            def polar_angle(point, reference_point):
                """
                Calculate the polar angle of a point relative to a reference intersection point.

                :param point: The point to calculate the angle for.
                :type point: tuple
                :param reference_point: The reference point with respect to which the angle is calculated.
                :type reference_point: tuple

                :return: The polar angle of the point relative to the reference point.
                :rtype: float
                """
                dx = point[0] - reference_point[0]
                dy = point[1] - reference_point[1]
                return (math.atan2(dy, dx) + 2 * math.pi) % (2 * math.pi)

            # Sorting all intersection points according to the polar angle of a point relative to a reference point:
            points = list(zip(i.intersectionsX, (y + self.system.deltaE for y in i.intersectionsY)))

            # Recompute the x and y average after adding various corner points:
            try:
                x_avg = sum(i.intersectionsX)/len(i.intersectionsX)
                y_avg = sum(i.intersectionsY)/len(i.intersectionsY)
            except ZeroDivisionError as e:
                x_avg = 0
                y_avg = 0

            sorted_points = sorted(points,
                                   key =
                                   lambda point:
                                   polar_angle(point, [x_avg, y_avg]))

            region = shapely.Polygon(tuple(sorted_points))
            minx, miny, maxx, maxy = region.bounds

            self.stable_regions[str(i.reactant_string)] = shapely.Polygon(tuple(sorted_points))

    def get_stable_phases(self):
        """
        Get all stable phases within the created Pourbaix diagram.

        :return: A list of stable phases.
        :rtype: list
        """
        return self.stable_regions.keys()

    def get_stable_phase_at(self, pH, potential):
        """
        Get the stable phase at a specific pH, potential coordinate relative to the reference electrode.

        :param pH: The pH value.
        :type pH: float
        :param potential: The potential value.
        :type potential: float

        :return: The stable phase at the specified pH and potential.
        :rtype: str

        :raises: warnings.warn if the point does not exist within the calculated range.
        """
        for key, value in self.stable_regions.items():
            if value.contains(shapely.Point(pH, potential)) is True:
                return key
            else:
                continue
            
        warnings.warn('Given point does not exist within the calculated range. Please modify the pH and potential limits of the diagram.')
        return 0
            
    def _get_matplotlib_plot(self, plot_regions=False, labelling=True):
        """
        Display the created Pourbaix diagram using Matplotlib.

        :return: None
        :rtype: None
        """
        plt.figure(figsize=(8, 8))
        ax = plt.axes()
        if self.inspectorMode is True:
            for i in self.system.reactions:
                xy = i.pourbaix_line
                ax.plot([xy[0], xy[2]], [xy[1] + self.system.deltaE, xy[3] + self.system.deltaE], color='k', lw=0.6)
        else:
            for i in self.system.reactions:
                if i.pourbaix_line is None:
                    continue
                if len(i.intersections) >= 2:
                    xy = i.intersections
                    ax.plot([xy[0][0], xy[1][0]], [xy[0][1] + self.system.deltaE, xy[1][1] + self.system.deltaE],
                            color='k', lw=0.6)

        if self.HER != None:
            ax.plot([self.HER[0], self.HER[2]], [self.HER[1] + self.system.deltaE, self.HER[3] + self.system.deltaE],
                    color='blue', lw=0.6)
        if self.OER != None:
            ax.plot([self.OER[0], self.OER[2]], [self.OER[1] + self.system.deltaE, self.OER[3] + self.system.deltaE],
                    color='blue', lw=0.6)

        nb_regions = len(self.get_stable_phases())
        if labelling is True:
            patches = []
            for key, value in self.stable_regions.items():
                polygon = Polygon(shapely.get_coordinates(value), closed=True, label=key)
                patches.append(polygon)
                ax.text(shapely.centroid(value).x, shapely.centroid(value).y, key,
                        ha='center', va='center', transform=ax.transData)
            if plot_regions is True:
                colors = 100 * np.arange(nb_regions)
                p = PatchCollection(patches, alpha=0.2)
                p.set_array(np.array(colors))
                ax.add_collection(p)
                
        ax.set_ylim([self.system.Emin + self.system.deltaE, self.system.Emax + self.system.deltaE])
        ax.set_xlim([self.system.pHmin, self.system.pHmax])
  
        ax.set_xlabel('pH', size=12)
        ax.set_ylabel('Potential V vs. ' + self.system.reference_abbreviation, size=12)
        plt.tight_layout()
        plt.show()

    def _get_bokeh_plot(self, plot_regions=True,labelling=True):
        """
        Display and return the created Pourbaix diagram using Bokeh.

        :return: Bokeh plot object.
        :rtype: Bokeh.plotting.figure
        """
        p = plotting.figure(
            title="POURBAIX DIAGRAM",
            x_axis_label='pH',
            y_axis_label='Potential V vs. ' + self.system.reference_abbreviation,
            x_range=(self.system.pHmin, self.system.pHmax),
            y_range=(self.system.Emin + self.system.deltaE,self.system.Emax + self.system.deltaE),
            width=800,
            height=800
        )

        if self.inspectorMode is True:
            for i in self.system.reactions:
                line_tooltip = [
                    ("pH, potential", "($x, $y)"),
                    ("Reaction", str(i.reaction_string),)
                ]
                p.line([i.pourbaix_line[0],i.pourbaix_line[2]],[i.pourbaix_line[1] + self.system.deltaE, i.pourbaix_line[3] + self.system.deltaE])
                p.add_tools(models.HoverTool(renderers=[p.renderers[-1]], tooltips=line_tooltip))
        else:
            for i in self.system.reactions:
                if len(i.intersections) >= 2 and i.pourbaix_line is not None:
                    line_tooltip = [
                    ("(pH, potential)", "($x, $y)"),
                    ("Reaction", str(i.reaction_string)),
                    ]
                    p.line([i.intersections[0][0],i.intersections[1][0]],[i.intersections[0][1] + self.system.deltaE, i.intersections[1][1] + self.system.deltaE])
                    p.add_tools(models.HoverTool(renderers=[p.renderers[-1]], tooltips=line_tooltip))



            # Plotting HER and OER:
            if self.HER != None:
                HER_tooltip = [
                ("(pH, potential)", "($x, $y)"),
                ("Component", "HER"),
                ]
                p.line([self.HER[0], self.HER[2]],[self.HER[1] + self.system.deltaE, self.HER[3] + self.system.deltaE], line_dash='dashed',line_color='black')
                p.add_tools(models.HoverTool(renderers=[p.renderers[-1]], tooltips=HER_tooltip))
            if self.OER != None:
                OER_tooltip = [
                ("(pH, potential)", "($x, $y)"),
                ("Reaction", "OER" ),
                ]
                p.line([self.OER[0], self.OER[2]],[self.OER[1] + self.system.deltaE, self.OER[3] + self.system.deltaE], line_dash='dashed',line_color='black')
                p.add_tools(models.HoverTool(renderers=[p.renderers[-1]], tooltips=OER_tooltip))

            # Plotting regions of stability        
            colors = itertools.cycle(palette)    


        stability_regions = []
        if plot_regions is True:
            unique_const = self._get_unique_constitutents()
            for i, fill_color in zip(unique_const, colors):
                if len(unique_const[i]) == 1:
                    continue
                coords = shapely.get_coordinates(self.stable_regions[str(i.reactant_string)])
                centroid = shapely.centroid(self.stable_regions[str(i.reactant_string)])

                sorted_x = coords[:, 0]
                sorted_y = coords[:, 1]
                x_avg = centroid.x
                y_avg = centroid.y
                
                stability_region = p.patch(sorted_x, sorted_y, fill_color=fill_color, alpha=0.5)
                stability_regions.append(stability_region)

                fill_tooltip = [
                    ("(pH, potential)", "($x, $y)"),
                    ("Component", str(i.reactant_string)),
                ]
                p.add_tools(models.HoverTool(renderers=[stability_region], tooltips=fill_tooltip))
                if labelling is True:
                    stability_label =p.text(x_avg, y_avg, text=[str(i.reactant_string)], text_align="center", text_baseline="middle")

        # pH range slider
        range_slider = models.RangeSlider(
            title="Adjust x-axis range",
            start=self.system.pHmin,
            end=self.system.pHmax,
            step=1,
            value=(p.x_range.start, p.x_range.end),
        )
        range_slider.js_link("value", p.x_range, "start", attr_selector=0)
        range_slider.js_link("value", p.x_range, "end", attr_selector=1)

        # Create Layout and Show Result
        layout_standard = layouts.layout([[range_slider],[p]])

        return layout_standard
