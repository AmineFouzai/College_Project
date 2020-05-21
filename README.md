# College_Project
A Simple Desktop App With Python Tkinter For Manging Soccer Tournaments.
<hr>
<h1>#setup:</h1>
<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/College_Project </td>
</tr>
<tr>
<td> 2) cd College_Project</td>
</tr>
<tr>
<td> 3) python app.py</td>
</tr>
</table>
<hr>
<h1>#Usage:<h1>
 <h4>No requirements needs for this app it works with the standard librarys of the language
 using the native widgets of an operating system  wich means the UI of the app will change from an OS to another. </h4>
<h4>the only requirement needed is to have python installed on your computer <a href="https://www.python.org/" >python >=3.5</a></h4>
 
<h2>#Executable:</h2>
 <h4>you can install <a href="https://pypi.org/project/PyInstaller/" >pyinstaller</a> via pip to build the app into an executable with this command:</h4> 


    pyinstaller --add-data="static/ball.ico;static" 
            --add-data "SQL/*.sql;SQL" 
            --icon="static/ball.ico" 
            --name="myapp" 
            --noconsole 
            app.py

<h4>OR:
all the hard work already done</h4>  
    
    pyinstaller myapp.spec
   
you can change the name inside the file <a href="https://github.com/MedAmineFouzai/College_Project/blob/master/myapp.spec">myapp.spec</a> where the name section is seted and all the other stuff.
