from .XLogger import _xlog
# import XObject, { XObjectPack } from "./XObject.js";

# /**
#  * Xpell Module Object Manager
#  * @description this manager holds the module XObjects that should be managed (XObject children will not be managed separately)
#  * XModules uses the Object Manager to create new XObjects by providing the class of the object by name
#  */



class XObjectManager:
  
    def __init__(self,moduleName):
         #Object Classes dictionary
        self._object_classes = {}

         #Live XObject that is being maintained by the Object Manager
        self._xobjects = {}

         #Object Names index - uses to get object by name
        self._names_index = {}
        if moduleName:
            _xlog.log("Object Manager for  " + moduleName + " loaded")
        else:
            _xlog.log("Object Manager loaded")
        



    @property
    def _objects(self):
        return self._xobjects
    
    @property
    def _classes(self):
        return self._object_classes
    

    # /**
    #  * Checks if an object is found in the object manager
    #  * @param xObjectId 
    #  * @returns 
    #  */
    def has_object(self,xObjectId):
        return hasattr(self._xobjects,xObjectId)
    

    # /**
    #  * Register multiple classes dictionary into the object manager
    #  * @param xObjects - key value list -> \{"view":XView,...\}
    #  */
    def register_objects(self,xObjects):
        for name in xObjects:
            self.register_object(name, xObjects[name])
    

    # /**
    #  * Registers single XObject
    #  * @param name - name of the object
    #  * @param xObjects The object class
    #  */
    def register_object(self,name, xObjects):
        self._object_classes[name] = xObjects
        _xlog.log("Object Manager Register " + name)


    # /**
    #  * Checks if a class (name) is found in the object manager classes dictionary
    #  * @param name - class name
    #  * @returns {boolean} 
    #  */
    def has_object_class(self,name):
        # print("has_object_class",name,self._object_classes)
        # return hasattr(self._object_classes,name)
        return name in self._object_classes
    

    # /**
    #  * Retrieves XObject class instance
    #  * @param name class name
    #  * @returns {XObject}
    #  */
    def get_object_class(self,name):
        return self._object_classes[name]
    

    # /**
    #  * Retrieves all the classes dictionary
    #  * @returns XObjectManagerIndex
    #  */
    def get_all_classes(self):
        return self._object_classes
    

    

    # /**
    #  * Add XObject instance to the manager
    #  * @param xObject XObject to maintain
    #  */
    def add_object(self,xObject):
        if xObject and xObject._id:
            self._xobjects[xObject._id] = xObject
            if not xObject._name or len(xObject._name)==0:
                xObject._name = xObject._id
            self._names_index[xObject._name] = xObject._id
        else:
            _xlog.log("unable to add object")

    '''
     * Remove XObject from the manager 
     * @param xObjectId object id to remove
     '''
    def remove_object(self,xObjectId):
        obj = self._xobjects[xObjectId]
        if obj:
            del self._names_index[obj.name] 
            del self._xobjects[xObjectId] 
        
    

    '''
     * Retrieves XObject instance
     * @param xObjectId XObject id 
     * @returns {XObject}
    '''
    def get_object(self,xObjectId):
        return self._xobjects[xObjectId]
    

    '''
     * alias to get_object
     * @param id 
     * @returns 
     '''
    def go(self,id):
        return self.get_object(id)
    
    

    '''
     * Retrieves XObject instance
     * @param objectName XObject name 
     * @returns {XObject}
    '''
    def get_object_by_name(self,objectName):
        if self._names_index[objectName]:
            return self.get_object(self._names_index[objectName])
        else: 
            return null
    
