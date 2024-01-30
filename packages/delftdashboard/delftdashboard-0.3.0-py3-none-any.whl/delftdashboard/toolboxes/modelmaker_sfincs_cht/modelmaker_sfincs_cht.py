# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:18:09 2021

@author: ormondt
"""

import numpy as np
import geopandas as gpd
from pyproj import CRS

from delftdashboard.operations.toolbox import GenericToolbox
from delftdashboard.app import app

from cht.bathymetry.bathymetry_database import bathymetry_database
from cht.misc.misc_tools import dict2yaml
from cht.misc.misc_tools import yaml2dict
from cht.sfincs2.quadtree_grid_snapwave import snapwave_quadtree2mesh

class Toolbox(GenericToolbox):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.long_name = "Model Maker"

        # Set variables

        # Grid outline
        self.grid_outline = gpd.GeoDataFrame()

        # Bathymetry
        self.selected_bathymetry_datasets = []

        # Include polygons
        self.include_polygon = gpd.GeoDataFrame()
        # Exclude polygons
        self.exclude_polygon = gpd.GeoDataFrame()
        # Boundary polygons
        self.open_boundary_polygon = gpd.GeoDataFrame()
        self.outflow_boundary_polygon = gpd.GeoDataFrame()
        # Include polygons SnapWave
        self.include_polygon_snapwave = gpd.GeoDataFrame()
        # Exclude polygons SnapWave
        self.exclude_polygon_snapwave = gpd.GeoDataFrame()
        # Refinement
        self.refinement_levels = []
        self.refinement_polygon = gpd.GeoDataFrame()

        self.setup_dict = {}

        # Set GUI variable
        group = "modelmaker_sfincs_cht"

        app.gui.setvar(group, "build_quadtree_grid", True)
        app.gui.setvar(group, "use_snapwave", False)
        app.gui.setvar(group, "use_subgrid", True)

        # Domain
        app.gui.setvar(group, "x0", 0.0)
        app.gui.setvar(group, "y0", 0.0)
        app.gui.setvar(group, "nmax", 0)
        app.gui.setvar(group, "mmax", 0)

        if app.crs.is_geographic:
            app.gui.setvar(group, "dx", 0.1)
            app.gui.setvar(group, "dy", 0.1)
        else:
            app.gui.setvar(group, "dx", 1000.0)
            app.gui.setvar(group, "dy", 1000.0)

        app.gui.setvar(group, "rotation", 0.0)

        # Refinement
        app.gui.setvar(group, "refinement_polygon_file", "quadtree.geojson")
        app.gui.setvar(group, "refinement_polygon_names", [])
        app.gui.setvar(group, "refinement_polygon_index", 0)
        app.gui.setvar(group, "refinement_polygon_level", 0)
        app.gui.setvar(group, "nr_refinement_polygons", 0)
        # Strings for refinement levels
        levstr = []
        for i in range(10):
            levstr.append(str(i))
        app.gui.setvar("modelmaker_sfincs_cht", "refinement_polygon_levels", levstr)    

        # Mask
        app.gui.setvar(group, "global_zmax",  10.0)
        app.gui.setvar(group, "global_zmin",  -10.0)
        app.gui.setvar(group, "include_polygon_file", "include.geojson")
        app.gui.setvar(group, "include_polygon_names", [])
        app.gui.setvar(group, "include_polygon_index", 0)
        app.gui.setvar(group, "nr_include_polygons", 0)
        app.gui.setvar(group, "include_zmax",  99999.0)
        app.gui.setvar(group, "include_zmin", -99999.0)
        app.gui.setvar(group, "exclude_polygon_file", "exclude.geojson")
        app.gui.setvar(group, "exclude_polygon_names", [])
        app.gui.setvar(group, "exclude_polygon_index", 0)
        app.gui.setvar(group, "nr_exclude_polygons", 0)
        app.gui.setvar(group, "exclude_zmax",  99999.0)
        app.gui.setvar(group, "exclude_zmin", -99999.0)

        app.gui.setvar(group, "open_boundary_polygon_file", "open_boundary.geojson")
        app.gui.setvar(group, "open_boundary_polygon_names", [])
        app.gui.setvar(group, "open_boundary_polygon_index", 0)
        app.gui.setvar(group, "nr_open_boundary_polygons", 0)
        app.gui.setvar(group, "open_boundary_zmax",  99999.0)
        app.gui.setvar(group, "open_boundary_zmin", -99999.0)

        app.gui.setvar(group, "outflow_boundary_polygon_file", "outflow_boundary.geojson")
        app.gui.setvar(group, "outflow_boundary_polygon_names", [])
        app.gui.setvar(group, "outflow_boundary_polygon_index", 0)
        app.gui.setvar(group, "nr_outflow_boundary_polygons", 0)
        app.gui.setvar(group, "outflow_boundary_zmax",  99999.0)
        app.gui.setvar(group, "outflow_boundary_zmin", -99999.0)

        app.gui.setvar(group, "global_zmax_snapwave",     -2.0)
        app.gui.setvar(group, "global_zmin_snapwave", -99999.0)
        app.gui.setvar(group, "include_polygon_file_snapwave", "include_snapwave.geojson")
        app.gui.setvar(group, "include_polygon_names_snapwave", [])
        app.gui.setvar(group, "include_polygon_index_snapwave", 0)
        app.gui.setvar(group, "nr_include_polygons_snapwave", 0)
        app.gui.setvar(group, "include_zmax_snapwave",  99999.0)
        app.gui.setvar(group, "include_zmin_snapwave", -99999.0)
        app.gui.setvar(group, "exclude_polygon_file_snapwave", "exclude_snapwave.geojson")
        app.gui.setvar(group, "exclude_polygon_names_snapwave", [])
        app.gui.setvar(group, "exclude_polygon_index_snapwave", 0)
        app.gui.setvar(group, "nr_exclude_polygons_snapwave", 0)
        app.gui.setvar(group, "exclude_zmax_snapwave",  99999.0)
        app.gui.setvar(group, "exclude_zmin_snapwave", -99999.0)

        # Bathymetry
        source_names, sources = bathymetry_database.sources()
        app.gui.setvar(group, "bathymetry_source_names", source_names)
        app.gui.setvar(group, "active_bathymetry_source", source_names[0])
        dataset_names, dataset_long_names, dataset_source_names = bathymetry_database.dataset_names(source=source_names[0])
        app.gui.setvar(group, "bathymetry_dataset_names", dataset_names)
        app.gui.setvar(group, "bathymetry_dataset_index", 0)
        app.gui.setvar(group, "selected_bathymetry_dataset_names", [])
        app.gui.setvar(group, "selected_bathymetry_dataset_index", 0)
        app.gui.setvar(group, "selected_bathymetry_dataset_zmin", -99999.0)
        app.gui.setvar(group, "selected_bathymetry_dataset_zmax", 99999.0)
        app.gui.setvar(group, "nr_selected_bathymetry_datasets", 0)

        # Subgrid
        app.gui.setvar(group, "subgrid_nr_bins", 10)
        app.gui.setvar(group, "subgrid_nr_pixels", 20)
        app.gui.setvar(group, "subgrid_max_dzdv", 5.0)
        app.gui.setvar(group, "subgrid_manning_max", 0.024)
        app.gui.setvar(group, "subgrid_manning_z_cutoff", 0.024)
        app.gui.setvar(group, "subgrid_zmin", -99999.0)

        # Boundary points
        app.gui.setvar(group, "boundary_dx", 50000.0)

    def set_layer_mode(self, mode):
        if mode == "inactive":
            # Make all layers invisible
            app.map.layer["modelmaker_sfincs_cht"].hide()
        if mode == "invisible":
            app.map.layer["modelmaker_sfincs_cht"].hide()

    def add_layers(self):
        # Add Mapbox layers
        layer = app.map.add_layer("modelmaker_sfincs_cht")

        # Grid outline
        from .domain import grid_outline_created
        from .domain import grid_outline_modified
        layer.add_layer("grid_outline", type="draw",
                             shape="rectangle",
                             create=grid_outline_created,
                             modify=grid_outline_modified,
                             polygon_line_color="mediumblue",
                             polygon_fill_opacity=0.3,
                             rotate=True
                            )

        ### Mask
        # Include
        from .mask_active_cells import include_polygon_created
        from .mask_active_cells import include_polygon_modified
        from .mask_active_cells import include_polygon_selected
        layer.add_layer("include_polygon", type="draw",
                             shape="polygon",
                             create=include_polygon_created,
                             modify=include_polygon_modified,
                             select=include_polygon_selected,
                             polygon_line_color="limegreen",
                             polygon_fill_color="limegreen",
                             polygon_fill_opacity=0.3)
        # Exclude
        from .mask_active_cells import exclude_polygon_created
        from .mask_active_cells import exclude_polygon_modified
        from .mask_active_cells import exclude_polygon_selected
        layer.add_layer("exclude_polygon", type="draw",
                             shape="polygon",
                             create=exclude_polygon_created,
                             modify=exclude_polygon_modified,
                             select=exclude_polygon_selected,
                             polygon_line_color="orangered",
                             polygon_fill_color="orangered",
                             polygon_fill_opacity=0.3)
        # Boundary
        from .mask_boundary_cells import open_boundary_polygon_created
        from .mask_boundary_cells import open_boundary_polygon_modified
        from .mask_boundary_cells import open_boundary_polygon_selected
        layer.add_layer("open_boundary_polygon", type="draw",
                             shape="polygon",
                             create=open_boundary_polygon_created,
                             modify=open_boundary_polygon_modified,
                             select=open_boundary_polygon_selected,
                             polygon_line_color="deepskyblue",
                             polygon_fill_color="deepskyblue",
                             polygon_fill_opacity=0.3)

        # Outflow boundary
        from .mask_boundary_cells import outflow_boundary_polygon_created
        from .mask_boundary_cells import outflow_boundary_polygon_modified
        from .mask_boundary_cells import outflow_boundary_polygon_selected
        layer.add_layer("outflow_boundary_polygon", type="draw",
                             shape="polygon",
                             create=outflow_boundary_polygon_created,
                             modify=outflow_boundary_polygon_modified,
                             select=outflow_boundary_polygon_selected,
                             polygon_line_color="red",
                             polygon_fill_color="orange",
                             polygon_fill_opacity=0.3)

        ### Mask SnapWave
        # Include
        from .mask_active_cells_snapwave import include_polygon_created_snapwave
        from .mask_active_cells_snapwave import include_polygon_modified_snapwave
        from .mask_active_cells_snapwave import include_polygon_selected_snapwave
        layer.add_layer("include_polygon_snapwave", type="draw",
                             shape="polygon",
                             create=include_polygon_created_snapwave,
                             modify=include_polygon_modified_snapwave,
                             select=include_polygon_selected_snapwave,
                             polygon_line_color="limegreen",
                             polygon_fill_color="limegreen",
                             polygon_fill_opacity=0.3)
        # Exclude
        from .mask_active_cells_snapwave import exclude_polygon_created_snapwave
        from .mask_active_cells_snapwave import exclude_polygon_modified_snapwave
        from .mask_active_cells_snapwave import exclude_polygon_selected_snapwave
        layer.add_layer("exclude_polygon_snapwave", type="draw",
                             shape="polygon",
                             create=exclude_polygon_created_snapwave,
                             modify=exclude_polygon_modified_snapwave,
                             select=exclude_polygon_selected_snapwave,
                             polygon_line_color="orangered",
                             polygon_fill_color="orangered",
                             polygon_fill_opacity=0.3)

        # Refinement polygons
        from .quadtree import refinement_polygon_created
        from .quadtree import refinement_polygon_modified
        from .quadtree import refinement_polygon_selected
        layer.add_layer("quadtree_refinement", type="draw",
                             shape="polygon",
                             create=refinement_polygon_created,
                             modify=refinement_polygon_modified,
                             select=refinement_polygon_selected,
                             polygon_line_color="red",
                             polygon_fill_color="orange",
                             polygon_fill_opacity=0.3)

    def set_crs(self):
        # Called when the CRS is changed
        group = "modelmaker_sfincs_cht"
        if app.crs.is_geographic:
            app.gui.setvar(group, "dx", 0.1)
            app.gui.setvar(group, "dy", 0.1)
        else:
            app.gui.setvar(group, "dx", 1000.0)
            app.gui.setvar(group, "dy", 1000.0)

    def generate_grid(self):
        group = "modelmaker_sfincs_cht"
        dlg = app.gui.window.dialog_wait("Generating grid ...")
        model = app.model["sfincs_cht"].domain
        model.clear_spatial_attributes()    
        x0       = app.gui.getvar(group, "x0")
        y0       = app.gui.getvar(group, "y0")
        dx       = app.gui.getvar(group, "dx")
        dy       = app.gui.getvar(group, "dy")
        nmax     = app.gui.getvar(group, "nmax")
        mmax     = app.gui.getvar(group, "mmax")
        rotation = app.gui.getvar(group, "rotation")
        model.input.variables.qtrfile = "sfincs.nc"
        app.gui.setvar("sfincs_cht", "qtrfile", model.input.variables.qtrfile)

        if len(self.refinement_polygon) == 0:
            refpol = None
        else:
            # Make list of separate gdfs for each polygon
            refpol = self.refinement_polygon
            # Add refinement_level column
            refpol["refinement_level"] = 0
            # Iterate through rows and set refinement levels            
            for irow, row in refpol.iterrows():
                refpol.loc[irow, "refinement_level"] = self.refinement_levels[irow]

        # Build grid 
        model.grid.build(x0, y0, nmax, mmax, dx, dy, rotation, refinement_polygons=refpol)
        # Save grid 
        model.grid.write()

        # If SnapWave also generate SnapWave mesh and save it
        if app.gui.getvar(group, "use_snapwave"):
            snapwave_quadtree2mesh(model.grid, file_name="snapwave.nc")

        # Replot everything
        app.model["sfincs_cht"].plot()

        dlg.close()

    def generate_bathymetry(self):
        dlg = app.gui.window.dialog_wait("Generating bathymetry ...")
        bathymetry_list = app.toolbox["modelmaker_sfincs_cht"].selected_bathymetry_datasets
        app.model["sfincs_cht"].domain.grid.set_bathymetry(bathymetry_list)
        app.model["sfincs_cht"].domain.grid.write()
        # If SnapWave also generate SnapWave mesh and save it
        if app.gui.getvar("modelmaker_sfincs_cht", "use_snapwave"):
            snapwave_quadtree2mesh(app.model["sfincs_cht"].domain.grid, file_name="snapwave.nc")
        dlg.close()

    def update_mask(self):
        # Should improve on this check
        grid = app.model["sfincs_cht"].domain.grid
        mask = app.model["sfincs_cht"].domain.mask
        z    = app.model["sfincs_cht"].domain.grid.data["z"]
        if np.all(np.isnan(z)):
            app.gui.window.dialog_warning("Please first generate a bathymetry !")
            return
        dlg = app.gui.window.dialog_wait("Updating mask ...")
        mask.build(zmin=app.gui.getvar("modelmaker_sfincs_cht", "global_zmin"),
                   zmax=app.gui.getvar("modelmaker_sfincs_cht", "global_zmax"),
                   include_polygon=app.toolbox["modelmaker_sfincs_cht"].include_polygon,
                   include_zmin=app.gui.getvar("modelmaker_sfincs_cht", "include_zmin"),
                   include_zmax=app.gui.getvar("modelmaker_sfincs_cht", "include_zmax"),
                   exclude_polygon=app.toolbox["modelmaker_sfincs_cht"].exclude_polygon,
                   exclude_zmin=app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmin"),
                   exclude_zmax=app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmax"),
                   open_boundary_polygon=app.toolbox["modelmaker_sfincs_cht"].open_boundary_polygon,
                   open_boundary_zmin=app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_zmin"),
                   open_boundary_zmax=app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_zmax"),
                   outflow_boundary_polygon=app.toolbox["modelmaker_sfincs_cht"].outflow_boundary_polygon,
                   outflow_boundary_zmin=app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_zmin"),
                   outflow_boundary_zmax=app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_zmax")
                   )
        app.map.layer["sfincs_cht"].layer["mask_include"].set_data(mask.to_gdf(option="include"))
        app.map.layer["sfincs_cht"].layer["mask_open_boundary"].set_data(mask.to_gdf(option="open"))
        app.map.layer["sfincs_cht"].layer["mask_outflow_boundary"].set_data(mask.to_gdf(option="outflow"))
        grid.write() # Write new qtr file
        dlg.close()

    def update_mask_snapwave(self):
        grid = app.model["sfincs_cht"].domain.grid
        mask = app.model["sfincs_cht"].domain.snapwave.mask
        if np.all(np.isnan(grid.data["z"])):
            app.gui.window.dialog_warning("Please first generate a bathymetry !")
            return
        dlg = app.gui.window.dialog_wait("Updating SnapWave mask ...")
        mask.build(zmin=app.gui.getvar("modelmaker_sfincs_cht", "global_zmin_snapwave"),
                   zmax=app.gui.getvar("modelmaker_sfincs_cht", "global_zmax_snapwave"),
                   include_polygon=app.toolbox["modelmaker_sfincs_cht"].include_polygon_snapwave,
                   include_zmin=app.gui.getvar("modelmaker_sfincs_cht", "include_zmin_snapwave"),
                   include_zmax=app.gui.getvar("modelmaker_sfincs_cht", "include_zmax_snapwave"),
                   exclude_polygon=app.toolbox["modelmaker_sfincs_cht"].exclude_polygon_snapwave,
                   exclude_zmin=app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmin_snapwave"),
                   exclude_zmax=app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmax_snapwave")
                   )
        app.map.layer["sfincs_cht"].layer["mask_include_snapwave"].set_data(mask.to_gdf(option="include"))
        if not app.model["sfincs_cht"].domain.input.variables.snapwave_mskfile:
            app.model["sfincs_cht"].domain.input.variables.snapwave_mskfile = "snapwave.msk"
        grid.write()
        # GUI variables
        app.gui.setvar("sfincs_cht", "snapwave_mskfile", app.model["sfincs_cht"].domain.input.variables.snapwave_mskfile)
        dlg.close()

    def generate_subgrid(self):
        group = "modelmaker_sfincs_cht"
        bathymetry_sets = app.toolbox["modelmaker_sfincs_cht"].selected_bathymetry_datasets
        roughness_sets = []
        nr_bins = app.gui.getvar(group, "subgrid_nr_bins")
        nr_pixels = app.gui.getvar(group, "subgrid_nr_pixels")
        max_dzdv = app.gui.getvar(group, "subgrid_max_dzdv")
        manning_max = app.gui.getvar(group, "subgrid_manning_max")
        manning_z_cutoff = app.gui.getvar(group, "subgrid_manning_z_cutoff")
        zmin = app.gui.getvar(group, "subgrid_zmin")
        p = app.gui.window.dialog_progress("               Generating Sub-grid Tables ...                ", 100)
        app.model["sfincs_cht"].domain.subgrid.build(bathymetry_sets,
                                                     roughness_sets,
                                                     nr_bins=nr_bins,
                                                     nr_subgrid_pixels=nr_pixels,
                                                     max_gradient=max_dzdv,
                                                     zmin=zmin,
                                                     progress_bar=p)
        app.model["sfincs_cht"].domain.input.variables.sbgfile = "sfincs.sbg"
        app.gui.setvar("sfincs_cht", "sbgfile", app.model["sfincs_cht"].domain.input.variables.sbgfile)
        app.gui.setvar("sfincs_cht", "bathymetry_type", "subgrid")

    def cut_inactive_cells(self):
        dlg = app.gui.window.dialog_wait("Cutting Inactive Cells ...")
        app.model["sfincs_cht"].domain.grid.cut_inactive_cells()
        app.model["sfincs_cht"].domain.grid.write()
        # Replot everything
        app.model["sfincs_cht"].plot()
        dlg.close()


    def build_model(self):
        self.generate_grid()
        self.generate_bathymetry()
        self.update_mask()
        self.generate_subgrid()

#    def update_polygons(self): # This should really be moved to the callback modules

        # nrp = len(self.include_polygon)
        # incnames = []
        # for ip in range(nrp):
        #     incnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_include_polygons", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "include_polygon_names", incnames)
        # app.gui.setvar("modelmaker_sfincs_cht", "include_polygon_index", max(nrp, 0))

        # nrp = len(self.exclude_polygon)
        # excnames = []
        # for ip in range(nrp):
        #     excnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_exclude_polygons", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "exclude_polygon_names", excnames)
        # app.gui.setvar("modelmaker_sfincs_cht", "exclude_polygon_index", max(nrp, 0))

        # nrp = len(self.open_boundary_polygon)
        # bndnames = []
        # for ip in range(nrp):
        #     bndnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_open_boundary_polygons", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "open_boundary_polygon_names", bndnames)

        # nrp = len(self.outflow_boundary_polygon)
        # bndnames = []
        # for ip in range(nrp):
        #     bndnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_outflow_boundary_polygons", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "outflow_boundary_polygon_names", bndnames)

        # nrp = len(self.include_polygon_snapwave)
        # incnames = []
        # for ip in range(nrp):
        #     incnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_include_polygons_snapwave", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "include_polygon_names_snapwave", incnames)

        # nrp = len(self.exclude_polygon_snapwave)
        # excnames = []
        # for ip in range(nrp):
        #     excnames.append(str(ip + 1))
        # app.gui.setvar("modelmaker_sfincs_cht", "nr_exclude_polygons_snapwave", nrp)
        # app.gui.setvar("modelmaker_sfincs_cht", "exclude_polygon_names_snapwave", excnames)

        # app.toolbox["modelmaker_sfincs_cht"].write_include_polygon()
        # app.toolbox["modelmaker_sfincs_cht"].write_exclude_polygon()
        # app.toolbox["modelmaker_sfincs_cht"].write_boundary_polygon()

    # READ

    def read_refinement_polygon(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "refinement_polygon_file")
        self.refinement_polygon = gpd.read_file(fname)
        # Loop through rows in geodataframe and set refinement levels        
        self.refinement_levels = []
        for i in range(len(self.refinement_polygon)):
            self.refinement_levels.append(self.refinement_polygon["refinement_level"][i])

    def read_include_polygon(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file")
        self.include_polygon = gpd.read_file(fname)

    def read_exclude_polygon(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file")
        self.exclude_polygon = gpd.read_file(fname)

    def read_open_boundary_polygon(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_polygon_file")
        self.open_boundary_polygon = gpd.read_file(fname)

    def read_outflow_boundary_polygon(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_polygon_file")
        self.outflow_boundary_polygon = gpd.read_file(fname)

    def read_include_polygon_snapwave(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file_snapwave")
        self.include_polygon_snapwave = gpd.read_file(fname)

    def read_exclude_polygon_snapwave(self):
        fname = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file_snapwave")
        self.exclude_polygon_snapwave = gpd.read_file(fname)

    # WRITE

    def write_refinement_polygon(self):
        if len(self.refinement_polygon) == 0:
            print("No refinement polygons defined")
            return
        gdf = gpd.GeoDataFrame({"geometry": self.refinement_polygon["geometry"],
                                "refinement_level": self.refinement_levels})
        # Iterate over all polygons and add refinement level
        # refinement_level = 1 means one level of refinement
        # refinement_level = 2 means two levels of refinement
        # etc.
        fname = app.gui.getvar("modelmaker_sfincs_cht", "refinement_polygon_file")
        gdf.to_file(fname, driver='GeoJSON')

    def write_include_polygon(self):
        if len(self.include_polygon) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.include_polygon["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file")
        gdf.to_file(fname, driver='GeoJSON')

    def write_exclude_polygon(self):
        if len(self.exclude_polygon) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.exclude_polygon["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file")
        gdf.to_file(fname, driver='GeoJSON')

    def write_open_boundary_polygon(self):
        if len(self.open_boundary_polygon) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.open_boundary_polygon["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_polygon_file")
        gdf.to_file(fname, driver='GeoJSON')

    def write_outflow_boundary_polygon(self):
        if len(self.outflow_boundary_polygon) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.outflow_boundary_polygon["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_polygon_file")
        gdf.to_file(fname, driver='GeoJSON')

    def write_include_polygon_snapwave(self):
        if len(self.include_polygon_snapwave) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.include_polygon_snapwave["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file_snapwave")
        gdf.to_file(fname, driver='GeoJSON')

    def write_exclude_polygon_snapwave(self):
        if len(self.exclude_polygon_snapwave) == 0:
            return
        gdf = gpd.GeoDataFrame(geometry=self.exclude_polygon_snapwave["geometry"])
        fname = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file_snapwave")
        gdf.to_file(fname, driver='GeoJSON')

    # PLOT

    def plot_refinement_polygon(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["quadtree_refinement"]
        layer.clear()
        layer.add_feature(self.refinement_polygon)

    def plot_include_polygon(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["include_polygon"]
        layer.clear()
        layer.add_feature(self.include_polygon)

    def plot_exclude_polygon(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["exclude_polygon"]
        layer.clear()
        layer.add_feature(self.exclude_polygon)

    def plot_open_boundary_polygon(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["open_boundary_polygon"]
        layer.clear()
        layer.add_feature(self.open_boundary_polygon)

    def plot_outflow_boundary_polygon(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["outflow_boundary_polygon"]
        layer.clear()
        layer.add_feature(self.outflow_boundary_polygon)

    def plot_include_polygon_snapwave(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["include_polygon_snapwave"]
        layer.clear()
        layer.add_feature(self.include_polygon_snapwave)

    def plot_exclude_polygon_snapwave(self):
        layer = app.map.layer["modelmaker_sfincs_cht"].layer["exclude_polygon_snapwave"]
        layer.clear()
        layer.add_feature(self.exclude_polygon_snapwave)


    def read_setup_yaml(self, file_name):

        # First set some default gui variables
        group = "modelmaker_sfincs_cht"
        app.gui.setvar(group, "refinement_polygon_file", "quadtree.geojson")
        app.gui.setvar(group, "global_zmin", -99999.0)
        app.gui.setvar(group, "global_zmax",  99999.0)
        app.gui.setvar(group, "include_polygon_index", 0)
        app.gui.setvar(group, "include_zmax",  99999.0)
        app.gui.setvar(group, "include_zmin", -99999.0)
        app.gui.setvar(group, "include_polygon_file", "include.geojson")
        app.gui.setvar(group, "exclude_polygon_index", 0)
        app.gui.setvar(group, "exclude_zmax",  99999.0)
        app.gui.setvar(group, "exclude_zmin", -99999.0)
        app.gui.setvar(group, "exclude_polygon_file", "exclude.geojson")
        app.gui.setvar(group, "open_boundary_polygon_index", 0)
        app.gui.setvar(group, "open_boundary_zmax",  99999.0)
        app.gui.setvar(group, "open_boundary_zmin", -99999.0)
        app.gui.setvar(group, "open_boundary_polygon_file", "open_boundary.geojson")
        app.gui.setvar(group, "outflow_boundary_polygon_index", 0)
        app.gui.setvar(group, "outflow_boundary_zmax",  99999.0)
        app.gui.setvar(group, "outflow_boundary_zmin", -99999.0)
        app.gui.setvar(group, "outflow_boundary_polygon_file", "outflow_boundary.geojson")
        app.gui.setvar(group, "global_zmin_snapwave", -99999.0)
        app.gui.setvar(group, "global_zmax_snapwave",  99999.0)
        app.gui.setvar(group, "include_polygon_index_snapwave", 0)
        app.gui.setvar(group, "include_zmax_snapwave",  99999.0)
        app.gui.setvar(group, "include_zmin_snapwave", -99999.0)
        app.gui.setvar(group, "include_polygon_file_snapwave", "include_snapwave.geojson")
        app.gui.setvar(group, "exclude_polygon_index_snapwave", 0)
        app.gui.setvar(group, "exclude_zmax_snapwave",  99999.0)
        app.gui.setvar(group, "exclude_zmin_snapwave", -99999.0)
        app.gui.setvar(group, "exclude_polygon_file_snapwave", "include_snapwave.geojson")

        # Empty geodataframes
        self.include_polygon = gpd.GeoDataFrame()    
        self.exclude_polygon = gpd.GeoDataFrame()    
        self.open_boundary_polygon = gpd.GeoDataFrame()    
        self.outflow_boundary_polygon = gpd.GeoDataFrame()    
        self.snapwave_include_polygon = gpd.GeoDataFrame()    
        self.snapwave_exclude_polygon = gpd.GeoDataFrame()    
        self.quadtree_polygon = gpd.GeoDataFrame()    

        # Read in yaml file
        dct = yaml2dict(file_name)
        self.setup_dict = dct

        group = "modelmaker_sfincs_cht"
        # Coordinates
        app.gui.setvar(group, "x0", dct["coordinates"]["x0"])
        app.gui.setvar(group, "y0", dct["coordinates"]["y0"])
        app.gui.setvar(group, "dx", dct["coordinates"]["dx"])
        app.gui.setvar(group, "dy", dct["coordinates"]["dy"])
        app.gui.setvar(group, "nmax", dct["coordinates"]["nmax"])
        app.gui.setvar(group, "mmax", dct["coordinates"]["mmax"])
        app.gui.setvar(group, "rotation", dct["coordinates"]["rotation"])
        app.model["sfincs_cht"].domain.crs = CRS(dct["coordinates"]["crs"])
        # Quadtree refinement
        if "quadtree" in dct:
            if "polygon_file" in dct["quadtree"]:
                app.gui.setvar(group, "refinement_polygon_file", dct["quadtree"]["polygon_file"])
                self.read_refinement_polygon()
                self.plot_refinement_polygon()
        # Mask
        if "global" in dct["mask"]:
            if "zmin" in dct["mask"]["global"]:
                app.gui.setvar(group, "global_zmin", dct["mask"]["global"]["zmin"])
            if "zmax" in dct["mask"]["global"]:    
                app.gui.setvar(group, "global_zmax", dct["mask"]["global"]["zmax"])
        if "include" in dct["mask"]:
            if "zmin" in dct["mask"]["include"]:
                app.gui.setvar(group, "include_zmin", dct["mask"]["include"]["zmin"])
            if "zmax" in dct["mask"]["include"]:
                app.gui.setvar(group, "include_zmax", dct["mask"]["include"]["zmax"])
            if "polygon_file" in dct["mask"]["include"]:
                app.gui.setvar(group, "include_polygon_file", dct["mask"]["include"]["polygon_file"])
                # Now read in polygons from geojson file (or other file)
                self.read_include_polygon()
                self.plot_include_polygon()
        # Now do the same for exclude polygons        
        if "exclude" in dct["mask"]:
            if "zmin" in dct["mask"]["exclude"]:
                app.gui.setvar(group, "exclude_zmin", dct["mask"]["exclude"]["zmin"])
            if "zmax" in dct["mask"]["exclude"]:
                app.gui.setvar(group, "exclude_zmax", dct["mask"]["exclude"]["zmax"])
            if "polygon_file" in dct["mask"]["exclude"]:
                app.gui.setvar(group, "exclude_polygon_file", dct["mask"]["exclude"]["polygon_file"])
                # Now read in polygons from geojson file
                self.read_exclude_polygon()
                self.plot_exclude_polygon()     
        # Now do the same for open boundary polygons
        if "open_boundary" in dct["mask"]:
            if "zmin" in dct["mask"]["open_boundary"]:
                app.gui.setvar(group, "open_boundary_zmin", dct["mask"]["open_boundary"]["zmin"])
            if "zmax" in dct["mask"]["open_boundary"]:
                app.gui.setvar(group, "open_boundary_zmax", dct["mask"]["open_boundary"]["zmax"])
            if "polygon_file" in dct["mask"]["open_boundary"]:
                app.gui.setvar(group, "open_boundary_polygon_file", dct["mask"]["open_boundary"]["polygon_file"])
                # Now read in polygons from geojson file
                self.read_open_boundary_polygon()
                self.plot_open_boundary_polygon()
        # Now do the same for outflow boundary polygons
        if "outflow_boundary" in dct["mask"]:
            if "zmin" in dct["mask"]["outflow_boundary"]:
                app.gui.setvar(group, "outflow_boundary_zmin", dct["mask"]["outflow_boundary"]["zmin"])
            if "zmax" in dct["mask"]["outflow_boundary"]:
                app.gui.setvar(group, "outflow_boundary_zmax", dct["mask"]["outflow_boundary"]["zmax"])
            if "polygon_file" in dct["mask"]["outflow_boundary"]:
                app.gui.setvar(group, "outflow_boundary_polygon_file", dct["mask"]["outflow_boundary"]["polygon_file"])
                # Now read in polygons from geojson file
                self.read_outflow_boundary_polygon()
                self.plot_outflow_boundary_polygon()

        if "mask_snapwave" in dct:
            if "global" in dct["mask_snapwave"]:
                if "zmin" in dct["mask_snapwave"]["global"]:
                    app.gui.setvar(group, "global_zmin_snapwave", dct["mask_snapwave"]["global"]["zmin"])
                if "zmax" in dct["mask_snapwave"]["global"]:    
                    app.gui.setvar(group, "global_zmax_snapwave", dct["mask_snapwave"]["global"]["zmax"])
            if "include" in dct["mask_snapwave"]:
                if "zmin" in dct["mask_snapwave"]["include"]:
                    app.gui.setvar(group, "include_zmin_snapwave", dct["mask_snapwave"]["include"]["zmin"])
                if "zmax" in dct["mask_snapwave"]["include"]:
                    app.gui.setvar(group, "include_zmax_snapwave", dct["mask_snapwave"]["include"]["zmax"])
                if "polygon_file" in dct["mask_snapwave"]["include"]:
                    app.gui.setvar(group, "include_polygon_file_snapwave", dct["mask_snapwave"]["include"]["polygon_file"])
                    # Now read in polygons from geojson file
                    self.read_include_polygon_snapwave()
                    self.plot_include_polygon_snapwave()
            if "exclude" in dct["mask_snapwave"]:
                if "zmin" in dct["mask_snapwave"]["exclude"]:
                    app.gui.setvar(group, "exclude_zmin_snapwave", dct["mask_snapwave"]["exclude"]["zmin"])
                if "zmax" in dct["mask_snapwave"]["exclude"]:
                    app.gui.setvar(group, "exclude_zmax_snapwave", dct["mask_snapwave"]["exclude"]["zmax"])
                if "polygon_file" in dct["mask_snapwave"]["exclude"]:
                    app.gui.setvar(group, "exclude_polygon_file_snapwave", dct["mask_snapwave"]["exclude"]["polygon_file"])
                    # Now read in polygons from geojson file
                    self.read_exclude_polygon_snapwave()
                    self.plot_exclude_polygon_snapwave()        

        # Bathymetry
        dataset_names = []
        self.selected_bathymetry_datasets = []
        for ddict in dct["bathymetry"]["dataset"]:
            name = ddict["name"]
            zmin = ddict["zmin"]
            zmax = ddict["zmax"] 
            d = bathymetry_database.get_dataset(name)
            dataset = {"dataset": d, "zmin": zmin, "zmax": zmax}
            app.toolbox["modelmaker_sfincs_cht"].selected_bathymetry_datasets.append(dataset)
            dataset_names.append(name)
        app.gui.setvar("modelmaker_sfincs_cht", "selected_bathymetry_dataset_names", dataset_names)
        app.gui.setvar("modelmaker_sfincs_cht", "selected_bathymetry_dataset_index", 0)

        layer = app.map.layer["modelmaker_sfincs_cht"].layer["grid_outline"]
        lenx = dct["coordinates"]["mmax"] * dct["coordinates"]["dx"]
        leny = dct["coordinates"]["nmax"] * dct["coordinates"]["dy"]
        layer.add_rectangle(dct["coordinates"]["x0"],
                            dct["coordinates"]["y0"],
                            lenx, leny,
                            dct["coordinates"]["rotation"])


    def write_setup_yaml(self):
        group = "modelmaker_sfincs_cht"
        dct = {}
        # Coordinates
        dct["coordinates"] = {}
        dct["coordinates"]["x0"] = float(app.gui.getvar(group, "x0"))
        dct["coordinates"]["y0"] = float(app.gui.getvar(group, "y0"))
        dct["coordinates"]["dx"] = float(app.gui.getvar(group, "dx"))
        dct["coordinates"]["dy"] = float(app.gui.getvar(group, "dy"))
        dct["coordinates"]["nmax"] = int(app.gui.getvar(group, "nmax"))
        dct["coordinates"]["mmax"] = int(app.gui.getvar(group, "mmax"))
        dct["coordinates"]["rotation"] = float(app.gui.getvar(group, "rotation"))
        dct["coordinates"]["crs"] = app.model["sfincs_cht"].domain.crs.name
        # QuadTree
        dct["quadtree"] = {}
        if len(app.toolbox["modelmaker_sfincs_cht"].refinement_polygon)>0:
            dct["quadtree"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "refinement_polygon_file")
        # Mask
        dct["mask"] = {}
        dct["mask"]["global"] = {}
        dct["mask"]["global"]["zmin"] = app.gui.getvar(group, "global_zmin")
        dct["mask"]["global"]["zmax"] = app.gui.getvar(group, "global_zmax")
        dct["mask"]["include"] = {}
        if len(app.toolbox["modelmaker_sfincs_cht"].include_polygon)>0:
            dct["mask"]["include"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "include_zmin")
            dct["mask"]["include"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "include_zmax")
            dct["mask"]["include"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file")
        dct["mask"]["exclude"] = {}
        if len(app.toolbox["modelmaker_sfincs_cht"].exclude_polygon)>0:
            dct["mask"]["exclude"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmin")
            dct["mask"]["exclude"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmax")
            dct["mask"]["exclude"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file")
        dct["mask"]["open_boundary"] = {}
        if len(app.toolbox["modelmaker_sfincs_cht"].open_boundary_polygon)>0:
            dct["mask"]["open_boundary"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_zmin")
            dct["mask"]["open_boundary"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_zmax")
            dct["mask"]["open_boundary"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "open_boundary_polygon_file")
        dct["mask"]["outflow_boundary"] = {}
        if len(app.toolbox["modelmaker_sfincs_cht"].outflow_boundary_polygon)>0:
            dct["mask"]["outflow_boundary"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_zmin")
            dct["mask"]["outflow_boundary"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_zmax")
            dct["mask"]["outflow_boundary"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "outflow_boundary_polygon_file")
        # SnapWave
        # Check if snapwave is enabled
        if app.model["sfincs_cht"].domain.input.variables.snapwave:  
            dct["mask_snapwave"] = {}
            dct["mask_snapwave"]["global"] = {}
            dct["mask_snapwave"]["global"]["zmin"] = app.gui.getvar(group, "global_zmin_snapwave")
            dct["mask_snapwave"]["global"]["zmax"] = app.gui.getvar(group, "global_zmax_snapwave")
            dct["mask_snapwave"]["include"] = {}
            if len(app.toolbox["modelmaker_sfincs_cht"].include_polygon_snapwave)>0:
                dct["mask_snapwave"]["include"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "include_zmin_snapwave")
                dct["mask_snapwave"]["include"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "include_zmax_snapwave")
                dct["mask_snapwave"]["include"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "include_polygon_file_snapwave")
            dct["mask_snapwave"]["exclude"] = {}
            if len(app.toolbox["modelmaker_sfincs_cht"].exclude_polygon_snapwave)>0:
                dct["mask_snapwave"]["exclude"]["zmin"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmin_snapwave")
                dct["mask_snapwave"]["exclude"]["zmax"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_zmax_snapwave")
                dct["mask_snapwave"]["exclude"]["polygon_file"] = app.gui.getvar("modelmaker_sfincs_cht", "exclude_polygon_file_snapwave")

        # Bathymetry
        dct["bathymetry"] = {}
        dct["bathymetry"]["dataset"] = []
        for d in app.toolbox["modelmaker_sfincs_cht"].selected_bathymetry_datasets:
            dataset = {}
            dataset["name"]   = d["dataset"].name
            dataset["source"] = "delftdashboard"
            dataset["zmin"]   = d["zmin"]
            dataset["zmax"]   = d["zmax"]
            dct["bathymetry"]["dataset"].append(dataset)    

        self.setup_dict = dct

        dict2yaml("model_setup.yml", dct)

        # Write out polygons 
        app.toolbox["modelmaker_sfincs_cht"].write_include_polygon()
        app.toolbox["modelmaker_sfincs_cht"].write_exclude_polygon()
        app.toolbox["modelmaker_sfincs_cht"].write_open_boundary_polygon()
        app.toolbox["modelmaker_sfincs_cht"].write_outflow_boundary_polygon()
        app.toolbox["modelmaker_sfincs_cht"].write_refinement_polygon()
        app.toolbox["modelmaker_sfincs_cht"].write_include_polygon_snapwave()
        app.toolbox["modelmaker_sfincs_cht"].write_exclude_polygon_snapwave()


def gdf2list(gdf_in):
   gdf_out = []
   for feature in gdf_in.iterfeatures():
      gdf_out.append(gpd.GeoDataFrame.from_features([feature]))
   return gdf_out
