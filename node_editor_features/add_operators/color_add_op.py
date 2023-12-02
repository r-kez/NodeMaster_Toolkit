import bpy
from ..master_op.master_op import MASTER_OT_Transform



''' ______________________________________________________________ '''

''' Color Nodes Start '''

#Brightness / Contrast
class NODES_OT_ColorBC_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_bc_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBrightContrast")
        return {"FINISHED"}
#Gamma
class NODES_OT_Gamma_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_gamma_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeGamma")
        return {"FINISHED"}
# Hue Saturation Value
class NODES_OT_HSV_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_hsv_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeHueSaturation")
        return {"FINISHED"}
# Gamma
class NODES_OT_Gamma_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_gamma_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeGamma")
        return {"FINISHED"}
# Invert Color
class NODES_OT_INVERT_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_invert_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeInvert")
        return {"FINISHED"}
# Light FallOff
class NODES_OT_LightFallOff_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_light_falloff_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeLightFalloff")
        return {"FINISHED"}
# Mix Color
class NODES_OT_MixColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, settings=[{"name":"data_type", "value":"'RGBA'"}], type="ShaderNodeMix")
        return {"FINISHED"}
# Mix Color
class NODES_OT_RGBCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.color_rgb_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeRGBCurve")
        return {"FINISHED"}
# Color Nodes END

# Color Operators

classes_color_OT = [
NODES_OT_ColorBC_Add,
NODES_OT_Gamma_Add,
NODES_OT_HSV_Add,
NODES_OT_INVERT_Add,
NODES_OT_LightFallOff_Add,
NODES_OT_MixColor_Add,
NODES_OT_RGBCurve_Add    
]