#----------------------------------------------------------------
# Generated CMake target import file for configuration "RELEASE".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "arpack" for configuration "RELEASE"
set_property(TARGET arpack APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(arpack PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "Fortran"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/arpack.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS arpack )
list(APPEND _IMPORT_CHECK_FILES_FOR_arpack "${_IMPORT_PREFIX}/lib/arpack.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
