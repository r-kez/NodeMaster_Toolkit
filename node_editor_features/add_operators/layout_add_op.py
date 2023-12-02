import bpy
from ..master_op.master_op import MASTER_OT_Transform



''' ______________________________________________________________ '''

''' Color Nodes Start '''

# Node Frame
class NODES_OT_LayoutFrame_Add(MASTER_OT_Transform):
    bl_idname = "nodes.layout_frame_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeFrame")
        return {"FINISHED"}
    
# Reroute
class NODES_OT_LayoutReroute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.layout_reroute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="NodeReroute")
        return {"FINISHED"}    
    
classes_layout_OT = [
NODES_OT_LayoutFrame_Add, 
NODES_OT_LayoutReroute_Add    
]    