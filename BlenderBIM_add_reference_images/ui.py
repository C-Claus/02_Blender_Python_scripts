import bpy
from bpy.types import Panel
from . import  properties, operator
from blenderbim.bim.ifc import IfcStore




class PANEL_PT_demo(Panel):
    bl_label = 'IFC Reference Images'
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "IFC Reference Images"

    def draw(self, context):

        image_properties = context.scene.image_properties

        #layout = self.layout
        #box = layout.box()
        #row = box.row()
        #box.operator("load.referenceimage")

        layout = self.layout
        box = layout.box()
        box.operator("load.allimages", text="Load all images")
        box.operator("image.collection_actions", text="Add", icon="ADD").action = "add"

        image_collection = context.scene.image_collection
        row = layout.row(align=True)

        #if len(custom_collection.items) > 0:
        #    row.operator("clear.clear_properties", text="Clear Properties")
       
        for i, item in enumerate(image_collection.items):

            row = box.row(align=True)
            row.prop(item, "image")

            op = row.operator("add.referenceimage", text="", icon="RIGHTARROW")
            op.index = i

            op = row.operator("store.referenceimage", text="", icon="PLUS")
            op.index = i 

            #op = row.operator("load.referenceimage",text="",icon="PINNED")
            #op.index = i


            op = row.operator("image.collection_actions", text="", icon="REMOVE")
            op.action = "remove"
            op.index = i 

 

def register():
    bpy.utils.register_class(PANEL_PT_demo)

   

def unregister():
    bpy.utils.unregister_class(PANEL_PT_demo)
