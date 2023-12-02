'''Cropped Resolution took from Amaranth Addon built-in in Blender'''


import bpy

from .view_3d_utils.view_3d_op_utils import *

bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(name="Filter Image Type", description="Enable image filtering by type", default=False)
bpy.types.Scene.show_filtered_images = bpy.props.BoolProperty()
bpy.types.Scene.world_hdri_texture_node = bpy.props.StringProperty(default="Environment Texture")



class RENDER_PT_resolutionHelper(bpy.types.Panel):
    bl_idname = "RENDER_PT_resolutionHelper"
    bl_label = "Resolution Helper"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom Panel"

    def draw(self, context):
        rd = context.scene.render
        #Define Information
        res_percentage = context.scene.render.resolution_percentage
        res_x = context.scene.render.resolution_x 
        res_y = context.scene.render.resolution_y  
        render_settings = context.scene.render
        final_res_x = int(res_x * (res_percentage/100))
        final_res_y = int(res_y * (res_percentage/100))
        final_res_x_border = round((final_res_x * (rd.border_max_x - rd.border_min_x)))
        final_res_y_border = round((final_res_y * (rd.border_max_y - rd.border_min_y)))

        #Draw UI Grid

        layout = self.layout
        layout.label(text="Render Resolution")

        #Define Grid Size
        grid = layout.grid_flow(row_major=True, columns=2)

        #Display Render Resolution
        grid.label(text="Resolution X:")
        grid.prop(render_settings, "resolution_x", text="")
        grid.label(text="Resolution Y:")
        grid.prop(render_settings, "resolution_y", text="")


        grid = layout.grid_flow(row_major=True, columns=1)

        grid.operator("render.res_flip", text="Flip Resolution")

        #Display Percentage Slider
        grid.prop(render_settings, "resolution_percentage", text="Percentage")

        grid = layout.grid_flow(row_major=True, columns=2, align=True)

        #Show Final Resolution
        grid.label(text="Final Resolution:")
        grid.label(text=f"{final_res_x} x {final_res_y}")     
        if rd.use_border:
            grid.label(text="Cropped Resolution:")
            grid.label(text=f"{final_res_x_border} x {final_res_y_border}")

#Get Image Information


class IMAGE_PT_ImageListsPanel(bpy.types.Panel):
    bl_idname = "IMAGE_PT_ImageListsPanel"
    bl_label = "Image Lists"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom Panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Botão para alternar entre as duas listas
        layout.prop(scene, "filter_image_type", text="Show Only EXR and HDR")

        layout.label(text="Set World Texture Name: ")
        #layout.label(text="Default -> Environment Texture ")
        layout.prop(scene, "world_hdri_texture_node", text="")

        # Botão para atualizar as listas de imagens
        layout.operator("object.update_image_lists", text="Update Image Lists")

        # Determinar qual lista usar
        image_list = scene.filtered_images if scene.show_filtered_images else scene.image_list

        if scene.filter_image_type:
            for idx, item in enumerate(image_list):
                if item.name.lower().endswith(('.exr', '.hdr')):        
                    row = layout.row(align=True)
                    row.label(text=f"{item.name}", icon='IMAGE_RGB')
                    depress = idx == scene.image_list_index
                    row.scale_x = 0.3
                    row.operator("object.select_image_from_list", text="Select", emboss=True, depress=depress).index = idx
                
        else:
            for idx, item in enumerate(image_list):
                row = layout.row(align=True)
                row.label(text=f"{item.name}", icon='IMAGE_RGB')
                depress = idx == scene.image_list_index
                row.scale_x = 0.3
                row.operator("object.select_image_from_list", text="Select", emboss=True, depress=depress).index = idx    

        grid = layout.grid_flow(row_major=True, columns=2)
        grid.operator("object.open_image_file_browser", text="Browse")
        grid.operator("object.update_image_list", text="Update")
        grid = layout.grid_flow(row_major=True, columns=1)
        grid.operator("object.link_to_environment", text="Link to World")



classes_view_3d_PT = [
RENDER_PT_resolutionHelper,
IMAGE_PT_ImageListsPanel

]
