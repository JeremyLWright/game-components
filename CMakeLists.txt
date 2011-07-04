cmake_minimum_required (VERSION 2.8)

project(game_components)

find_package(GTest)
find_package(Doxygen)
include_directories(${GTEST_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
#doxygen confg
add_custom_target(doxygen
${DOXYGEN_EXECUTABLE}
${CMAKE_CURRENT_SOURCE_DIR}/config.doxygen)
#cleanup documentation on "make clean"
set_property(DIRECTORY APPEND PROPERTY
ADDITIONAL_MAKE_CLEAN_FILES
../docs)
#add doxygen as dependency to doc-target
get_target_property(DOC_TARGET doc TYPE)
if(NOT DOC_TARGET)
add_custom_target(doc)
endif()
add_dependencies(doc doxygen)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g3 -pedantic -Wall")
add_subdirectory(models)
add_subdirectory(views)
add_subdirectory(controllers)
# Build the executable
add_executable(main main.cpp)
target_link_libraries(main models views controllers pthread dl)
if(0)
if(GTEST_FOUND)
    add_custom_target(test COMMAND test_${PROJECT_NAME} DEPENDS test_${PROJECT_NAME})
    add_executable(test_${PROJECT_NAME} ${MODEL_TESTS})
    target_link_libraries(test_${PROJECT_NAME} models)
    target_link_libraries(test_${PROJECT_NAME} ${GTEST_BOTH_LIBRARIES} pthread)
endif(GTEST_FOUND) 
endif(0)
