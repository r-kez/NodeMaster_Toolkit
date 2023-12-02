import bpy



# Instances Input Instance Scale
class TESTE_OT(bpy.types.Operator):
    bl_idname = "nodes.test_ot"
    bl_label = "Node Add Tool"
    bl_space_type = 'NODE_EDITOR'
    bl_context = "object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        material = context.material
        if material:
            # Obtém as coordenadas do mouse
            mouse_x, mouse_y = bpy.context.region.view2d.region_to_view(bpy.context.window.width / 2, bpy.context.window.height / 2)
            
            # Adiciona o nó ShaderNodeSeparateRGB na posição do mouse
            separate_node = material.node_tree.nodes.new(type='ShaderNodeSeparateRGB')
            separate_node.location = (mouse_x, mouse_y)

            # Adiciona o nó ShaderNodeCombineRGB ao lado do nó ShaderNodeSeparateRGB
            combine_node = material.node_tree.nodes.new(type='ShaderNodeCombineRGB')
            combine_node.location = (mouse_x + 200, mouse_y)  # Ajuste a posição conforme necessário

            # Conecta a saída do nó ShaderNodeSeparateRGB à entrada do nó ShaderNodeCombineRGB
            material.node_tree.links.new(separate_node.outputs["R"], combine_node.inputs["R"])
            material.node_tree.links.new(separate_node.outputs["G"], combine_node.inputs["G"])
            material.node_tree.links.new(separate_node.outputs["B"], combine_node.inputs["B"])

            # Ativa o modo de link de sockets para permitir a conexão manual
            bpy.ops.node.link_make('INVOKE_DEFAULT')
            
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

        return {'FINISHED'}
