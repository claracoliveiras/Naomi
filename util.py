from datetime import datetime
import parsedatetime

def time_String_Parser(args):
    new_string = ""
    for i in range(1, len(args)):
        new_string += " " + args[i]
    return new_string

def time_String_Parser_Pos(args):
    new_string = ""
    for i in range(2, len(args)):
        new_string += " " + args[i]
    return new_string

def string_to_datetime(args):
    cal = parsedatetime.Calendar()
    time_struct, status = cal.parse(time_String_Parser(args))
    return datetime(*time_struct[:6])