class NoSecDef(Exception):
    print("No security definition could be found")


class ConnError(Exception):
    print("Couldn't connect to TWS.")
