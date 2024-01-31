# -*- coding: utf-8 -*-
"""
GUI methods for modelmaker_hurrywave -> domain

Created on Mon May 10 12:18:09 2021

@author: Maarten van Ormondt
"""
import numpy as np
import math

from delftdashboard.app import app
from delftdashboard.operations import map

def select(*args):
    # De-activate() existing layers
    map.update()
    # Show the grid outline layer
    app.map.layer["hurrywave"].layer["grid"].activate()
    app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].activate()


def draw_grid_outline(*args):
    # Clear grid outline layer
    app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].crs = app.crs
    app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].draw()


def grid_outline_created(gdf, index, id):
    if len(gdf) > 1:
        # Remove the old grid outline
        id0 = gdf["id"][0]
        app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].delete_feature(id0)
        gdf = gdf.drop([0]).reset_index()
    app.toolbox["modelmaker_hurrywave"].grid_outline = gdf
    update_geometry()
    app.gui.window.update()


def grid_outline_modified(gdf, index, id):
    app.toolbox["modelmaker_hurrywave"].grid_outline = gdf
    update_geometry()
    app.gui.window.update()


def generate_grid(*args):
    app.toolbox["modelmaker_hurrywave"].generate_grid()


def update_geometry():
    gdf = app.toolbox["modelmaker_hurrywave"].grid_outline
    group = "modelmaker_hurrywave"
    app.gui.setvar(group, "x0", round(gdf["x0"][0], 3))
    app.gui.setvar(group, "y0", round(gdf["y0"][0], 3))
    lenx = gdf["dx"][0]
    leny = gdf["dy"][0]
    app.toolbox["modelmaker_hurrywave"].lenx = lenx
    app.toolbox["modelmaker_hurrywave"].leny = leny
    app.gui.setvar(group, "rotation", round(gdf["rotation"][0] * 180 / math.pi, 1))
    app.gui.setvar(
        group, "nmax", np.floor(leny / app.gui.getvar(group, "dy")).astype(int)
    )
    app.gui.setvar(
        group, "mmax", np.floor(lenx / app.gui.getvar(group, "dx")).astype(int)
    )


def edit_origin(*args):
    redraw_rectangle()


def edit_nmmax(*args):
    redraw_rectangle()


def edit_rotation(*args):
    redraw_rectangle()


def edit_dxdy(*args):
    group = "modelmaker_hurrywave"
    lenx = app.toolbox["modelmaker_hurrywave"].lenx
    leny = app.toolbox["modelmaker_hurrywave"].leny
    app.gui.setvar(
        group, "nmax", np.floor(leny / app.gui.getvar(group, "dy")).astype(int)
    )
    app.gui.setvar(
        group, "mmax", np.floor(lenx / app.gui.getvar(group, "dx")).astype(int)
    )


def redraw_rectangle():
    group = "modelmaker_hurrywave"
    app.toolbox["modelmaker_hurrywave"].lenx = app.gui.getvar(
        group, "dx"
    ) * app.gui.getvar(group, "mmax")
    app.toolbox["modelmaker_hurrywave"].leny = app.gui.getvar(
        group, "dy"
    ) * app.gui.getvar(group, "nmax")
    app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].clear()
    app.map.layer["modelmaker_hurrywave"].layer["grid_outline"].add_rectangle(
        app.gui.getvar(group, "x0"),
        app.gui.getvar(group, "y0"),
        app.toolbox["modelmaker_hurrywave"].lenx,
        app.toolbox["modelmaker_hurrywave"].leny,
        app.gui.getvar(group, "rotation"),
    )

def read_setup_yaml(*args):
    fname = app.gui.window.dialog_open_file("Select yml file", filter="*.yml")
    if fname[0]:
        app.toolbox["modelmaker_hurrywave"].read_setup_yaml(fname[0])

def write_setup_yaml(*args):
    app.toolbox["modelmaker_hurrywave"].write_setup_yaml()
    app.toolbox["modelmaker_hurrywave"].write_include_polygon()
    app.toolbox["modelmaker_hurrywave"].write_exclude_polygon()
    app.toolbox["modelmaker_hurrywave"].write_boundary_polygon()

def build_model(*args):
    app.toolbox["modelmaker_hurrywave"].build_model()

def info(*args):
    pass
