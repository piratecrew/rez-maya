name = "maya"

""" Version: 20#.EXT.SP """
version = "2017.0.0"

description = \
    """
    Autodesk Maya
    """

variants = [
    ["Linux"]
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
    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagment.xml"
    env.MAYA_VERSION = 2017.0
    env.MAYA_VP2_USE_GPU_MAX_TARGET_SIZE = 1
