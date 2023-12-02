import bpy
from ..master_op.master_op import MASTER_OT_Transform, NODE_OT_AutoConnect



AutoConnect: bpy.props.BoolProperty(default=False )

#################### READ #######################

# Mesh On Points
class GEONODES_OT_MeshEdgeAngle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_angle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeAngle")
        return {"FINISHED"}

# Mesh Edge Neighbors
class GEONODES_OT_MeshEdgeNeighbors_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_neigbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeNeighbors")
        return {"FINISHED"}

# Mesh Edge Vertices
class GEONODES_OT_MeshEdgeVertices_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_vertices_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshEdgeVertices")
        return {"FINISHED"}

# Mesh Edge To Face Group
class GEONODES_OT_MeshEdgeToFaceGroup_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_edge_to_face_group_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesToFaceGroups")
        return {"FINISHED"}

# Mesh Face Area
class GEONODES_OT_MeshFaceArea_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_area_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceArea")
        return {"FINISHED"}

# Mesh Face Set Boundaries
class GEONODES_OT_MeshFaceSetBoundaries_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_set_boundaries_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshFaceSetBoundaries")
        return {"FINISHED"}

# Mesh Face Neighbors
class GEONODES_OT_MeshFaceNeighbors_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_neighbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceNeighbors")
        return {"FINISHED"}

# Mesh FaceIs Planar
class GEONODES_OT_MeshFaceIsPlanar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_face_is_planar_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshFaceIsPlanar")
        return {"FINISHED"}

# Mesh Is Shade Smooth
class GEONODES_OT_MeshIsShadeSmooth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_is_shade_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputShadeSmooth")
        return {"FINISHED"}

# Mesh Is Edge Smooth
class GEONODES_OT_MeshIsEdgeSmooth_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_is_edge_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputEdgeSmooth")
        return {"FINISHED"}

# Mesh Island
class GEONODES_OT_MeshIsland_Add(MASTER_OT_Transform):
    bl_idname = "nodes.mesh_island_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshIsland")
        return {"FINISHED"}

# Mesh Shortest Edge Paths
class GEONODES_OT_MeshShortestEdgePaths_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_shortest_edges_paths_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputShortestEdgePaths")
        return {"FINISHED"}

# Mesh Vertex Neighbors
class GEONODES_OT_MeshVertexNeighbors_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_vertex_neighbors_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputMeshVertexNeighbors")
        return {"FINISHED"}


#################### SAMPLE #######################
# Mesh Sample Nearest Surface
class GEONODES_OT_MeshSampleNearestSurface_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_sample_nearest_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleNearestSurface")
        return {"FINISHED"}

# Mesh Sample UV Surface
class GEONODES_OT_MeshSampleUVSurface_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_saple_uv_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleUVSurface")
        return {"FINISHED"}


#################### Write #######################

# Mesh Write Set Shade Smooth
class GEONODES_OT_MesWriteSetShadeSmooth_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_write_set_shade_smooth_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetShadeSmooth")
        return {"FINISHED"}


#################### Operations #######################

# Mesh Operations Dual Mesh
class GEONODES_OT_MeshOperationsDualMesh_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_dual_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDualMesh")
        return {"FINISHED"}

# Mesh Operations Edge Paths To Curves
class GEONODES_OT_MeshOperationsEdgePathsToCurves_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_edge_paths_to_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgePathsToCurves")
        return {"FINISHED"}

# Mesh Operations Edge Paths To Selection
class GEONODES_OT_MeshOperationsEdgePathsToSelection_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_edge_paths_to_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgePathsToSelection")
        return {"FINISHED"}

# Mesh Operations Extrude Mesh
class GEONODES_OT_MeshOperationsExtrudeMesh_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_extrude_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeExtrudeMesh")
        return {"FINISHED"}

# Mesh Operations Flip Faces
class GEONODES_OT_MeshOperationsFlipFaces_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_flip_faces_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFlipFaces")
        return {"FINISHED"}

# Mesh Operations Mesh Boolean
class GEONODES_OT_MeshOperationsMeshBoolean_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_mesh_boolean_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshBoolean")
        return {"FINISHED"}

# Mesh Operations Mesh To Curve
class GEONODES_OT_MeshOperationsMeshToCurve_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_mesh_to_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToCurve")
        return {"FINISHED"}

# Mesh Operations Mesh To Points
class GEONODES_OT_MeshOperationsMeshToPoints_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_mesh_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToPoints")
        return {"FINISHED"}

# Mesh Operations Mesh To Volume
class GEONODES_OT_MeshOperationsMeshToVolume_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_mesh_to_volume_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshToVolume")
        return {"FINISHED"}

# Mesh Operations Scale Elements
class GEONODES_OT_MeshVOperationsScaleElements_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_scale_elements_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeScaleElements")
        return {"FINISHED"}

# Mesh Operations Split Edges
class GEONODES_OT_MeshOperationsSplitEdges_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_split_edges_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplitEdges")
        return {"FINISHED"}

# Mesh Operations Subdivide Mesh
class GEONODES_OT_MeshOperationsSubdivideMesh_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_subdivide_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivideMesh")
        return {"FINISHED"}

# Mesh Operations Subdivision Surface
class GEONODES_OT_MeshOperationsSubdivisionSurface_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_subdivision_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivisionSurface")
        return {"FINISHED"}

# Mesh Operations Triangulate
class GEONODES_OT_MeshOperationsTriangulate_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_op_triangulate_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTriangulate")
        return {"FINISHED"}


#################### Primitives #######################

# Mesh Primitives Cone
class GEONODES_OT_MeshPrimitivesCone_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_cone_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCone")
        return {"FINISHED"}

# Mesh Primitives Cube
class GEONODES_OT_MeshPrimitivesCube_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_cube_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCube")
        return {"FINISHED"}

# Mesh Primitives Cylinder
class GEONODES_OT_MeshPrimitivesCylinder_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_cylinder_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCylinder")
        return {"FINISHED"}

# Mesh Primitives Grid
class GEONODES_OT_MeshPrimitivesGrid_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_grid_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshGrid")
        return {"FINISHED"}

# Mesh Primitives IcoSphere
class GEONODES_OT_MeshPrimitivesIcoSphere_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_ico_sphere_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshIcoSphere")
        return {"FINISHED"}

# Mesh Primitives Circle
class GEONODES_OT_MeshPrimitivesCircle_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_circle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshCircle")
        return {"FINISHED"}

# Mesh Primitives Line
class GEONODES_OT_MeshPrimitivesLine_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_mesh_line_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshLine")
        return {"FINISHED"}

# Mesh Primitives UVSphere
class GEONODES_OT_MeshPrimitivesUVSphere_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_primitive_uv_sphere_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeMeshUVSphere")
        return {"FINISHED"}


#################### Topology #######################

# Mesh Topology Corners Of Edge
class GEONODES_OT_MeshTopologyCornersOfEdge_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_corners_of_edge_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfEdge")
        return {"FINISHED"}

# Mesh Topology Corners Of Face
class GEONODES_OT_MeshTopologyCornersOfFace_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_corner_of_face_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfFace")
        return {"FINISHED"}

# Mesh Topology Corners Of Vertex
class GEONODES_OT_MeshTopologyCornersOfVertex_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_corner_of_vertex_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCornersOfVertex")
        return {"FINISHED"}

# Mesh Topology Edges Of Corner
class GEONODES_OT_MeshTopologyEdgesOfCorner_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_edges_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesOfCorner")
        return {"FINISHED"}

# Mesh Topology Edges Of Vertex
class GEONODES_OT_MeshTopologyEdgeOfVertex_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_edges_of_vertex_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeEdgesOfVertex")
        return {"FINISHED"}

# Mesh Topology Face Of Corner
class GEONODES_OT_MeshTopologyFaceOfCorner_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_face_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFaceOfCorner")
        return {"FINISHED"}

# Mesh Topology Offset Corner In Face
class GEONODES_OT_MeshTopologyOffsetCornerInFace_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_offset_corner_in_face_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeOffsetCornerInFace")
        return {"FINISHED"}

# Mesh Topology Vertex Of Corner
class GEONODES_OT_MeshTopologyVertexOfCorner_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_topo_vertex_of_corner_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeVertexOfCorner")
        return {"FINISHED"}

#################### UV #######################

# Mesh UV Pack Islands
class GEONODES_OT_MeshUVPackIslands_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_uv_pack_island_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeUVPackIslands")
        return {"FINISHED"}

# Mesh UV Unwrap
class GEONODES_OT_MeshUVUnwrap_Add(MASTER_OT_Transform, NODE_OT_AutoConnect):
    bl_idname = "nodes.mesh_uv_unwrap_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeUVUnwrap")
        return {"FINISHED"}






classes_geo_mesh_OT = [
# Read
GEONODES_OT_MeshEdgeAngle_Add,
GEONODES_OT_MeshEdgeNeighbors_Add,
GEONODES_OT_MeshEdgeVertices_Add,
GEONODES_OT_MeshEdgeToFaceGroup_Add,
GEONODES_OT_MeshFaceArea_Add,
GEONODES_OT_MeshFaceSetBoundaries_Add,
GEONODES_OT_MeshFaceNeighbors_Add,
GEONODES_OT_MeshFaceIsPlanar_Add,
GEONODES_OT_MeshIsShadeSmooth_Add,
GEONODES_OT_MeshIsEdgeSmooth_Add,
GEONODES_OT_MeshIsland_Add,
GEONODES_OT_MeshShortestEdgePaths_Add,
GEONODES_OT_MeshVertexNeighbors_Add,
# Sample
GEONODES_OT_MeshSampleNearestSurface_Add,
GEONODES_OT_MeshSampleUVSurface_Add,
# Write
GEONODES_OT_MesWriteSetShadeSmooth_Add,
# Operations
GEONODES_OT_MeshOperationsDualMesh_Add,
GEONODES_OT_MeshOperationsEdgePathsToCurves_Add,
GEONODES_OT_MeshOperationsEdgePathsToSelection_Add,
GEONODES_OT_MeshOperationsExtrudeMesh_Add,
GEONODES_OT_MeshOperationsFlipFaces_Add,
GEONODES_OT_MeshOperationsMeshBoolean_Add,
GEONODES_OT_MeshOperationsMeshToCurve_Add,
GEONODES_OT_MeshOperationsMeshToPoints_Add,
GEONODES_OT_MeshOperationsMeshToVolume_Add,
GEONODES_OT_MeshVOperationsScaleElements_Add,
GEONODES_OT_MeshOperationsSplitEdges_Add,
GEONODES_OT_MeshOperationsSubdivideMesh_Add,
GEONODES_OT_MeshOperationsSubdivisionSurface_Add,
GEONODES_OT_MeshOperationsTriangulate_Add,
# Primitives
GEONODES_OT_MeshPrimitivesCone_Add,
GEONODES_OT_MeshPrimitivesCube_Add,
GEONODES_OT_MeshPrimitivesCylinder_Add,
GEONODES_OT_MeshPrimitivesGrid_Add,
GEONODES_OT_MeshPrimitivesIcoSphere_Add,
GEONODES_OT_MeshPrimitivesCircle_Add,
GEONODES_OT_MeshPrimitivesLine_Add,
GEONODES_OT_MeshPrimitivesUVSphere_Add,
# Topology
GEONODES_OT_MeshTopologyCornersOfEdge_Add,
GEONODES_OT_MeshTopologyCornersOfFace_Add,
GEONODES_OT_MeshTopologyCornersOfVertex_Add,
GEONODES_OT_MeshTopologyEdgesOfCorner_Add,
GEONODES_OT_MeshTopologyEdgeOfVertex_Add,
GEONODES_OT_MeshTopologyFaceOfCorner_Add,
GEONODES_OT_MeshTopologyOffsetCornerInFace_Add,
GEONODES_OT_MeshTopologyVertexOfCorner_Add,
# UV
GEONODES_OT_MeshUVPackIslands_Add,
GEONODES_OT_MeshUVUnwrap_Add
]