import base64
import jpype
from jpype import *

my_port = ''
my_auth = ''


def init(port, auth):
    global my_auth, my_port
    data_bytes = ("riot:" + auth).encode()
    auth = bytes.decode(base64.b64encode(data_bytes))
    my_auth = "Basic " + auth
    my_port = port


def get_match_history(puuid, bound):
    jars = ["../dependency/jars/okhttp-3.10.0.jar", "../dependency/jars/okio-1.14.0.jar",
            "../dependency/jars/Okhttp.jar"]
    jvm_cp = "-Djava.class.path={}".format(";".join(jars))
    if not isJVMStarted():
        startJVM("../dependency/jre/bin/server/jvm.dll", "-ea", jvm_cp)
    execute = jpype.JPackage('com.flod.exec').Main
    my_exec = execute()
    global my_auth, my_port
    my_exec.get_player_match_history(my_port, puuid, my_auth, bound)


def get_match_detail(gameID):
    jars = ["../dependency/jars/okhttp-3.10.0.jar", "../dependency/jars/okio-1.14.0.jar",
            "../dependency/jars/Okhttp.jar"]
    jvm_cp = "-Djava.class.path={}".format(";".join(jars))
    if not isJVMStarted():
        startJVM("../dependency/jre/bin/server/jvm.dll", "-ea", jvm_cp)
    execute = jpype.JPackage('com.flod.exec').Main
    my_exec = execute()
    global my_auth, my_port
    my_exec.get_match_detail(gameID)
