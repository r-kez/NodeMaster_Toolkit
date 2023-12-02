import bpy







# Filter Image Property Gropup
bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(name="Filter Image Type", description="Enable image filtering by type", default=False)

bpy.types.Scene.show_filtered_images = bpy.props.BoolProperty()
#bpy.types.Scene.world_hdri_texture_node = bpy.props.StringProperty(default="Environment Texture")

####### FLIP RESOLUTION START

class RENDER_OT_Res_Flip(bpy.types.Operator):
    bl_idname = "render.res_flip"
    bl_label = "Flip render resolution"
    bl_options = {'UNDO'}
    bl_description = "Flip Current Resolution"

    def execute(self, context):

        res_x = context.scene.render.resolution_x 
        res_y = context.scene.render.resolution_y    

        context.scene.render.resolution_x = res_y
        context.scene.render.resolution_y = res_x

        return ({'FINISHED'})



class RENDER_OT_Perfcentage(bpy.types.Operator):
    bl_idname = "render.percentage_operator"
    bl_label = "Display Render Final Resolution"
    
    def execute(self, context):

        res_percentage = context.scene.render.resolution_percentage
        res_x = context.scene.render.resolution_x
        res_y = context.scene.render.resolution_y



####### Image List OPERATOR START

if not hasattr(bpy.types.Scene, "filter_image_type"):
    bpy.types.Scene.filter_image_type = bpy.props.BoolProperty(
        name="Filter Image Type",
        description="Enable image filtering by type",
        default=False
    )

class IMAGE_OT_FilterImageType(bpy.types.Operator):
    bl_idname = "object.filter_image_type"
    bl_label = "Filter EXR and HDR images"

    def execute(self, context):
        scene = context.scene

        # Filtra as imagens que terminam com .exr ou .hdr
        scene.filtered_images.clear()  # Limpa a lista filtrada antes de adicionar as imagens filtradas
        for image in scene.image_list:
            if image.name.lower().endswith((".exr", ".hdr")):
                filtered_image = scene.filtered_images.add()
                filtered_image.name = image.name
                filtered_image.width = image.width
                filtered_image.height = image.height

        return {"FINISHED"}



class OpenImageFileBrowserOperator(bpy.types.Operator):
    bl_idname = "object.open_image_file_browser"
    bl_label = "Open Image File Browser"
    bl_options = {'UNDO'}
    bl_description = "Open File Browser"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        # Carrega a imagem selecionada no Blender
        bpy.ops.image.open(filepath=self.filepath, relative_path=True, filter_image=True)
        return {'FINISHED'}

    def invoke(self, context, event):
        # Configurações para filtrar apenas arquivos de imagem
        context.window_manager.fileselect_add(self)

        return {'RUNNING_MODAL'}

class UpdateImageListOperator(bpy.types.Operator):
    bl_idname = "object.update_image_list"
    bl_label = "Update Image List"
    bl_options = {'UNDO'}
    bl_description = "Update Image List"
    
    def execute(self, context):
        # Atualiza a lista de imagens na cena
        scene = context.scene
        scene.image_list.clear()
        for image in bpy.data.images:
            item = scene.image_list.add()
            item.name = image.name
            item.width = image.size[0]
            item.height = image.size[1]
        return {'FINISHED'}

import bpy


class IMAGE_OT_LinkToWorld(bpy.types.Operator):
    bl_idname = "object.link_to_environment"
    bl_label = "Link Selected Image to Environment Node"
    bl_options = {'UNDO'}
    bl_description = "Link selected image to World Node"


    def find_node_by_name_in_group(self, node_group, node_name):
        for node in node_group.nodes:
            if node.name == node_name:
                return node
        return None

    def execute(self, context):
        selected_image = context.scene.image_list[context.scene.image_list_index]

        # Obtém o nome do nó a partir da variável da cena
        node_name = context.scene.world_hdri_texture_node

        # Percorre todos os grupos no Shader Editor
        for node_group in bpy.data.node_groups:
            hdri_texture_node = self.find_node_by_name_in_group(node_group, node_name)
            if hdri_texture_node:
                # Tenta encontrar a imagem pelo nome
                image = bpy.data.images.get(selected_image.name)

                # Conecta a imagem ao nó especificado pelo nome
                if image:
                    hdri_texture_node.image = image
                    self.report({'INFO'}, f"Imagem '{selected_image.name}' vinculada ao nó '{node_name}' no grupo '{node_group.name}'.")
                    return {'FINISHED'}
                else:
                    self.report({'ERROR'}, f"Imagem '{selected_image.name}' não encontrada.")
                    return {'CANCELLED'}

        self.report({'ERROR'}, f"Nenhum nó com o nome '{node_name}' encontrado em nenhum grupo.")
        return {'CANCELLED'}

    

####### Image List OPERATOR START

class IMAGE_OT_SelectFromList(bpy.types.Operator):
    bl_idname = "object.select_image_from_list"
    bl_label = "Select Image"
    bl_description = "Select image to be added to World Node"
    
    
    index: bpy.props.IntProperty()  # Defina o atributo como uma anotação de tipo
    
    def execute(self, context):
        context.scene.image_list_index = self.index
        return {"FINISHED"}



"""-------------------------------------------------------------------------------------"""

####### Define Selected OPERATOR START CHAT GPT    

class selectedButton(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    selected = bpy.props.BoolProperty(default=False)

"""-------------------------------------------------------------------------------------"""    


class IMAGE_PT_ImageInfo(bpy.types.PropertyGroup):

    name = bpy.props.StringProperty()   #Store Image Name
    width = bpy.props.IntProperty()     #Store Image width 
    height = bpy.props.IntProperty()    #Store Image height


"""-------------------------------------------------------------------------------------"""    

####### Filter OPERATOR START CHAT GPT      

class IMAGE_OT_FilterImageButton(bpy.types.Operator):
    bl_idname = "object.filter_image_button"
    bl_label = "Simple Operator"

    filter_image_button: bpy.props.BoolProperty()

    def execute(self, context):
        if self.filter_image_button:
            self.report({'INFO'}, 'Boolean ativado!')
        else:
            self.report({'INFO'}, 'Boolean desativado!')
        return {'FINISHED'}


classes_view_3d_OT = [
RENDER_OT_Res_Flip,   
RENDER_OT_Perfcentage,
IMAGE_OT_FilterImageType,
OpenImageFileBrowserOperator,
UpdateImageListOperator,
IMAGE_OT_LinkToWorld,
IMAGE_OT_SelectFromList,
selectedButton,
IMAGE_OT_FilterImageButton
]

