
from .XUtils import XUtils
from .XNanoCommands import  _xobject_basic_nano_commands
from .XEventManager import _xem
from .XData import _xd

reservedWords = { "_children": "child nodes" }

class XObject:

    '''
     * XObject constructor is creating the object and adding all the data keys to the XObject instance
     * @param data constructor input data (object)
     * @param defaults - defaults to merge with data
     * @param skip_parse - skip data parsing 
     * if override this method make sure to call super.init(data,skip_parse) and to set skip_parse to true
    '''
    def __init__(self, data, defaults=None, skip_parse=False):
        
    
        if (defaults):
            XUtils.merge_defaults_with_data(data, defaults)
        

        # self._id = (data && data._id) ? data._id : "xo-" + XUtils.guid();
        self._id = data["_id"] if data and "_id" in data else "xo-" + XUtils.guid()
        self._type = "object" #default type
        self._children = []
        self._nano_commands = {}
        self._name = data["_name"] if data and "_name" in data else self._id
        self._data_source =  None #XData source
        self._on = {}
        self._once = {}
        self._on_create = data["_on_create"] if data and "_on_create" in data else None
        self._on_mount = data["_on_mount"] if data and "_on_mount" in data else None
        self._on_frame = data["_on_frame"] if data and "_on_frame" in data else None
        self._on_data = data["_on_data"] if data and "_on_data" in data else None
        self._on_event = data["_on_event"] if data and "_on_event" in data else None


        #real-time controllers
        self._process_frame = True
        self._process_data = True



        #local cache for nano commands

        self._cache_cmd_txt = None
        self._cache_jcmd = None
        self._event_listeners_ids = {}
        self._xporter = {
            "_ignore_fields": ["_to_xdata_ignore_fields", "_xporter","_children","_on","_once","_on_create","_on_mount","_on_frame","_on_data","_process_frame","_process_data","_xem_options","_event_listeners_ids"],
            "_instance_xporters": {}
        }


        #add Xporter ignore field and instance handler (uses as example also)
        self.add_xporter_data_ignore_fields(["_nano_commands"]) 
        # self.addXporterInstanceXporter(XObject,(objectInstance: XObject) => {
        #     return objectInstance.to_xdata()
        # })
        self.add_xporter_instance_xporter(XObject, lambda object_instance: object_instance.to_xdata())

        self._xem_options = {
            
        }
        self.init(data,skip_parse)
        
    

    def init(self,data,skip_parse=False):
        if not skip_parse and data:
            # print(data)
            # check if _id field exists in data, if yes delete it to prevent duplication
            if "_id" in data:
                del data["_id"] # delete the _id field to remove duplication by the parse function
            self.parse(data, reservedWords)
            self.parse_events(self._xem_options)
            self.add_nano_command_pack(_xobject_basic_nano_commands)
    
    # addEventListener(eventName:string,handler:XObjectOnEventHandler,options?:XEventListenerOptions) {

    #     const xem =  _xem
    #     const event_listener_id = xem.on(eventName,(eventData) => {  handler(this,eventData)},options)
    #     self._event_listeners_ids[eventName] = event_listener_id
    # }

    def add_event_listener(event_name, handler, options=None):
        event_listener_id = _xem.on(event_name, lambda event_data: handler(self, event_data), options)
        self._event_listeners_ids[event_name] = event_listener_id

    # parse_events(options) {
    #     Object.keys(self._on).forEach(eventName => {
    #         if(typeof self._on[eventName] === "function") {
    #             self.addEventListener(eventName,self._on[eventName],options)
    #         }
    #         // else if(typeof self._on[eventName] === "string") {
    #         //     console.error("string event handler not supported yet")
    #         // }
    #         else {
    #             throw new Error("event handler must be a function " +eventName)
    #         }
    #     })

    #     const onceOptions:XEventListenerOptions =  {}
    #     Object.assign(onceOptions,options)
    #     onceOptions._once = true
        
    #     Object.keys(self._once).forEach(eventName => {
    #         if(typeof self._once[eventName] === "function") {
    #             self.addEventListener(eventName,self._once[eventName],onceOptions)
    #         }
    #         else {
    #             throw new Error("event handler must be a function")
    #         }
    #     })
    # }
    def parse_events(self,options):
        for event_name, event_handler in self._on.items():
            if callable(event_handler):
                self.add_event_listener(event_name, event_handler, options)
            else:
                raise ValueError("Event handler must be a function for event: " + event_name)

        once_options = dict(options) if options else {}
        once_options["_once"] = True

        for event_name, once_handler in self._once.items():
            if callable(once_handler):
                self.add_event_listener(event_name, once_handler, once_options)
            else:
                raise ValueError("Event handler must be a function for event: " + event_name)



    


    # removeEventListener(eventName:string) {
    #     if(self._event_listeners_ids[eventName]) {
    #         self.___options._instance?.remove(self._event_listeners_ids[eventName])
    #         delete self._event_listeners_ids[eventName]
    #     }
    # }

    def remove_event_listener(self,event_name):
        if event_name in self._event_listeners_ids:
            _xem.remove(self._event_listeners_ids[event_name])
            del self._event_listeners_ids[event_name]

    # removeAllEventListeners() {
    #     const keys = Object.keys(self._event_listeners_ids)
    #     keys.forEach(key => self.removeEventListener(key))
    # }

    def remove_all_event_listeners(self):
        keys = self._event_listeners_ids.keys()
        for key in keys:
            self.remove_event_listener(key)



    '''
     * Append a child XObject to this XObject
     * @param xobject 
    '''
    # append(xobject:XObject) {
    #     self._children?.push(xobject)
    # }

    def append(self,xobject):
        self._children.append(xobject)


    '''
     * Add single nano command to the object
     * @param commandName - the nano command name
     * @param nanoCommandFunction 
    '''
    # addNanoCommand(commandName: string, nanoCommandFunction: XNanoCommand) {
    #     if (typeof nanoCommandFunction === 'function') {
    #         // _xlog.log("command " + commandName + " loaded to xobject " + self._id)
    #         self._nano_commands[commandName] = nanoCommandFunction
    #     }
    # }

    def add_nano_command(self,command_name, nano_command_function):
        if callable(nano_command_function):
            self._nano_commands[command_name] = nano_command_function


    '''
     * Add nano commands from nano command pack
     * @param ncPack - the nano command pack
    '''

    # addNanoCommandPack(ncPack: XNanoCommandPack) {
    #     if (ncPack) {
    #         Object.keys(ncPack).forEach((key: string) => {
    #             self.addNanoCommand(key, ncPack[key])
    #         })
    #     }
    # }

    def add_nano_command_pack(self,nc_pack):
        if nc_pack:
            for key, value in nc_pack.items():
                self.add_nano_command(key, value)


   

    '''
     * List of fields to ignore when exporting the xobject to XData or string format
     * @param <string[]> ignoreFields - an array with all the fields to ignore 
    '''
    # addXporterDataIgnoreFields(ignoreFields:string[]) {
    #     self._xporter._ignore_fields = self._xporter._ignore_fields.concat(ignoreFields)
    # }

    def add_xporter_data_ignore_fields(self,ignore_fields):
        self._xporter["_ignore_fields"].extend(ignore_fields)


    '''
     * Add XData Xporter instance handler
     * @param <XDataInstanceXporter> ie - the instance exporter object
    '''
    # addXporterInstanceXporter(classOfInstance:any,handler:XDataXporterHandler) {
    #     const xporterName = XUtils.guid()
    #     self._xporter._instance_xporters[xporterName] = {
    #         cls:classOfInstance,
    #         handler:handler
    #     }
    # }

    def add_xporter_instance_xporter(self,class_of_instance, handler):
        xporter_name = XUtils.guid()
        self._xporter["_instance_xporters"][xporter_name] = {
            'cls': class_of_instance,
            'handler': handler
        }




    # js:
    # async dispose() {
    #     self._process_data = false
    #     self._process_frame = false
    #     self.removeAllEventListeners()
    #     if(self._children) {
    #         self._children.forEach(child => {
    #             if (typeof child.dispose == "function") {
    #                  child.dispose()
    #             }
    #         })
    #     }
    #     self._children = []
    # }

    async def dispose(self):
        self._process_data = False
        self._process_frame = False
        self.remove_all_event_listeners()
        if self._children:
            for child in self._children:
                if callable(child.dispose):
                    await child.dispose()
        self._children = []



   

    '''
     * Parse data to the XObject
     * @param data data to parse
     * @param ignore - lis of words to ignore in the parse process
    '''
    # parse(data: XObjectData, ignore = reservedWords) {

    #     let cdata = Object.keys(data);
    #     cdata.forEach(field => {
    #         if (!ignore.hasOwnProperty(field) && data.hasOwnProperty(field)) {
    #             this[field] = <any>data[field];
    #         }
    #     });
    # }
    def parse(self,data, ignore=None):
        if ignore is None:
            ignore = reserved_words

        for field, value in data.items():
            if field not in ignore and field in data:
                setattr(self, field, value)


    '''
     * Parse data to the XObject
     * @param data data to parse
     * @param {object} fields- object with fields and default values (IXData format)
     * 
     * fields example = {
     *  _name : "default-name",
     * ...
     * }
    '''
    # js:
    # parseFieldsFromXDataObject(data: XObjectData, fields: { [name: string]: any }) {
    #     let cdata = Object.keys(fields);
    #     cdata.forEach((field: string) => {
    #         if (data.hasOwnProperty(field)) {
    #             this[field] = <any>data[field];
    #         } else {
    #             this[field] = fields[field]
    #         }
    #     })
    # }

    def parse_fields_from_xdata_object(self,data, fields):
        for field, value in fields.items():
            if field in data:
                setattr(self, field, data[field])
            else:
                setattr(self, field, value)


    '''
     * Parse list of fields from IXObjectData to the class
     * @param {IXObjectData} data -  the data
     * @param {Array<string>} fields - array of field names (string)
     * @param checkNonXParams - also check non Xpell fields (fields that not starting with "_" sign)
    '''
    # js:
    # parseFields(data: XObjectData, fields: Array<string>, checkNonXParams?: boolean) {
    #     fields.forEach(field => {
    #         if (data.hasOwnProperty(field)) {
    #             this[field] = <any>data[field];
    #         } else if (checkNonXParams && field.startsWith("_")) {
    #             const choppedField = field.substring(1) // remove "_" from field name "_id" = "id"
    #             if (data.hasOwnProperty(choppedField)) {
    #                 this[field] = <any>data[choppedField]
    #                 this[choppedField] = <any>data[choppedField] //add both to support Three arguments
    #             }
    #         }
    #     })
    # }

    def parse_fields(self,data, fields, check_non_x_params=False):
        for field in fields:
            if field in data:
                setattr(self, field, data[field])
            elif check_non_x_params and field.startswith("_"):
                chopped_field = field[1:] # remove "_" from field name "_id" = "id"
                if chopped_field in data:
                    setattr(self, field, data[chopped_field])
                    setattr(self, chopped_field, data[chopped_field]) #add both to support Three arguments


    


    '''
     * this method triggered after the HTML DOM object has been created and added to the parent element
     * support external _on_create anonymous function in the , example:
     * _on_create: async (xObject) => {
     *      // xObject -> The XObject parent of the _on_create function, use instead of this keyword
     *      // write code that will be executed each frame.
     *      // make sure to write async anonymous function. 
     * }
     * 
   '''
    # js:
    # async onCreate() {
    #     if (this._on_create) {
    #         if (typeof this._on_create == "function") {
    #             this._on_create(this)
    #         } else if (typeof this._on_create == "string") {
    #             this.run(this._id + " " + this._on_create) //
    #         }
    #     }
    #     //propagate event to children
    #     this._children.forEach((child) => {
    #         if (child.onCreate && typeof child.onCreate === 'function') {
    #             child.onCreate()
    #         }
    #     })
    # }


    async def on_create(self):
        if self._on_create:
            if callable(self._on_create):
                self._on_create(self)
            elif isinstance(self._on_create, str):
                self.run(self._id + " " + self._on_create) #
        
        #propagate event to children
        for child in self._children:
            if callable(child.on_create):
                await child.on_create()



    '''
     * Triggers when the object is being mounted to other element
     * support external _on_create anonymous function in the , example:
     * _on_mount: async (xObject) => {
     *      // xObject -> The XObject parent of the _on_mount function, use instead of this keyword
     *      // write code that will be executed each frame.
     *      // make sure to write async anonymous function. 
     * }
    '''
    # js:
    # async onMount() {
    #     if (this._on_mount) {
    #         if (typeof this._on_mount == "function") {
    #             this._on_mount(this)
    #         } else if (typeof this._on_mount == "string") {
    #             this.run(this._id + " " + this._on_mount) //
    #         }
    #     }
    #     //propagate event to children
    #     this._children.forEach((child) => {
    #         if (child.onMount && typeof child.onMount === 'function') {
    #             child.onMount()
    #         }
    #     })
    # }

    async def on_mount(self):
        if self._on_mount:
            if callable(self._on_mount):
                self._on_mount(self)
            elif isinstance(self._on_mount, str):
                self.run(self._id + " " + self._on_mount) #
        
        #propagate event to children
        for child in self._children:
            if callable(child.on_mount):
                await child.on_mount()



    '''
    * Empty the data source of the object from the XData
    '''
    # js:
    # emptyDataSource() {
    #     if(this._data_source && typeof this._data_source === "string") {
    #         _xd.delete(this._data_source)
    #     }
    # }

    def empty_data_source(self):
        if self._data_source and isinstance(self._data_source, str):
            _xd.delete(self._data_source)



    '''
     * Triggers when new data is being received from the data source
     * @param data - the data
     * if override this method make sure to call super.onData(data) to run the _on_data attribute
    '''
    # js:
    # async onData(data: any) {
    #     if (this._on_data && this._process_data) {
    #         if (typeof this._on_data == "function") {
    #             this._on_data(this, data)
    #         } else if (typeof this._on_data == "string") {
    #             this.run(this._id + " " + this._on_data) 
    #         }
    #     }
    # }

    async def on_data(self,data):
        if self._on_data and self._process_data:
            if callable(self._on_data):
                self._on_data(self, data)
            elif isinstance(self._on_data, str):
                self.run(self._id + " " + self._on_data) 




    '''
     * Triggers from Xpell frame every frame
     * Support _on_frame atrribute that can be XCommand string or function
     * @param {number} frameNumber 
     * 
     * XObject supports
     * 1. External _on_frame anonymous function in the , example:
     * _on_frame: async (xObject,frameNumber) => {
     *      // xObject -> The XObject parent of the _on_frame function, use instead of this keyword
     *      // frameNumber = Xpell current frame number 
     *      // write code that will be executed each frame.
     *      // make sure to write async anonymous function. 
     *      // be wise with the function execution and try to keep it in the 15ms running time to support 60 FPS
     * }
     * 
     * 2. String execution of nano commands
     * 
     * _on_frame: "nano command text"
     * 
    '''
    # async on_frame(frameNumber: number) {
    #     //
    #     if (this._on_frame && this._process_frame) {
    #         if (typeof this._on_frame == "function") {
    #             await this._on_frame(this, frameNumber)
    #         } else if (typeof this._on_frame == "string") {
    #             await this.run(this._id + " " + this._on_frame) //
    #         }
    #     }

    #     if(this._data_source && this._process_data) {
    #         if(_xd.has(this._data_source)) {
    #             await this.onData(_xd._o[this._data_source])
    #         }
    #     }

    #     //propagate event to children
    #     this._children.forEach((child) => {
    #         if (child.on_frame && typeof child.on_frame === 'function') {
    #             child.on_frame(frameNumber)
    #         }
    #     })
    # }

    async def on_frame(self,frame_number):
        if self._on_frame and self._process_frame:
            if callable(self._on_frame):
                await self._on_frame(self, frame_number)
            elif isinstance(self._on_frame, str):
                await self.run(self._id + " " + self._on_frame) #

        if self._data_source and self._process_data:
            if self._data_source in _xd:
                await self.on_data(_xd._o[self._data_source])

        #propagate event to children
        for child in self._children:
            if callable(child.on_frame):
                await child.on_frame(frame_number)



    


    '''
     * Runs object nano commands
     * @param nanoCommand - object nano command (string)
     * @param cache - cache last command to prevent multiple parsing on the same command
    '''

    # async run(nanoCommand: string, cache = true) {

    #     let jcmd: XCommand = (this._cache_cmd_txt && this._cache_cmd_txt == nanoCommand) ? <XCommand>this._cache_jcmd : XParser.parse(nanoCommand)
    #     //cache command to prevent parsing in every frame
    #     if (cache) {
    #         this._cache_cmd_txt = nanoCommand
    #         this._cache_jcmd = jcmd
    #     }
    #     this.execute(jcmd) //execute nano commands

    # }

    async def run(self,nano_command, cache=True):
        jcmd = self._cache_jcmd if self._cache_cmd_txt and self._cache_cmd_txt == nano_command else XParser.parse(nano_command)
        #cache command to prevent parsing in every frame
        if cache:
            self._cache_cmd_txt = nano_command
            self._cache_jcmd = jcmd
        self.execute(jcmd) #execute nano commands



  


    '''
     * Execute XCommand within the XObject Nano Commands
     * @param xCommand XCommand to execute
     * 
     * Nano command example:
     * 
     * "set-text" : (xCommand,xObject) => {
     *      xObject.setText(xCommands.params.text)
     * }
     * 
    '''
    # async execute(xCommand: XCommand | XCommandData) {
    #     // run nano commands

    #     if (xCommand._op && this._nano_commands[xCommand._op]) {
    #         try {
    #             this._nano_commands[xCommand._op](<XCommand>xCommand, this)
    #         } catch (err) {
    #             _xlog.error(this._id + " has error with command name " + xCommand._op + " " + err)
    #         }
    #     } else {
    #         _xlog.error(this._id + " has no command name " + xCommand._op)
    #     }
    # }

    async def execute(self,x_command):
        if x_command._op and x_command._op in self._nano_commands:
            try:
                self._nano_commands[x_command._op](x_command, self)
            except Exception as err:
                _xlog.error(self._id + " has error with command name " + x_command._op + " " + err)
        else:
            _xlog.error(self._id + " has no command name " + x_command._op)





    '''
     * Return an IXObjectData JSON representation of the XObject
     * @returns IXObjectData
    '''
    # to_xdata(): IXData {
    #     const out: IXData = {}
    #     Object.keys(this).forEach(field => {
    #         if (!this._xporter._ignore_fields.includes(field) &&
    #             this.hasOwnProperty(field) && this[field] !== undefined) {
    #             const tf = this[field]
    #             if (typeof tf === "function") {
    #                 const funcStr = tf.toString()
    #                 if (!funcStr.startsWith("class")) { //in case of class reference it being ignored
    #                     out[field] = funcStr
    #                 } 
    #             } else if (typeof tf === "object") {
    #                 const xporters = Object.keys(this._xporter._instance_xporters)
    #                 let regField = true
    #                 xporters.forEach(xporter => {
    #                     const xp = this._xporter._instance_xporters[xporter]
    #                     if (tf instanceof this._xporter._instance_xporters[xporter].cls) {
    #                         out[field] = this._xporter._instance_xporters[xporter].handler(tf)
    #                         regField = false
    #                     }
    #                 })
                    
    #                 if (regField) {
    #                     out[field] = tf
    #                 }
    #             }
    #             else {
    #                 out[field] = tf
    #             }

    #         }
    #     })
    #     //children are being created separately
    #     out._children = []
    #     if(this._children.length>0) {
    #         this._children.forEach(child => {
    #             if(typeof child.to_xdata === "function") {
    #                 (out._children as Array<IXData>)?.push(child.to_xdata())
    #             }
    #         })
    #     }

    #     return out
    # }

    def to_xdata(self):
        out = {}
        for field in dir(self):
            if field not in self._xporter._ignore_fields and hasattr(self, field) and getattr(self, field) is not None:
                tf = getattr(self, field)
                if callable(tf):
                    func_str = tf.__str__()
                    if not func_str.startswith("class"):
                        out[field] = func_str
                elif isinstance(tf, object):
                    xporters = self._xporter["_instance_xporters"].keys()
                    reg_field = True
                    for xporter in xporters:
                        xp = self._xporter["_instance_xporters"][xporter]
                        if isinstance(tf, xp["cls"]):
                            out[field] = xp["handler"](tf)
                            reg_field = False
                    
                    if reg_field:
                        out[field] = tf
                else:
                    out[field] = tf

        #children are being created separately
        out["_children"] = []
        if len(self._children)>0:
            for child in self._children:
                if callable(child.to_xdata):
                    out["_children"].append(child.to_xdata())

        return out
    




    '''
     * Return a string representation of the XObject
     * @returns string
    '''
    # toString() {
    #     return JSON.stringify(this.to_xdata())
    # }

    def __str__(self):
        return json.dumps(self.to_xdata())

