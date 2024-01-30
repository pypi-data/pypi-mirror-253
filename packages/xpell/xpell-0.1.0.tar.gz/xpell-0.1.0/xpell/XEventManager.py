'''
 * XEventManager (_xem) is Xpell event system manager.
 * This engine enables event dispatching and listening
 * Usage: 
 * 
 * 1.Event Listen
 *      // listen to event name "my-event" and display the event data to the console when fired
 *      _xem.on("my-event",(eventName,data)=>{
 *          _Xlog.log("XEM Event " + eventName,data)
 *      })
 * 
 * 2. Event Fire
 *      //fire (trigger) event name "my-event" and simple object as data
 *      _xem.fire("my-event",{_data_param:"my data"})
'''
from .XLogger import _xlog 
from .XUtils import _xu



# export type XEvent = {
#     _id: number
#     _name: string
#     _data: any,
# }


# export type XEventListenerOptions =  {
#     _once?: boolean
#     _instance?: _XEventManager
# }

'''
 * This interface define the listener callable function (provided with "on" method)
'''
# interface XEventListener {
#     _id?: string
#     (data: any): void
#     _options?:XEventListenerOptions
# }

'''
 * XEventDispatcher is the system event dispatcher and manager
'''
class _XEventManager:
    

    #events dictionary object and listeners list
    # protected _events: { [name: string]: Array<XEventListener> }
    # protected _listeners_to_event_index: { [listernerId: string]: string} = {}
    def __init__(self):
        self._log_rules = {
            "register": True,
            "remove": True
        }
        self._events = {}
        self._listeners_to_event_index = {}
    

    '''
     * This method listen to event name and register the listener function
     * @param eventName event name to listen to
     * @param listener listener function to be called when event fired
     * @returns listener id
     * @example
     *     // listen to event name "my-event" and display the event data to the console when fired
     *    _xem.on("my-event",(data)=>{
     *         _xlog.log("XEM Event " + data)
     *    })
    '''
    # on(eventName: string, listener: XEventListener, options?:XEventListenerOptions): string {
    #     if (!self._events[eventName]) {
    #         self._events[eventName] = [];
    #     }
    #     self._events[eventName].push(listener)
    #     listener._id =  _xu.guid()
    #     listener._options = options
    #     self._listeners_to_event_index[listener._id] = eventName
    #     if(self._log_rules.register) _xlog.log("XEM Register " + eventName, listener._id)
    #     return listener._id
    # }
    def on(self, event_name, listener, options=None):
        if event_name not in self._events:
            self._events[event_name] = []

        self._events[event_name].append(listener)
        listener._id = _xu.guid()
        listener._options = options
        self._listeners_to_event_index[listener._id] = event_name

        if self._log_rules.get("register"):
            _xlog.log(f"XEM Register {event_name}", listener._id)

        return listener._id

    

    '''
     * This method listen to event name and register the listener function
     * The listener will be removed after first fire
     * @param eventName event name to listen to
     * @param listener listener function to be called when event fired
     * @returns listener id
    '''
    # once(self,eventName: string, listener: XEventListener) {
    #     return self.on(eventName,listener,{_once:true})
    # }
    def once(self, event_name, listener):
        options = {"_once": True}
        return self.on(event_name, listener, options)

    '''
     * This method remove listener by listener id
     * @param listenerId listener id to remove
    '''
    # remove(self,listenerId: string) {
    #     if (self._listeners_to_event_index[listenerId]) {
    #         const eventName = self._listeners_to_event_index[listenerId]
    #         self._events[eventName].forEach((listener, index) => {
    #             if (listener._id == listenerId) {
    #                 self._events[eventName].splice(index, 1)
    #             }
    #         })
    #         delete self._listeners_to_event_index[listenerId]
    #         if(self._log_rules.remove) _xlog.log("XEM Remove " + eventName, listenerId)
    #     }
    # }
    def remove(self, listener_id):
        if listener_id in self._listeners_to_event_index:
            event_name = self._listeners_to_event_index[listener_id]
            if event_name in self._events:
                for index, listener in enumerate(self._events[event_name]):
                    if listener._id == listener_id:
                        self._events[event_name].pop(index)
                        break

            del self._listeners_to_event_index[listener_id]
            if self._log_rules.get("remove`"):
                _xlog.log(f"XEM Remove {event_name}", listener_id)

    # // '''
    # //  * This method remove all listeners by event name
    # //  * @param eventName event name to remove all listeners
    # //  * currently not in use because of safety issues
    # // '''
    # // removeEventListeners(eventName: string) {
    # //     if (self._events[eventName]) {
    # //         self._events[eventName].forEach((listener, index) => {
    # //             if (listener._id) delete self._listeners_to_event_index[listener._id]
    # //         })
    # //         delete self._events[eventName]
    # //     }
    # // }

    '''
     * This method fire (trigger) event name and data
     * @param eventName event name to fire
     * @param data data to be passed to the listener function
    '''
    # async fire(self,eventName: string, data?: any) {
    #     if (self._events[eventName]) {
    #         const eventsToRemove:Array<string> = []
    #         self._events[eventName].forEach((listener) => {
    #             listener(data)
    #             if(listener._options && listener._options._once && listener._id){
    #                 eventsToRemove.push(listener._id)
    #             }
    #         });
    #         eventsToRemove.forEach((listenerId)=>self.remove(listenerId))
    #     }
    # }
    async def fire(self, event_name, data={}):
        if event_name in self._events:
            events_to_remove = []
            # _xlog.log(f"XEM Fire {event_name}", data, self._events[event_name])
            for listener in self._events[event_name]:
                listener(data)
                
                if listener._options and listener._options.get("_once") and listener._id:
                    events_to_remove.append(listener._id)

            for listener_id in events_to_remove:
                self.remove(listener_id)

    




XEventManager = _XEventManager()

_xem = XEventManager

