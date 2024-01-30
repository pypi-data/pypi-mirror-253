

from datetime import datetime
import json

# export type XCommandData = {
#     _id?: string, // the command external id (optional)
#     _module: string , // the module to handle the command
#     _object?:string , // the object to handle the command (optional)
#     _op:string, // the operation to execute
#     _params?: {
#         [k:string] : any // the parameters to send to the operation
#     },
# }


# /**
#  * XCommand class - this command is being sent to the Xpell parser or every XModule/XObject for execution
#  */

class XCommand:
    #data = json object of XCommandData
    def __init__(self, data):
        if data: 
            for key in data:
                self[key] = data[key]
        self.d =  datetime.now()
    

    '''
     * Gets th parameter value from the XCommand whether it has a name or just a position
     * There are 2 ways to send XCommand with parameters: 
     *  1. <module> <op> <param-0> <param-1> <param-2>     // position is for this case
     *  2. <module> <op> param-name:param-value            // name is for this case
     * @param position the position of the parameter if no name is send 
     * @param name the name of the parameter 
     * @param defaultValue the default value if none above exists
     * @returns {any} the actual parameter value
     '''
    def getParam(position, name,defaultValue):
        if self._params:
            if self._params.get(name):
                return self._params[name]
            elif self._params.get(position):
                return self._params[position]
            else:
                return defaultValue
    

