#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "MQT::Core" for configuration "Debug"
set_property(TARGET MQT::Core APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(MQT::Core PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/mqt-core.lib"
  )

list(APPEND _cmake_import_check_targets MQT::Core )
list(APPEND _cmake_import_check_files_for_MQT::Core "${_IMPORT_PREFIX}/lib/mqt-core.lib" )

# Import target "MQT::CoreDD" for configuration "Debug"
set_property(TARGET MQT::CoreDD APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(MQT::CoreDD PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/mqt-core-dd.lib"
  )

list(APPEND _cmake_import_check_targets MQT::CoreDD )
list(APPEND _cmake_import_check_files_for_MQT::CoreDD "${_IMPORT_PREFIX}/lib/mqt-core-dd.lib" )

# Import target "MQT::CoreZX" for configuration "Debug"
set_property(TARGET MQT::CoreZX APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(MQT::CoreZX PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/mqt-core-zx.lib"
  )

list(APPEND _cmake_import_check_targets MQT::CoreZX )
list(APPEND _cmake_import_check_files_for_MQT::CoreZX "${_IMPORT_PREFIX}/lib/mqt-core-zx.lib" )

# Import target "MQT::CoreECC" for configuration "Debug"
set_property(TARGET MQT::CoreECC APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(MQT::CoreECC PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/mqt-core-ecc.lib"
  )

list(APPEND _cmake_import_check_targets MQT::CoreECC )
list(APPEND _cmake_import_check_files_for_MQT::CoreECC "${_IMPORT_PREFIX}/lib/mqt-core-ecc.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
