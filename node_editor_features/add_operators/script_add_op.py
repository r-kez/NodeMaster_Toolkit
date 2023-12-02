import bpy
from ..master_op.master_op import MASTER_OT_Transform



# Script
class NODES_OT_Script_Add(MASTER_OT_Transform):
    bl_idname = "nodes.script_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeScript")
        return {"FINISHED"}
    

classes_script_OT = [
NODES_OT_Script_Add    
]    