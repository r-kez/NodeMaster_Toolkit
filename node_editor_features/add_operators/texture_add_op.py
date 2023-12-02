import bpy
from ..master_op.master_op import MASTER_OT_Transform




''' _____________________________________________________________ ''' # TEXTURE Nodes START


# Brick Texture
class NODES_OT_TexBrick_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_brick_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexBrick")
        return {"FINISHED"}
# Checker Texture
class NODES_OT_TexCheck_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_checker_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexChecker")
        return {"FINISHED"}
# Environment Texture
class NODES_OT_TexEnvironment_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_environment_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexEnvironment")
        return {"FINISHED"}
# Environment Texture
class NODES_OT_TexGradient_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_gradient_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexGradient")
        return {"FINISHED"}
# IES Texture
class NODES_OT_TexIES_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_ies_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexIES")
        return {"FINISHED"}
# Image Texture
class NODES_OT_TexImage_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_image_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexImage")
        return {"FINISHED"}
# Magic Texture
class NODES_OT_TexMagic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_magic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexMagic")
        return {"FINISHED"}
# Musgrave Texture
class NODES_OT_TexMusgrave_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_musgrave_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexMusgrave")
        return {"FINISHED"}
# Noise Texture
class NODES_OT_TexNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexNoise")
        return {"FINISHED"}
# Point Density Texture
class NODES_OT_TexPointDensity_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_point_density_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexPointDensity")
        return {"FINISHED"}
# Sky Texture
class NODES_OT_TexSky_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_sky_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexSky")
        return {"FINISHED"}
# Voronoi Texture
class NODES_OT_TexVoronoi_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_voronoi_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexVoronoi")
        return {"FINISHED"}
# Wave Texture
class NODES_OT_TexWave_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_wave_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexWave")
        return {"FINISHED"}
# Wave Texture
class NODES_OT_TexWhiteNoise_Add(MASTER_OT_Transform):
    bl_idname = "nodes.texture_white_noise_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeTexWhiteNoise")
        return {"FINISHED"}
# Texture Operators End


# Texture Operators
classes_texture_OT = [
NODES_OT_TexBrick_Add,
NODES_OT_TexCheck_Add,
NODES_OT_TexEnvironment_Add,
NODES_OT_TexGradient_Add,
NODES_OT_TexIES_Add,
NODES_OT_TexImage_Add,
NODES_OT_TexMagic_Add,
NODES_OT_TexMusgrave_Add,
NODES_OT_TexNoise_Add,
NODES_OT_TexPointDensity_Add,
NODES_OT_TexSky_Add,
NODES_OT_TexVoronoi_Add,
NODES_OT_TexWave_Add,
NODES_OT_TexWhiteNoise_Add
]