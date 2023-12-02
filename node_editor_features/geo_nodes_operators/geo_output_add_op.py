import bpy
from ..master_op.master_op import MASTER_OT_Transform


#### Constant

# Group Output
class GEONODES_OT_OutputGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.output_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeGroupOutput")
        return {"FINISHED"}

# Viewer Node
class GEONODES_OT_OutputViewer_Add(MASTER_OT_Transform):
    bl_idname = "nodes.output_viewer_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeViewer")
        return {"FINISHED"}

classes_geo_output_OT = [
GEONODES_OT_OutputGroup_Add,
GEONODES_OT_OutputViewer_Add
]
