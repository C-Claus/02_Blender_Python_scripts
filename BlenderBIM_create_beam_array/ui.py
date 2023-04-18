import bpy
from bpy.types import Panel
from . import  properties, operator


class PANEL_PT_demo(Panel):
    bl_label = 'Panel demo'
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "Bim"

    def draw(self, context):

        dimension_properties = context.scene.dimension_properties

        layout = self.layout

        box = layout.box()
        box.label(text = "Total Dimensions")
        row = box.row()
        
        row.prop(dimension_properties, 'my_height')

        box.prop(dimension_properties, "my_n")
        box.prop(dimension_properties, "my_center_to_center_distance")
        box.prop(dimension_properties,'my_length',emboss=False)


        box = layout.box()
        row = box.row()
        box.label(text = "Profile Dimensions")
        box.prop(dimension_properties, "my_profile_x")
        box.prop(dimension_properties, "my_profile_y")


        box = layout.box()
        row = box.row()
        row.operator("create.array")
     

def register():
    bpy.utils.register_class(PANEL_PT_demo)
   

def unregister():
    bpy.utils.unregister_class(PANEL_PT_demo)