"""Example: display map"""

import dearpygui.dearpygui as dpg
from dearpygui_map.tile_source import OpenStreetMap
import dearpygui_map.widget as dpg_map

dpg.create_context()

with dpg.window(label="Map demo"):
    dpg_map.add_map_widget(700, 500, (60.1641, 24.9402), 12, OpenStreetMap)

dpg.create_viewport(title="Dear PyGui map widget demo", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
