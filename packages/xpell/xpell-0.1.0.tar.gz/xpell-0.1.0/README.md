# Xpell-Python - Real-Time Interpreter for Python


Xpell-Python is a real-time interpreter for Python application development, such application requires control on several modules  and AI engine.

Xpell enables real-time translation and routing from any command (XCommand) to platform specific command.

This package include Wormholes protocol for real-time communication between Xpell and the application.

This is the Python version of Xpell, it is based on Python 3.7 and above.


The way to communicate with Xpell engine is to send XCommand that will be analyzed and activate the appropriate module:

```
  [XCommand]
     - module (the name of the module to run the command)
     - created (date/timestamp of the command)
     - object - optional - the object within the module to run the command
     - op (the operation (method/function) to run within the module)
     - params (list of parameters)
```





# Credits & License

 ---

 Author: Fridman Fridman <fridman.tamir@gmail.com>
         Kylie Koshet
         
 License:  GPL-3 

 First Release: 28/01/2024

 Copyright Aime Technologies 2024, all right reserved

 
 