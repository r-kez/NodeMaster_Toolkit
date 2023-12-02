import bpy
from ..master_op.master_op import MASTER_OT_Transform

#### Constant

# Input Bool
class GEONODES_OT_InputBool_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_bool_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputBool")
        return {"FINISHED"}

# Input Color
class GEONODES_OT_InputColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputColor")
        return {"FINISHED"}

# Input Image
class GEONODES_OT_InputImage_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_image_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputImage")
        return {"FINISHED"}

# Input Integer
class GEONODES_OT_InputIntegerd_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_integer_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputInt")
        return {"FINISHED"}

# Input Material
class GEONODES_OT_InputMateriald_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMaterial")
        return {"FINISHED"}

# Input String
class GEONODES_OT_InputString_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_string_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="FunctionNodeInputString")
        return {"FINISHED"}

# Input Value
class GEONODES_OT_Inputvalue_Add(MASTER_OT_Transform):
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
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeValue")
        return {"FINISHED"}

# Input Store Named Attribute
class GEONODES_OT_InputStoreNamedAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_store_named_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeStoreNamedAttribute")
        return {"FINISHED"}

################################################## Input Group

# Input Group
class GEONODES_OT_InputGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeGroupInput")
        return {"FINISHED"}

################################################## Scene

class GEONODES_OT_InputColInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_col_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCollectionInfo")
        return {"FINISHED"}

class GEONODES_OT_InputImageInfo_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_image_info_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeImageInfo")
        return {"FINISHED"}

class GEONODES_OT_InputIsViewport_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_is_viewport_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeIsViewport")
        return {"FINISHED"}

class GEONODES_OT_InputObjectInfo_Add(MASTER_OT_Transform):
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
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeObjectInfo")
        return {"FINISHED"}

class GEONODES_OT_InputSceneTime_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_scene_time_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSceneTime")
        return {"FINISHED"}

class GEONODES_OT_InputSelfObject_Add(MASTER_OT_Transform):
    bl_idname = "nodes.input_self_object_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSelfObject")
        return {"FINISHED"}

classes_geo_input_OT = [
#Constant
GEONODES_OT_InputBool_Add,
GEONODES_OT_InputColor_Add,
GEONODES_OT_InputImage_Add,
GEONODES_OT_InputIntegerd_Add,
GEONODES_OT_InputMateriald_Add,
GEONODES_OT_InputString_Add,
GEONODES_OT_Inputvalue_Add,
GEONODES_OT_InputStoreNamedAttribute_Add,
#Group
GEONODES_OT_InputGroup_Add,
#Scene
GEONODES_OT_InputColInfo_Add,
GEONODES_OT_InputImageInfo_Add,
GEONODES_OT_InputIsViewport_Add,
GEONODES_OT_InputObjectInfo_Add,
GEONODES_OT_InputSceneTime_Add,
GEONODES_OT_InputSelfObject_Add
]