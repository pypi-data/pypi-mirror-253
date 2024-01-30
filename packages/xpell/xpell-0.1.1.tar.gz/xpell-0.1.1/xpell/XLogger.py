# /**
#  * Xpell-logger
#  */



from datetime import datetime
# 
#  @class XLoggerEngine Xpell Logger engine
#  
class _XLogger:
    def __init__(self):
            # /**
            # * Enable logger activity if false no logs will be displayed
            # */
            self.enabled = True
            # /**
            # * Show the date in every log message
            # */
            self.showDate = False
            # /**
            # * Show the Time in every log message
            # */
            self.showTime = True

            self._debug = False



    # /**
    #  * Generates the log output date/time signature (affected by showDate & showTime properties)
    #  * @returns {string}
    #  */
    def get_log_date_time_signature(self):
        d = datetime.now()
        return d.strftime("%H:%M:%S.%f")

    

    # /**
    #  * Log a message to the output log (console)
    #  * @param message - message to present
    #  * @param optionalParams 
    #  */
    def log(self, message=None, *optional_params):
        if self.enabled:
            args = [self.get_log_date_time_signature()]
            if message is not None:
                args.append(message)
            args.extend(optional_params)
            print(*args)
        
    

    # debug(message?: any, ...optionalParams: any[]) {
    #     if (this._debug) {
    #         var args = Array.prototype.slice.call(arguments);
    #         args.unshift(this.get_log_date_time_signature());
    #         console.debug.apply(console, args);
    #     }
    # }
            
            
    # def debug(self, message=None, *optional_params):
    #     if self._debug:
    #         args = [self.get_log_date_time_signature()]
    #         if message is not None:
    #             args.append(message)
    #         args.extend(optional_params)
    #         print(*args)

    '''	
      Log an error message to the output log (console)
      @param message - message to present
      @param optionalParams 
    '''	

    # def error(self, message=None, *optional_params):
    #     args = [self.get_log_date_time_signature()]
    #     if message is not None:
    #         args.append(message)
    #     args.extend(optional_params)
    #     print(*args)
        
    # error(message?: any, ...optionalParams: any[]) {
    #     var args = Array.prototype.slice.call(arguments);
    #     args.unshift(this.get_log_date_time_signature());
    #     console.error.apply(console, args);

    # }


XLogger = _XLogger()
_xlog = XLogger