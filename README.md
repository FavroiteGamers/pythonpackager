# pythonpackager
Packages .py file into windows compatible .EXE file

Getting Started:
1. Open setup.py in a directory with the file that you are converting
2. First, it will ask you what the file is called
3. Next, type the name of the application in (This will show up in details via properties on windows explorer as well as the rest of the metadata)
4. Type the version of the program (ONLY NUMBERS)
5. Make a description for your program (again metadata for the details tab)
6. Name all of the python pip (or pypy) packages you are using in your file (This is required so the setup.py can copy over all of the package files) 
*NOTE There is a specific way to write out the packages, it is like this nameofpackage,nameofanotherpackage etc.. etc...
7. Go forth and slay dragons! XD

Thanks for checking out my project! 
All credit goes to the creators of cx_Freeze , Anthony Tuininga and Marcelo Duarte.
All I did was add the questions to make it easier to package. 
And credits to the creators of idna, you can find them here https://github.com/kjd/idna
