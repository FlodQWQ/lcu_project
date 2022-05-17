import jpype
import sys
from jpype import *


if __name__ == "__main__":
    jars = ["../dependency/jars/okhttp-3.10.0.jar", "../dependency/jars/okio-1.14.0.jar",
            "../dependency/jars/Okhttp.jar"]
    jvm_cp = "-Djava.class.path={}".format(";".join(jars))
    if not isJVMStarted():
        startJVM("../dependency/jre/bin/server/jvm.dll", "-ea", jvm_cp)
    execute = jpype.JPackage('com.flod.exec').Main
    Exec = execute()
    Exec.get("6477", "3a9e4148-c910-5093-b9f2-f10f96ea2837", "Basic cmlvdDpkWEtMMVZ2Q0RzYWRkV1lrdWVfOURB")
    shutdownJVM()