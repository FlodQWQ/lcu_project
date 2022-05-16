import jpype
from jpype import *

if __name__ == "__main__":
    if not isJVMStarted():
        startJVM("../dependency/jre/bin/server/jvm.dll")
    java.lang.System.out.println("Hello World")
    shutdownJVM()
