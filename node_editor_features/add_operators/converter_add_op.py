import bpy
from ..master_op.master_op import MASTER_OT_Transform




''' ___________________________________________________________________________________________ '''   # Converter Operators START

# Converter Blackbody
class NODES_OT_ConvBackbody_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_blackbody_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBlackbody")
        return {"FINISHED"}
# Clamp Blackbody
class NODES_OT_ConvClamp_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_clamp_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeClamp")
        return {"FINISHED"}
# Converter Color Ramp 
class NODES_OT_ConvRamp_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_ramp_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeValToRGB")
        return {"FINISHED"}    
# Converter Combine Color 
class NODES_OT_ConvCombColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_comb_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeCombineColor")
        return {"FINISHED"}
 
 
 # Converter Combine XYZ 
class NODES_OT_ConvCombXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_comb_xyx_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeCombineXYZ")
        return {"FINISHED"}
# Converter Float Curve
class NODES_OT_ConvFloatCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_float_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeFloatCurve")
        return {"FINISHED"}
# Converter Map Range
class NODES_OT_ConvMapRange_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_map_range_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMapRange")
        return {"FINISHED"}
# Converter Math
class NODES_OT_ConvMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_math_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMath")
        return {"FINISHED"}
# Converter Mix
class NODES_OT_ConvMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMix")
        return {"FINISHED"}
# Converter RGB to BW
class NODES_OT_ConvRGBToBw_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_rgb_to_bw_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeRGBToBW")
        return {"FINISHED"}
# Converter Separate Color
class NODES_OT_ConvSeparateColor_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_separate_color_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSeparateColor")
        return {"FINISHED"}
# Converter Separate XYZ
class NODES_OT_ConvSeparateXYZ_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_separate_xyz_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSeparateXYZ")
        return {"FINISHED"}
# Converter Vector Math
class NODES_OT_ConvVectorMath_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_vector_math_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVectorMath")
        return {"FINISHED"}
# Converter Wave Length
class NODES_OT_ConvWaveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_wave_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeWavelength")
        return {"FINISHED"}
# Converter Wave Length
class NODES_OT_ConvWaveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.conv_wave_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeWavelength")
        return {"FINISHED"}
    


classes_converter_OT = [
NODES_OT_ConvBackbody_Add,
NODES_OT_ConvClamp_Add,
NODES_OT_ConvRamp_Add,
NODES_OT_ConvCombColor_Add,
NODES_OT_ConvCombXYZ_Add,
NODES_OT_ConvFloatCurve_Add,
NODES_OT_ConvMapRange_Add,
NODES_OT_ConvMath_Add,
NODES_OT_ConvMix_Add,
NODES_OT_ConvRGBToBw_Add,
NODES_OT_ConvSeparateColor_Add,
NODES_OT_ConvSeparateXYZ_Add,
NODES_OT_ConvVectorMath_Add,
NODES_OT_ConvWaveLength_Add    
]    