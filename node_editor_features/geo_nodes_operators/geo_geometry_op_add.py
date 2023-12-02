import bpy
from ..master_op.master_op import MASTER_OT_Transform

############################## Main ####################################

# Geometry to Distance
class GEONODES_OT_GeometryGeometryToDistance_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_to_distance_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeGeometryToInstance")
        return {"FINISHED"}

# Geometry Join Geometry
class GEONODES_OT_GeometryJoinGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_join_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeJoinGeometry")
        return {"FINISHED"}


############################## Read ####################################

# Geometry ID
class GEONODES_OT_GeometryID_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_id_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputID")
        return {"FINISHED"}

# Geometry Index
class GEONODES_OT_GeometryIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputIndex")
        return {"FINISHED"}

# Geometry Named Attribute
class GEONODES_OT_GeometryAttribute_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_attribute_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputNamedAttribute")
        return {"FINISHED"}

# Geometry Normal
class GEONODES_OT_GeometryNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputNormal")
        return {"FINISHED"}

# Geometry Position
class GEONODES_OT_GeometryPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputPosition")
        return {"FINISHED"}

# Geometry Radius
class GEONODES_OT_GeometryRadious_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_radius_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputRadius")
        return {"FINISHED"}

############################## Sample ####################################

# Geometry Proximity
class GEONODES_OT_GeometryProximity_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_proximity_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeProximity")
        return {"FINISHED"}

# Geometry Index of Nearest
class GEONODES_OT_GeometryNearest_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_index_nearest_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeIndexOfNearest")
        return {"FINISHED"}

# Geometry Raycast
class GEONODES_OT_GeometryRaycast_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_raycast_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeRaycast")
        return {"FINISHED"}

# Geometry Sample Index
class GEONODES_OT_GeometrySampleIndex_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_sample_index_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleIndex")
        return {"FINISHED"}

# Geometry Sample Nearest
class GEONODES_OT_GeometrySampleNearest_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_sample_nearest_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleNearest")
        return {"FINISHED"}


############################## Write ####################################


# Geometry Sample Nearest
class GEONODES_OT_GeometrySetIDt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_set_id_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = 'NODE'
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetID")
        return {"FINISHED"}


# Geometry Sample Nearest
class GEONODES_OT_GeometrySetPosition_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_set_position_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = 'NODE'
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetPosition")
        return {"FINISHED"}


############################## Operations ####################################

# Geometry Bounding Box
class GEONODES_OT_GeometryBoundBox_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_bound_box_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeBoundBox")
        return {"FINISHED"}

# Geometry Convex Hull
class GEONODES_OT_GeometryConvexHUll_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_convex_hull_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeConvexHull")
        return {"FINISHED"}

# Geometry Delete Geometry
class GEONODES_OT_GeometryDeleteGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_delete_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDeleteGeometry")
        return {"FINISHED"}

# Geometry Duplicate Elements
class GEONODES_OT_GeometryDuplicateElements_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_duplicate_elements_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDuplicateElements")
        return {"FINISHED"}

# Geometry Merge by Distance
class GEONODES_OT_GeometryMergeByDistance_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_merge_by_distance_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMergeByDistance")
        return {"FINISHED"}

# Geometry Transform
class GEONODES_OT_GeometryTransform_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_transform_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTransform")
        return {"FINISHED"}

# Geometry Separate Geometry
class GEONODES_OT_GeometrySeparateComponents_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_separate_components_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSeparateComponents")
        return {"FINISHED"}

# Geometry Separate Geometry
class GEONODES_OT_GeometrySeparateGeometry_Add(MASTER_OT_Transform):
    bl_idname = "nodes.geometry_separate_geometry_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSeparateGeometry")
        return {"FINISHED"}





classes_geo_geometry_OT = [
GEONODES_OT_GeometryGeometryToDistance_Add,
GEONODES_OT_GeometryJoinGeometry_Add,
GEONODES_OT_GeometryID_Add,
GEONODES_OT_GeometryIndex_Add,
GEONODES_OT_GeometryAttribute_Add,
GEONODES_OT_GeometryNormal_Add,
GEONODES_OT_GeometryPosition_Add,
GEONODES_OT_GeometryRadious_Add,
GEONODES_OT_GeometryProximity_Add,
GEONODES_OT_GeometryNearest_Add,
GEONODES_OT_GeometryRaycast_Add,
GEONODES_OT_GeometrySampleIndex_Add,
GEONODES_OT_GeometrySampleNearest_Add,
GEONODES_OT_GeometrySetIDt_Add,
GEONODES_OT_GeometrySetPosition_Add,
GEONODES_OT_GeometryBoundBox_Add,
GEONODES_OT_GeometryConvexHUll_Add,
GEONODES_OT_GeometryDeleteGeometry_Add,
GEONODES_OT_GeometryDuplicateElements_Add,  
GEONODES_OT_GeometryMergeByDistance_Add,
GEONODES_OT_GeometryTransform_Add,
GEONODES_OT_GeometrySeparateComponents_Add,
GEONODES_OT_GeometrySeparateGeometry_Add
]