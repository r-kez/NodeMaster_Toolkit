import bpy
from ..master_op.master_op import MASTER_OT_Transform


############################## Instances ####################################

# Instances On Points
class GEONODES_OT_InstancesOnPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_on_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInstanceOnPoints")
        return {"FINISHED"}

# Instances To Points
class GEONODES_OT_InstancesToPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInstancesToPoints")
        return {"FINISHED"}

# Instances Realize Instances
class GEONODES_OT_InstancesRealizeInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_realize_insances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRealizeInstances")
        return {"FINISHED"}

# Instances Rotate Instances
class GEONODES_OT_InstancesRotateInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instance_rotate_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRotateInstances")
        return {"FINISHED"}

# Instances Scale Instances
class GEONODES_OT_InstancesScaleInstances_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_scale_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeScaleInstances")
        return {"FINISHED"}

# Instances Translate Instances
class GEONODES_OT_InstancesTranslateInstancess_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_translate_instances_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTranslateInstances")
        return {"FINISHED"}

# Instances Input Instance Rotaion
class GEONODES_OT_InstancesInputInstanceRotaion_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_input_instance_rotation_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputInstanceRotation")
        return {"FINISHED"}

# Instances Input Instance Scale
class GEONODES_OT_InstancesInputInstanceScale_Add(MASTER_OT_Transform):
    bl_idname = "nodes.instances_input_instance_scale_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputInstanceScale")
        return {"FINISHED"}

classes_geo_instances_OT = [
GEONODES_OT_InstancesOnPoints_Add,
GEONODES_OT_InstancesToPoints_Add,
GEONODES_OT_InstancesRealizeInstances_Add,
GEONODES_OT_InstancesRotateInstances_Add,
GEONODES_OT_InstancesScaleInstances_Add,
GEONODES_OT_InstancesTranslateInstancess_Add,
GEONODES_OT_InstancesInputInstanceRotaion_Add,
GEONODES_OT_InstancesInputInstanceScale_Add,
]

