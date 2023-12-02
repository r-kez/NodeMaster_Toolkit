import bpy
from ..master_op.master_op import MASTER_OT_Transform




''' ___________________________________________________________________________________________ ''' # INPUT Attributes START


# .select_poly
class NODES_OT_InputSelectPoly_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_poly_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_poly")
        return {"FINISHED"}
    
    
# .vs.UVMap
class NODES_OT_InputVSUVMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_vs_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".vs.UVMap")
        return {"FINISHED"}    


# .corner_edge
class NODES_OT_InputCornerEdge_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_corner_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".corner_edge")
        return {"FINISHED"}     
    
    
# .select_vert
class NODES_OT_InputSelectVert_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_vert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_vert")
        return {"FINISHED"} 
        
        
# .corner_vert
class NODES_OT_InputCornertVert_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_corner_vert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".corner_vert")
        return {"FINISHED"}
    
# position
class NODES_OT_InputPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name="position")
        return {"FINISHED"} 


# .es.UVMap
class NODES_OT_InputEsUvMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_es_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".es.UVMap")
        return {"FINISHED"}     


# .select_edge
class NODES_OT_InputSelectEdge_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_select_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".select_edge")
        return {"FINISHED"}     


# .edge_verts
class NODES_OT_InputEdgeVerts_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_edge_verts_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name=".edge_verts")
        return {"FINISHED"}  

# UVMap att
class NODES_OT_InputUVMapAtt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_att_uvmap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=False,
    )

    def execute(self, context):
        bpy.ops.node.nw_add_attr_node(attr_name="UVMap")
        return {"FINISHED"}     
    
    

    
''' ___________________________________________________________________________________________ '''   # Input Operators START  

# Ambient Occlusion
class NODES_OT_InputAO_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_ao_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeAmbientOcclusion") 
        return {"FINISHED"}     
# Attribute
class NODES_OT_InputAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeAttribute") 
        return {"FINISHED"}     
# Bevel
class NODES_OT_InputBevel_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_bevel_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeBevel") 
        return {"FINISHED"}     
# Camera Data
class NODES_OT_InputCameraData_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_camera_data_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeCameraData") 
        return {"FINISHED"}     
# Vertex Color
class NODES_OT_InputVertexColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_vertex_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeVertexColor") 
        return {"FINISHED"}                     


 # Curve Info
class NODES_OT_InputCurveInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_curve_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeHairInfo") 
        return {"FINISHED"}                     


 # Curve Info
class NODES_OT_InputFresnel_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_fresnel_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeFresnel") 
        return {"FINISHED"}                     

 # Geometry
class NODES_OT_InputGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeNewGeometry") 
        return {"FINISHED"}                     


 # Geometry
class NODES_OT_InputLayerWeight_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_layer_weight_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeLayerWeight") 
        return {"FINISHED"}                     

 
 # Object Info
class NODES_OT_InputLightPath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_light_path_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeLightPath") 
        return {"FINISHED"}                     
# Object Info
class NODES_OT_InputObjectInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_object_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeObjectInfo") 
        return {"FINISHED"}                     
# Particle Info
class NODES_OT_InputParticleInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_particle_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeParticleInfo") 
        return {"FINISHED"}                     
# Point Info
class NODES_OT_InputPointInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_point_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodePointInfo") 
        return {"FINISHED"}                     
# RGB
class NODES_OT_InputRGB_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_rgb_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeRGB") 
        return {"FINISHED"}                     
# Tangent
class NODES_OT_InputTangent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_tangent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTangent") 
        return {"FINISHED"}                     
# Texture Coordenates
class NODES_OT_InputTexCoord_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_tex_coord_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTexCoord") 
        return {"FINISHED"}                     
# UV Map
class NODES_OT_InputUVMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_uv_map_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeUVMap") 
        return {"FINISHED"}     
# Value 
class NODES_OT_InputValue_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_value_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeValue") 
        return {"FINISHED"}     
# Volume Info
class NODES_OT_InputVolumeInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_volume_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeVolumeInfo") 
        return {"FINISHED"}     
# Wireframe
class NODES_OT_InputWireframe_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_wireframe_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=True, type="ShaderNodeWireframe") 
        return {"FINISHED"}  
    
classes_input_OT= [
NODES_OT_InputSelectPoly_Add,
NODES_OT_InputVSUVMap_Add,
NODES_OT_InputCornerEdge_Add,
NODES_OT_InputSelectVert_Add,
NODES_OT_InputCornertVert_Add,
NODES_OT_InputPosition_Add,
NODES_OT_InputEsUvMap_Add,
NODES_OT_InputSelectEdge_Add,
NODES_OT_InputEdgeVerts_Add,
NODES_OT_InputUVMapAtt_Add,
# Input Operators
NODES_OT_InputAO_Add,
NODES_OT_InputAttribute_Add,
NODES_OT_InputBevel_Add,
NODES_OT_InputCameraData_Add,
NODES_OT_InputVertexColor_Add,
NODES_OT_InputCurveInfo_Add,
NODES_OT_InputFresnel_Add,
NODES_OT_InputGeometry_Add,
NODES_OT_InputLayerWeight_Add,
NODES_OT_InputLightPath_Add,
NODES_OT_InputObjectInfo_Add,
NODES_OT_InputParticleInfo_Add,
NODES_OT_InputPointInfo_Add,
NODES_OT_InputRGB_Add,
NODES_OT_InputTangent_Add,
NODES_OT_InputTexCoord_Add,
NODES_OT_InputUVMap_Add,
NODES_OT_InputValue_Add,
NODES_OT_InputVolumeInfo_Add,
NODES_OT_InputWireframe_Add,    
]    
