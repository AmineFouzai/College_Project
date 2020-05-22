# College_Project

A Simple Desktop App With Python Tkinter For Manging Soccer Tournaments.

# setup:
 ----------------------

    1) git clone https://github.com/MedAmineFouzai/College_Project/ 
    2) cd College_Project                                           
    3) python app.py                                                 


# Usage:

No requirements needed for this app because it works with the standard libraries of the language
using the native widgets of an operating system  wich means the UI of the app will change from an OS to another.
the only requirement needed is to have python installed on your computer [python >= 3.5](https://www.python.org/) 
 
## Executable:

you can install [pyinstaller](https://pypi.org/project/PyInstaller/) via pip to build the app into an executable with this command: 


    pyinstaller --add-data="static/ball.ico;static" 
            --add-data "SQL/*.sql;SQL" 
            --icon="static/ball.ico" 
            --name="myapp" 
            --noconsole 
            app.py

OR: all the hard work already done 
    
    pyinstaller myapp.spec
   
you can change the name inside the file [myapp.spec](https://github.com/MedAmineFouzai/College_Project/blob/master/myapp.spec) where the name section is set and all the other stuff.
