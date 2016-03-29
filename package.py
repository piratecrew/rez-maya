name = "maya"

""" Version: 20#.EXT.SP """
version = "2015.1.6"

description = \
    """
    Autodesk Maya
    """

variants = [
    ["platform-linux"]
]

uuid = "repository.maya"

tools = [
    "maya",
    "register_maya"
]

def commands():
    env.MAYA_LOCATION.set("{root}/maya")
    env.PATH.prepend("{root}/maya/bin")
    env.PATH.prepend("{root}/bin")
    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")
