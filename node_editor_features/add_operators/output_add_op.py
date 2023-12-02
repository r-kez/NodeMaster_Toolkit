import bpy
from ..master_op.master_op import MASTER_OT_Transform




# AOV Output
class NODES_OT_OutAOV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_aov_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputAOV")
        return {"FINISHED"}

# Output Light
class NODES_OT_OutLight_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_light_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputLight")
        return {"FINISHED"}

# Output Material
class NODES_OT_OutMaterial_Add(MASTER_OT_Transform):
    bl_idname = "nodes.outout_material_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeOutputMaterial")
        return {"FINISHED"}
    
classes_output_OT = [
NODES_OT_OutAOV_Add,
NODES_OT_OutLight_Add, 
NODES_OT_OutMaterial_Add    
]    