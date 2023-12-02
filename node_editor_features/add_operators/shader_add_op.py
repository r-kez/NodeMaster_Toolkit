import bpy
from ..master_op.master_op import MASTER_OT_Transform




# Add Shader
class NODES_OT_ShaderrAdd_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_add_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeAddShader")
        return {"FINISHED"}

# BSDF Anisotropic
class NODES_OT_ShaderAniso_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_anisotropic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfAnisotropic")
        return {"FINISHED"}

# BSDF Diffuse
class NODES_OT_ShaderDiff_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_diff_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfDiffuse")
        return {"FINISHED"}

# Emission
class NODES_OT_ShaderEmission_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_emission_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeEmission")
        return {"FINISHED"}

# BSDF Glass
class NODES_OT_ShaderGlass_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_glass_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfGlass")
        return {"FINISHED"}

# BSDF Glossy
class NODES_OT_ShaderGlossy_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_glossy_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfGlossy")
        return {"FINISHED"}

# BSDF Hair
class NODES_OT_ShaderHair_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_hair_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfHair")
        return {"FINISHED"}

# Holdout
class NODES_OT_ShaderHold_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_holdout_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeHoldout")
        return {"FINISHED"}

# Mix Shader
class NODES_OT_ShaderMix_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_mix_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeMixShader")
        return {"FINISHED"}

# BSDF Principled
class NODES_OT_ShaderPrincipled_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_principled_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfPrincipled")
        return {"FINISHED"}

# BSDF Principled Hair
class NODES_OT_ShaderPrincipledHair_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_hair_principled_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfHairPrincipled")
        return {"FINISHED"}

# Volume Principled
class NODES_OT_ShaderPrincipledVolume_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_principled_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumePrincipled")
        return {"FINISHED"}

# BSDF Refraction
class NODES_OT_ShaderRefraction_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_refraction_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfRefraction")
        return {"FINISHED"}

# BSDF Sheen
class NODES_OT_ShaderSheen_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_sheen_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfSheen")
        return {"FINISHED"}

# Subsurface Scattering
class NODES_OT_ShaderSubSurf_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_sub_surf_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeSubsurfaceScattering")
        return {"FINISHED"}

# BSDF Toon
class NODES_OT_ShaderToon_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_toon_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfToon")
        return {"FINISHED"}

# BSDF Translucent
class NODES_OT_ShaderTranslucent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_translucent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfTranslucent")
        return {"FINISHED"}

# BSDF Transparent
class NODES_OT_ShaderTransparent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_transparent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeBsdfTransparent")
        return {"FINISHED"}

# Volume Absorption
class NODES_OT_ShaderVolAbsorption_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_vol_abs_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumeAbsorption")
        return {"FINISHED"}

# Volume Scattering
class NODES_OT_VolScattering_Add(MASTER_OT_Transform):
    bl_idname = "nodes.shader_vol_scattering_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="ShaderNodeVolumeScatter")
        return {"FINISHED"}
    


classes_shader_OT= [
NODES_OT_ShaderrAdd_Add,
NODES_OT_ShaderAniso_Add,
NODES_OT_ShaderDiff_Add,
NODES_OT_ShaderEmission_Add,
NODES_OT_ShaderGlass_Add,
NODES_OT_ShaderGlossy_Add,
NODES_OT_ShaderHair_Add,
NODES_OT_ShaderHold_Add,
NODES_OT_ShaderMix_Add,
NODES_OT_ShaderPrincipled_Add,
NODES_OT_ShaderPrincipledHair_Add,
NODES_OT_ShaderPrincipledVolume_Add,
NODES_OT_ShaderRefraction_Add,
NODES_OT_ShaderSheen_Add,
NODES_OT_ShaderSubSurf_Add,
NODES_OT_ShaderToon_Add,
NODES_OT_ShaderTranslucent_Add,
NODES_OT_ShaderTransparent_Add,
NODES_OT_ShaderVolAbsorption_Add,
NODES_OT_VolScattering_Add    
]    
