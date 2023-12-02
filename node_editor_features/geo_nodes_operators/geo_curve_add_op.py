import bpy
from ..master_op.master_op import MASTER_OT_Transform

############################## Curve -- Read ####################################

# Curve Handle Positions
class GEONODES_OT_CurveHandlePositions_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_handle_positions_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputCurveHandlePositions")
        return {"FINISHED"}

# Curve Length
class GEONODES_OT_CurveLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveLength")
        return {"FINISHED"}

# Curve Tangent
class GEONODES_OT_CurveTangent_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_tangent_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputTangent")
        return {"FINISHED"}

# Curve Tilt
class GEONODES_OT_CurveTilt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_tilt_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputCurveTilt")
        return {"FINISHED"}

# Curve End Point Selection
class GEONODES_OT_CurveEndPointSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_end_point_selection__add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveEndpointSelection")
        return {"FINISHED"}

# Curve Handle Type Selection
class GEONODES_OT_CurveHandleTypeSelection_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_handle_type_selection_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveHandleTypeSelection")
        return {"FINISHED"}

# Curve Spline Cyclic
class GEONODES_OT_CurveSplineCyclic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_cyclic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSplineCyclic")
        return {"FINISHED"}

# Curve Spline Length
class GEONODES_OT_CurveSplineLength_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_length_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplineLength")
        return {"FINISHED"}

# Curve Spline Parameter
class GEONODES_OT_CurveSplineParameter_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_parameter_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSplineParameter")
        return {"FINISHED"}

# Curve Spline Resolution
class GEONODES_OT_CurveSplineResolution_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spline_resolution_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInputSplineResolution")
        return {"FINISHED"}

############################## Curve -- Sample ####################################

# Curve Spline Resolution
class GEONODES_OT_CurveSample_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_sample_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSampleCurve")
        return {"FINISHED"}

############################## Curve -- Sample ####################################

# Curve Set Curve Normal
class GEONODES_OT_CurveSetCurveNormal_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_normal_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveNormal")
        return {"FINISHED"}

# Curve Set Curve Radius
class GEONODES_OT_CurveSetCurveRadius_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_radius_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveRadius")
        return {"FINISHED"}

# Curve Set Curve Tilt
class GEONODES_OT_CurveSetCurveTilt_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_curve_tilt_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveTilt")
        return {"FINISHED"}

# Curve Set Curve Handle Positions
class GEONODES_OT_CurveSetCurveHandlePositions_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_handle_positions_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetCurveHandlePositions")
        return {"FINISHED"}

# Curve Set Handles
class GEONODES_OT_CurveSetHandleType_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_handle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSetHandles")
        return {"FINISHED"}

# Curve Set Spline Cyclic
class GEONODES_OT_CurveSetSplineCyclic_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_cyclic_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetSplineCyclic")
        return {"FINISHED"}

# Curve Set Spline Resolution
class GEONODES_OT_CurveSetSplineResolution_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_resolution_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSetSplineResolution")
        return {"FINISHED"}

# Curve Set Spline Type
class GEONODES_OT_CurveSetSplineType_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_set_spline_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSplineType")
        return {"FINISHED"}

############################## Curve -- Operations ####################################

# Curve To Mesh
class GEONODES_OT_CurveToMesh_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_to_mesh_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveToMesh")
        return {"FINISHED"}

# Curve Curve To Points
class GEONODES_OT_CurveCurveToPoints_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_to_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveToPoints")
        return {"FINISHED"}

# Curve Deform Curves On Surface
class GEONODES_OT_CurveDeformCurvesOnSurface_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_deform_curves_on_surface_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeDeformCurvesOnSurface")
        return {"FINISHED"}

# Curve Fill Curve
class GEONODES_OT_CurveFillCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_fill_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFillCurve")
        return {"FINISHED"}

# Curve Fillet Curve
class GEONODES_OT_CurveFilletCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_fillet_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeFilletCurve")
        return {"FINISHED"}

# Curve Interpolate Curves
class GEONODES_OT_CurveInterpolateCurves_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_interpolate_curves_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeInterpolateCurves")
        return {"FINISHED"}

# Curve Resample Curve
class GEONODES_OT_CurveResampleCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_resample_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeResampleCurve")
        return {"FINISHED"}

# Curve Reverse Curve
class GEONODES_OT_CurveReverseCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_reverse_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeReverseCurve")
        return {"FINISHED"}

# Curve Subdvide Curve
class GEONODES_OT_CurveSubdvideCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_subdivide_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeSubdivideCurve")
        return {"FINISHED"}

# Curve Trim Curve
class GEONODES_OT_CurveTrimCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_trim_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeTrimCurve")
        return {"FINISHED"}

############################## Curve -- Primitives ####################################

# Curve Arc
class GEONODES_OT_CurveArc_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_arc_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveArc")
        return {"FINISHED"}

# Curve Bezier Segment
class GEONODES_OT_CurveBezierSegment_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_bezier_segment_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveBezierSegment")
        return {"FINISHED"}

# Curve Circle
class GEONODES_OT_CurveCircle_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_circle_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveCircle")
        return {"FINISHED"}

# Curve Line
class GEONODES_OT_CurveLine_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_line_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveLine")
        return {"FINISHED"}

# Curve Spiral
class GEONODES_OT_CurveSpiral_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_spiral_type_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveSpiral")
        return {"FINISHED"}

# Curve Quadratic Bezier
class GEONODES_OT_CurveQuadraticBezier_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_quadratic_bezier_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveQuadraticBezier")
        return {"FINISHED"}

# Curve Quadrilateral
class GEONODES_OT_CurveQuadrilateral_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_quadrilateral_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurvePrimitiveQuadrilateral")
        return {"FINISHED"}

# Curve Curve Star
class GEONODES_OT_CurveCurveStar_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_curve_star_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveStar")
        return {"FINISHED"}

############################## Curve -- Topology ####################################

# Curve Curve of Point
class GEONODES_OT_CurveCurveofPoint_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_of_points_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeCurveOfPoint")
        return {"FINISHED"}

# Curve Offset Point in Curve
class GEONODES_OT_CurveOffsetPointinCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_offset_point_in_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodeOffsetPointInCurve")
        return {"FINISHED"}

# Curve Points of Curve
class GEONODES_OT_CurvePointsofCurve_Add(MASTER_OT_Transform):
    bl_idname = "nodes.curve_points_in_curve_add"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    use_transform: bpy.props.BoolProperty(
        name="Use Transform",
        default=True,
    )

    def execute(self, context):
        bpy.ops.node.add_node(use_transform=self.use_transform, type="GeometryNodePointsOfCurve")
        return {"FINISHED"}



classes_geo_curve_OT = [
GEONODES_OT_CurveHandlePositions_Add, 
GEONODES_OT_CurveLength_Add,    
GEONODES_OT_CurveTangent_Add,
GEONODES_OT_CurveTilt_Add,
GEONODES_OT_CurveEndPointSelection_Add,
GEONODES_OT_CurveHandleTypeSelection_Add,
GEONODES_OT_CurveSplineCyclic_Add,
GEONODES_OT_CurveSplineLength_Add,
GEONODES_OT_CurveSplineParameter_Add,
GEONODES_OT_CurveSplineResolution_Add,
GEONODES_OT_CurveSetCurveNormal_Add,
GEONODES_OT_CurveSetCurveRadius_Add,
GEONODES_OT_CurveSetCurveTilt_Add,
GEONODES_OT_CurveSetCurveHandlePositions_Add,
GEONODES_OT_CurveSetHandleType_Add,
GEONODES_OT_CurveSetSplineCyclic_Add,
GEONODES_OT_CurveSetSplineResolution_Add,
GEONODES_OT_CurveSetSplineType_Add,
# Curve -- Operations
GEONODES_OT_CurveToMesh_Add,
GEONODES_OT_CurveCurveToPoints_Add,
GEONODES_OT_CurveDeformCurvesOnSurface_Add,
GEONODES_OT_CurveFillCurve_Add,
GEONODES_OT_CurveFilletCurve_Add,
GEONODES_OT_CurveInterpolateCurves_Add,
GEONODES_OT_CurveResampleCurve_Add,
GEONODES_OT_CurveReverseCurve_Add,
GEONODES_OT_CurveSubdvideCurve_Add,
GEONODES_OT_CurveTrimCurve_Add,
# Primitives
GEONODES_OT_CurveArc_Add, 
GEONODES_OT_CurveBezierSegment_Add, 
GEONODES_OT_CurveCircle_Add, 
GEONODES_OT_CurveLine_Add, 
GEONODES_OT_CurveSpiral_Add, 
GEONODES_OT_CurveQuadraticBezier_Add, 
GEONODES_OT_CurveQuadrilateral_Add, 
GEONODES_OT_CurveCurveStar_Add, 
# Topology
GEONODES_OT_CurveCurveofPoint_Add, 
GEONODES_OT_CurveOffsetPointinCurve_Add, 
GEONODES_OT_CurvePointsofCurve_Add
]
