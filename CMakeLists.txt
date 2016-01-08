CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(url_maya ${CMAKE_CURRENT_SOURCE_DIR}/archives/Autodesk_Maya_${MAYA_MAJOR_VERSION}_EXT${MAYA_MINOR_VERSION}_SP${MAYA_PATCH_VERSION}_EN_Linux_64bit.tgz)

if(${REZ_BUILD_INSTALL})
    set(install_cmd rpm -ivh --prefix=${CMAKE_INSTALL_PREFIX} Maya*.rpm)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    maya
    URL ${url_maya}
    PREFIX maya
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/maya.cmake
    DESTINATION .
)