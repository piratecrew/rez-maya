name = "maya"

""" Version: 20#.EXT.SP """
version = "2016.1.4"

description = \
    """
    Autodesk Maya
    """

variants = [
    ["platform-linux"]
]

uuid = "repository.maya"

def commands():
	env.MAYA_LOCATION.set("{root}/autodesk/maya")
	env.PATH.prepend("{root}/autodesk/maya/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/autodesk/maya/lib")