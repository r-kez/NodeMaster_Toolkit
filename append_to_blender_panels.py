import bpy
from .view_3d_utils.view_3d_op_utils import RENDER_OT_Res_Flip

def FlipResolutionAppend(self, context):
    layout = self.layout

    layout.operator("render.res_flip", text="Flip Resolution")

