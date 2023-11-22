@echo off

REM Create the directory structure
md python101
md python101\setup
md python101\basics
md python101\control_structures
md python101\data_structures
md python101\functions
md python101\error_handling
md python101\file_io
md python101\modules_and_libraries
md python101\mini_projects

REM Create the .py files
echo # setup code goes here > python101\setup\setup.py

echo print("Hello, world!") > python101\basics\hello_world.py
echo # variables and types code goes here > python101\basics\variables_and_types.py
echo # basic operations code goes here > python101\basics\basic_operations.py

echo # conditionals code goes here > python101\control_structures\conditionals.py
echo # loops code goes here > python101\control_structures\loops.py

echo # lists code goes here > python101\data_structures\lists.py
echo # dictionaries code goes here > python101\data_structures\dictionaries.py

echo # functions code goes here > python101\functions\functions.py

echo # error handling code goes here > python101\error_handling\error_handling.py

echo # file I/O code goes here > python101\file_io\file_io.py

echo # modules code goes here > python101\modules_and_libraries\modules.py
echo # external libraries code goes here > python101\modules_and_libraries\external_libraries.py

echo # mini project 1 code goes here > python101\mini_projects\mini_project_1.py
echo # mini project 2 code goes here > python101\mini_projects\mini_project_2.py
echo # mini project 3 code goes here > python101\mini_projects\mini_project_3.py

echo Directory structure and files for python101 created successfully.
