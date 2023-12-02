import bpy
from ..master_op.master_op import MASTER_OT_Transform




# Bump
class NODES_OT_VectorBump_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_bump_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "BANANA"

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBump")
        return {"FINISHED"}

# Displacement
class NODES_OT_Displacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeDisplacement")
        return {"FINISHED"}

# Mapping
class NODES_OT_VectorMapping_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_mapping_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMapping")
        return {"FINISHED"}

# Normal
class NODES_OT_VectorNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeNormal")
        return {"FINISHED"}

# Normal Map
class NODES_OT_VectorNormalMap_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_normal_map_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeNormalMap")
        return {"FINISHED"}

# Vector Curves
class NODES_OT_VectorCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorCurve")
        return {"FINISHED"}

# Vector Displacement
class NODES_OT_VectorDisplacement_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_displacement_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorDisplacement")
        return {"FINISHED"}

# Vector Rotate
class NODES_OT_VectorRotate_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_rotate_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorRotate")
        return {"FINISHED"}

# Vector Transform
class NODES_OT_VectorTransform_Add(MASTER_OT_Transform):
    bl_idname = "nodes.vector_transform_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorTransform")
        return {"FINISHED"}
    

classes_vector_OT = [
NODES_OT_VectorBump_Add,
NODES_OT_Displacement_Add,
NODES_OT_VectorMapping_Add,
NODES_OT_VectorNormal_Add,
NODES_OT_VectorNormalMap_Add,
NODES_OT_VectorCurve_Add,
NODES_OT_VectorDisplacement_Add,
NODES_OT_VectorRotate_Add,
NODES_OT_VectorTransform_Add    
]    
