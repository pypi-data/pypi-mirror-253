import threading
import time
import uuid
import asyncio
#Xpell imports
from .XLogger import _xlog
from .XEventManager import _xem
from .XUtils import _xu
from .XParser import XParser

# export class
# @class Xpell main engine
class _XpellEngine:
    def __init__(self):
        self._version = "0.0.1"
        self._fire_on_frame_event = False
        self._engine_id = _xu.guid()
        self._frame_number = 0
        self._fps = 1 
        self.parser = XParser 
        self._modules = {}
        self._running = False
        # XEM.fire("xpell-init")
        # _xlog.enabled = False

        self._interval = None
        self._xlog_enabled = False
        _xlog.log("Xpell Engine for Python has been initialized.")
        asyncio.run(_xem.fire("xpell-init"))

    # Enable Xpell logs to console
    def verbose(self):
        self._xlog_enabled = True

    # loads xpell module into engine
        # @param {XModule} xModule
    def load_module(self, xModule):
        if self._modules.get(xModule._name):
            _xlog.log("Module " + xModule._name + " already loaded.")
        else:
            _xlog.log("Loading module " + xModule._name)
            self._modules[xModule._name] = xModule
            xModule.load()

    # loads xpell modules into engine
        # @param {XModule[]} xModules
    # def load_modules(self, xModules):
    #     sself = self
    #     for index, xModule in enumerate(xModules):
    #         sself.load_module(xModule)

    # display information about the xpell engine to the console
    def info(self):
        _xlog.log("Xpell Information: \n- Engine ID: " + self._engine_id + "\n- Version: " + self._version)
    
    def start(self):
        _xlog.log("Starting Xpell")
        self._running = True
        # self.on_frame()
        threading.Thread(target=self.__run_loop).start()
    
    def stop(self): 
        _xlog.log("Stopping Xpell")
        self._running = False
        
    #run textual xCommand
        # @param {cmd} - text command

    def run(self, stringXCommand):
        if (stringXCommand.length > 2):
            scmd = XParser.parse(stringXCommand)
            return self.execute(scmd)
        else:
            raise Exception("Unable to parse Xpell command.")
        
    def __run_loop(self):
        while self._running:
            self.on_frame()
            time.sleep(self._fps)


    # Main on_frame method
    # class all tge sub-modules on_frame methods (if implemented)
    def on_frame(self):

        self._frame_number += 1
        # _xlog.log("Frame: " + str(self._frame_number))
        if self._fire_on_frame_event:
            asyncio.run(_xem.fire("xpell-frame", self._frame_number))
        for key, xModule in self._modules.items():
            if hasattr(xModule, "on_frame") and callable(getattr(xModule, "on_frame")):
                asyncio.run(xModule.on_frame(self._frame_number))

        # if self._running:
            # interval_timer = threading.Timer(self._fps, self.on_frame)
            # line 89 is under
            # interval_timer.start()
                
        # def set_interval(func, sec):
        #     def func_wrapper():
        #         set_interval(func, sec)
        #         func()

        #     t = threading.Timer(sec, func_wrapper)
        #     t.start()
        #     return t
        
        # XData._o["frame-number"] = self._frame_number

Xpell = _XpellEngine()
_x = Xpell
