import bpy
from ..master_op.master_op import MASTER_OT_Transform





# Geo Nodes Attribute Start

# Attribute Statistic
class GEONODES_OT_AttStatistic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_statistic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeAttributeStatistic")
        return {"FINISHED"}

# Attribute Domain Size
class GEONODES_OT_AttDomainSize_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_domain_size_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeAttributeDomainSize")
        return {"FINISHED"}

# Attribute Blur
class GEONODES_OT_AttBlur_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_blur_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeBlurAttribute")
        return {"FINISHED"}    

# Attribute Capture Named Attribute
class GEONODES_OT_AttCapture_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_capture_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCaptureAttribute")
        return {"FINISHED"}    

# Attribute Remove
class GEONODES_OT_AttRemove_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_remove_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRemoveAttribute")
        return {"FINISHED"}


# Attribute Remove
class GEONODES_OT_AttStoreNamed_Add(MASTER_OT_Transform):
    bl_idname = "nodes.att_store_named_add"
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





classes_geo_attribute_OT = [
GEONODES_OT_AttStatistic_Add,
GEONODES_OT_AttDomainSize_Add,
GEONODES_OT_AttBlur_Add,
GEONODES_OT_AttCapture_Add, 
GEONODES_OT_AttRemove_Add,
GEONODES_OT_AttStoreNamed_Add

]