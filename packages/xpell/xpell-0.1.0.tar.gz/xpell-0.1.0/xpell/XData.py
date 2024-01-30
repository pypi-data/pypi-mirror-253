
'''
 * XData (Xpell Global shared Variables & Objects)
 * This object uses as a real-time shared memory between all Xpell modules nad components
 * Usage:
 *  - store primitive variable: 
 *      XData._v["my-var-id"] = "my-var-value"
 *  - get primitive variable:
 *      const v = XData._v["my-var-id"]
 *  - store object:
 *      XData._o["my-object-id"] = {my:"object"}
 *  - get object:
 *      const o = XData._o["my-object-id"]
'''

# export type XDataObject = {[_id: string ]: any}
# export type XDataVariable = {[_id: string ]: string | number | boolean}


class _XData:

    def __init__(self):
        self.__objects = {}


    

    '''
     * This method gets the XData object
     * @returns XDataObject object
     * @example
     *  // get the XDataObject object
     *  your_obj = XData._o
     *  // set the XDataObject object
     *  XData._o["my-object-id"] = {my:"object"}
    '''
    # js:
    # get _o(){
    #     return this.__objects
    # }

   
    @property
    def _o(self):
        return self.__objects



    '''
     * This method adds an object to the XData object
     * @param objectId 
     * @param object
     * @comment It is also possible to use the XData._o property -> XData._o["my-object-id"] = {my:"object"} 
    '''
    # js:
    # set(objectId:string, object:any) {
    #     this.__objects[objectId] = object
    # }

    def set(self,objectId, object):
        self.__objects[objectId] = object

    '''
     * This method checks if the XData object has an object by id
     * @param objectId
     * @returns boolean
     * @comment It is also possible to query the XData._o property -> if(XData._o["my-object-id"])...
     *'''
    # js:
    # has(objectId:string):boolean {
    #     return this.__objects.hasOwnProperty(objectId)
    # }

    def has(self,objectId):
        return objectId in self.__objects


    '''
     * Deletes an object from the XData object
     * @param objectId 
    '''
    # js:
    # delete(objectId:string) {
    #     delete this.__objects[objectId]
    # }

    def delete(self,objectId):
        del self.__objects[objectId]
    

    '''
     * Gets an object and delete it from the XData object list
     * @param objectId 
     * @returns 
    '''
    # js:
    # pick(objectId:string) {
    #     const obj = this.__objects[objectId]
    #     this.delete(objectId)
    #     return obj
    # }

    def pick(self,objectId):
        obj = self.__objects[objectId]
        self.delete(objectId)
        return obj
    


    '''
     * This method cleans the XData Memory
    '''
    # js:
    # clean(){
    #     this.__objects = {}
    # }

    def clean(self):
        self.__objects = {}




XData =  _XData()

_xd = XData