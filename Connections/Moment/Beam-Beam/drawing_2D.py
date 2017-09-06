'''
Created on 24-Aug-2017

@author: reshma
'''
from numpy import math
import svgwrite
import cairosvg
import numpy as np
import os


class ExtendedEndPlate(object):
    def __init__(self):
        # self.filename = filename
        self.beam_length_L1 = 1000
        self.beam_length_L2 = 1000

        self.beam_depth_D1 = 400
        self.beam_depth_D2 = 400

        self.beam_width_B1 = 140
        self.beam_width_B2 = 140

        self.plate_thickness_p1 = 20
        self.plate_thickness_p2 = 20

        self.plate_width_B1 = 178.4
        self.plate_width_B2 = 178.4

        self.plate_length_L1 = 613.4
        self.plate_length_L2 = 613.4

        self.flange_thickness_T1 = 16
        self.flange_thickness_T2 = 16

        self.web_thickness_tw1 = 8.9
        self.web_thickness_tw2 = 8.9

        self.flange_weld_thickness = 12
        self.web_weld_thickness = 8

        self.bolt_diameter = 24
        self.bolt_hole_diameter =26
        self.edge_dist = 44.2
        self.end_dist = self.edge_dist
        self.cross_centre_gauge_dist = 90
        self.pitch = 60

        self.bolts_outside_top_flange_col = 2
        self.bolts_outside_top_flange_row = 1  # TODO value should come from dict

        self.bolts_inside_top_flange_col = 2
        self.bolts_inside_top_flange_row = 2    # TODO value should come from dict

        self.bolts_inside_bottom_flange_col = 2
        self.bolts_inside_bottom_flange_row = 2   # TODO value should come from dict

        self.bolts_outside_bottom_flange_col = 2
        self.bolts_outside_bottom_flange_row = 1   # TODO value should come from dict

    def add_s_marker(self, dwg):
        """

        Args:
            dwg: svgwrite (obj)

        Returns: Container for all svg elements

        """
        smarker = dwg.marker(insert=(8, 3), size=(30, 30), orient="auto")
        smarker.add(dwg.path(d=" M0,0 L3,3 L0,6 L8,3 L0,0", fill="black"))
        dwg.defs.add(smarker)
        return smarker

    def add_section_marker(self, dwg):
        """

        Args:
            dwg: svgwrite (obj)

        Returns: Container for all svg elements

        """
        section_marker = dwg.marker(insert=(0,5), size=(10, 10), orient="auto")
        section_marker.add(dwg.path(d="M 0 0 L 10 5 L 0 10 z", fill="blue", stroke="black"))
        dwg.defs.add(section_marker)
        return section_marker

    def add_e_marker(self, dwg):
        """

        Args:
            dwg: svgwrite (obj)

        Returns: Container for all svg elements

        """
        emarker = dwg.marker(insert=(0, 3), size=(30, 20), orient="auto")
        emarker.add(dwg.path(d=" M0,3 L8,6 L5,3 L8,0 L0,3", fill="black"))
        dwg.defs.add(emarker)
        return emarker

    def draw_start_arrow(self, line, s_arrow):
        """

        Args:
            line: start line marker
            s_arrow: start arrow

        Returns:

        """
        line["marker-start"] = s_arrow.get_funciri()

    def draw_end_arrow(self, line, e_arrow):
        """

        Args:
            line: end line marker
            e_arrow: end arrow

        Returns:

        """
        line["marker-end"] = e_arrow.get_funciri()

    def draw_faint_line(self, pt_one, pt_two, dwg):
        """

        Args:
            pt_one: first point
            pt_two: second point
            dwg: svgwrite (obj)

        Returns:

        """
        dwg.add(dwg.line(pt_one, pt_two).stroke("#D8D8D8", width=2.5, linecap="square", opacity=0.70))

    def draw_dimension_outer_arrow(self, dwg, pt1, pt2, text, params):
        # TODO

        """

        Args:
            dwg: svgwrite (obj)
            pt1: first point
            pt2: second point
            text: text message
            params:

        Returns:

        """
        smarker = self.add_s_marker(dwg)
        emarker = self.add_e_marker(dwg)
        line_vector = pt2 - pt1               #[a, b]
        normal_vector = np.array([-line_vector[1], line_vector[0]])     #[-b, a]
        normal_unit_vector = self.normalize(normal_vector)

        if params["lineori"] == "left":
            normal_unit_vector = -normal_unit_vector

        Q1 = pt1 + params["offset"] * normal_unit_vector
        Q2 = pt2 + params["offset"] * normal_unit_vector
        line = dwg.add(dwg.line(Q1, Q2).stroke("black", width=2.5, linecap="square"))
        self.draw_start_arrow(line, emarker)
        self.draw_end_arrow(line, smarker)

        Q12_mid = 0.5 * (Q1 + Q2)
        text_pt = Q12_mid + params["textoffset"] * normal_unit_vector
        dwg.add(dwg.text(text, insert=text_pt, fill="black", font_family="sans-serif", font_size=28))

        L1 = Q1 + params["endlinedim"] * normal_unit_vector
        L2 = Q1 + params["endlinedim"] * (-normal_unit_vector)
        dwg.add(dwg.line(L1, L2).stroke("black", width=2.5, linecap="square", opacity=1.0))

        L3 = Q2 + params["endlinedim"] * normal_unit_vector
        L4 = Q2 + params["endlinedim"] * (-normal_unit_vector)
        dwg.add(dwg.line(L3, L4).stroke("black", width=2.5, linecap="square", opacity=1.0))

    def normalize(self, vector):
        """

        Args:
            vector: vector

        Returns:

        """
        a = vector[0]
        b = vector[1]
        magnitude = math.sqrt(a*a + b*b)
        return vector/magnitude

    def draw_cross_section(self, dwg, pt_a, pt_b, text_pt, text):
        """

        Args:
            dwg: svgwrite (obj)
            pt_a: point A
            pt_b: point B
            text_pt: text point
            text: text message

        Returns:

        """
        line = dwg.add(dwg.line(pt_a, pt_b). stroke("black", width=2.5, linecap="square"))
        sec_arrow = self.add_section_marker(dwg)
        self.draw_end_arrow(line, sec_arrow)
        dwg.add(dwg.text(text, insert=text_pt, fill="black", font_family="sans-serif", font_size=52))

    def draw_dimension_inner_arrow(self, dwg, pt_a, pt_b, text, params):
        # TODO
        """

        Args:
            dwg: svgwrite (obj)
            pt_a: point A
            pt_b: point B
            text: text message
            params:
        Returns:

        """
        smarker = self.add_s_marker(dwg)
        emarker = self.add_e_marker(dwg)
        u = pt_b - pt_a          #[a, b]
        u_unit = self.normalize(u)
        v_unit = np.array([-u_unit[1], u_unit[0]])       #[-b, a]

        A1 = pt_a + params["endlinedim"] * v_unit
        A2 = pt_a + params["endlinedim"] * (-v_unit)
        dwg.add(dwg.line(A1, A2).stroke("black", width=2.5, linecap="square"))

        B1 = pt_b + params["endlinedim"] * v_unit
        B2 = pt_a + params["endlinedim"] * (-v_unit)
        dwg.add(dwg.line(B1, B2). stroke("black",width=2.5, linecap="square"))

        A3 = pt_a - params["arrowlen"] * u_unit
        B3 = pt_b + params["arrowlen"] * u_unit
        line = dwg.add(dwg.line(A3, pt_a).stroke("black", width=2.5, linecap="square"))
        self.draw_end_arrow(line, smarker)

        line = dwg.add(dwg.line(B3, pt_b).stroke("black", width=2.5, linecap="butt"))
        self.draw_end_arrow(line, smarker)

        if params["lineori"] == "right":
            text_pt = B3 + params["textoffset"] * u_unit
        else:
            text_pt = A3 - (params["textoffset"] + 100) * u_unit

        dwg.add(dwg.text(text, insert=text_pt, fill="black", font_family='sans-serif', font_size=28))

    def draw_oriented_arrow(self, dwg, point, theta, orientation, offset, textup, textdown):
        """

        Args:
            dwg: svgwrite (obj)
            point: point
            theta: theta
            orientation: direction (east, west, south, north)
            offset: position of the text
            textup: text written above line
            textdown: text written below line

        Returns:

        """
        #Right Up.
        theta = math.radians(theta)
        char_width = 16
        x_vector = np.array([1, 0])
        y_vector = np.array([0, 1])

        p1 = point
        length_A = offset/(math.sin(theta))

        arrow_vector = None
        if orientation == "NE":
            arrow_vector = np.array([-math.cos(theta), math.sin(theta)])
        elif orientation == "NW":
            arrow_vector = np.array([math.cos(theta), math.sin(theta)])
        elif orientation == "SE":
            arrow_vector = np.array([-math.cos(theta), -math.sin(theta)])
        elif orientation == "SW":
            arrow_vector = np.array([math.cos(theta), -math.sin(theta)])
        p2 = p1 - length_A * arrow_vector

        text = textdown if len(textdown) > len(textup) else textup
        length_B = len(text) * char_width

        label_vector = None
        if orientation == "NE":
            label_vector = -x_vector
        elif orientation == "NW":
            label_vector = x_vector
        elif orientation == "SE":
            label_vector = -x_vector
        elif orientation == "SW":
            label_vector = x_vector
        p3 = p2 + length_B * (-label_vector)

        text_offset = 18
        offset_vector = -y_vector

        text_point_up = None
        text_point_down = None
        if orientation == "NE":
            text_point_up = p2 + 0.1 * length_B * (-label_vector) + text_offset * offset_vector
            text_point_down = p2 - 0.2 * length_B * label_vector - (text_offset + 15) * offset_vector
        elif orientation == "NW":
            text_point_up = p3 + 0.1 * length_B * (label_vector) + text_offset * offset_vector
            text_point_down = p3 - 0.2 * length_B * label_vector - (text_offset + 15) * offset_vector
        elif orientation == "SE":
            text_point_up = p2 + 0.1 * length_B * (-label_vector) + text_offset * offset_vector
            text_point_down = p2 - 0.1 * length_B * label_vector - (text_offset + 15) * offset_vector
        elif orientation == "SW":
            text_point_up = p3 + 0.2 * length_B * (label_vector) + text_offset * offset_vector
            text_point_down = p3 - 0.2 * length_B * label_vector - (text_offset + 15) * offset_vector

        line = dwg.add(dwg.polyline(points=[p1, p2, p3], fill="none", stroke='black', stroke_width=2.5))

        emarker = self.add_e_marker(dwg)
        self.draw_start_arrow(line, emarker)

        dwg.add(dwg.text(textup, insert=text_point_up, fill='black', font_family='sans-serif', font_size=28))
        dwg.add(dwg.text(textdown, insert=text_point_down, fill='black', font_family='sans-serif', font_size=28))

        print "successful"

    def save_to_svg(self, filename, view):
        """

        Args:
            filename: path of the folder
            view: front, top, side views of drawings to be generated

        Returns:
            None

        Note:


        """
        extnd_bothway_end_2d_front = ExtendedEnd2DFront(self)
        extnd_bothway_end_2d_top = ExtendedEnd2DTop(self)
        extnd_bothway_end_2d_side = ExtendedEnd2DSide(self)
        if view == "Front":
            extnd_bothway_end_2d_front.call_ExtndBoth_front(filename)
            # cairosvg.svg2png(file_obj=filename, write_to="D:\PyCharmWorkspace\Osdag\Connections\Moment\Beam-Beam")
        elif view == "Top":
            extnd_bothway_end_2d_top.call_ExtndBoth_top(filename)

        elif view == "Side":
            extnd_bothway_end_2d_side.call_ExtndBoth_side(filename)
        else:
            filename = "D:\PyCharmWorkspace\Osdag\Connections\Moment\Beam-Beam\TFront.svg"
            extnd_bothway_end_2d_front.call_ExtndBoth_front(filename)


class ExtendedEnd2DFront(object):
    """
    Contains functions for generating the front view of the Extended bothway endplate
     connection.
    """
    def __init__(self, extnd_common_object):
        self.data_object = extnd_common_object

        # --------------------------------------------------------------------------
        #                               FRONT VIEW
        # --------------------------------------------------------------------------
        # ================ Primary Beam 1 ================

        ptA1x = 0
        ptA1y =0
        self.A1 = np.array([ptA1x, ptA1y])

        ptA2x = ptA1x + self.data_object.beam_length_L1
        ptA2y = 0
        self.A2 = np.array([ptA2x, ptA2y])

        ptA6x = ptA2x
        ptA6y = ptA2y + self.data_object.flange_thickness_T1
        self.A6 = np.array([ptA6x, ptA6y])

        ptA7x = ptA2x
        ptA7y = ptA2y + (self.data_object.beam_depth_D1 - self.data_object.flange_thickness_T1)
        self.A7 = np.array([ptA7x, ptA7y])

        ptA3x = ptA2x
        ptA3y = ptA2y + self.data_object.beam_depth_D1
        self.A3 = np.array([ptA3x, ptA3y])

        ptA4x = ptA1x
        ptA4y = ptA1y + self.data_object.beam_depth_D1
        self.A4 = np.array([ptA4x, ptA4y])

        ptA8x = ptA1x
        ptA8y =  ptA4y - self.data_object.flange_thickness_T1 #(self.data_object.beam_depth_D1 - self.data_object.flange_thickness_T1)
        self.A8 = np.array([ptA8x, ptA8y])

        ptA5x = ptA1x
        ptA5y = self.data_object.flange_thickness_T1
        self.A5 = np.array([ptA5x, ptA5y])

        self.Q = self.A6 + self.data_object.web_weld_thickness * np.array([-1, 0])

        # =========================  End Plate 1  =========================

        ptP1x = self.data_object.beam_length_L1
        ptP1y = -(self.data_object.plate_length_L1 - self.data_object.beam_depth_D1)/2
        self.P1 = np.array([ptP1x, ptP1y])

        ptP2x = ptP1x + self.data_object.plate_thickness_p1
        ptP2y = ptP1y
        self.P2 = np.array([ptP2x, ptP2y])

        ptP3x =  ptP2x
        ptP3y = (self.data_object.plate_length_L1 + self.data_object.beam_depth_D1)/2
        self.P3 = np.array([ptP3x, ptP3y])

        ptP4x = ptP1x
        ptP4y = ptP3y
        self.P4 = np.array([ptP4x, ptP4y])

        # ------------------------------------------  Weld triangle  UP-------------------------------------------
        self.B3 = self.A2
        self.B2 = self.B3 + self.data_object.flange_weld_thickness * np.array([-1, 0])
        self.B1 = self.B3 + self.data_object.flange_weld_thickness * np.array([0, -1])

        self.B6 = self.A3
        self.B5 = self.B6 + self.data_object.flange_weld_thickness * np.array([-1, 0])
        self.B4 = self.B6 + self.data_object.flange_weld_thickness * np.array([0, 1])

        # ------------------------------------------  Weld triangle  DOWN -------------------------------------------
        self.B7 = self.A6
        self.B8 = self.B7 + self.data_object.flange_weld_thickness * np.array([0, 1])
        self.B9 = self.B7 + self.data_object.flange_weld_thickness * np.array([-1, 0])

        self.B11 = self.A7
        self.B12 = self.B11 + self.data_object.flange_weld_thickness * np.array([-1, 0])
        self.B13 = self.B11 + self.data_object.flange_weld_thickness * np.array([0, -1])

        # =========================  End Plate 2  =========================

        ptPP1x = ptP2x
        ptPP1y = -(self.data_object.plate_length_L2 - self.data_object.beam_depth_D2)/2
        self.PP1 = np.array([ptPP1x, ptPP1y])

        ptPP2x = ptPP1x + self.data_object.plate_thickness_p2
        ptPP2y = ptPP1y
        self.PP2 = np.array([ptPP2x, ptPP2y])

        ptPP3x = ptPP2x
        ptPP3y = (self.data_object.plate_length_L2 + self.data_object.beam_depth_D2)/2
        self.PP3 = np.array([ptPP3x, ptPP3y])

        ptPP4x = ptPP1x
        ptPP4y = ptPP3y
        self.PP4 = np.array([ptPP4x, ptPP4y])

        # =========================  Primary Beam 2  =========================

        ptAA1x = ptPP2x  #self.data_object.beam_length_L1 + self.data_object.plate_thickness_p1 + self.data_object.plate_thickness_p2
        ptAA1y = 0
        self.AA1 = np.array([ptAA1x, ptAA1y])

        ptAA2x = ptAA1x + self.data_object.beam_length_L2
        ptAA2y = 0
        self.AA2 = np.array([ptAA2x, ptAA2y])

        ptAA6x = ptAA2x
        ptAA6y = self.data_object.flange_thickness_T2
        self.AA6 = np.array([ptAA6x, ptAA6y])

        ptAA7x = ptAA2x
        ptAA7y = (self.data_object.beam_depth_D2 - self.data_object.flange_thickness_T2)
        self.AA7 = np.array([ptAA7x, ptAA7y])

        ptAA3x = ptAA2x
        ptAA3y = self.data_object.beam_depth_D2
        self.AA3 = np.array([ptAA3x, ptAA3y])

        ptAA4x = ptAA1x
        ptAA4y = self.data_object.beam_depth_D2
        self.AA4 = np.array([ptAA4x, ptAA4y])

        ptAA8x = ptAA1x
        ptAA8y = (self.data_object.beam_depth_D2 - self.data_object.flange_thickness_T2)
        self.AA8 = np.array([ptAA8x, ptAA8y])

        ptAA5x = ptAA1x
        ptAA5y = self.data_object.flange_thickness_T2
        self.AA5 = np.array([ptAA5x, ptAA5y])

        # ------------------------------------------  Weld triangle UP -------------------------------------------
        self.BB3 = self.AA1
        self.BB2 = self.BB3 + self.data_object.flange_weld_thickness * np.array([1, 0])
        self.BB1 = self.BB3 + self.data_object.flange_weld_thickness * np.array([0, -1])

        self.BB7 = self.AA5
        self.BB8 = self.BB7 + self.data_object.flange_weld_thickness * np.array([0, 1])
        self.BB9 = self.BB7 + self.data_object.flange_weld_thickness * np.array([1, 0])


        # ------------------------------------------  Weld triangle  DOWN -------------------------------------------
        self.BB6 = self.AA4
        self.BB5 = self.BB6 + self.data_object.flange_weld_thickness * np.array([1, 0])
        self.BB4 = self.BB6 + self.data_object.flange_weld_thickness * np.array([0, 1])

        self.BB11 = self.AA8
        self.BB12 = self.BB11 + self.data_object.flange_weld_thickness * np.array([1, 0])
        self.BB13 = self.BB11 + self.data_object.flange_weld_thickness * np.array([0, -1])


    def call_ExtndBoth_front(self, filename):
        dwg = svgwrite.Drawing(filename, size=('100%', '100%'), viewBox=('-330 -600 1600 1800'))
        dwg.add(dwg.polyline(points=[self.A1, self.A2, self.A3, self.A4, self.A1], stroke='blue', fill='none', stroke_width=2.5))
        dwg.add(dwg.line(self.A5, self.A6).stroke('blue', width=2.5, linecap='square'))
        dwg.add(dwg.line(self.A8, self.A7).stroke('blue', width=2.5, linecap='square'))

        dwg.add(dwg.polyline(points=[self.P1, self.P2, self.P3, self.P4, self.P1], stroke='blue', fill='none', stroke_width='2.5'))
        dwg.add(dwg.polyline(points=[self.PP1, self.PP2, self.PP3, self.PP4, self.PP1], stroke='blue', fill='none', stroke_width=2.5))

        dwg.add(dwg.polyline(points=[self.AA1, self.AA2, self.AA3, self.AA4, self.AA1], stroke='blue', fill='none', stroke_width=2.5))
        dwg.add(dwg.line(self.AA5, self.AA6).stroke('blue', width=2.5, linecap='square'))
        dwg.add(dwg.line(self.AA8, self.AA7).stroke('blue', width=2.5, linecap='square'))

        pattern = dwg.defs.add(dwg.pattern(id="diagonalHatch", size=(6, 6), patternUnits="userSpaceOnUse", patternTransform="rotate(45 2 2)"))
        pattern.add(dwg.path(d="M 0,1 l 6,0", stroke='#000000', stroke_width=2.5))
        dwg.add(dwg.rect(insert=self.Q, size=(self.data_object.web_weld_thickness, (self.data_object.beam_depth_D1 - self.data_object.flange_thickness_T1 - self.data_object.flange_weld_thickness - 10)), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.AA5, size=(self.data_object.web_weld_thickness, (self.data_object.beam_depth_D2 - self.data_object.flange_thickness_T2 - self.data_object.flange_weld_thickness - 10)), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))

        dwg.add(dwg.polyline(points=[self.B3, self.B2, self.B1, self.B3], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.B6, self.B5, self.B4, self.B6], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.B7, self.B8, self.B9, self.B7], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.B11, self.B12, self.B13, self.B11], stroke='black', fill='black', stroke_width=2.5))

        dwg.add(dwg.polyline(points=[self.BB3, self.BB2, self.BB1, self.BB3], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.BB6, self.BB5, self.BB4, self.BB6], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.BB8, self.BB7, self.BB9, self.BB8], stroke='black', fill='black', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.BB12, self.BB11, self.BB13, self.BB12], stroke='black', fill='black', stroke_width=2.5))

        # ------------------------------------------  Primary Beam 1& 2 -------------------------------------------
        point = self.A1 + (self.data_object.beam_length_L1/2) * np.array([1, 0])
        theta = 60
        offset = 50
        textup = "Primary beam 1 " + str(self.data_object.beam_length_L1) + " x "+ str(self.data_object.beam_depth_D1)+ " x " + str(self.data_object.beam_width_B1)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NW", offset, textup, textdown)

        point = self.AA1 + (self.data_object.beam_length_L2/2) * np.array([1, 0])
        theta = 60
        offset = 50
        textup = "Primary beam 2 " + str(self.data_object.beam_length_L2) + " x "+ str(self.data_object.beam_depth_D2)+ " x " + str(self.data_object.beam_width_B2)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NE", offset, textup, textdown)

        # ------------------------------------------  End Plate 1 & 2-------------------------------------------
        point = self.P1
        theta = 60
        offset = 50
        textup = "End Plate 1 " + str(self.data_object.plate_length_L1) + " x "+ str(self.data_object.plate_thickness_p1) + " x " + str(self.data_object.plate_width_B1)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NW", offset, textup, textdown)

        point = self.PP2
        theta = 60
        offset = 50
        textup = "End Plate 2 " + str(self.data_object.plate_length_L2) + " x "+ str(self.data_object.plate_thickness_p2) + " x " + str(self.data_object.plate_width_B2)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NE", offset, textup, textdown)

        # ------------------------------------------  View details-------------------------------------------
        ptx = self.P4 - 100 * np.array([1, 0]) + 100 * np.array([0, 1])
        dwg.add(dwg.text('Front view (Sec C-C) ', insert=ptx, fill='black', font_family="sans-serif", font_size=30))
        ptx1 = ptx + 40 * np.array([0, 1])
        dwg.add(dwg.text('(All distances are in "mm")', insert=ptx1, fill='black', font_family="sans-serif", font_size=30))

        dwg.save()


class ExtendedEnd2DTop(object):
    """

    """
    def __init__(self, extnd_common_object):
        self.data_object = extnd_common_object
        # -------------------------------------------------------------------------------------------------
        #                                           TOP VIEW
        # -------------------------------------------------------------------------------------------------
        # ====================== Primary Beam 1  =====================

        ptA1x = 0
        ptA1y = 0
        self.A1 = np.array([ptA1x, ptA1y])

        ptA2x = ptA1x + self.data_object.beam_length_L1
        ptA2y = 0
        self.A2 = np.array([ptA2x, ptA2y])

        ptA7x = ptA2x
        ptA7y = ptA2y + (self.data_object.beam_width_B1 - self.data_object.web_thickness_tw1)/2
        self.A7 = np.array([ptA7x, ptA7y])

        ptA8x = ptA2x
        ptA8y = ptA7y + self.data_object.web_thickness_tw1
        self.A8 = np.array([ptA8x, ptA8y])

        ptA3x = ptA2x
        ptA3y = ptA2y + self.data_object.beam_width_B1
        self.A3 = np.array([ptA3x, ptA3y])

        ptA4x = 0
        ptA4y = ptA1y + self.data_object.beam_width_B1
        self.A4 = np.array([ptA4x, ptA4y])

        ptA5x = 0
        ptA5y = ptA1y + (self.data_object.beam_width_B1 + self.data_object.web_thickness_tw1)/2
        self.A5 = np.array([ptA5x, ptA5y])

        ptA6x = 0
        ptA6y = ptA5y - self.data_object.web_thickness_tw1
        self.A6 = np.array([ptA6x, ptA6y])

        # ------------------------------------------  Weld triangle  UP-------------------------------------------
        self.B1 = self.A7
        self.B2 = self.B1 + self.data_object.web_weld_thickness * np.array([-1, 0])
        self.B3 = self.B1 + self.data_object.web_weld_thickness * np.array([0, -1])

        # ------------------------------------------  Weld triangle  DOWN -------------------------------------------
        self.B4 = self.A8
        self.B5 = self.B4 + self.data_object.web_weld_thickness * np.array([-1, 0])
        self.B6 = self.B4 + self.data_object.web_weld_thickness * np.array([0, 1])

        # ====================== End Plate 1  =====================
        ptP1x = self.data_object.beam_length_L1
        ptP1y = -(self.data_object.plate_width_B1 - self.data_object.beam_width_B1)/2
        self.P1 = np.array([ptP1x, ptP1y])

        ptP2x = ptP1x + self.data_object.plate_thickness_p1
        ptP2y = ptP1y
        self.P2 = np.array([ptP2x, ptP2y])

        ptP3x = ptP2x
        ptP3y = (self.data_object.plate_width_B1 + self.data_object.beam_width_B1)/2
        self.P3 = np.array([ptP3x, ptP3y])

        ptP4x = ptP1x
        ptP4y = ptP3y
        self.P4 = np.array([ptP4x, ptP4y])

        # ====================== End Plate 2  =====================
        ptPP1x = ptP2x
        ptPP1y = -(self.data_object.plate_width_B2 - self.data_object.beam_width_B2)/2
        self.PP1 = np.array([ptPP1x, ptPP1y])

        ptPP2x = ptPP1x + self.data_object.plate_thickness_p2
        ptPP2y = ptPP1y
        self.PP2 = np.array([ptPP2x, ptPP2y])

        ptPP3x = ptPP2x
        ptPP3y = (self.data_object.plate_width_B2 + self.data_object.beam_width_B2)/2
        self.PP3 = np.array([ptPP3x, ptPP3y])

        ptPP4x = ptPP1x
        ptPP4y = ptPP3y
        self.PP4 = np.array([ptPP4x, ptPP4y])

        # ====================== Primary Beam 2  =====================
        ptAA1x = ptPP2x
        ptAA1y = 0
        self.AA1 = np.array([ptAA1x, ptAA1y])

        ptAA2x = ptAA1x + self.data_object.beam_length_L2
        ptAA2y = 0
        self.AA2 = np.array([ptAA2x, ptAA2y])

        ptAA7x = ptAA2x
        ptAA7y = ptAA2y + (self.data_object.beam_width_B2 - self.data_object.web_thickness_tw2)/2
        self.AA7 = np.array([ptAA7x, ptAA7y])

        ptAA8x = ptAA2x
        ptAA8y = ptAA7y + self.data_object.web_thickness_tw2
        self.AA8 = np.array([ptAA8x, ptAA8y])

        ptAA3x = ptAA2x
        ptAA3y = ptAA2y + self.data_object.beam_width_B2
        self.AA3 = np.array([ptAA3x, ptAA3y])

        ptAA4x = ptAA1x
        ptAA4y = ptAA1y + self.data_object.beam_width_B2
        self.AA4 = np.array([ptAA4x, ptAA4y])

        ptAA5x = ptAA1x
        ptAA5y =  ptAA4y - (self.data_object.beam_width_B2 - self.data_object.web_thickness_tw2)/2
        self.AA5 = np.array([ptAA5x, ptAA5y])

        ptAA6x = ptAA1x
        ptAA6y = ptAA5y - self.data_object.web_thickness_tw2
        self.AA6 = np.array([ptAA6x, ptAA6y])

        self.P = self.A2 + self.data_object.flange_weld_thickness * np.array([-1, 0])

        # ------------------------------------------  Weld triangle  UP-------------------------------------------
        self.BB1 = self.AA6
        self.BB2 = self.BB1 + self.data_object.web_weld_thickness * np.array([1, 0])
        self.BB3 = self.BB1 + self.data_object.web_weld_thickness * np.array([0, -1])

        # ------------------------------------------  Weld triangle  DOWN-------------------------------------------
        self.BB4 = self.AA5
        self.BB5 = self.BB4 + self.data_object.web_weld_thickness * np.array([1, 0])
        self.BB6 = self.BB4 + self.data_object.web_weld_thickness * np.array([0, 1])


    def call_ExtndBoth_top(self, filename):
        dwg = svgwrite.Drawing(filename, size=('100%', '100%'), viewBox=('-150 -700 1500 1800' ))
        dwg.add(dwg.line(self.A5, self.A8).stroke('red', width=2.5, linecap='square').dasharray(dasharray=[5, 5]))
        dwg.add(dwg.line(self.A6, self.A7).stroke('red', width=2.5, linecap='square').dasharray(dasharray=[5, 5]))
        dwg.add(dwg.polyline(points=[self.A1, self.A2, self.A3, self.A4, self.A1], stroke='blue', fill='none', stroke_width=2.5))

        dwg.add(dwg.polyline(points=[self.P1, self.P2, self.P3, self.P4, self.P1], stroke='blue', fill='none', stroke_width='2.5'))
        dwg.add(dwg.polyline(points=[self.PP1, self.PP2, self.PP3, self.PP4, self.PP1], stroke='blue', fill='none', stroke_width=2.5))

        dwg.add(dwg.line(self.AA5, self.AA8).stroke('red', width=2.5, linecap='square').dasharray(dasharray=[5, 5]))
        dwg.add(dwg.line(self.AA6, self.AA7).stroke('red', width=2.5, linecap='square').dasharray(dasharray=[5, 5]))
        dwg.add(dwg.polyline(points=[self.AA1, self.AA2, self.AA3, self.AA4, self.AA1], stroke='blue', fill='none', stroke_width=2.5))

        dwg.add(dwg.polyline(points=[self.B1, self.B2, self.B3, self.B1], stroke='red', fill='red', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.B4, self.B5, self.B6, self.B4], stroke='red', fill='red', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.BB1, self.BB2, self.BB3, self.BB1], stroke='red', fill='red', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.BB4, self.BB5, self.BB6, self.BB4], stroke='red', fill='red', stroke_width=2.5))

        pattern = dwg.defs.add(dwg.pattern(id="diagonalHatch", size=(6, 6), patternUnits="userSpaceOnUse", patternTransform="rotate(45 2 2)"))
        pattern.add(dwg.path(d="M 0,1 l 6,0", stroke='#000000', stroke_width=2.5))
        dwg.add(dwg.rect(insert=self.P, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.AA1, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B2), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))

        # ------------------------------------------  Primary Beam 1& 2 -------------------------------------------
        point = self.A3 - self.data_object.beam_length_L1 /2 * np.array([1, 0])
        theta = 60
        offset = 150
        textup = " "
        textdown = "Primary Beam1 " + " x "+ str(self.data_object.beam_length_L1) + " x " + str(self.data_object.beam_width_B1) +" x " + str(self.data_object.beam_depth_D1)
        self.data_object.draw_oriented_arrow(dwg, point, theta, "SE", offset, textup, textdown)

        point = self.AA2 - self.data_object.beam_length_L2/2 * np.array([1, 0])
        theta = 60
        offset = 50
        textup = "Primary Beam2 " + " x "+ str(self.data_object.beam_length_L2) + " x " + str(self.data_object.beam_width_B2) + " x " + str(self.data_object.beam_depth_D2)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NE", offset, textup, textdown)

        # ------------------------------------------  End Plate 1 & 2-------------------------------------------
        point = self.P4
        theta = 60
        offset = 50
        textup = " "
        textdown = "End Plate1 " + " x " + str(self.data_object.plate_length_L1) + " x " + str(self.data_object.plate_width_B1) + " x " + str(self.data_object.plate_thickness_p1)
        self.data_object.draw_oriented_arrow(dwg, point, theta, "SE", offset, textup, textdown)

        point = self.PP2
        theta = 60
        offset = 100
        textup = "End Plate2 " + " x " + str(self.data_object.plate_length_L2) + " x " + str(self.data_object.plate_width_B2) + " x " + str(self.data_object.plate_thickness_p2)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point,  theta, "NE", offset, textup, textdown)

        # ------------------------------------------  View details-------------------------------------------
        ptx = self.P4 - 50 * np.array([1, 0]) + 400 * np.array([0, 1])
        dwg.add(dwg.text('Top view (Sec A-A) ', insert=ptx, fill='black', font_family="sans-serif", font_size=30))
        ptx1 = ptx + 40 * np.array([0, 1])
        dwg.add(dwg.text('(All distances are in "mm")', insert=ptx1, fill='black', font_family="sans-serif", font_size=30))

        dwg.save()

class ExtendedEnd2DSide(object):
    """

    """
    def __init__(self, extnd_common_object):
        self.data_object = extnd_common_object

        # =========================  End Plate 1  =========================
        ptP1x = 0
        ptP1y = 0 #(self.data_object.plate_length_L1 + self.data_object.beam_depth_D1)/2
        self.P1 = np.array([ptP1x, ptP1y])

        ptP2x = self.data_object.plate_width_B1
        ptP2y = 0
        self.P2 = np.array([ptP2x, ptP2y])

        ptP3x = self.data_object.plate_width_B1
        ptP3y = self.data_object.plate_length_L1
        self.P3 = np.array([ptP3x, ptP3y])

        ptP4x = 0
        ptP4y = self.data_object.plate_length_L1
        self.P4 = np.array([ptP4x, ptP4y])

        # =========================  Primary Beam 1  =========================
        ptA1x = (self.data_object.plate_width_B1 - self.data_object.beam_width_B1) / 2
        ptA1y = (self.data_object.plate_length_L1 - self.data_object.beam_depth_D1) / 2
        self.A1 = np.array([ptA1x, ptA1y])

        ptA2x = ptA1x + self.data_object.beam_width_B1
        ptA2y = ptA1y
        self.A2 = np.array([ptA2x, ptA2y])

        ptA3x = ptA2x
        ptA3y = ptA2y + self.data_object.flange_thickness_T1
        self.A3 = np.array([ptA3x, ptA3y])

        ptA12x = ptA1x
        ptA12y = ptA1y + self.data_object.flange_thickness_T1
        self.A12 = np.array([ptA12x, ptA12y])

        ptA4x = ptA12x + (self.data_object.beam_width_B1 / 2 + self.data_object.web_thickness_tw1 / 2)
        ptA4y = ptA3y
        self.A4 = np.array([ptA4x, ptA4y])

        ptA8x = ptA1x
        ptA8y = (self.data_object.plate_length_L1 + self.data_object.beam_depth_D1) / 2
        self.A8 = np.array([ptA8x, ptA8y])

        ptA9x = ptA1x
        ptA9y = ptA8y - self.data_object.flange_thickness_T1
        self.A9 = np.array([ptA9x, ptA9y])

        ptA7x = ptA8x + self.data_object.beam_width_B1
        ptA7y = ptA8y
        self.A7 = np.array([ptA7x, ptA7y])

        ptA6x = ptA7x
        ptA6y = ptA7y - self.data_object.flange_thickness_T1
        self.A6 = np.array([ptA6x, ptA6y])

        ptA5x = ptA4x
        ptA5y = ptA6y
        self.A5 = np.array([ptA5x, ptA5y])

        ptA11x = ptA12x + (self.data_object.beam_width_B1 / 2 - self.data_object.web_thickness_tw1 / 2)
        ptA11y = ptA12y
        self.A11 = np.array([ptA11x, ptA11y])

        ptA10x = ptA11x
        ptA10y = ptA9y
        self.A10 = np.array([ptA10x, ptA10y])

        self.P = self.A11 - self.data_object.web_weld_thickness * np.array([1, 0])
        self.Q = self.A1 - self.data_object.web_weld_thickness * np.array([1, 0])
        self.R = self.A9 - self.data_object.web_weld_thickness * np.array([1, 0])


    def call_ExtndBoth_side(self, filename):
        dwg = svgwrite.Drawing(filename, size=('100%', '100%'), viewBox=('-350 -500 1200 1400'))
        dwg.add(dwg.polyline(points=[self.A1, self.A2, self.A3, self.A4, self.A5 , self.A6, self.A7, self.A8, self.A9, self.A10, self.A11, self.A12, self.A1], stroke='blue', fill='none', stroke_width=2.5))
        dwg.add(dwg.polyline(points=[self.P1, self.P2, self.P3, self.P4, self.P1], stroke='blue', fill='none', stroke_width='2.5'))

        pattern = dwg.defs.add(dwg.pattern(id="diagonalHatch", size=(6, 6), patternUnits="userSpaceOnUse", patternTransform="rotate(45 2 2)"))
        pattern.add(dwg.path(d="M 0,1 l 6,0", stroke='#000000', stroke_width=2.5))
        dwg.add(dwg.rect(insert=self.P, size=(self.data_object.web_weld_thickness, (self.data_object.beam_depth_D1 - (2 * self.data_object.flange_thickness_T1))), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.A4, size=(self.data_object.web_weld_thickness, (self.data_object.beam_depth_D2 - (2 * self.data_object.flange_thickness_T2))), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.Q, size=(self.data_object.web_weld_thickness, self.data_object.flange_thickness_T2), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.A2, size=(self.data_object.web_weld_thickness, self.data_object.flange_thickness_T2), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.R, size=(self.data_object.web_weld_thickness, ( self.data_object.flange_thickness_T2)), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))
        dwg.add(dwg.rect(insert=self.A6, size=(self.data_object.web_weld_thickness, ( self.data_object.flange_thickness_T2)), fill="url(#diagonalHatch)", stroke='white', stroke_width=1.0))

        # TODO hatching lines flange welding (horizontally)
        # pattern1 = dwg.defs.add(dwg.pattern(id="diagonalHatch1", size=(6, 6), patternUnits="userSpaceOnUse", patternTransform="rotate(45 2 2)"))
        # pattern1.add(dwg.path(d="M 0,1 l 6,0", stroke='#000000', stroke_width=2.5))
        # dwg.add(dwg.rect(insert=self.S, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))
        # dwg.add(dwg.rect(insert=self.T, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))
        # dwg.add(dwg.rect(insert=self.S, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))
        # dwg.add(dwg.rect(insert=self.S, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))
        # dwg.add(dwg.rect(insert=self.S, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))
        # dwg.add(dwg.rect(insert=self.S, size=(self.data_object.flange_weld_thickness, self.data_object.beam_width_B1), fill="url(#diagonalHatch1)", stroke='white', stroke_width=1.0))

        botfc = self.data_object.bolts_outside_top_flange_col
        botfr = self.data_object.bolts_outside_top_flange_row
        bitfc = self.data_object.bolts_inside_top_flange_col
        bitfr = self.data_object.bolts_inside_top_flange_row
        bolt_r = int(self.data_object.bolt_diameter)/2

        # ------------------------------------------  Bolts Outside Top Flange -------------------------------------------
        pt_outside_top_column_list = []

        for i in range(1, (botfr + 1)):
            col_outside_list_top = []
            for j in range(1, (botfc + 1)):
                pt = self.P1 + ((self.data_object.plate_length_L1 - self.data_object.beam_depth_D1)/2 - self.data_object.end_dist) * np.array([0, 1]) + \
                     self.data_object.edge_dist * np.array([1, 0]) + (i - 1) * self.data_object.pitch * np.array([0, 1]) + (j - 1) * self.data_object.cross_centre_gauge_dist * np.array([1, 0])
                dwg.add(dwg.circle(center=pt, r=bolt_r, stroke='blue', fill='none', stroke_width=1.5))
                pt_C = pt - (bolt_r + 4) * np.array([1, 0])
                pt_D = pt + (bolt_r + 4) * np.array([1, 0])
                dwg.add(dwg.line(pt_C, pt_D).stroke('red', width=1.0, linecap='square'))

                pt_C1 = pt - (bolt_r + 4) * np.array([0, 1])
                pt_D1 = pt + (bolt_r + 4) * np.array([0, 1])
                dwg.add(dwg.line(pt_C1, pt_D1).stroke('red', width=1.0, linecap='square'))

                col_outside_list_top.append(pt)
            pt_outside_top_column_list.append(col_outside_list_top)

        # ------------------------------------------  Bolts Inside Top Flange -------------------------------------------
        # pt_inside_top_column_list = []
        # for i in range(1, (bitfr + 1)):
        #     col_inside_list_top = []
        #     for j in range(1, (bitfc + 1)):
        #         pt = self.A12 + (self.data_object.end_dist) * np.array([0, -1]) + \
        #              self.data_object.edge_dist * np.array([1, 0]) + (i - 1) * self.data_object.pitch * np.array([0, 1]) + (j - 1) * self.data_object.cross_centre_gauge_dist * np.array([1, 0])
        #         dwg.add(dwg.circle(center=pt, r=bolt_r, stroke='blue', fill='none', stroke_width=1.5))
        #         pt_C = pt - (bolt_r + 4) * np.array([1, 0])
        #         pt_D = pt + (bolt_r + 4) * np.array([1, 0])
        #         dwg.add(dwg.line(pt_C, pt_D).stroke('red', width=1.0, linecap='square'))
        #
        #         pt_C1 = pt - (bolt_r + 4) * np.array([0, 1])
        #         pt_D1 = pt + (bolt_r + 4) * np.array([0, 1])
        #         dwg.add(dwg.line(pt_C1, pt_D1).stroke('red', width=1.0, linecap='square'))
        #
        #         col_inside_list_top.append(pt)
        #     pt_inside_top_column_list.append(col_inside_list_top)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------

        bobfc = self.data_object.bolts_outside_bottom_flange_col
        bobfr = self.data_object.bolts_outside_bottom_flange_row
        bibfc = self.data_object.bolts_inside_bottom_flange_col
        bibfr = self.data_object.bolts_inside_bottom_flange_row
        # ------------------------------------------  Bolts Outside Bottom Flange -------------------------------------------

        pt_outside_bottom_column_list = []
        for i in range(1, (bobfr + 1)):
            col_outside_list_bottom = []
            for j in range(1, (bobfc + 1)):
                pt = self.P4 + ((self.data_object.plate_length_L1 - self.data_object.beam_depth_D1)/2 - self.data_object.end_dist) * np.array([0, -1]) + \
                     self.data_object.edge_dist * np.array([1, 0]) + (i - 1) * self.data_object.pitch * np.array([0, 1]) + (j - 1) * self.data_object.cross_centre_gauge_dist * np.array([1, 0])
                dwg.add(dwg.circle(center=pt, r=bolt_r, stroke='blue', fill='none', stroke_width=1.5))
                pt_C = pt - (bolt_r + 4) * np.array([1, 0])
                pt_D = pt + (bolt_r + 4) * np.array([1, 0])
                dwg.add(dwg.line(pt_C, pt_D).stroke('red', width=1.0, linecap='square'))

                pt_C1 = pt - (bolt_r + 4) * np.array([0, 1])
                pt_D1 = pt + (bolt_r + 4) * np.array([0, 1])
                dwg.add(dwg.line(pt_C1, pt_D1).stroke('red', width=1.0, linecap='square'))

                col_outside_list_bottom.append(pt)
            pt_outside_bottom_column_list.append(col_outside_list_bottom)

        # ------------------------------------------  Bolts Inside Bottom Flange -------------------------------------------

        # ------------------------------------------  End Plate 1 -------------------------------------------

        point = self.P2 - self.data_object.plate_width_B1/2 * np.array([1, 0])
        theta = 60
        offset = 50
        textup = "End plate 1 " + str(self.data_object.plate_width_B1)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NE", offset, textup, textdown)

        # ------------------------------------------  Primary Beam 1 -------------------------------------------
        point = self.A3
        theta = 60
        offset = 50
        textup = "Primary Beam 1 " + str(self.data_object.flange_thickness_T1) + " x " + str(self.data_object.beam_width_B1)+ " x " + str(self.data_object.beam_depth_D1)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "SE", offset, textdown, textup)

        # ---------------------------------------------  Web Welding ----------------------------------------------
        point = self.A4 + self.data_object.beam_depth_D1/2 * np.array([0, 1])
        theta = 1
        offset = 1
        textup = " z             " + str(self.data_object.web_thickness_tw1)
        textdown = " "
        self.data_object.draw_oriented_arrow(dwg, point, theta, "SE", offset, textdown, textup)

        # ---------------------------------------------  Flange Welding -------------------------------------------
        point = self.A2
        theta = 60
        offset =50
        textup = " "
        textdown = "z           " + str(self.data_object.flange_weld_thickness)
        self.data_object.draw_oriented_arrow(dwg, point, theta, "NE", offset, textdown, textup)


        # ------------------------------------------  View details-------------------------------------------
        ptx = self.P4 * np.array([0, 1]) + 100 * np.array([0, 1])
        dwg.add(dwg.text('Side view (Sec B-B) ', insert=ptx, fill='black', font_family="sans-serif", font_size=30))
        ptx1 = ptx + 40 * np.array([0, 1])
        dwg.add(dwg.text('(All distances are in "mm")', insert=ptx1, fill='black', font_family="sans-serif", font_size=30))

        dwg.save()







































