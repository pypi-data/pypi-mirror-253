

'''
 * XModule - Xpell Base Module
 * The class is being extended by modules with the following logic:
 * 1. Every module must have a name
 * 2. Module holds Object manager to manager the module specific object (extends XObject)
 * 3. Every module can execute XCommand (XCommand, JSON, text(CLI style)),
 *    the rules of the method invocation is the "underscore" sign, meaning functions that will start with "_" sign
 *    will be exposed to XPell Interpreter
 *
 * @example
 *  
 *    The following module:
 *      
 *    class myModule extends XModule {
 *          constructor() {...}
 *          _my_Command(xCommand) {
 *              ...
 *          }
 *    }
 * 
 *    will be called like:
 * 
 *    XModule.execute("my-Command")
 *      - when calling the method there is no need for the underscore sign, spaces and dashes will be converted to underscore
 *  
'''

from .XLogger import _xlog
from .XObjectManager import XObjectManager
from .XObject import XObject
from .XCommand import XCommand
from .XLogger import _xlog
from .XUtils import _xu

import json
import uuid
import asyncio

# /**
#  * Xpell Base Module
#  * This class represents xpell base module to be extends
#  * @class XModule
#  * 
#  */
class XModule:


    # data - json object of XModuleData
    def __init__(self,data):
        self._name = data["_name"]
        self._id =  _xu.guid()
        self._object_manager = XObjectManager(self._name)
        

    

    def load(self): 
        _xlog.log("Module " + self._name + " loaded")
    

    '''
     * Creates new XObject from data object
     * @param data - The data of the new object (JSON)
     * @return {XObject|*}
    '''
    def create(self,data):
        x_object = None
        if "_type" in data:
            # _xlog.log("create object of type: " + data["_type"])
            # _xlog.log(self._object_manager.get_all_classes())
            if self._object_manager.has_object_class(data["_type"]):
                x_object_class = self._object_manager.get_object_class(data["_type"])
                if hasattr(x_object_class, "defaults"):
                    XUtils.merge_defaults_with_data(data, x_object_class.defaults)
                x_object = x_object_class(data)
            else:
                raise Exception("Xpell object '" + data["_type"] + "' not found")
        else:
            x_object = XObject(data)

        self._object_manager.add_object(x_object)

        if "_children" in data:
            for spell in data["_children"]:
                new_spell = self.create(spell)
                x_object.append(new_spell)

        asyncio.run(x_object.on_create())

        return x_object
       
    

    # /**
    #  * removes and XObject from the object manager
    #  * @param objectId op
    #  */
    def remove(self,objectId):
        obj = self._object_manger.get_object(objectId)
        if (obj):
            self._object_manger.remove_object(objectId)
            if hasattr(obj, "dispose") and callable(getattr(obj, "dispose")):
                obj.dispose()

        
    


    def _info(self,xCommand):
        _xl.log("module info")
    

    # //xpell interpreter 
    # /**
    #  * Run xpell command - 
    #  * CLI mode, parse the command to XCommand JSON format and call execute method
    #  * @param {string} XCommand input - text 
    #  * @returns command execution result
    #  */
    async def run(self,stringXCommand): 
        if stringXCommand:
            strCmd = stringXCommand.trim()
            #//add module name to run command if not exists (in case of direct call from the module)
            if not strCmd.startsWith(this._name):
                strCmd = this._name + " " + strCmd            
            #xCommand = XParser.parse(strCmd)
            return await this.execute(xCommand)
        else:
            # throw an error "Unable to parse Xpell Command"
            raise Exception("Unable to parse Xpell Command")
            
    
    




    # /**
    #  * execute xpell command - CLI mode
    #  * @param {XCommand} XCommand input (JSON)
    #  * @returns command execution result
    #  */
    async def execute(self,xCommand):
        # _xlog.log("execute command: " + json.dumps(xCommand))


        # //search for xpell wrapping functions (starts with _ "underscore" example -> _start() , async _spell_async_func() )
        # if xCommand._op:
        #     lop:string = "_" + xCommand._op.replaceAll('-', '_') #//search for local op = lop
        # if (this[lop] && typeof this[lop] === 'function') {
        #     return this[lop](xCommand)
        # }
        # else if (this._object_manger) //direct xpell injection to specific module
        # {

        #     const o = this._object_manger.get_object_by_name(xCommand._op)
        #     if (o) { o.execute(xCommand) }
        #     else { throw "Xpell Module cant find op:" + xCommand._op }
        # }
        # else {
        #     throw "Xpell Module cant find op:" + xCommand._op
        # }
        # }

        # //search for xpell wrapping functions (starts with _ "underscore" example -> _start() , async _spell_async_func() )
        if xCommand._op:
            lop = "_" + xCommand._op.replace('-', '_')
            if hasattr(self, lop) and callable(getattr(self, lop)):
                return await getattr(self, lop)(xCommand)
            elif self._object_manager:
                o = self._object_manager.get_object_by_name(xCommand._op)
                if o:
                    o.execute(xCommand)
                else:
                    raise Exception("Xpell Module cant find op:" + xCommand._op)
            else:
                raise Exception("Xpell Module cant find op:" + xCommand._op)
        else:
            raise Exception("Xpell Module cant find op:" + xCommand._op)

        



    # /**
    #  * This method triggers every frame from the Xpell engine.
    #  * The method can be override by the extending module to support extended on_frame functionality
    #  * @param frameNumber Current frame number
    #  */
    async def on_frame(self,frameNumber):
        # _xlog.log("on_frame module: " + str(frameNumber))
        om_objects = self._object_manager._objects  # Assuming self is an instance of a class containing _object_manager
        for key in om_objects:
            on_frame_callback = om_objects[key]
            if on_frame_callback and hasattr(on_frame_callback, 'on_frame') and callable(getattr(on_frame_callback, 'on_frame')):
                await on_frame_callback.on_frame(frameNumber)

    


    
    '''
     * Returns the XObject instance from the module Object Manager
     * @param objectId 
     * @returns XObject
    '''
    def get_object(objectId):
        return self._object_manger.get_object(objectId)
    

    '''
     * Imports external object pack to the engine
     * The object class should be like XObjects with static implementation of get_object() method
     * @param {XObjects} xObjectPack 
    '''
    def import_object_pack(xObjectPack):
        self._object_manger.register_objects(xObjectPack.get_objects())
    

    
    

    '''
     * Imports external objects to the engine
     * The object class should be like XObjects with static implementation of get_objects() method
     * @param xObjectName 
     * @param xObject 
    '''
    def import_object(xObjectName, xObject):
         self._object_manger.register_objects(xObjectName, xObject)
    


gm = {"_name":"xmodule"}
# GenericModule = XModule(gm)

class _GenericModule(XModule):
    def __init__(self):
        super().__init__(gm)
        self._object_manager.register_object("xobject",XObject)

    def _info(self,xCommand):
        _xlog.log("generic module info")

GenericModule = _GenericModule()