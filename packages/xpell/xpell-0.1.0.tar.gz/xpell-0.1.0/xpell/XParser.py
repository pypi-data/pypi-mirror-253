
#import XCommand from "./XCommand.js"
from .XCommand import XCommand
'''
 * Xpell Parser - Parse XML, HTML, Raw Text & Json to Xpell Command
'''

class _XParser:




    '''
     * convert text command to Xpell json command
     * @param {string} txt 
    '''
    # js:
    # parse(txt:string,module?:string):XCommand {        
    #     const carr:string[] = txt.split(" ")
    #     let rv = new XCommand()
    #     if(module){

    #         rv["_module"]= module
    #         rv["_op"] =  carr[0]
    #     } else {
    #         rv["_module"]= carr[0]
    #         rv["_op"] =  carr[1]
    #     }
    #     rv["_params"] = {}
        
    #     if(carr.length>1){
    #         for (let i=2;i<carr.length;++i){
    #             const v = carr[i]
    #             const dl = v.indexOf(":")
    #             if(dl>-1){
    #                 const mc = v.split(":")
    #                 rv._params[mc[0]] = mc[1]
    #             }
    #             else
    #             {
    #                 rv._params[i-1] = carr[i]
    #             }
    #         }
    #     }
    #     return rv
    # }

    def parse(self,txt,module=None):
        carr = txt.split(" ")
        rv = XCommand()
        if module:
            rv["_module"]= module
            rv["_op"] =  carr[0]
        else:
            rv["_module"]= carr[0]
            rv["_op"] =  carr[1]
        rv["_params"] = {}
        
        if len(carr)>1:
            for i in range(2,len(carr)):
                v = carr[i]
                dl = v.indexOf(":")
                if dl>-1:
                    mc = v.split(":")
                    rv._params[mc[0]] = mc[1]
                else:
                    rv._params[i-1] = carr[i]
        return rv


   

    # '''
    #  * Convert raw Xpell command (JSON) to XCommand
    #  * @param rawXpell JSON of Xpell command
    #  * @returns {XCommand}
    # '''
    # parseXpell(rawXpell:string):XCommand {
    #     let code = rawXpell.trim();

    #     let args:Array<string> = XParser.parseArguments(code);

    #     let cmd = new XCommand();
    #     cmd._module = args[0];
    #     cmd._op = args[1];
    #     cmd._params = {};


    #     // start params from index 2
    #     for (let i = 2; i < args.length; i++) {
    #         let paramStr:string = args[i];
    #         let delimiterIdx = paramStr.indexOf(':');
    #         let quotesIdx = paramStr.indexOf('"');
    #         let finalDelimiter = (quotesIdx < delimiterIdx) ? -1 : delimiterIdx;

    #         let paramName = (finalDelimiter === -1) ? i.toString() : paramStr.substring(0, delimiterIdx);
    #         let paramValue = XParser.fixArgumentValue(paramStr.substring(finalDelimiter + 1));

    #         cmd._params[paramName] = paramValue
    #     }


    #     return cmd;
    # }


    '''
     * Parse CLI arguments
     * @param code arguments
     * @returns Array<string> 
    '''
    # parseArguments(code:string):Array<string>  {
    #     let args:Array<string> = [];

    #     while (code.length) {
    #         let argIndex = XParser.getNextArgumentIndex(code);
    #         if (argIndex == -1) {
    #             // error
    #             console.error('error: ' + code);
    #             break;
    #         }
    #         else {
    #             args.push(code.substring(0, argIndex));

    #             let oldCode = code; // this variable is used to check if loop in endless
    #             code = code.substring(argIndex).trim();

    #             if (code.length == oldCode.length) {
    #                 // error - while loop is in endless
    #                 console.error('error: while loop is in endless - leftovers: ' + code);
    #                 break;
    #             }

    #         }
    #     }
    #     return args;
    # }

    

    # fixArgumentValue(arg:any) {
    #     let finalArg = "";
    #     let prevChar = "";
    #     for (var i = 0; i < arg.length; i++) {
    #         let char = arg.charAt(i);
    #         let addToFinal = true;

    #         if (char === '"' && prevChar !== "\\")
    #             addToFinal = false;

    #         if (addToFinal)
    #             finalArg += char;
    #         prevChar = char;
    #     }


    #     finalArg = finalArg.replace(/\\\"/g, '"');

    #     return finalArg;
    # }


    '''
     * Get next argument from string
     * @param {String} str
     * @return {number} indexOf the end of the argument
    '''
    # getNextArgumentIndex(str:string) {
    #     let idx = -1;
    #     let count = str.length;
    #     let zeroCount = count - 1;
    #     let inQuotes = false;
    #     let prevChar = "";
    #     for (let i = 0; i < count; i++) {
    #         let char = str.charAt(i);


    #         if (char === '"') {
    #             if (inQuotes) {
    #                 if (prevChar === '\\') {
    #                     // ignore
    #                 }
    #                 else {
    #                     // end of arguments
    #                     inQuotes = false;
    #                 }

    #             }
    #             else {
    #                 inQuotes = true;
    #             }
    #         }
    #         else if (char === ' ') {
    #             if (!inQuotes) {
    #                 // end of arguments
    #                 idx = i;
    #                 break;
    #             }
    #         }

    #         if (i === zeroCount) {
    #             idx = count;
    #             break;
    #         }


    #         prevChar = char;
    #         // argument is still processing
    #     }

    #     return idx;

XParser =  _XParser()
_xp = XParser
