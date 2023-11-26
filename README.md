# NodeMaster_Toolkit
A simple addon to help in your workflow


This still a addonin development. I did not the idea of creating many addons, then maybe the name will not fit well on future. I'm open for suggestions.
If you want to help, you are wellcome. Also, fell free for give feedback.

This addon will include the following features, some are already implemented, but as it is a lot of things, some may be incomplete for now.

  ### Shading Editor:
    Native Blender Nodes ¹
    LuxCore Shading Nodes ²
    LuxCore Volume Nodes ³
    Octane Shading Nodes ³
    Octane Composite ³
    Octane Render AOV Nodes ³
    Octane Kernel ³  
    Extra Nodes ²
  ### Geometry Nodes:
    Native Geometry Nodes ¹
    Exclusive Nodes for GeoNodes Toos ¹

### General Node Editor Features:
    Favorite Tab ¹
    Most Used Nodes ¹
    Nodes in Current Scene ¹

  ##### Description:
    1 = Fully Implemented   |   2 = Missing Features   |   3 = Yet to be Implemented
  
*as is too many things, i may miss some nodes or forget to excluse nodes from specific context, please, report if you see something like it

### Favorites

  ![Captura de tela 2023-11-26 151216](https://github.com/r-kez/NodeMaster_Toolkit/assets/150207615/31d85ed4-f752-4788-b5be-2a4a862cb446)
  ![Captura de tela 2023-11-26 151422](https://github.com/r-kez/NodeMaster_Toolkit/assets/150207615/20a417c9-f9c4-447b-bf8c-551a0bb28376)

  The Favorite List is saved in the Native Blender folder "\AppData\Roaming\Blender Foundation\Blender\4.0\config"
  Then you can always have your Favorites in new projects.
  Aiming to not make calls for each context change is necessary to click on "Force Update List" when you change Node Editor Context.
  The Favorite list will be exclusive for each Context, GeoNodes, Shading, LuxCore, Octane, etc.

  Features:
    Favorite List Display: Set the maximum number of displayed Favorites in the list, this will not exclude the nodes, only trim the list.
    Force Update List: CLick for Redraw the list.
    Add node to Favorite: Add the selected node to the list.
    Press the X button to Delete the node form Favories.
    Press Arrow Up / Down to Move your Favorites.
    Press E to call the Pie Menu, It will show all the favories in the list



      
### Extra Nodes:
  ![Captura de tela 2023-11-26 145158](https://github.com/r-kez/NodeMaster_Toolkit/assets/150207615/a38ea70a-9b3a-43f9-91dc-f05839f90eb2)
  
  My initial idea was to add operators for the user to add new sockets in Node Groups, this work well in Blender 3.6, but i could not make it work well in 4.0.
  The solution for this issue was to create such extra nodes in 3.6 and use the append method to import these custom node groups for the active Node tree. This makes easier some tasks in blender.
  initialy the idea was to add all extra node input such as: Image, String, Texture, etc. but it seams to do not work as expected outside of Geometry Nodes.

  Issues:
  1 - in 3.6, if you have a Bool input in a group, as you hit "add new input" the new sockets will follow the same type of the selected input/output, this is not the case in 4.0. 
  In newer versions of Blender you will need to add these Extra Nodes for each input what you want in your group.
  
  2 - Unfortunately, the Extra Node will be created outside of the Current Node Group what you are in. You will need to get out from your group and grab the Extra Node Inside your Group Tree.

  
