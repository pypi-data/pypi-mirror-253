# Purpose: Nano commands for XObject
_xobject_basic_nano_commands = {
    "info": lambda xCommand, xObject=None: _xlog.log(f"XObject id {xObject._id}" if xObject else "")
}
