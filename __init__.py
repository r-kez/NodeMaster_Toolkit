bl_info = {
    "name": "Custom Panel - Node Editor",
    "description": "Custom panel for easier access of Shader Nodes. /n Current support: Native Blender Shader Nodes /n Comming: GeoNodes, Lux Core Render and Octane Render",
    "author": "R_Kez",
    "version": (4, 0),
    "blender": (4, 0, 0),
    "location": "Node Editor > N-Panel",
    "warning": "", # used for warning icon and text in addons panel
    "doc_url": "Yet to be made",
    "tracker_url": "Yet to be made",
    "support": "COMMUNITY",
    "category": "UI Utilities",
}



import bpy

# Import Operators Master
from .node_editor_features.master_op.master_op import classes_master_OT

# Import Add Color Nodes Operators 
from .node_editor_features.add_operators.color_add_op import classes_color_OT

# Import Add Converter Nodes Operators 
from .node_editor_features.add_operators.converter_add_op import classes_converter_OT

# Import Add Input Nodes Operators
from .node_editor_features.add_operators.input_add_op import classes_input_OT

# Import Add Texture Nodes Operators
from .node_editor_features.add_operators.texture_add_op import classes_texture_OT

# Import Add Output
from .node_editor_features.add_operators.output_add_op import classes_output_OT 

# Import Add Shader operator
from .node_editor_features.add_operators.shader_add_op import classes_shader_OT

# Import Vector Operators
from .node_editor_features.add_operators.vector_add_op import classes_vector_OT

# Import Utilities Operators
from .node_editor_features.add_operators.node_editor_utils import classes_utils_OT

# Import Script Node Operator
from .node_editor_features.add_operators.script_add_op import classes_script_OT

# Import Layout Nodes Operator
from .node_editor_features.add_operators.layout_add_op import classes_layout_OT


# Import GeoNodes Attributes Operators
from .node_editor_features.geo_nodes_operators.geo_attribute_add_op import classes_geo_attribute_OT

# Import GeoNodes Input Operators
from .node_editor_features.geo_nodes_operators.geo_input_add_op import classes_geo_input_OT

# Import GeoNodes Operators
from .node_editor_features.geo_nodes_operators.geo_output_add_op import classes_geo_output_OT

# Import GeoNodes Geometry Operators
from .node_editor_features.geo_nodes_operators.geo_geometry_op_add import classes_geo_geometry_OT

# Import GeoNodes Curve
from .node_editor_features.geo_nodes_operators.geo_curve_add_op import classes_geo_curve_OT

# Import GeoNodes Instances
from .node_editor_features.geo_nodes_operators.geo_instances_add_op import classes_geo_instances_OT

# Import GeoNodes Mesh
from .node_editor_features.geo_nodes_operators.geo_mesh_add_op import classes_geo_mesh_OT

# Import 3D View Operators
from .view_3d_utils.view_3d_op_utils import classes_view_3d_OT 


########### TESTE

from .node_editor_features.add_operators.extra_nodes_add_op import *


# Import Node Panels
from .node_editor_custom_panel import classes_Shader_PT 

# Import GeoNodes Panels
from .geo_nodes_custom_panel import classes_GeoNodes_PT

# IMport 3D View Panels
from .view_3d_custom_panel import classes_view_3d_PT, IMAGE_PT_ImageInfo

from .append_to_blender_panels import FlipResolutionAppend

#Extra Nodes
#from .node_editor_features.add_operators.extra_nodes_add_op import NODES_OT_ExtraTEST_Add


#__Classes_List__

op = [TESTE_OT]

shader_classes = classes_Shader_PT + classes_color_OT + classes_converter_OT + classes_input_OT + classes_texture_OT + classes_output_OT + classes_shader_OT + classes_vector_OT + classes_utils_OT + classes_script_OT + classes_layout_OT
geoNodes_classes = classes_GeoNodes_PT + classes_geo_attribute_OT + classes_geo_input_OT + classes_geo_output_OT + classes_geo_geometry_OT + classes_geo_curve_OT + classes_geo_instances_OT + classes_geo_mesh_OT
view3D_classes = classes_view_3d_PT + classes_view_3d_OT


all_classes = classes_master_OT + shader_classes + geoNodes_classes + op + view3D_classes


#                                                           __Register__


def register():
    #### View 3D
    bpy.utils.register_class(IMAGE_PT_ImageInfo)
    bpy.types.Scene.image_list = bpy.props.CollectionProperty(type=IMAGE_PT_ImageInfo)
    bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(name="Filter Image Type", description="Enable image filtering by type", default=False)
    bpy.types.Scene.world_hdri_texture_node = bpy.props.StringProperty(default="Environment Texture", description="FOR NODE IN GROUP ONLY!")
    bpy.types.Scene.image_list = bpy.props.CollectionProperty(type=IMAGE_PT_ImageInfo)
    bpy.types.Scene.image_list_index = bpy.props.IntProperty()
    bpy.types.Scene.filter_image_button = bpy.props.BoolProperty()

    #### Shader Nodes 
    bpy.types.Scene.Shader_Break_Col = bpy.props.BoolProperty()
    #### GeoNodes
    bpy.types.Scene.GeoNode_Break_Col = bpy.props.BoolProperty()    # General Toogle for Break Column Panels
    bpy.types.Scene.AutoConnect = bpy.props.BoolProperty() 
    bpy.types.RENDER_PT_format.append(FlipResolutionAppend)
    for cls in all_classes:
        bpy.utils.register_class(cls)


def unregister():
        #### View 3D
    bpy.utils.unregister_class(IMAGE_PT_ImageInfo)
    del bpy.types.Scene.filter_image_type
    del bpy.types.Scene.world_hdri_texture_node
    del bpy.types.Scene.image_list
    del bpy.types.Scene.image_list
    del bpy.types.Scene.image_list_index  
    del bpy.types.Scene.filtered_images
    #### Unregister filter image button

    #### Shader Nodes    
    del bpy.types.Scene.Shader_Break_Col
    #### GeoNodes
    del bpy.types.Scene.GeoNode_Break_Col   # General Toogle for Break Column Panels
    del bpy.types.Scene.AutoConnect
    bpy.types.RENDER_PT_format.remove(FlipResolutionAppend)
    for cls in all_classes:
        bpy.utils.unregister_class(cls)

            #View 3D




if __name__ == "__main__":
    register()


