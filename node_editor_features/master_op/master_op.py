import bpy

# Reuse Transform Operator

class MASTER_OT_Transform(bpy.types.Operator):
    bl_idname = "master.operator_transform"
    bl_label = "Transform Operator."

    def invoke(self, context, event):
            self.store_mouse_cursor(context, event)
            result = self.execute(context)

            if self.use_transform and ('FINISHED' in result):
                # removes the node again if transform is canceled
                bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

            return result
        
    def store_mouse_cursor(self, context, event):
    # Implement your cursor location storage logic here
        pass 

# Empty Operator
class NULL_OT_Null(bpy.types.Operator):
    bl_idname = "null.operator_type"
    bl_label = "Node Add Tool"
    
    def execute(self, context):
        
        return {"FINISHED"}
    
class NODE_OT_AutoConnect(bpy.types.Operator):
    bl_idname = "node.auto_connect"
    bl_label = "When add new node: Connect to Output socket from the selected node"

    def execute(self, context):
        bpy.ops.node.link_make('INVOKE_DEFAULT')



    
classes_master_OT = [
MASTER_OT_Transform,
NULL_OT_Null,
NODE_OT_AutoConnect
]

