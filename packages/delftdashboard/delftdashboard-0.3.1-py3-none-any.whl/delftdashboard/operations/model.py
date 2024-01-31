# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 13:40:07 2022

@author: ormondt
"""
import importlib

from delftdashboard.app import app
from delftdashboard.operations.toolbox import select_toolbox
#from guitares.gui import set_missing_menu_values

class GenericModel:
    def __init__(self):
        self.name      = "model"
        self.long_name = "Model"
        self.exe_path  = None

    def open(self):
        pass

    def add_layers(self):
        pass

    def select(self):

        elements = app.gui.window.elements

        # Set tab panel for current model to visible
        for element in elements:
            if element.style == "tabpanel":
                if element.id == self.name:
                    element.widget.setVisible(True)
                    element.visible = True
        # And the others to invisible
        for element in elements:
            if element.style == "tabpanel":
                if element.id != self.name:
                    element.widget.setVisible(False)
                    element.visible = False

        app.active_model = self
        app.gui.setvar("menu", "active_model_name", app.active_model.name)

        # Check which toolboxes we can add and update the menu
        toolboxes_to_add = []
        for toolbox_name in app.toolbox:
            if toolbox_name in self.toolbox:
                toolboxes_to_add.append(toolbox_name)

        # Clear toolbox menu
        toolbox_menu = app.gui.window.menus[2]
        toolbox_menu.widget.clear()

        # Add toolboxes_to_add
        menu_to_add = []
        for toolbox_name in toolboxes_to_add:
            dependency = [{"action": "check",
                           "checkfor": "all",
                           "check": [{"variable": "active_toolbox_name",
                                      "operator": "eq",
                                      "value": toolbox_name}]
                           }]
            menu_to_add.append({"text": app.toolbox[toolbox_name].long_name,
                                "variable_group": "menu",
                                "module": "delftdashboard.menu.toolbox",
                                "method": "select",
                                "id": toolbox_name,
                                "option": toolbox_name,
                                "checkable": True,
                                "dependency": dependency})
        toolbox_menu.menus = []
        app.gui.window.add_menu_to_tree(toolbox_menu.menus, menu_to_add, toolbox_menu)
        app.gui.window.add_menus(toolbox_menu.menus, toolbox_menu, app.gui)

        # Check if the current toolbox is available. If not, select a new toolbox.
        if app.active_toolbox.name in toolboxes_to_add:
            # Select active toolbox
            select_toolbox(app.active_toolbox.name)
        else:
            # Select first toolbox from the list
            select_toolbox(toolboxes_to_add[0])

        app.gui.window.update()

    def set_crs(self):        
        pass

def select_model(model_name):
    # Called from menu
    app.active_model = app.model[model_name]
    app.model[model_name].select()
