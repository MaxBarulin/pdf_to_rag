User's Guide
General Toolkit Concepts
Tribon M3
Copyright © 1993-2005 AVEVA AB
1 Introduction
User's Guide General Toolkit Concepts
Copyright © 1993-2005 AVEVA AB
1.1 General
The Tribon Developer's Toolkit is a collection of tools, available for customers to develop their own application functions based on Tribon. The toolkit offers an advanced Tribon customerwith programming skills the possibility to customise functions in Tribon in order to create an efficient and streamlined set of variants and new programs. There are also features for
integration with external systems, for example ERP-type systems.
The Tribon Developer's Toolkit can be used to create new functions in Tribon. Typical tasks a customer may want to achieve by using the Tribon Developer's Toolkit are:
 Extract data from the Tribon Product model and create interactive as well as printed reports.
 Create reports that are tailor-made for the customer's specific needs and that can be easily repeated for efficiency.
 Create drawings with a high level of automatics to meet the customer's standards for e.g. production purposes.
 Create and modify model data in an automatic and standardised way.
 Create new functions, complete with an interactive user interface, to perform frequent tasks according to the customer's standards.
 Integrating Tribon with other systems.
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.2 Tools
Included in the Tribon Developer's Toolkit are the following tools and functions:
 Data Extraction
 Vitesse
```
 Production Data Interface (PDI)
```
```
 Enterprise Resource Planning (ERP) Integration
```
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.3 Services and Training
A number of services related to the Tribon Developer's Toolkit are available from AVEVA. These can be utilised to ensure that maximum benefit is gained from the usage of theDeveloper's Toolkit.
There are also training courses for some of the tools in the Developer's Toolkit, e.g. Vitesse and Production Data Interface.
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.4 Add-Ins
User defined Vitesse add-ins can be automatically added to the menu in the Drafting based modeling applications.
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.4.1 Basic Setup of Vitesse Add-ins
```
The steps below (1-4) must be done to define the Vitesse script as a Vitesse add-in. The script will be available from Tools->Vitesse AddIns->DirName, where DirName is thesubdirectory for the add-in (see below).
```
1. All Vitesse script files and subdirectiories mus be collected under one directory.
2. The add-in directory must be placed under AddIns subdirectory in directory specified by SB_PYTHON environment variable.
3. Vitesse add-in must have __init__.py file defined under its main directory. This allows python interpreter to treat the source as a python package. It is not necessary to add AddIn
directory to python path when __init__.py file exist. Contents of the file can be empty.
4. Define Start.py file that will be used to start your add-in.
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
```
Example:
```
Tools->Vitesse AddIns->ADDIN1
```
Example:
```
ADDIN1
SUBDIR1
SUBDIR2
File1.py
File2.py
```
Example:
```
Vitesse\AddIns\ADDIN1
```
Example:
```
ADDIN1
SUBDIR1
SUBDIR2
File1.py
File2.py
__init__.py
```
Example:
```
ADDIN1
SUBDIR1
SUBDIR2
File1.py
File2.py
__init__.py
Start.py
Copyright © 1993-2005 AVEVA AB
1.4.2 Additional customization of Vitesse Add-ins
Further customization of the Vitesse add-in can be done by additional definitions in the add-in __init__.py file.
Enable/Disable the Add-in depending on Tribon application.
```
Define IsEnabled() function in your __init__.py file. System will call this function to check if the add-in is valid under given Tribon application. The function must return 1 if add-in is
```
enabled otherwise 0.
Define Menu location
```
Define Menu() function if script will take control on creating its menu item. System calls this method instead of creating standard menu item for the add-in.
```
Define add-in name
Define Menu string variable instead of Menu function to be used as name for menu item. System will use it instead of directory name.
Define add-in start module
Define Start string variable if you want to use another starting module then Start.py
User's Guide General Toolkit Concepts
```
Chapter: Introduction
```
```
Example:
```
```
def IsEnabled():
```
import kcs_util
```
if kcs_util.app_drafting():
```
return 1
```
else:
```
return 0
```
Example:
```
```
def Menu():
```
# create menu item and connect it to starting script.
....
```
Example:
```
File structure of add-in:
ADDIN1
SUBDIR1
SUBDIR2
File1.py
File2.py
__init__.py
Content of __init__.py:
```
Menu = 'My add-in'
```
Menu created:
Tools->Vitesse AddIns->My add-in
```
Example:
```
File structure of add-in:
ADDIN1
SUBDIR1
SUBDIR2
File1.py
File2.py
__init__.py
Content of __init__.py:
```
Start = 'File1.py'
```
Copyright © 1993-2005 AVEVA AB
User's Guide
Vitesse
Tribon M3
Copyright © 1993-2005 AVEVA AB
1 Introduction
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
1.1 General
```
Tribon Vitesse is an easy and productive way to create customised, user developed Tribon extensions (Vitesse programs) in an object oriented language enabled with access to theTribon Product Information Model and Tribon Core Modelling functionality. Such a Vitesse program can be directly executed through a file browser, recent list and customised toolbars
```
and menus, and can also be connected to events in form of triggers.
Tribon Vitesse incorporates the language Python, a general purpose, freely available, interpreted language which has been integrated with Tribon to form the programmable environmentin which a Vitesse program is created. The syntax includes all normal features in a programming language, like branching, loops etc. as well as full support for the object paradigm
although the user also has the full freedom to work in a more traditional function oriented fashion.
Many tasks that earlier have been complicated or even impossible to do can now be performed with the help of Tribon Vitesse. The following examples describe a very limited subset ofwhat can be performed. Some more are shown in the proceeding sections.
Due to the combination between Product Information Model Data Extraction and access to modelling functions in Tribon Vitesse it is possible to create rule-based constructions whichautomatically adjust to the surroundings and where the rules are defined by the customer. This can dramatically reduce the input that has to be given to the Tribon application, and
minimise the error rate, since once the Vitesse program is written it can be executed any number of times with little or no possibility for human mistakes. This in total has a significantimpact on the time needed for design.
Easier updates of constructions can be performed, either by rerunning the original Vitesse program, or, in the Tribon Hull case, by executing a Vitesse program that automatically rerunsschemes, instead of activating, running and storing a number of hull schemes manually. This reduces the time needed for changes.
Customised drawings can be automatically created based on model data and existing drawings can be processed for a multitude of purposes. One example could be visualisation ofselected Product Information Model features, by changing display features in a drawing depending on the state of the underlying Product Information Model item. This can efficiently show
e.g. the progress of a design, or group models with common features for easy identification.
Interactive creation of lists. With easy access to the product model of Tribon, it is straightforward to create various types of customised listings or extractions, optionally in combinationwith interactive identification of parts included.
User's Guide Vitesse
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.2 Installation
The Tribon installation procedure properly sets up the necessary environment to run Vitesse. The distribution includes the following files, which are placed in different directories belowthe Tribon installation root directory pointed out by SB_SYSTEM.
 Run-time Python libraries
 Vitesse Library files and Python classes
 Example files
 Tribon standard Vitesse triggers
```
The run-time Python libraries delivered with Tribon are of version 2.3 bug-fix 3. These libraries only represent a necessary subset of a full Python installation. If the Vitesse developmentenvironment is extended by a full Python installation, please make sure that it is of the same version (2.3).
```
Some standard features of the Tribon system make use of Vitesse in combination with wxPython for creating Graphical User Interface dialogues. An example of this is the right mouseclick menu, which pops up under certain conditions. The corresponding script is trig_draft_popup_menu.py. wxPython must be installed if these functions should operate properly.
To install wxPython 2.4.2.4, Python 2.3 must have been installed first. Installation routines for both Python 2.3.3 and wxPython 2.4.2.4 can be found on the distribution CD for Tribon M3in the subdirectory named Python.
The Windows system environment variable PYTHONPATH is used by Python to find modules for the import command. This is automatically set up for directories required by Tribonduring installation and any previous value will be overwritten. This means that user directories must be added to PYTHONPATH after installation.
```
Note: Please also note that installation of other software packages might modify PYTHONPATH and cause Tribon Vitesse to malfunction.
```
The main directory for Vitesse is located directly below the Tribon installation root directory. The Tribon Environment Variable SB_PYTHON is set up to point to this directory. This is alsothe default directory used when running Vitesse scripts through the file browser in Tribon programs.
There is also a variable that defines the location of trigger scripts, SBB_TRIGDIR. This is used by Tribon Standard Vitesse Triggers, and should normally not be modified. For moreinformation about triggers, see Triggers.
User's Guide Vitesse
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
1.3 Development and Migration Guidelines
By applying accepted program development principles when creating Vitesse programs, a number of benefits can be achieved. AVEVA takes a great effort to provide compatibility in theVitesse area between different releases of the system. However, in some cases minor changes might have to be done, for example functions might become obsolete and be replaced by
new functions.
To minimise the migration effort in such cases, we recommend that Vitesse developers encapsulate the Tribon functionality into their own functions. This can for example be done bycreating Python modules that are later used by higher level application functions. If such a strategy is implemented, any changes to the Tribon Vitesse interfaces in coming releases can
be applied to custom developed functions with little effort.
There are also other advantages to this approach. One possibility is that additional functionality can be added in one place. If the Vitesse developer for instance would like to put allmessages given to the user by the message_confirm or message_noconfirm functions into a log file, this functionality could be easily added into the encapsulation module, and would
immediately be in effect in all programs calling this module. Another possibility is to create higher lever functions that perform several tasks and has more functionality than is offered by asingle Tribon Vitesse function.
By applying these and other commonly accepted program development principles, the Vitesse program development can be made more efficient, easily maintainable and robust. Theinformation given in this text only provides a few tips, we highly recommend to also refer to commonly available literature on software development principles to get a further knowledge in
this area and ensure an effective result.
User's Guide Vitesse
```
Chapter: Introduction
```
Copyright © 1993-2005 AVEVA AB
2 Using Vitesse in Tribon Programs
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
2.1 Vitesse Menu and Toolbar
The Vitesse menu can be found under Tools-Vitesse in all Drafting-based interactive programs.
Figure 2:1. Vitesse menu
The Vitesse toolbar can be accessed from the View-Toolbars menu in all Drafting-based interactive programs.
Figure 2:2. Vitesse Toolbar.
The functions in menu and toolbar are the following:
1. Run Vitesse script from file browser.
2. Edit the recent Vitesse script selected in the combo-box.
3. Re-run the recent Vitesse script selected in the combo-box.
4. Combo-box containing the latest executed scripts, script name is automatically added when script is run from file browser. Select and click on script to bring it to the top of list, andthen either use edit button or re-run button for this script. To delete a script from the list, press the Delete key while pointing the mouse to one of the script names in the list. If two or
```
more scripts having the same name have been run from different directories, they will be suffixed by (1), (2) and so on. Let the mouse hover over the script name to display a tooltipcontaining the full file path of the script.
```
5. Activate debugger. This executes a script having a predefined name that can invoke a debugger. A debugger capable of being used together with Vitesse must support anEmbedded Python Interpreter. An example of a debugger that works together with Tribon and that can be connected to this button is Wing that can be downloaded from following
```
website:
```
User's Guide Vitesse
```
Chapter: Using Vitesse in Tribon Programs
```
archaeopteryx.com.
See also Vitesse Options
Vitesse log. When this button is pressed, a dialog showing log messages from Vitesse calls is displayed. See Vitesse Log Window.
6. Reload Python modules. This will clear all Python buffers so that modules changed on disk will be re-loaded next time they are imported.
7. Vitesse options, only available from the menu. See Vitesse Options
Copyright © 1993-2005 AVEVA AB
2.2 Vitesse Log Window
Figure 2:3. Vitesse Log Window
In the upper list box, there is a log of:
1. Scripts started
2. Triggers executed
3. Vitesse functions called, with their name, input parameters, return values and any exceptions.
4. When reload is performed
In the lower list box, only exceptions are listed. To position yourself in the top list on the function call that caused the exception, double click the exception in the lower list box. This can beuseful to find exceptions raised during lengthy executions.
There are also buttons to clear the contents of the log window and to close the window.
See also Vitesse Options for logging options.
```
It is also possible to issue debug messages from a Vitesse script which will be displayed in the log window. This can be done by using the kcs_ui.message_debug() function.
```
User's Guide Vitesse
```
Chapter: Using Vitesse in Tribon Programs
```
Copyright © 1993-2005 AVEVA AB
2.3 Vitesse Options
Figure 2:4. Vitesse Options Dialog
The Vitesse Options Dialog is available from the Tools-Vitesse-Options menu item. The following settings and options are available:
1. Editor. Here it is possible to set up the editor used when clicking on the "edit" button in the toolbar.
 "Notepad" is the default editor
 "File association" will use the editor connected to the .py file extension in Windows.
 "Custom" will enable entering of your own editor of choice, e.g. Pythonwin
2. Logging options. Here it is possible to control when and where the log messages should be presented. See also Vitesse Log Window.
3. Other.
 "Debug script name" can be used to set up the name of a Python script to be executed when the debug toolbar button is clicked. It is supposed that this script will start a
debugger of your choice. See also Vitesse Menu and Toolbar.
 "Number of recent scripts" controls the number of scripts that will be displayed in the recent list in the toolbar. Please note that you will need to restart the program before this
setting will be applied.
```
Note: All logging of script executions can affect the performance of the application negatively and give a longer response time. This is especially valid for the "Logging to logfile" option, which should only be used when necessary. Note that also Python "print" statements can lower the performance significantly.
```
User's Guide Vitesse
```
Chapter: Using Vitesse in Tribon Programs
```
Copyright © 1993-2005 AVEVA AB
2.4 Availability in Tribon Applications
The following link holds a table that illustrates the availability of the Vitesse interfaces in Tribon applications:
vitesse_access.xls
User's Guide Vitesse
```
Chapter: Using Vitesse in Tribon Programs
```
Copyright © 1993-2005 AVEVA AB
3 Utilities
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
3.1 Batch Vitesse
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.1.1 General
There is a possibility to run Vitesse scripts in batch mode. This is made possible through a set of command line arguments for Drafting-based programs in combination with a function toexit the running program. This enables Vitesse scripts to be run in batch without user interaction from any scripting or program language capable of starting an executable program. Below
is an example of how this can be done from a DOS BAT file:
```
Note: All tribon programs should be started through tbstartjob.exe. If the executable itself is started directly, for example specifying sz001.exe instead of tbstartjob.exe -application"Drafting", the Tribon run-time environment including Log Browser and output log file handling will not be properly initialised.
```
```
At the end of the Vitesse script, there should be a call to the exit_program() function. This will instruct the program to end execution, and control will be transferred to the calling script orexecutable. In the example above the "echo" statement will be performed.
```
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
tbstartjob.exe -application "Drafting" -script o:\tribon\m2\vitesse\examples\drafting\kcs_ex_draft10.py
echo "Tribon Drafting Vitesse script finished, continuing with next task
Copyright © 1993-2005 AVEVA AB
3.1.2 Command Line Parameters
These command line parameters can be used in all Drafting-based programs.
User's Guide Vitesse
```
Chapter: Utilities
```
Command line parameters
-script filename Run python script on program start-up. The script can be defined with full path or placed in SB_PYTHON directory.
```
Example:
```
tbstartjob.exe -application "Drafting" -script myscript.py
-nosplash Disable displaying splash window on program start-up
```
Example:
```
tbstartjob.exe -application "Drafting" -nosplash
-minimize Run program in minimized state, it will be visible only in the task bar.
```
Example:
```
tbstartjob.exe -application "Drafting" -minimize
```
-scriptargs argument This will set command line arguments for all python scripts (including triggers) started from drafting-based applications.
```
To get the command line arguments in the Python script, argv from sys library should be used.
Use double-quotes if there are spaces or tabs in argument string.
One -scriptargs switch defines one item on Python argv list.
To define more than one arguments, a multiple use of this switch is allowed. First item on python argv list will always be name and path of started python script.
```
Examples:
```
tbstartjob -application "Drafting" -scripargs "c:\program files\note.txt"
sys.argv: ['c:\script1.py', 'c:\program files\note.txt']
tbstartjob -application "Drafting" -scriptargs argtext
sys.argv: ['c:\script1.py', 'argtext']
tbstartjob -application "Drafting" -scripargs argtext1 /scriptargs argtext2
sys.argv: ['c:\script1.py', 'argtext1', 'argtext2']
Copyright © 1993-2005 AVEVA AB
3.2 Customisable User Interface
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.2.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_gui. The functions are then referred to as kcs_gui.<function name>. Before
using a new function, please carefully read the function description.
Customisation of the graphical user interface of Drafting based applications is supported. This means that from within a Vitesse program it is possible to:
 Add new menus and menu items.
 Remove menus and menu items.
 Add new tool bars and tool bar buttons.
 Remove tool bar buttons.
 Modify the frame title.
In the function descriptions, parameters in italic means optional parameters. If omitted, a default value for that particular parameter is used instead.
All functions in the Vitesse GUI interface are designed to be used from the Initialize Drafting post-trigger. This trigger is fired in all Drafting based applications when the application hasstarted and has been initialized. All changes made in the post-trigger script will be available during the current session. To have the same changes applied to successive application
```
launches, the post-trigger code must be available, none of the changes are saved for later with one exception; the last location of new tool bars will be saved. However, if tool bars areadded or removed from the post-trigger, the tool bar state in the registry is no longer valid and will be ignored the first time. In this case a new tool bar state will be saved.
```
For more information about triggers, see Triggers.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.2.2 Exception Handling
The Vitesse GUI interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_gui.error. The exception is also displayed in the Vitesse Log window which is available by the
Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.2.3 Menu Function Ids and Tool bar Ids
Some of the functions in the following chapters use a function id or a tool bar id as parameter. Instead of documenting all these ids there is a special Vitesse script that lists all availableids for each application. The first time an application is started a Vitesse script named kcs_gui_<application>.py will be created in the Lib subdirectory of the directory defined by
SB_PYTHON environment variable.
This script contains Vitesse functions for all available Tribon functions and tool bars. When referring to any of these IDs in the Initialize Drafting trigger, either import this Vitesse script anduse the Vitesse function or use the number itself.
If the Vitesse script is deleted it will be regenerated by starting the application again.
```
Note: The names and IDs may change in future releases.
```
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.2.4 Menu Index
```
When the child window is maximized, the child window menu will appear as the left-most menu (with an icon instead of a string) in the main menu. This menu will always be ignored whenyou refer to a menu using a position. This means that the "File" menu will always have position 0 at the start of a program.
```
```
The right-most menus (the Tribon logo and the windows state menus: minimize, restore, and close) are also ignored.
```
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.2.5 User-defined Functions
When menu_item_usr_add or toolbar_button_usr_add is used to add a user-defined function, there are some rules to follow:
 Give the script name only, no path and no ".py" extension.
 The script file must be in one of the directories in the PYTHONPATH OS variable.
 When this script is executed, it is always the "run" function that is called. A sample script might look like below.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
import kcs_ui
```
def run():
```
```
kcs_ui.message_noconfirm("Hello")
```
Copyright © 1993-2005 AVEVA AB
3.2.6 Menu Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
menu_get(Menu, Position)
```
```
The function retrieves a menu object for later manipulation. Please note that the returned menu object is a temporary object that might be destroyed when the application has idle timein its event loop. This can typically happen when you show a dialog from Vitesse (e.g. kcs_ui.answer_req).
```
Input parameters:
Menu object If this is None, the main menu of the application is returned and Position is ignored.
```
If it is not None it must be a menu object returned from a menu_get() or a menu_add() call.
```
Position integer Specifies the position within Menu where the wanted pop-up menu is. This is a zero-based index.
Returned value:
[0] object The requested menu object.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_IndexError Invalid Position parameter.
kcs_MenuError Invalid Menu parameter.
kcs_RetrieveError Failed to retrieve the menu.
kcs_WindowError The main window has not been created yet.
```
menu_add(Menu, Position, Caption)
```
```
The function adds a pop-up menu to the application. Please note that the returned menu object is a temporary object that might be destroyed when the application has idle time in itsevent loop. This can typically happen when you show a dialog from Vitesse (e.g. kcs_ui.answer_req).
```
Input parameters:
```
Menu object Add the pop-up menu to this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the pop-up menu should be inserted. This is a zero-based index.
Caption string The caption of the pop-up menu. Must be at least one character long. If the character '&' is present in Caption it will be removed and the following character will beused as an accelerator.
Returned value:
[0] object The created menu object.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Invalid Caption parameter.
kcs_CreateError Failed to create the menu.
kcs_IndexError Invalid Position parameter.
kcs_InsertError Failed to insert the menu.
kcs_MenuError Invalid Menu parameter.
```
menu_item_get(Menu, Position)
```
The function returns information about the menu item.
Input parameters:
```
Menu object Get information from a menu item within this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the item is located. This is a zero-based index.
Returned value:
[0] string The caption of the menu item.
[1] integer The function id of the menu item.
-1 indicates a popup menu.
0 indicates a separator and [0] is invalid.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Failed to get the menu caption.
kcs_IndexError Invalid Position parameter.
kcs_MenuError Invalid Menu parameter.
```
menu_item_set(Menu, Position, Caption, Function)
```
The function modifies a menu item. If Position indicates a popup menu in Menu, Function is ignored and the Caption will be the new caption of the popup menu.
Input parameters:
```
Menu object Modify the menu item within this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the item is located. This is a zero-based index.
Caption string The caption of the menu item. Must be at least one character long unless Function is negative. If the character '&' is present in Caption it will be removed and thefollowing character will be used as an accelerator.
Function integer Specifies the id of the Tribon function. See separate chapter for available functions. If Function is negative a menu separator is added.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Invalid Caption parameter.
kcs_IndexError Invalid Position parameter.
kcs_MenuError Invalid Menu parameter.
kcs_ModifyError Failed to modify the menu item.
```
menu_item_std_add(Menu, Position, Caption, Function)
```
The function adds a menu item for a Tribon function to a menu.
Input parameters:
```
Menu object Add the menu item to this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the item will be located. This is a zero-based index.
Caption string The caption of the menu item. Must be at least one character long unless Function is negative. If the character '&' is present in Caption it will be removed and thefollowing character will be used as an accelerator.
Function integer Specifies the id of the Tribon function to insert. See separate chapter for available functions. If Function is negative a menu separator is added.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Invalid Caption parameter.
kcs_IndexError Invalid Position parameter.
kcs_InsertError Failed to insert the menu item.
kcs_MenuError Invalid Menu parameter.
```
menu_item_usr_add(Menu, Position, Caption, Script, Message)
```
The function adds a menu item for a user function to a menu.
Input parameters:
```
Menu object Add the menu item to this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the item will be located. This is a zero-based index.
Caption string The caption of the menu item. Must be at least one character long. If the character '&' is present in Caption it will be removed and the following character will beused as an accelerator.
Script string Specifies the name of a Vitesse script to call when this menu item is chosen. Path and extension must be omitted. The Vitesse script must be in a directory that isin PYTHONPATH. The name of the script must be at least one character long. For more information on this script see above.
Message string Specifies the help message displayed in the status bar when the menu item is highlighted.
Returned value:
[0] integer The function id of the added function.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Invalid Caption parameter.
kcs_IndexError Invalid Position parameter.
kcs_InsertError Failed to insert the menu item.
kcs_LimitError Maximum number of user-defined functions reached.
kcs_MenuError Invalid Menu parameter.
kcs_ValueError Invalid Script parameter.
```
menu_remove(Menu, Position)
```
The function removes a menu or menu item from the application.
Input parameters:
```
Menu object Remove the menu or menu item from this menu. This must be a menu object returned from either menu_get() or menu_add().
```
Position integer Specifies the position within Menu where the item is located. This is a zero-based index.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_IndexError Invalid Position parameter.
kcs_MenuError Invalid Menu parameter.
kcs_RemoveError Failed to remove the menu item.
```
Example:
```
# Example: kcs_ex_gui1.py
Copyright © 1993-2005 AVEVA AB
3.2.7 Tool bar Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
toolbar_get(Id)
```
The function retrieves a tool bar object for later manipulation.
Input parameters:
Id integer The id of the tool bar. See separate chapter for available ids.
Returned value:
[0] object The requested tool bar object.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_ValueError Invalid Id parameter.
```
toolbar_add(Caption)
```
The function adds a tool bar to the application. The first time the tool bar appears it will be placed in the top dock bar. Later application launches will fetch the position of the tool barfrom the tool bar state in the registry.
Input parameters:
Caption string The caption of the tool bar. This will be used in the "User Tool bars" menu and as a caption when the tool bar is floating.
Returned value:
[0] object The added tool bar object.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_CaptionError Invalid Caption parameter.
kcs_CreateError Failed to create the tool bar.
kcs_InsertError Failed to inserte the tool bar in the View/User Tool bars menu.
kcs_MenuCreateError Failed to create the View/User Tool bars menu.
kcs_RetrieveError Failed to retrieve the View/User Tool bars menu to add the tool bar.
```
toolbar_button_std_add(Toolbar, Position, Function, ImageFile, Tooltip, Message)
```
The function adds a button for a Tribon function to a tool bar.
Input parameters:
```
Toolbar object The tool bar to add a button to. This must be a tool bar object returned from either toolbar_get() or toolbar_add().
```
Position integer Specifies the position within Toolbar where the button should be inserted. This is a zero-based index.
Function integer Specifies the id of the Tribon function to insert. See separate chapter for available functions. If Function is negative a separator is added.
```
ImageFile string Specifies the name of a bitmap file (*.bmp) or an icon file (*.ico). The absolute path including directory and extension must be specified. If ImageFile is a bitmapfile, please use the menu system colour as background for the bitmap.
```
If ImageFile is omitted a standard button will be used.
Tooltip string Specifies the tool tip string for the button.
Message string Specifies the help message displayed in the status bar when the menu item is highlighted.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_ImageError Failed to handle the bitmap image.
kcs_IndexError Invalid Position parameter.
kcs_InsertError Failed to insert the button.
kcs_ToolbarError Invalid Toolbar object.
kcs_ValueError Invalid Function parameter.
```
toolbar_button_usr_add(Toolbar, Position, Script, ImageFile, Tooltip, Message)
```
The function adds a button for a user function to a tool bar.
Input parameters:
```
Toolbar object The tool bar to add a button to. This must be a tool bar object returned from either toolbar_get() or toolbar_add().
```
Position integer Specifies the position within Toolbar where the button should be inserted. This is a zero-based index.
Script string Specifies the name of a Vitesse script to call when the button is pressed. Path and extension must be omitted. The Vitesse script must be in a directory that is inPYTHONPATH.
```
ImageFile string Specifies the name of a bitmap file (*.bmp) or an icon file (*.ico). The absolute path including directory and extension must be specified. If ImageFile is a bitmapfile, please use the menu system colour as background for the bitmap.
```
Tooltip string Specifies the tool tip string for the button.
Message string Specifies the help message displayed in the status bar when the menu item is highlighted.
Returned value:
[0] integer The function id of the added function.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_ImageError Failed to handle the bitmap image.
kcs_IndexError Invalid Position parameter.
kcs_InsertError An error occurred when inserting the button.
kcs_LimitError Maximum number of user-defined functions reached.
kcs_ToolbarError Invalid Toolbar object.
kcs_ValueError Invalid Script, or Bitmap parameter.
```
toolbar_button_remove(Toolbar, Position)
```
The function removes a button from a tool bar.
Input parameters:
```
Toolbar object The tool bar to remove a button from. This must be a tool bar object returned from either toolbar_get() or toolbar_add().
```
Position integer Specifies the position within Toolbar from where the button should be removed. This is a zero-based index.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_DeleteError Failed to delete the button.
kcs_IndexError Invalid Position parameter.
kcs_ToolbarError Invalid Toolbar object.
```
Example:
```
# Example: kcs_ex_gui2.py
Copyright © 1993-2005 AVEVA AB
```
3.2.8 Main Window (Frame) Functions
```
User's Guide Vitesse
```
Chapter: Utilities
```
```
frame_title_set(Application, Format)
```
The function sets the frame title of the main window. The title will appear as <Format> - <Application>.
Input parameters:
Application string The name of the application.
Format string A format string describing how the left part of the title should look like. All characters in the format string will appear in the title with three exceptions:
```
 %o will be substituted with the current object (drawing) name.
```
 %p will be substituted with the current project name.
```
 %r will be substituted with the current drawing revision (TDM only).
```
```
 %s will be substituted with the current sub project name (if it exists).
```
```
 %v will be substituted with the current version (TDM only).
```
If Format is omitted an empty format string is used.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
```
Example:
```
# Example: kcs_ex_gui3.py
Copyright © 1993-2005 AVEVA AB
3.2.9 Accelerator Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
accelerator_add(Key, SystemKeys, Function)
```
```
The function sets Key (optionally in combination with SystemKeys) as an accelerator key for Function. Pressing this accelerator will invoke Function.
```
Input parameters:
Key string One of the following pre-defined strings:
RETURN
NUMPAD0-NUMPAD9
MULTIPLY
ADD
SUBTRACT
DIVIDE
DECIMAL
F2-F12
These strings represent the keys on the numerical keypad. Please note that F1 is not available. F1 is reserved for Help.
SystemKeys integer Which system keys that must be pressed together with Key.
0: None.
1: ALT must be pressed.
2: CTRL must be pressed.
4: SHIFT must be pressed.
```
To combine (require ALT and CTRL to be pressed), add the numbers above.
```
Function integer Specifies the id of the Tribon function to use. See separate chapter for available functions.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments to the function.
kcs_KeyError Invalid Key parameter.
kcs_SystemKeyError Invalid SystemKeys parameter.
```
Example:
```
# Example: kcs_ex_gui4.py
Copyright © 1993-2005 AVEVA AB
3.3 User-defined Attributes
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.3.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_att. The functions are then referred to as kcs_att.<function name>. Before using anew function, please carefully read the function description.
User-defined attributes makes it possible to store user specified data in the Tribon Product Information Model. Using the Tribon Toolkit Preference program, attribute templates can becreated. An attribute template describes what kind of data that is stored in an attribute. An attribute template can contain any number of the following:
 Integer number
 Real number
 String
 Date and time
 Reference to an external file
In the function descriptions, parameters in Italic means optional parameters. If omitted, a default value for that particular parameter is used instead.
Several of the functions described below uses a Target parameter. The target parameter should be one of the following:
 Model class indicates a model.
 None indicates current drawing.
 ElementHandle class indicates a drawing view.
For some model types it is allowed to attach user-defined attributes to both the model and parts within the model. In these cases, setting Model.PartId to zero indicates the model itself.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.3.2 Exception Handling
The Vitesse User Defined Attributes interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except"construct of the Python language. The type of error can then be examined by checking the value of kcs_att.error. The exception is also displayed in the Vitesse Log window which is
available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.3.3 Restrictions
Please note that user-defined attributes can not be attached to any other hull objects than plane panels and curved panels. For these two model types user-defined attributes can only beattached to the object head.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.3.4 Attribute Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
attribute_create(Target, Category, Template)
```
The function creates an attribute and attaches it to Target. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target SeeaboveIndicates where to attach the attribute.
Category string The name of the category to which the attribute template belongs.
Template string The name of the template.
Returned value:
[0] object The created attribute.
```
Exceptions:
```
kcs_AttachError Failed attaching the attribute.
kcs_AttributeError Failed creating the attribute.
kcs_CategoryError Could not find the category.
kcs_DatabaseError Could not find the Target in the database.
kcs_DrawingError No current drawing.
kcs_ListError Failed retrieving attribute list from Target.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
kcs_TemplateError Could not find the template.
kcs_ValueError Invalid Category or Template parameter.
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_copy(Target, Attribute)
```
The function copies an attribute and attaches the copy to Target. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target SeeaboveIndicates where to attach the attribute.
Attribute object The attribute to copy.
Returned value:
[0] object The copied attribute.
```
Exceptions:
```
kcs_AttachError Failed attaching the attribute.
kcs_AttributeError Invalid Attribute parameter.
kcs_CopyError Failed copying the attribute.
kcs_DatabaseError Could not find the Target in the database.
kcs_DrawingError No current drawing.
kcs_ListError Failed retrieving attribute list from Target.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_first_get(Target, Readonly, Iterator)
```
The function searches the model for user-defined attributes and returns the first found. If Readonly is 0 and Target is a Model it will be locked. In this case, model_save must be calledto release the lock.
Input parameters:
Target SeeaboveIndicates where to search for attributes.
Readonly integer 0: Target will be locked.
1: Target will not be locked.
Iterator integer An iterator index. The default value of this is 0. The only reason to use anything else than the default value is if more than oneattribute_first_get/attribute_next_get pair are active at the same time. Each such pair should have a unique iterator index.
The iterator index must be in the range 0-9.
Returned value:
[0] object The first user-defined attribute that belongs to Target. If no user-defined attributes exist in Target, None is returned. Please note that the returned object istemporary. This means that it should not be stored and no modelling functions should be used between retrieving the attribute and using it.
```
Exceptions:
```
kcs_DatabaseError Could not find the model in the database.
kcs_DrawingError No current drawing.
kcs_IteratorError Illegal iterator index.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_next_get(Iterator)
```
The function searches for the next user-defined attribute. Must be called after a call to attribute_first_get.
Input parameters:
Iterator integer An iterator index. The default value is zero. If this parameter is used, it must be the same as the iterator index used in the belonging call to attribute_first_get.
Returned value:
[0] object The next user-defined attribute that belongs to Target used in corresponding call to attribute_first_get. If no more user-defined attributes exist, None is returned.Please note that the returned object is temporary. This means that it should not be stored and no modelling functions should be used between retrieving the
attribute and using it.
```
Exceptions:
```
kcs_IteratorError Illegal iterator index.
kcs_ListError Failed retrieving attribute list from Target.
```
attribute_detach(Target, Attribute)
```
The function detaches a user-defined attribute from Target. Please note that a call to attribute_detach invalidates all iterators pointing to this attribute. If Target is a Model it will belocked. In this case, model_save must be called to release the lock.
Input parameters:
Target SeeaboveIndicates from where to detach the attribute.
Attribute object The user-defined attribute to detach.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_DrawingError No current drawing.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_edit(Target, Readonly)
```
The function displays a dialogue with all user-defined attributes belonging to Target and optionally lets the user edit them. If Readonly is 0 and Target is a Model it will be locked. In thiscase, model_save must be called to release the lock.
Input parameters:
Target SeeaboveIndicates where the attributes belong.
Readonly integer 0: Target will be locked.
```
1: Target will not be locked (default).
```
Returned value:
None.
```
Exceptions:
```
kcs_DatabaseError Could not find the model in the database.
kcs_DrawingError No current drawing.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_is(Attribute, Uuid)
```
The function checks if a user-defined attribute is of the given type.
Input parameters:
Attribute object The attribute to check.
Uuid string The uuid of the attribute template. Use one of the Python alias functions created by the Toolkit Preference application.
Returned value:
[0] integer 0: The attribute is not of the given type.
1: The attribute is of the given type.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_ValueError Invalid Category or Template parameter.
```
attribute_match(Target, Attribute, Convert)
```
The function checks if a user-defined attribute belonging to Target matches the template on the database. The attribute can be converted to the latest version of the template. All datawhere the title in the attribute matches the title in the template will be copied to the converted attribute. If Convert is larger than 0 and Target is a Model it will be locked. In this case,
model_save must be called to release the lock.
Input parameters:
Target SeeaboveIndicates where the attributes belong.
Attribute object The attribute to check.
```
Convert integer 0: Do not convert (default).
```
1: Convert the attribute so it matches the template.
2: Ask if the attribute should be converted.
Returned value:
[0] integer -2: The attribute matches the template, but one or more titles are different.
-1: The attribute matches the template but the UUIDs are different. This means that the template has been deleted and recreated using the same category andname.
0: The attribute does not match the template.
1: The attribute matches the template.
```
Exceptions:
```
kcs_AttributeError Failed creating the attribute.
kcs_CategoryError Could not find the category.
kcs_DatabaseError Could not find the model in the database.
kcs_DrawingError No current drawing.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
kcs_TemplateError Could not find the template.
```
kcs_ViewError Invalid ElementHandle parameter (Target).
```
```
attribute_title_get(Attribute)
```
The function returns the category and template titles of the attribute.
Input parameters:
Attribute object The attribute to get titles from.
Returned value:
[0] string The category title.
[1] string The template title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
model_save(Target)
```
```
Saves Target and releases the lock. Must be used if any of the following functions have been used on a Model object: attribute_create, attribute_copy, attribute_first_get (Readonly=0),attribute_detach, attribute_edit (Readonly=0), and attribute_match (Convert=1 or Convert=2).
```
Input parameters:
Target Model Indicates which Target to save.
Returned value:
[0] integer 0: Model not saved.
1: Model saved.
```
Exceptions:
```
kcs_AccessError Access denied to the model.
kcs_DatabaseError Could not find the model in the database.
kcs_InternalError Internal error.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
Example:
```
# Example: kcs_ex_att1.py
Copyright © 1993-2005 AVEVA AB
3.3.5 Integer Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
integer_count_get(Attribute)
```
The function returns the number of integers in the attribute.
Input parameters:
Attribute object The attribute.
Returned value:
[0] integer The number of integers.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
integer_get(Attribute, Index)
```
The function returns a given integer in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the integer. The first integer has index 0.
Returned value:
[0] integer The specified integer.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
integer_set(Target, Attribute, Index, Value)
```
The function sets a given integer in the attribute. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target See above Indicates where the attributes belong.
Attribute object The attribute.
Index integer The index of the integer. The first integer has index 0.
Value integer The integer value.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_IndexError Invalid Index parameter.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
integer_title_get(Attribute, Index)
```
The function returns the title of a given integer in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the integer. The first integer has index 0.
Returned value:
[0] string The title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
Example:
```
# Example: kcs_ex_att2.py
Copyright © 1993-2005 AVEVA AB
3.3.6 Real Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
real_count_get(Attribute)
```
The function returns the number of reals in the attribute.
Input parameters:
Attribute object The attribute.
Returned value:
[0] integer The number of reals.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
real_get(Attribute, Index)
```
The function returns a given real in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the real. The first real has index 0.
Returned value:
[0] real The specified real.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
real_set(Target, Attribute, Index, Value)
```
The function sets a given real in the attribute. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target See above Indicates where the attributes belong.
Attribute object The attribute.
Index integer The index of the real. The first real has index 0.
Value real The real value.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_IndexError Invalid Index parameter.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
real_title_get(Attribute, Index)
```
The function returns the title of a given real in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the real. The first real has index 0.
Returned value:
[0] string The title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
Example:
```
# Example: kcs_ex_att2.py
Copyright © 1993-2005 AVEVA AB
3.3.7 String Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
string_count_get(Attribute)
```
The function returns the number of strings in the attribute.
Input parameters:
Attribute object The attribute.
Returned value:
[0] integer The number of strings.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
string_get(Attribute, Index)
```
The function returns a given string in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the string. The first string has index 0.
Returned value:
[0] string The specified string.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
string_set(Target, Attribute, Index, Value)
```
The function sets a given string in the attribute. If Target is a Model it will be locked. In this case, model_save must be called to release the lock
Input parameters:
Target See above Indicates where the attributes belong.
Attribute object The attribute.
Index integer The index of the string. The first string has index 0.
Value string The string value.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_IndexError Invalid Index parameter.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
string_title_get(Attribute, Index)
```
The function returns the title of a given string in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the string. The first string has index 0.
Returned value:
[0] string The title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
Example:
```
# Example: kcs_ex_att2.py
Copyright © 1993-2005 AVEVA AB
3.3.8 Date Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
date_count_get(Attribute)
```
The function returns the number of dates in the attribute.
Input parameters:
Attribute object The attribute.
Returned value:
[0] integer The number of dates.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
date_get(Attribute, Index)
```
The function returns a given date in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the date. The first date has index 0.
Returned value:
[0] integer Number of seconds since midnight 1st of January 1970.
[1] integer Number of milliseconds.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
date_set(Target, Attribute, Index, Seconds, Milliseconds)
```
The function sets a given date in the attribute. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target See above Indicates where the attributes belong.
Attribute object The attribute.
Index integer The index of the date. The first date has index 0.
Seconds integer The number of seconds since midnight 1st January 1970. If Seconds is left out, the current date will be set.
Milliseconds integer The number of milliseconds. If Milliseconds is left out, zero will be used.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_IndexError Invalid Index parameter.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
date_title_get(Attribute, Index)
```
The function returns the title of a given date in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the date. The first date has index 0.
Returned value:
[0] string The title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
Example:
```
# Example: kcs_ex_att2.py
Copyright © 1993-2005 AVEVA AB
3.3.9 Reference Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
reference_count_get(Attribute)
```
The function returns the number of references in the attribute.
Input parameters:
Attribute object The attribute.
Returned value:
[0] integer The number of references.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
```
reference_get(Attribute, Index)
```
The function returns a given reference in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the reference. The first reference has index 0.
Returned value:
[0] string The specified reference.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
reference_set(Target, Attribute, Index, Value)
```
The function sets a given reference in the attribute. If Target is a Model it will be locked. In this case, model_save must be called to release the lock.
Input parameters:
Target See above Indicates where the attributes belong.
Attribute object The attribute.
Index integer The index of the reference. The first reference has index 0.
Value string The reference value.
Returned value:
None.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_DatabaseError Could not find the model in the database.
kcs_IndexError Invalid Index parameter.
kcs_LockError Target locked by another user.
```
kcs_ModelError Invalid Model parameter (Target).
```
```
reference_title_get(Attribute, Index)
```
The function returns the title of a given reference in the attribute.
Input parameters:
Attribute object The attribute.
Index integer The index of the reference. The first reference has index 0.
Returned value:
[0] string The title.
```
Exceptions:
```
kcs_AttributeError Invalid Attribute parameter.
kcs_IndexError Invalid Index parameter.
```
Example:
```
# Example: kcs_ex_att2.py
Copyright © 1993-2005 AVEVA AB
3.4 Databank Object List
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.4.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_db. The functions are then referred to as kcs_db.<function name>. Before using anew function, please carefully read the function description.
The Vitesse Databank interface contains functions for:
 Listing of objects in a databank
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.4.2 Exception Handling
The Vitesse Databank interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct ofthe Python language. The type of error can then be examined by checking the value of kcs_db.error. The exception is also displayed in the Vitesse Log window which is available by
the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.4.3 List Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
object_list_get(objectCriteria, databankName, resultList)
```
The function returns list of objects matching given criteria from specified indexed data bank.
Input Parameters:
objectCriteria ObjectCriteria Instance of python ObjectCriteria class specifying objects selection criteria.
databankName string Data bank file path. Logical name can be used.
Output Parameters:
resultList python list Result list.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_CouldNotOpenDatabank Data bank file could not be open.
kcs_DatabankReadError Error during data reading.
Example
# Example: kcs_ex_db01.py
Copyright © 1993-2005 AVEVA AB
3.5 Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.5.1 General
Triggers are connected to events in the Tribon system that activates Python scripts. Each trigger is a Python file having a predefined name. Further down in this documentation there is alist of all events and their corresponding trigger file name. The Tribon Environment Variable SBB_TRIGDIR should be set up to point to the directory where the trigger are located. In a
default installation, this variable points to the /Vitesse/Trigger directory below the Tribon installation root directory.
```
Note: The SBB_TRIGDIR and the some of the triggers are used by standard Tribon functionality. User additions can be done to these trigger files, but the existing implementationshould be left intact for the Tribon standard functionality to work properly. See documentation for each trigger for further information. Please also note that in order to minimise migration
```
work in connection with installation of new Tribon releases, user added functionality in the trigger file should only include a call to another module. Then the actual implementation of thetrigger functionality should be in the other module. This will make it easy to just introduce the user function call into a new Tribon release of the trigger.
```
The trigger file should include two functions, pre() and post(). The pre() function is called before the Tribon event is performed, and the post() function is called after the Tribon event.
```
```
Triggers are implemented in such a way that only interactive events will result in a trigger call. For example, the interactive File-Open will initiate a call to the trig_draft_dwg_new trigger,while using the kcs_draft.dwg_new() Vitesse function will not activate any trigger. If the processing of the Interactive Event fails or is interrupted by the user, the Post Trigger will never be
```
called.
For trigger functions that should return values other than the result, a list should be used. The first element of the list should be the trigger result.
There is a possibility for a trigger to control the execution of the Tribon event by means of a number of predefined return codes. These codes can be obtained using the kcs_util.trigger*functions. If an unknown return code is issued or if the Python interpretation fails for a Pre-trigger, the Tribon event will be interrupted.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
# trig_draft_insert_model_filter.py
import kcs_att
import kcs_util
import KcsModel
```
def pre(*args):
```
```
list = []
```
```
for i in range(len(args[0])):
```
```
att = kcs_att.attribute_get_first(args[0][i])
```
if att != None:
```
list.append(args[0][i])
```
```
result = []
```
```
result.append(kcs_util.trigger_ok())
```
```
result.append(list)
```
return result
Copyright © 1993-2005 AVEVA AB
3.5.2 Drafting Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Equipment move pre-trigger
```
Event: Tools / Equipment / Move
```
```
Type: Pre
```
File name: trig_draft_equip_move
Input Parameters: None
Allowed return: Standard for Pre-Trigger
```
Note: This trigger fires before user will be indicated to select equipment to move.
```
Equipment move post-trigger
```
Event: Tools / Equipment / Move
```
```
Type: Post
```
```
File name: trig_draft_equip_move(equipname)
```
Input Parameters: Name Type Description
equipname string equipment name
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if selected equipment will be moved successfully.
```
Init Drafting Pre-Trigger
```
Event: Every time a Drafting based program is started.
```
```
Type: Pre
```
```
Name: trig_draft_init
```
Input Parameters: None
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality: None.
```
Notes: None.
```
Init Drafting Post-Trigger
```
Event: Every time a Drafting based program is started.
```
```
Type: Post
```
```
Name: trig_draft_init
```
Input Parameters: None
```
Allowed returnvalues:kcs_util.trigger_ok()
```
```
Overridefunctionality:None.
```
```
Notes: This trigger is used by some of the Tribon standard functionality. User additions can be done to this triggers, but the existing implementation should be left intactfor the Tribon standard functionality to work properly.
```
The Vitesse API kcs_gui is designed to be used within this trigger.
See kcs_ex_gui1.py, kcs_ex_gui2.py, and kcs_ex_gui3.py for examples.
New drawing pre-trigger
```
Event: File / New
```
```
Type: Pre
```
File name: trig_draft_dwg_new
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be prompted to indicate name of the drawing frame.
```
New drawing post-trigger
```
Event: File / New
```
```
Type: Post
```
File name: trig_draft_dwg_new
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger only executes after new drawing has been successfully created. If an error occurs during creation, the trigger will not be executed.
```
Open drawing pre-trigger
```
Event: File / Open
```
```
Type: Pre
```
File name: trig_draft_dwg_open
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be prompted to indicate name of the drawing to open.
```
Open drawing post-trigger
```
Event: File / Open
```
```
Type: Post
```
File name: trig_draft_dwg_open
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger only executes after drawing has been successfully opened. If an error occurs during opening, the trigger will not be executed.
```
Close drawing pre-trigger
```
Event: File / Close
```
```
Type: Pre
```
File name: trig_draft_dwg_open
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before drawing will be close.
```
Close drawing post-trigger
```
Event: File / Close
```
```
Type: Post
```
File name: trig_draft_dwg_close
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger only executes after drawing has been successfully closed. If an error occurs during closing, the trigger will not be executed.
```
Save drawing pre-trigger
```
Event: File / Save
```
```
Type: Pre
```
File name: trig_draft_dwg_save
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before drawing will be save.
```
Save drawing post-trigger
```
Event: File / Save
```
```
Type: Post
```
File name: trig_draft_dwg_save
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger only executes after drawing has been successfully saved. If an error occurs during saving, the trigger will not be executed.
```
Save As drawing pre-trigger
```
Event: File / Save As
```
```
Type: Pre
```
File name: trig_draft_dwg_save_as
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before drawing will be save.
```
Save As drawing post-trigger
```
Event: File / Save As
```
```
Type: Post
```
File name: trig_draft_dwg_save_as
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger only executes after drawing has been successfully saved. If an error occurs during saving, the trigger will not be executed.
```
Print drawing pre-trigger
```
Event: File / Print
```
```
Type: Pre
```
File name: trig_draft_dwg_print
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before drawing will be print.
```
Print drawing post-trigger
```
Event: File / Print
```
```
Type: Post
```
File name: trig_draft_dwg_print
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if the interactive command is completed without errors.
```
Insert Model pre-trigger
```
Event: Insert / Model
```
```
Type: Pre
```
File name: trig_draft_insert_model
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select model.
```
Insert Model post-trigger
```
Event: Insert / Model
```
```
Type: Post
```
File name: trig_draft_insert_model
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if the insertion of model will end with success.
```
Model Info pre-trigger
```
Event: Tools / Inquiry / Model
```
```
Type: Pre
```
File name: trig_draft_model_info
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select model.
```
Model Info post-trigger
```
Event: Tools / Inquiry / Model
```
```
Type: Post
```
File name: trig_draft_model_info
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if the model info will be obtained successfully.
```
Model Info property edit pre-trigger
```
Event: Tools / Inquiry / Model / Edit
```
```
Type: Pre
```
File name: trig_draft_property_edit
Input Parameters: Name Type Description
Model object Model Model information
Value string First value
Value string Last value
```
Allowed return values: kcs_util.trigger_ok()
```
```
Note: This trigger will be fired when the Edit function is selected in the dialogue.
```
Verify drawing pre-trigger
```
Event: Tools / Inquiry / Verify
```
```
Type: Pre
```
File name: trig_draft_dwg_verify
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select geometry.
```
Verify drawing post-trigger
```
Event: Tools / Inquiry / Verify
```
```
Type: Post
```
File name: trig_draft_dwg_verify
Input Parameters: None
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if the geometry info will be obtained successfully.
```
Equipment place pre-trigger
```
Event: Tools / Equipment / Place
```
```
Type: Pre
```
File name: trig_draft_equip_place
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select equipment to place.
```
Equipment place post-trigger
```
Event: Tools / Equipment / Place
```
```
Type: Post
```
```
File name: trig_draft_equip_place(equipname)
```
Input Parameters: Name Type Description
equipname string equipment name
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if selected equipment will be placed successfully.
```
Equipment delete pre-trigger
```
Event: Tools / Equipment / Delete
```
```
Type: Pre
```
File name: trig_draft_equip_delete
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select equipment to delete.
```
Equipment delete post-trigger
```
Event: Tools / Equipment / Delete
```
```
Type: Post
```
```
File name: trig_draft_equip_delete(equipname)
```
Input Parameters: Name Type Description
equipname string equipment name
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if selected equipment will be deleted successfully.
```
Equipment ready pre-trigger
```
Event: Tools / Equipment / Ready
```
```
Type: Pre
```
File name: trig_draft_equip_ready
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard input model function will not be performed.
```
```
Note: This trigger fires before user will be indicated to select equipment to mark as ready.
```
Equipment ready post-trigger
```
Event: Tools / Equipment / Ready
```
```
Type: Post
```
```
File name: trig_draft_equip_ready(equipname)
```
Input Parameters: Name Type Description
equipname string equipment name
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if selected equipment will be successfully marked as ready.
```
Insert Model Filter Pre-Trigger
```
Event: When the user clicks the "Filter" button in the Insert/Model dialogue.
```
```
Type: Pre
```
Name trig_draft_insert_model_filter
Input Parameters: Name Type Description
Model object Model First model information
Model object Model Last model information
Allowed return values: Name Type Description
```
kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
```
If kcs_util.trigger_ok(), a number of model classes could also be returned (see below).
```
Model objects List of Models Python list of all models to be included.
Override functionality: None.
```
Note: See kcs_ex_att3.py for an example.
```
Popup menu pre-trigger
```
Event: Ctrl + Right Click in Drawing or Drawing Tree
```
```
Type: Pre
```
File name: trig_draft_popup_menu
Input Parameters: Name Type Description
Model/Element KcsModel/KcsElementHandleEither a ModelClass or Element handle, depending on if the user has indicated a model item or other geometry
Point KcsPoint2D Point2D position in drawing
Allowed return values: Standard for Pre-Trigger
Override functionality: None.
```
Note: Can for instance be used to create a pop-up or context menu by using kcs_gui.
```
Copyright © 1993-2005 AVEVA AB
3.5.3 Pipe Modelling Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Pipe PipeGroup Rename Pre-trigger
```
Event: Pipe / Pipe group / Rename
```
```
Type: Pre
```
File name: trig_pipe_pipegroup_rename.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe / Pipe group / Rename function will be performed.
```
```
Note: The trigger is called before any interaction
```
Pipe PipeGroup Rename Post-trigger
```
Event: Pipe / Pipe group / Rename
```
```
Type: Post
```
File name: trig_pipe_pipegroup_rename.py
Input Parameters: Name Type Length Description
OldModule String 256 Pipe module
OldSubsystem String 256 Pipe subsystem
NewModule String 256 Pipe module
NewSubsystem String 256 Pipe subsystem
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Pipe PipeGroup Duplicate Pre-trigger
```
Event: Pipe / Pipe group / Duplicate
```
```
Type: Pre
```
File name: trig_pipe_pipegroup_duplicate.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe / Pipe group / Duplicate function will be performed.
```
```
Note: The trigger is called before any interaction
```
Pipe PipeGroup Duplicate Post-trigger
```
Event: Pipe / Pipe group / Duplicate
```
```
Type: Post
```
File name: trig_pipe_pipegroup_duplicate.py
Input Parameters: Name Type Length Description
OldModule String 256 Pipe module
OldSubsystem String 256 Pipe subsystem
NewModule String 256 Pipe module
NewSubsystem String 256 Pipe subsystem
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeProduction PipeInfo Update Pre-trigger
```
Event: Pipe Production / Pipe info / Update
```
```
Type: Pre
```
File name: trig_pipe_pipeinfo_update.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Production / Pipe info / Update function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeProduction PipeInfo Update Post-trigger
```
Event: Pipe Production / Pipe info / Update
```
```
Type: Post
```
File name: trig_pipe_pipeinfo_update.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeProduction SpoolInfo Update Pre-trigger
```
Event: Pipe Production / Spool info / Update
```
```
Type: Pre
```
File name: trig_pipe_spoolinfo_update.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Production / Spool info / Update function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeProduction SpoolInfo Update Post-trigger
```
Event: Pipe Production / Spool info / Update
```
```
Type: Post
```
File name: trig_pipe_spoolinfo_update.py
Input Parameters: Name Type Length Description
PosNo String 256 Position name
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeProduction SpoolInfo Delete Pre-trigger
```
Event: Pipe Production / Spool info / Delete
```
```
Type: Pre
```
File name: trig_pipe_spoolinfo_delete.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Production / Spool info / Delete function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeProduction SpoolInfo Delete Post-trigger
```
Event: Pipe Production / Spool info / Delete
```
```
Type: Post
```
File name: trig_pipe_spoolinfo_delete.py
Input Parameters: Name Type Length Description
PosNo String 256 Position name
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeProduction PartInfo Update Pre-trigger
```
Event: Pipe Production / Part info / Update
```
```
Type: Pre
```
File name: trig_pipe_partinfo_update.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Production / Part info / Update function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeProduction PartInfo Update Post-trigger
```
Event: Pipe Production / Part info / Update
```
```
Type: Post
```
File name: trig_pipe_partinfo_update.py
Input Parameters: Name Type Length Description
Id Integer 31 Part id
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeModel Material FrameToPipe Pre-trigger
```
Event: Pipe Model / Material / Frame to pipe
```
```
Type: Pre
```
File name: trig_pipe_material_frametopipe.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Model / Material / Frame to pipe function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeModel Material FrameToPipe Post-trigger
```
Event: Pipe Model / Material / Frame to pipe
```
```
Type: Post
```
File name: trig_pipe_material_frametopipe.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
PipeModel Material SubstituteBend Pre-trigger
```
Event: Pipe Model / Material / Subst Bend
```
```
Type: Pre
```
File name: trig_pipe_subst_bend.py
Input Parameters: Name Type Length Description
ComponentName String 256 Component name for the bend to insert
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe Model / Material / Frame to pipe function will be performed.
```
```
Note: The trigger is called after the user have selected component for the bend to insert.
```
PipeModel Material SubstituteBend Post-trigger
```
Event: Pipe Model / Material / Subst Bend
```
```
Type: Post
```
File name: trig_pipe_subst_bend.py
Input Parameters: Name Type Length Description
ComponentName String 256 Component name for the inserted bend
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Pipe New Pre-trigger
```
Event: Pipe / New
```
```
Type: Pre
```
File name: trig_pipe_new.py
Input Parameters: Name Type Length Description
PipeName String 256 The name of the pipe that the user has given in the dialog
ComponentName String 256 The name of the component that the user has given in the dialog
SubType Integer 31 The selected subtype by the user
Colour Integer 31 The selected colour by the user
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe / New funtion will be performed.
```
```
Note:
```
Pipe New Post-trigger
```
Event: Pipe / New
```
```
Type: Post
```
File name: trig_pipe_new.py
Input Parameters: Name Type Length Description
PipeName String 256 The name of the created pipe
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Pipe ready pre-trigger
```
Event: Pipe / Ready
```
```
Type: Pre
```
File name: trig_pipe_ready
Input Parameters: None
Allowed return values: Standard for Pre-Trigger
```
Note: This trigger fires befor user will be indicated to select equipment to mark asready
```
Pipe ready post-trigger
```
Event: Pipe / Ready
```
```
Type: Post
```
```
File name: trig_pipe_ready(pipename)
```
Input Parameters: Name Type Description
pipename string pipe name
Allowed return values: Standard for Post-Trigger
```
Note: This trigger will be executed if selected eqipment will be successfully marked as ready.
```
Copyright © 1993-2005 AVEVA AB
3.5.4 Cable Modelling Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
CableWay Group Rename Pre-trigger
```
Event: Cable Way / Group / Rename
```
```
Type: Pre
```
File name: trig_cable_cway_rename.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Cable Way / Group / Rename function will be performed.
```
```
Note: The trigger is called before any interaction
```
CableWay Group Rename Post-trigger
```
Event: Cable Way / Group / Rename
```
```
Type: Post
```
File name: trig_cable_cway_rename.py
Input Parameters: Name Type Length Description
```
OldName String 256 Cable way name (without project name)
```
```
NewName String 256 Cable way name (without project name)
```
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
CableWay Group Duplicate Pre-trigger
```
Event: Cable Way / Group / Duplicate
```
```
Type: Pre
```
File name: trig_cable_cway_duplicate.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Cable Way / Group / Duplicate function will be performed.
```
```
Note: The trigger is called before any interaction
```
CableWay Group Duplicate Post-trigger
```
Event: Cable Way / Group / Duplicate
```
```
Type: Post
```
File name: trig_cable_cway_duplicate.py
Input Parameters: Name Type Length Description
```
OriginName String 256 Cable way name (without project name)
```
```
NewName String 256 Cable way name (without project name)
```
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cable Route Pre-trigger
```
Event: Cable / Route / Manual
```
Cable / Route / Automatic
Cable / Route / Intermediate
Cable / Route / Copy other route
Cable / Route / Background
```
Type: Pre
```
File name: trig_cable_cable_route.py
Input Parameters: Name Type Length Description
SystemName String 256 System name
CableName String 256 Cable name
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard events for this trigger will be performed.
```
```
Note: The trigger is called before any interaction
```
Cable Route Post-trigger
```
Event: Cable / Route / Manual
```
Cable / Route / Automatic
Cable / Route / Intermediate
Cable / Route / Copy other route
Cable / Route / Background
```
Type: Post
```
File name: trig_cable_cable_route.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cableway New Pre-trigger
```
Event: Cableway / New
```
```
Type: Pre
```
File name: trig_cable_cway_new.py
Input Parameters: Cableway name as given by user
Allowed return values: Standard for pre-trigger.
```
Note: See example kcs_ex_trig_cable_cway_new.py
```
Cableway New Post-trigger
```
Event: Cableway / New
```
```
Type: Post
```
File name: trig_cable_cway_new.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cableway Rename Pre-trigger
```
Event: Cableway / Rename
```
```
Type: Pre
```
File name: trig_cable_cway_rename.py
Input Parameters: New cableway name as given by user
Allowed return values: Standard for pre-trigger.
```
Note: See example kcs_ex_trig_cable_cway_rename.py
```
Cableway Rename Post-trigger
```
Event: Cableway / Rename
```
```
Type: Post
```
File name: trig_cable_cway_rename.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cableway Material Straight Pre-trigger
```
Event: Cableway / Material / Straight part
```
```
Type: Pre
```
File name: trig_cable_cway_comp_straight.py
Input Parameters: Component name as given by user
Allowed return values: Standard for pre-trigger.
```
Note: See example kcs_ex_trig_cable_cway_comp_straight.py
```
Cableway Material Straight Post-trigger
```
Event: Cableway / Material / Straight part
```
```
Type: Post
```
File name: trig_cable_cway_comp_straight.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cableway Material Bent Pre-trigger
```
Event: Cableway / Material / Bent part
```
```
Type: Pre
```
File name: trig_cable_cway_comp_bent.py
Input Parameters: Component name as given by user
Allowed return values: Standard for pre-trigger.
```
Note: See example kcs_ex_trig_cable_cway_comp_bent.py
```
Cableway Material Bent Post-trigger
```
Event: Cableway / Material / Bent part
```
```
Type: Post
```
File name: trig_cable_cway_comp_bent.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Cableway Material Intermediate Pre-trigger
```
Event: Cableway / Material / Intermediate part
```
```
Type: Pre
```
File name: trig_cable_cway_comp_intermediate.py
Input Parameters: Component name as given by user
Allowed return values: Standard for pre-trigger.
```
Note: See example kcs_ex_trig_cable_cway_comp_intermediate.py
```
Cableway Material Intermediate Post-trigger
```
Event: Cableway / Material / Intermediate part
```
```
Type: Post
```
File name: trig_cable_cway_comp_intermediate.py
Input Parameters: None
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Copyright © 1993-2005 AVEVA AB
3.5.5 Structure Modelling Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Structure Group Duplicate Pre-trigger
```
Event: Structure / Group / Duplicate
```
```
Type: Pre
```
File name: trig_struct_group_duplicate.py
Input Parameters: None
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Structure / Group / Duplicate function will be performed.
```
```
Note: The trigger is called before any interaction
```
Structure Group Duplicate Post-trigger
```
Event: Structure / Group / Duplicate
```
```
Type: Post
```
File name: trig_struct_group_duplicate.py
Input Parameters: Name Type Length Description
```
OriginName String 256 Structure name (without project name)
```
```
NewName String 256 Structure name (without project name)
```
Allowed returnvalues:Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned from the pre-
```
trigger.
Copyright © 1993-2005 AVEVA AB
3.5.6 Pipe Support Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
PipeSupport Save for New Pre-trigger
```
Event: Pipe support / Save
```
```
Type: Pre
```
File name: trig_struct_pipesupport_new_save.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for pre-trigger.
```
Note: The trigger is called before any interaction
```
PipeSupport Save for New Post-trigger
```
Event: Pipe support / Save
```
```
Type: Post
```
File name: trig_struct_pipesupport_new_save.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
PipeSupport Save for Add Pre-trigger
```
Event: Pipe support / Save
```
```
Type: Pre
```
File name: trig_struct_pipesupport_add_save.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for pre-trigger.
```
Note: The trigger is called before any interaction
```
PipeSupport Save for Add Post-trigger
```
Event: Pipe support / Save
```
```
Type: Post
```
File name: trig_struct_pipesupport_add_save.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
PipeSupport Delete for Model Pre-trigger
```
Event: Pipe support / Delete
```
```
Type: Pre
```
File name: trig_struct_pipesupport_mod_del.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for pre-trigger.
```
Note: The trigger is called before any interaction
```
PipeSupport Delete for Model Post-trigger
```
Event: Pipe support / Delete
```
```
Type: Post
```
File name: trig_struct_pipesupport_mod_del.py
Input Parameters: Name Type Length Description
SupportName String 256 Name of the Support
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
PipeSupport Delete for Part Pre-trigger
```
Event: Pipe support / Delete
```
```
Type: Pre
```
File name: trig_struct_pipesupport_part_del.py
Input Parameters: Name Type Length Description
Name String 256 Name of the part
Id int ID of part to be deleted
Allowed return values: Standard for pre-trigger.
```
Note: The trigger is called before any interaction
```
PipeSupport Delete for Part Post-trigger
```
Event: Pipe support / Delete
```
```
Type: Post
```
File name: trig_struct_pipesupport_part_del.py
Input Parameters: Name Type Length Description
Name String 256 Name of the part
Id int ID of part to be deleted
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
PipeSupport Rename for Model Pre-trigger
```
Event: Pipe support / Rename
```
```
Type: Pre
```
File name: trig_struct_pipesupport_mod_ren.py
Input Parameters: Name Type Length Description
OldName String 256 Old Name of the Support
NewName String 256 New Name of the Support
Allowed return values: Standard for pre-trigger.
```
Note: The trigger is called before any interaction
```
PipeSupport Rename for Model Post-trigger
```
Event: Pipe support / Rename
```
```
Type: Post
```
File name: trig_struct_pipesupport_mod_ren.py
Input Parameters: Name Type Length Description
OldName String 256 Old Name of the Support
NewName String 256 New Name of the Support
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
PipeSupport Rename for Part Pre-trigger
```
Event: Pipe support / Rename
```
```
Type: Pre
```
File name: trig_struct_pipesupport_part_ren.py
Input Parameters: Name Type Length Description
Id int ID of the part
OldName String 256 Old Name of the part
NewName String 256 New Name of the part
Allowed return values: Standard for pre-trigger.
```
Override functionality: If kcs_util.trigger_override() is returned, no part of the standard Pipe support / Rename function will be performed.
```
```
Note: The trigger is called before any interaction
```
PipeSupport Rename for Part Post-trigger
```
Event: Pipe support / Rename
```
```
Type: Post
```
File name: trig_struct_pipesupport_part_ren.py
Input Parameters: Name Type Length Description
Id int ID of the part
OldName String 256 Old Name of the part
NewName String 256 New Name of the part
Allowed return values: Standard for post-trigger.
```
Note: The trigger will only be executed if the interactive command is completed without errors and if kcs_util.trigger_override() is not returned.
```
Copyright © 1993-2005 AVEVA AB
3.5.7 Tribon Data Management Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Change status Pre-trigger
```
Event: Tools / Data Management / Change Status (Drafting)
```
```
Change Status (Design Manager)
```
```
Type: Pre
```
File name: trig_tdm_status_change
Input Parameters: Name Type Description
Model object Model Model information
Type integer Status type
1: Design
2: Manufacturing
3: Assembly
4: Material control
Current integer Current status
New integer New status
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
```
Note: The trigger is fired for every object prior to changing status.
```
Change status Post-trigger
```
Event: Tools / Data Management / Change Status (Drafting)
```
```
Popup / Change Status (Design Manager)
```
```
Type: Post
```
File name: trig_tdm_status_change
Input Parameters: Name Type Description
Model object Model Model information
Type integer Status type
1: Design
2: Manufacturing
3: Assembly
4: Material control
Old integer Old status
Current integer Current status
Allowed return values: Standard for post-trigger.
```
Note: The trigger is fired for every object after the status has been changed.
```
Create Vitesse reference Pre-trigger
```
Event: Tools / Data Management / Attributes / Document references / New Vitesse Reference (Drafting)
```
```
Popup / Attributes / Document references / New Vitesse Reference (Design Manager)
```
```
Type: Pre
```
File name: trig_tdm_vitesse_ref_new
Input Parameters: Name Type Description
Model object Model Model information
Allowed return values: Name Type Description
```
kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
```
If kcs_util.trigger_ok(), the following should also be returned.
```
Type integer The user-defined type to distinguish it from other Vitesse references.
Name string The name of the reference.
Description string The description of the Vitesse reference.
```
Note: A Vitesse reference is created if kcs_util.trigger_ok() is returned.
```
Open Vitesse reference Pre-trigger
```
Event: Tools / Data Management / Attributes / Document references / Open (Drafting)
```
```
Popup / Attributes / Document references / New Vitesse Reference (Design Manager)
```
```
Popup / Open (Vitesse reference node, Design Manager)
```
```
Type: Pre
```
File name: trig_tdm_vitesse_ref_open
Input Parameters: Name Type Description
Model object Model Model information
Type integer The user-defined type to distinguish it from other Vitesse references.
Name string The name of the reference.
Description string The description of the Vitesse reference.
Allowed return values: Standard for pre-trigger.
```
Note:
```
Copyright © 1993-2005 AVEVA AB
3.5.8 Tribon Design Manager Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Filter Active Pre-trigger
```
Event: When user ticks "Enable Customizable Filter" in the Scene Properties dialog.
```
```
Type: Pre.
```
File name: trig_dm_activate_model_filter
Input Parameters: None.
Allowed return Name values: Type Description
```
kcs_util.trigger_ok() If kcs_util.trigger_ok(), a filter name could also be returned (see below).
```
```
kcs_util.trigger_abort() String Optional. Name of filter set as current filter.
```
```
Overridefunctionality:None.
```
```
Note: This trigger can e.g. include a user dialogue for filter definition, or select a filter among a set predefined filters and let it be current filter for later drag & dropoperations. Current filter is indicated in a separate field in the bottom frame of Design Manager.
```
Drag & drop filter Pre-trigger
```
Event: When user performs a drag & drop operation from the product model tree to the model graphics display. Executed only one time per drag & drop operation.
```
```
Type: Pre
```
```
Name: trig_dm_drop_model_filter
```
```
InputParameters:Name Type Description
```
```
Model Object Model Optional. Node in product model tree from where the drag & drop operation starts. In case the selected node is not a named object but afolder like e.g. "Plane Panels" a complementary Model parameter is given holding the parent Model node in tree (see below). The
```
argument may not exist at all in case an invalid node is selected, i.e. a node not representing a model object e.g. drawing referencesetc.
```
Parent Model Object Model Optional. Complementary Model (see above).
```
Filter name String Required. Name of current filter.
Allowed returnvalues:Name. Type. Description.
```
kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
```
If kcs_util.trigger_ok(), a filter name could also be returned (see below).
```
Filter name. String Optional. Changed name of filter set as current filter.
OverridefunctionalityNone.
```
Note: This trigger is invoked only if filter is ON which is indicated in separate field in the bottom frame of Design Manager. Filter is switched ON/OFF by the Filter Activefunction. This trigger could also be used to define or select a filter. If a filter name is returned by this function, this will override the filter name returned from the trigger
```
trig_dm_activate_model_filter
Drag & drop filter Post-Trigger
```
Event: When user performs a drag & drop operation from the product model tree to the model graphics display. Executed for each node included in a drag & dropoperation.
```
```
Type: Post.
```
File name: trig_dm_drop_model_filter.
Input Parameters: Name Type Description
Model object Model Required. Current Model node processed.
Filter name. String Required. Name of current filter.
Allowed returnvalues:Name Type Description
```
kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
```
kcs_util.trigger_ok(), if Model should be included in the drop.
```
Colour String The name of the colour, see KcsColourClass.
Overridefunctionality.None.
```
Note: This trigger is invoked only if filter is ON which is indicated in separate field in the bottom frame of Design Manager. Filter is switched ON/OFF by the Filter Activefunction.
```
Parts List Pre-Trigger
```
Event: Parts List to Vitesse function from the Parts List window in Design Manager. The purpose by the pre-trigger is to make KcsModel(s) of the parts enumerated in theparts list window and to make them available for a processing in batch mode. For more information see the Parts List to Vitesse function and the example script
```
included in the installation.
```
Type: Pre.
```
File name: trig_dm_parts_list.
```
InputParameters:Name Type Description
```
```
Model Object(s) Model Model objects representing the parts in the Parts List Window.
```
Allowed returnvalues:Standard for Pre-Trigger
Parts List Post-Trigger
```
Event: Parts List to Vitesse function from the Parts List window in Design Manager. Invoked by a drafting process running in batch mode. For more information see theParts List to Vitesse function and the example script included in the installation.
```
```
Type: Post.
```
File name: trig_dm_parts_list
Input Parameters: None.
Allowed returnvalues:Standard for Pre-Trigger
```
Note: Following lines are required to get a batch process of Drafting to execute the post-trigger properly.
```
```
## Start of main body if __name__ == '__main__': post()
```
Copyright © 1993-2005 AVEVA AB
3.5.9 Hull Planar Modelling Triggers
User's Guide Vitesse
```
Chapter: Utilities
```
Panel store pre-trigger
```
Event: Storing of panel.
```
```
Type: Pre.
```
```
File name: trig_hull_ppan_store (panelname)
```
Input Parameters: Name Type Description
Panelname String Name of panel to store.
Allowed return values: Standard for Pre-Trigger.
```
Override functionality. If kcs_util.trigger_override() is returned the panel will not be stored.
```
```
Note: This trigger fires before storing a panel.
```
Panel store post-trigger
```
Event: Storing of panel.
```
```
Type: Post.
```
```
File name: trig_hull_ppan_store (panelname)
```
Input Parameters: Name Type Description
Panelname String Name of panel to store.
Allowed return values: Standard for Post-Trigger.
```
Note: This trigger fires after storing a panel.
```
Copyright © 1993-2005 AVEVA AB
3.5.10 Examples
The example file kcs_ex_trig01.py contains a generic trigger example that can be used to verify the operation of a trigger. To enable this onto a certain trigger, please copy the file to thename of the trigger, e.g. trig_draft_dwg_new.py. Using this sample, it is possible to see input arguments and specify return values and result codes in an easy and interactive way.
```
Note: The trigger example files are located under the \Vitesse\Trigger directory below the Tribon installation root directory. The reason that they are not in the \Vitesse\Examplesdirectory together with the rest of the example files is that the SBB_TRIGDIR variable by default points to the \Vitesse\Trigger directory. This makes it easy to enable the trigger
```
samples by just copying or changing the name of the file in its current location.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.5.11 Registering trigger functions
It is possible to register triggers dynamically instead of using external trigger files. The main advantages are:
 Registering/unregistering can be done dynamically during execution of user application.
 All needed triggers can be defined in one python module.
When using dynamic registration it is necessary to have a callable object defined. This object will be called when the trigger is invoked. A callable object means here a function name thatis defined by the user. It is recommended to register all the triggers at user application startup and unregister them before the application is terminated.
Tribon provides three functions in kcs_util module for supporting dynamic triggers. See detailed description and example below.
User's Guide Vitesse
```
Chapter: Utilities
```
```
register_trigger(name, type, function)
```
This function registers new user trigger. It is only possible to register triggers that don't return any other additional values than return code. See General in Triggers chapter.
Input Parameters:
Name string Name of trigger. The same name as used for trigger file. See General in Triggers chapter.
type constant kcs_util.kcsPOST_TRIGGER or kcs_util.kcsPRE_TRIGGER
```
function Callable object Trigger function.
```
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Argument Error.
kcs_ValueError Given function argument is not a callable object, trigger name not found or trigger type invalid.
```
unregister_trigger(name, type, function)
```
This function un-registers user trigger.
Input Parameters:
Name string Name of trigger. The same name as used for trigger file. See General in Triggers chapter.
Type constant kcs_util.kcsPOST_TRIGGER or kcs_util.kcsPRE_TRIGGER
Function Callable object Trigger function.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Argument Error.
kcs_ValueError Given function not found, or not callable or invalid trigger type.
kcs_ElementNotFound Trigger function was not registered.
```
get_registered_triggers ()
```
This function returns registered triggers as a dictionary.
Input Parameters:
None.
Returned value:
[0] dictionary All defined triggers are stored in a dictionary.
```
Exceptions:
```
kcs_GeneralError General Error.
```
Example:
```
```
Module: Triggers.py
```
import kcs_util
# callable objects that will be used by triggers
```
def NewDrawingPreTrigger():
```
# user code
```
def OpenDrawingPreTrigger():
```
# user code
# function for trigger registration
```
def RegisterTriggers():
```
```
kcs_util.register_trigger("trig_draft_dwg_new", kcs_util.kcsPRE_TRIGGER, NewDrawingPreTrigger)
```
```
kcs_util.register_trigger("trig_draft_dwg_open", kcs_util.kcsPRE_TRIGGER, OpenDrawingPreTrigger)
```
# clean up registered triggers
```
def UnregisterTriggers():
```
```
kcs_util.unregister_trigger("trig_draft_dwg_new", kcs_util.kcsPRE_TRIGGER, NewDrawingPreTrigger)
```
```
kcs_util.unregister_trigger("trig_draft_dwg_open", kcs_util.kcsPRE_TRIGGER, OpenDrawingPreTrigger)
```
Copyright © 1993-2005 AVEVA AB
3.5.12 Project Copy Triggers
```
Note: Since Project Copy can handle other object types than the valid object types of KcsModel, the KcsModel parameter has been extended to also cover the following object types:
```
```
Note: KcsProjectCopyArg is a python class containing the extracted status values from the object in the transfer set. If the object has no status values assigned or status is notapplicable (e.g. for components), then a status value Undefined (-1) is passed.
```
User's Guide Vitesse
```
Chapter: Utilities
```
KcsModel type string
"standard object" Hull, Outfitting, Basic and Assembly standard objetcts
"component" Components
"pipeline" Pipe lines
"pipe spec" Pipe specifications
"point" Points
"raw/rest plate" Raw and rest plates
"hull reference plane" Hull reference planes
"pin jig" Pin Jigs
"diagram" Diagrams
"diagram template" Diagram templates
"diagram stencil" Diagram stencils
"unplaced volume" Unplaced volumes
"standard structure" Standard structures
Project copy export pre-trigger
```
Event: Every time before an object is exported.
```
```
Type: Pre.
```
```
Name: trig_projcopy_export
```
Input Parameters: Model KCSModel ModelClass of source object
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality. None.
```
Note: None.
```
Project copy export post-trigger
```
Event: Every time after an object is exported.
```
```
Type: Post.
```
```
Name: trig_projcopy_export
```
Input Parameters: Model KCSModel ModelClass of source object
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality. None.
```
Note: None.
```
Project copy import pre-trigger
```
Event: Every time before an object is imported.
```
```
Type: Pre.
```
```
Name: trig_projcopy_import
```
Input Parameters: Model
Status
KCSModel
KCSProjectCopyArg
ModelClass of target objcet
Status from transfer set object.
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality. None.
```
Note: None.
```
Project copy import post-trigger
```
Event: Every time after an object is imported.
```
```
Type: Post.
```
```
Name: trig_projcopy_import
```
Input Parameters: Model KCSModel ModelClass of target objcet
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality. None.
```
Note: None.
```
Copyright © 1993-2005 AVEVA AB
3.5.13 Assembly Planning Triggers
See the example trigger trig_ap_parts_list_create.py.
```
This example trigger takes as input the two Assembly Parts List csv files and runs an MSExcel macro (named AssemblyLists.xls) to produce an Excel file and a formatted text file.
```
This Excel macro has been developed and verified with MS Office 2000.
User's Guide Vitesse
```
Chapter: Utilities
```
Part List Create Post-Trigger
```
Event: Fired as the Assembly Parts List function is finished with an assembly. I.e. is called per assembly with a pair of csv files as parameters. The purpose by the triggeris for user to create a formatted parts list file by the given csv files.
```
```
Type: Post.
```
File Name: trig_ap_parts_list_create
Input Parameters: Name of parts list "csv" files generated by the Assembly Parts List functions.
File name string name of csv file 1.
File name string name of csv file 2.
```
Allowed returnvalues:kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Overridefunctionality.None.
Copyright © 1993-2005 AVEVA AB
3.5.14 Sistership Management Triggers
The Sistership Management triggers are similar to the triggers in Project Copy.
```
Note: Since Sistership Management (i.e. Project Copy) can handle other object types than the valid object types of KcsModel, the KcsModel parameter has been extended to alsocover the following object types:
```
```
Note: KcsProjectCopyArg is a python class containing the extracted status values from the object in the master project. If the object has no status values assigned or status is notapplicable (e.g. for components), then a status value Undefined (-1) is passed.
```
User's Guide Vitesse
```
Chapter: Utilities
```
KcsModel type string
"standard obejct" Hull, Outfitting, Basic and Assembly standard objects
"component" Components
"pipeline" Pipe lines
"pipe spec" Pipe specifications
"point" Points
"raw/rest plate" Raw and rest plates
"hull reference plane" Hull reference planes
"pin jig" Pin Jigs
"diagram" Diagrams
"diagram template" Diagram templates
"diagram stencil" Diagram stencils
"unplaced volume" Unplaces volumes
"standard structure" Standard structures
Sistership Management import pre-trigger
```
Event: Every time before an object is imported.
```
```
Type: Pre.
```
```
Name: trig_sistership_import
```
Input Parameters: Model KCSModel ModelClass of target object
Status KCSProjectCopyArg Status from object in the master project
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality: None.
```
Note: None.
```
Sistership Management import post-trigger
```
Event: Every time after an object is imported.
```
```
Type: Post.
```
```
Name: trig_sistership_import
```
Input Parameters: Model KCSModel ModelClass of target object
```
Allowed return values: kcs_util.trigger_ok()
```
```
kcs_util.trigger_abort()
```
Override functionality: None.
```
Note: None.
```
Copyright © 1993-2005 AVEVA AB
3.6 Utility Interface
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.6.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_util. The functions are then referred to as kcs_util.<function name>. Before using anew function, please carefully read the function description.
The Vitesse Utility interface contains functions for:
 Comparing with the user response from Vitesse UI functions.
 Return codes from trigger functions.
 Checking which application is currently running.
 Accessing Tribon environment variables
 General purpose, such as coordinate translations etc.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.6.2 Exception Handling
The Vitesse Utility interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_util.error. The exception is also displayed in the Vitesse Log window which is available by
the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below. .
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
import kcs_util
```
env = 'SB_PYTHON'
```
```
try:
```
```
cur_value = kcs_util.TB_environment_get(env)
```
```
except:
```
print kcs_util.error
Copyright © 1993-2005 AVEVA AB
3.6.3 Functions to Check the User Response from Vitesse UI
```
These function are used to check the resulting "User Response" in all Vitesse UI functions. After a call of such a UI function, a completed user input will yield the user response ok(), ifnothing else is stated. Otherwise the cause of user interruption could be checked against any other function below. Note that the "check" functions below do not cover all possible user
```
responses from a UI function.
User's Guide Vitesse
```
Chapter: Utilities
```
```
ok()
```
The function returns a value that is equal to user response OK.
Input parameters:
None
```
Result:
```
[0] integer The value of OK
```
Exceptions:
```
None
```
cancel()
```
The function returns a value that is equal to user response CANCEL.
Input parameters:
None
```
Result:
```
[0] integer The value of CANCEL
```
Exceptions:
```
None
```
quit()
```
The function returns a value that is equal to user response QUIT.
Input parameters:
None
```
Result:
```
[0] integer The value of QUIT
```
Exceptions:
```
None
```
options()
```
The function returns a value that is equal to user response OPTIONS.
Input parameters:
None
```
Result:
```
[0] integer The value of OPTIONS
```
Exceptions:
```
None
```
operation_complete()
```
The function returns a value that is equal to user response OPERATION COMPLETE.
Input parameters:
None
```
Result:
```
[0] integer The value of OPERATION COMPLETE
```
Exceptions:
```
None
```
yes()
```
The function returns a value that is equal to user response YES.
Input parameters:
None
```
Result:
```
[0] integer The value of YES
```
Exceptions:
```
None
```
no()
```
The function returns a value that is equal to user response NO.
Input parameters:
None
```
Result:
```
[0] integer The value of NO
```
Exceptions:
```
None
```
all()
```
The function returns a value that is equal to user response ALL.
Input parameters:
None
```
Result:
```
[0] integer The value of ALL
```
Exceptions:
```
None
```
undo()
```
The function returns a value that is equal to user response UNDO.
Input parameters:
None
```
Result:
```
[0] integer The value of UNDO
```
Exceptions:
```
None
```
reject()
```
The function returns a value that is equal to user response REJECT.
```
Note: that REJECT is equal to CANCEL.
```
Input parameters:
None
```
Result:
```
[0] integer The value of REJECT
```
Exceptions:
```
None
```
exit_function()
```
The function returns a value that is equal to user response EXIT_FUNCTION.
```
Note: that EXIT_FUNCTION is equal to QUIT.
```
Input parameters:
None
```
Result:
```
[0] integer The value of EXIT_FUNCTION
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_util2.py
Copyright © 1993-2005 AVEVA AB
3.6.4 Functions used to Return from Trigger Scripts
User's Guide Vitesse
```
Chapter: Utilities
```
```
trigger_abort()
```
Return this function from a trigger to abort the function that fired the trigger.
Input parameters:
None
Returned value:
[0] integer The value of abort
```
Exceptions:
```
None
```
trigger_ok()
```
Return this function from a trigger to continue the function that fired the trigger.
Input parameters:
None
Returned value:
[0] integer The value of ok
```
Exceptions:
```
None
```
trigger_override()
```
Return this function from a trigger to override the function that fired the trigger.
Input parameters:
None
Returned value:
[0] integer The value of override
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_util3.py
Copyright © 1993-2005 AVEVA AB
3.6.5 Functions to Check which Application is currently running
User's Guide Vitesse
```
Chapter: Utilities
```
```
app_basic_design()
```
The function checks if Basic Design is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_cable()
```
The function checks if Cable Modelling is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_curved_hull()
```
The function checks if Curved Hull Modelling is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_diagram()
```
The function checks if Diagram is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_drafting()
```
The function checks if Drafting is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_planar_hull()
```
The function checks if Hull Modelling is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_nesting()
```
The function checks if Nesting is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_pipe()
```
The function checks if Pipe Modelling is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_structure()
```
The function checks if Structure is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
app_ventilation()
```
The function checks if Ventilation is the current application.
Input parameters:
None
Returned value:
[0] integer 0=No, 1=Yes
```
Exceptions:
```
None
```
Example:
```
# Example: ksc_ex_util3.py
Copyright © 1993-2005 AVEVA AB
3.6.6 Functions to Access Tribon Environment Variables
User's Guide Vitesse
```
Chapter: Utilities
```
```
TB_environment_get(Env)
```
The function gets the value of a Tribon environment variable.
Input parameters:
Env string The name of the environment variable
Returned value:
[0] string The value of the variable
```
Exceptions:
```
kcs_TranslateError No translation could be done
```
TB_environment_set(Env, Value)
```
The function sets a Tribon environment variable.
```
Note: The variable is changed only in the current process. Variables that set databank paths will not take effect.
```
Input parameters:
Env string The name of the environment variable
Value string The new value of the environment variable
Returned value:
None
```
Exceptions:
```
None
Copyright © 1993-2005 AVEVA AB
3.6.7 Coordinate Translation Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
coord_to_pos(Axis, Coord)
```
```
Express a co-ordinate as a main axis position (FR or LP term).
```
Input parameters:
Axis short integer Main axis:
```
1 = X (FR term)
```
```
2 = Y (horizontal LP term)
```
```
3 = Z (vertical LP term)
```
Coord real The co-ordinate to be translated
Returned value:
[0] integer Result:
0 = success,
otherwise failure
[1] short integer FR or LP number
[2] real offset from the FR or LP number
```
Exceptions:
```
None
```
pos_to_coord(Axis, No)
```
Translate a FR or LP position to a co-ordinate.
Input parameters:
Axis short integer Main axis:
```
1 = X (FR term)
```
```
2 = Y (horizontal LP term)
```
```
3 = Z (vertical LP term)
```
No short integer The FR or LP number
Returned value:
[0] integer Result:
0 = success,
otherwise failure
[1] real the translated co-ordinate
```
Exceptions:
```
None
```
tra_coord_ship (Ucoord, Vcoord, Name)
```
Get a coordinate in the ship coordinate system, from an earlier made indication in the picture. If the name of a panel is given, the point is calculated in the plane of the panel. If thename is empty, the plane of the view closest to the point given is used.
Input parameters:
Ucoord real U-coordinate of the point
Vcoord real V-coordinate of the point
Name string Name of panel defining the definition plane
Returned value:
[0] integer Result:
0 = success,
otherwise failure
[1] real the resulting point, X-coordinate
[2] real the resulting point, Y-coordinate
[3] real the resulting point, Z-coordinate
```
Exceptions:
```
None
```
tra_coord_pan (Ucoord, Vcoord, Name)
```
Get a co-ordinate in the panel co-ordinate system from an earlier made indication in the picture. The name of the panel has to be supplied, as the point is expressed in the local co-ordinate system of that panel.
Input parameters:
Ucoord real U-coordinate of the point
Vcoord real V-coordinate of the point
Name string Name of panel defining the definition plane
Returned value:
[0] integer Result
0 = success
otherwise failure
[1] real the resulting point, X-coordinate
[2] real the resulting point, Y-coordinate
[3] real the resulting point, Z-coordinate
```
Exceptions:
```
None
Copyright © 1993-2005 AVEVA AB
3.6.8 Exit Program
User's Guide Vitesse
```
Chapter: Utilities
```
```
exit_program()
```
The function terminates the Tribon program.
```
Note: The program is not terminated until the Python script is finished
```
```
(This function is necessary for Batch Vitesse)
```
Input parameters:
None.
Output parameters:
None.
Returned value
None.
```
Exceptions:
```
None.
Copyright © 1993-2005 AVEVA AB
3.6.9 Clean Workspace
User's Guide Vitesse
```
Chapter: Utilities
```
```
clean_workspace()
```
The function cleans the workspace of all objects not reserved by the current application.
Input parameters:
None
Returned value:
[] None
```
Exceptions:
```
kcs_Error
Copyright © 1993-2005 AVEVA AB
3.7 UI Interface
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.7.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_ui. The functions are then referred to as kcs_ui.<function name>. Before using anew function, please carefully read the function description.
The Vitesse UI Interface supports the following simple User Interface functions:
 Perform interactive indication in the graphical display of the Tribon application
 Pop up dialogue boxes in the same way as the Tribon application itself uses.
 Application window maximize, minimize, refresh display etc.
```
The returned value "User Response" in the functions should be checked against a proper function in the Utility interface. Normally, the User Response kcs_util.ok() is returned when theuser has completed the input, while other responses like kcs_util.cancel(), kcs_util.quit() gives the specific user interruption.
```
```
Note: that the User Response kcs_util.ok() should not be checked against the function answer_req.
```
In the general Python programming environment there are also more advanced tools for User Interface available. One example of such a tool is wxPython which can be downloadedfrom www.wxpython.org
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.7.2 Exception Handling
The Vitesse UI interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_ui.error. The exception is also written to the Vitesse log. The meaning of the exception can be
found in the documentation of the corresponding function.
The default error is kcs_Error. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
import kcs_ui
```
msg = 'Please give a position'
```
```
coord = KcsPoint2D.Point2D()
```
```
try:
```
```
res = kcs_ui.point2D_req(msg,coord)
```
```
except:
```
print kcs_ui.error
Copyright © 1993-2005 AVEVA AB
3.7.3 Classes
Some of the functions in the Vitesse UI interface use objects as input. These objects are instances of Python classes. The classes used in this interface are described in section General.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.7.4 Basic Input Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
int_req(Message, InitValue)
```
The function presents a box with a message and lets the user key in an integer.
Input parameters:
```
Message string The message (max 512 characters)
```
```
InitValue integer The predefined value (optional)
```
Returned value:
[0] integer User Response
[1] integer The resulting integer
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
real_req(Message, InitValue)
```
The function presents a box with a message and lets the user key in a real.
Input parameters:
```
Message string The message (max 512 characters)
```
```
InitValue real The predefined value (optional)
```
Returned value:
[0] integer User Response
[1] real The resulting real
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
string_req(Message, InitValue)
```
The function presents a box with a message and lets the user key in a string.
Input parameters:
```
Message string The message (max 512 characters)
```
```
InitValue string The predefined value (optional, max 512 characters)
```
Returned value:
[0] integer User Response
```
[1] string The resulting string (max 512 characters)
```
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
Example:
```
# Example: kcs_ex_ui5.py
Copyright © 1993-2005 AVEVA AB
3.7.5 Point Request Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
point2D_req(Message, Point <Status>, <Buttons>))
```
The function presents a message to the user and lets him define a 2D point in the current drawing. The initial point definition mode is "cursor position".
U/V locking
```
U/V locking can easily be implemented in the 2D point selection. If the lock buttons are enabled (see documentation of Class KcsButtonState.ButtonState class), the function will returnone of the following response codes if the user has pressed any lock button:
```
```
 kcs_util.u_lock()
```
```
 kcs_util.v_lock()
```
```
 kcs_util.unlock()
```
Handling these codes allows the user to take up special actions like draw help locking lines, change cursor type before next point2d_req call etc.
By default 2D lock buttons are disabled so it is required to give the Buttons parameter if you want to enable them.
Use Point2DLockReq function defined in kcs_ex_ui1.py as example of handling u/v locking with point2D_req. It draws help locking lines and adjusts result point to locked coordinate.
Input parameters:
```
Message string The message to the user (max 512 characters)
```
Status Stat_point2D_req Point definition mode and cursor type. This parameter is optional.
Buttons ButtonState Controls visibility of buttons and u/v lock handling. This parameter is optional
Output parameters:
Point Point2D The resulting 2D point
Returned value:
[0] integer User response
[1] Point2D The resulting 2D point
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
```
point3D_req(Message, InitStatus, Point)
```
The function presents a message to the user and lets him define a 3D point in the drawing. The optional InitStatus parameter guides some initial conditions for the point definition.
Input parameters:
```
Message string The message to the user (max 512 characters)
```
```
InitStatus Stat_point3D_req Initial conditions (optional)
```
Output parameters:
Point Point3D The resulting 3D point
InitStatus Stat_point3
```
D_req Resulting lock and initial point definition status (optional)
```
Returned value
[0] integer User response
[1] Point3D The resulting 3D point
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
```
Example:
```
# Example: kcs_ex_ui1.py
Copyright © 1993-2005 AVEVA AB
3.7.6 Message Functions
Figure 3:1. Example of a message that has to be confirmed.
User's Guide Vitesse
```
Chapter: Utilities
```
```
answer_req(Title, Question)
```
The function presents a box with a question and lets the user give the answer.
Input parameters:
```
Title string The title of the box (max 132 characters)
```
```
string The question (max 512 characters)
```
Question
Returned value:
[0] integer User Response
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
message_confirm(Message)
```
The function presents a box with a message and lets the user confirm it.
Input parameters:
```
Message string The message to the user (max 512 characters)
```
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
message_noconfirm(Message)
```
The function presents a message to the user without confirmation.
Input parameters
```
Message string The message to the user (max 512 characters)
```
Returned value
None
Exceptions
kcs_ValueError Invalid parameter value
```
Example:
```
# Example: kcs_ex_ui2.py
```
message_debug (Message, <Color>,<Bold>,<Underline>)
```
The function displays a message in the Vitesse Log Window
Input Parameters:
Object Message String representation of given python object will be send to log window.
```
Integer or Tuple <Color> Text colour. The parameter can be defined as integer colour value or tuple representing (R, G, B) values.
```
Integer <Bold> Bold text. When parameter is different then 0 the text is displayed using bold font.
Integer <Underline> Underline text. When parameter is different then 0 the text is displayed with underline.
Returned value:
None
```
Exceptions:
```
None
Copyright © 1993-2005 AVEVA AB
3.7.7 Selection Functions
Figure 3:2. Box created with choice_select.
Figure 3:3. Example on a box created with string_select.
User's Guide Vitesse
```
Chapter: Utilities
```
```
choice_select(Title, Header, Actions)
```
The function presents a box with a list of actions and lets the user select one of these.
Input parameters:
```
Title string The title of the box (max 132 characters)
```
```
Header string The header of the list (max 512 characters)
```
```
Actions Stringlist List of actions (max 132 characters for each action and max 20 actions)
```
Returned value:
[0] integer User response
[1] integer The chosen action
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
string_select(Title, Header, Prompt, Alternatives)
```
The function presents a box with a list of strings and lets the user select one of these.
Input parameters:
```
Title string The title of the box (max 132 characters)
```
```
Header string The header of the list (max 512 characters)
```
```
Prompt string The prompt (max 512 characters)
```
```
Alternatives Stringlist List of alternatives (max 132 characters for each alternative)
```
Returned value:
[0] integer User response
[1] integer The selected alternative
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
colour_select(Title, Colour)
```
The function presents a colour box and lets the user select a colour.
Input parameters:
```
Title string The title of the box (max 132 characters)
```
Output parameters:
Colour Colour The selected colour
Returned value:
[0] integer User response
[1] integer The selected colour
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
symbol_select(Prompt, Font)
```
The function lets the user select a symbol from a menu of all symbols in a given font.
Input parameters:
```
Prompt string The prompt (max 512 characters)
```
Font integer The symbol font
Returned value
[0] integer User response
:[1] integer The selected symbol within given font
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_FontInvalid The symbol font was not found
kcs_FontEmpty There are no symbols in the symbol font
```
symbol_select(Prompt, SymbList)
```
The function lets the user select a symbol from a menu of all symbols in a given list. This list may contain symbols from any existing symbol font. Non-existing symbols in the list willappear as blanks entries in the menu, thus alerting the user of incorrect input values.
Input parameters:
```
Prompt string The prompt (max 512 characters)
```
SymbList Symbollist The symbol font
Returned value:
[0] integer User response
[1] integer The font containing the selected symbol
[2] integer The selected symbol within that font
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
Example:
```
# Example: kcs_ex_ui3.py
# Example: kcs_ex_ui4.py
Copyright © 1993-2005 AVEVA AB
3.7.8 Model Information Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
model_info()
```
The function displays information about user-indicated models. The function interacts with the user.
Input parameters:
None
Returned value:
[0] integer User Response
```
Exceptions:
```
None
Copyright © 1993-2005 AVEVA AB
3.7.9 Application Window Functions
User's Guide Vitesse
```
Chapter: Utilities
```
```
app_window_minimize ()
```
The function minimizes application window.
Input parameters:
None.
Returned value:
None.
```
Exceptions:
```
None.
```
app_window_maximize ()
```
The function maximizes application window.
Input parameters:
None.
Returned value:
None.
```
Exceptions:
```
None.
```
app_window_restore ()
```
The function restores application window to its original size..
Input parameters:
None.
Returned value:
None.
```
Exceptions:
```
None.
```
app_window_refresh()
```
```
This function is used to make output to the application window immediately visible. Normally, the user should not bother about this: such "refreshing" is done automatically whenever theTribon application stops and waits for user input. However, when the user interaction is (temporarily or permanently) handled by tools outside the Vitesse UI interface (e.g. when using a
```
```
wxPython script) this function might be necessary to refresh the application window.
```
Input parameters:
None.
Output parameters:
None.
Returned value
None.
```
Exceptions:
```
None.
Copyright © 1993-2005 AVEVA AB
3.8 Data Extraction Interface
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.8.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_dex. The functions are then referred to as kcs_dex.<function name>. Before usinga new function, please carefully read the function description.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.8.2 Functions
These functions deal with data extraction. All data possible to extract in Tribon User's Guide Data Extraction are available here as well.
This gives the ability to handle rules in Vitesse programs, since the surroundings of a construction can be investigated. It also gives the possibility to produce all kinds of listings,containing data from Tribon databases.
User's Guide Vitesse
```
Chapter: Utilities
```
```
extract(dexstring)
```
Perform data extraction.
Input parameters:
dexstring string string containing a valid Tribon data extraction statement. Please consult the Tribon User's Guide Data Extraction.
Returned value:
[0] integer Result:
0 = success
otherwise failure
```
next_result()
```
Activate the next result of a previously made data extraction.
Returned value:
[0] integer indicates the type of the result value
= 0 empty tree part.
= 1 integer type result
= 2 real value type result.
= 3 string type result.
= 4 real vector 3D type result
= 5 box type result
= 6 real vector 2D type
>10 real vector nD type. Subtracting 10 from the result gives the number of elements in the vector.
= -1 End of result tree.
```
get_commandstring()
```
Get the data extraction command string for current result.
Returned value:
[0] string the command string
```
get_int()
```
Get current integer value.
Returned value:
[0] integer the integer value
```
get_real()
```
Get current real value.
Returned value:
[0] real the real value
```
get_string()
```
Get current string value.
Returned value:
[0] string the string value
```
get_reavec3d()
```
Get current real vector 3D
Returned value:
[0] real x value
[1] real y value
[2] real z value
```
get_box()
```
Get current box
Returned value:
[0] real x min
[1] real y min
[2] real z min
[3] real x max
[4] real y max
[5] real z max
```
get_reavec2d()
```
Get current real vector 2D
Returned value:
[0] real x value
[1] real y value
```
get_indexedreal(index)
```
Get value from current real vector nD.
Input parameters:
index integer index of wanted real
Returned value:
[0] real the real value
Copyright © 1993-2005 AVEVA AB
3.8.3 Examples
This example shows how to calculate the total weight of a hull block, and then just print out the sum.
1. Make data extraction statements available in the Vitesse program.
2. Initialise sum variable.
3. Ask user to key in name of hull block to calculate weight for. This command is further explained in the user interface section.
4. Build up the data extraction string.
5. Do the actual data extraction.
6. Check the outcome of the extraction command.
7. Loop to pick up all the values from the data extraction result tree.
8. Add the weight from this panel to the total sum.
9. Simply print out the sum accompanied with a simple explanation.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
import kcs_uiimport kcs_util
import kcs_dex1
```
total_weight = 0.0block = kcs_ui.string_req('Key in name of block')
```
```
if block[0] == kcs_util.ok():string = "HULL.BLOCK('" + block[1]\
```
```
+"').PANEL(*).WEIGHT"kcs_dex.extract(string)
```
```
type = kcs_dex.next_result()while type >= 0:
```
if type == 2:total_weight = total_weight\
```
+kcs_dex.get_real()type = kcs_dex.next_result()
```
print "Total weight for block " + block[1] + \" is: " + `total_weight` + " tons"
23
45
67
89
Copyright © 1993-2005 AVEVA AB
3.9 Miscellaneous Tools and Examples
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.9.1 General
Installed together with the Tribon system are a collection of miscellaneous minor Tools and Examples that might be useful. These can found in the \Vitesse\Tools directory and areprovided on an "as-is" basis, meaning that they might in some cases not be fully complete.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.9.2 Model Unit
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
Functional Description
The purpose of this group of Vitesse scripts is to handle a number of functions for grouping model objects together in a so called Model Unit.
The Model unit functionality could be inserted in any Drafting based Tribon Modelling application.
The functionality is utilizing a user-defined attribute called ModelUnit.
The user functions are grouped in a user-defined menu called "Model unit". The Model Unit menu includes the following user functions:
 Define Model Unit
A Model Unit is created from a selection of Model objects.
 Undefine Model Unit
By indicating one model object included in the Model Unit, the Model unit is deleted.
 Highlight Model Unit
Highlight all the model objects which are included in a certain Model Unit.
 Unhighlight Model Unit
Turn off the highlighting of the Model Unit.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
The included Vitesse Scripts
The following Vitesse scripts are included:
munDefineModelUnit.py
Define a Model Unit.
munUnDefineModelUnit.py
Undefine a Model Unit.
munHighlightModelUnit.py
Highlight a Model Unit.
munUnHighlightModelUnit.py
Turn off the highlighting of the Model Unit.
munModelUnitMenu.py
Class needed for creating the Model Unit menu.
muntrig_draft_init.py
This file contains the code required to initialize the Model Unit function menu. The code should be copied to the respective Modelling application's appropriate start-up trigger.
munModel_Unit.py
This file contains sample code to be attached if the Model Unit attribute is to be included in the Object Property page.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
Installation of the Model Unit Functions
To do this installation, a basic knowledge about Vitesse, Vitesse triggers and User-defined attributes is required.
1. Copy the Vitesse code from the file muntrig_draft_init.py into the respective Modelling application's start-up trigger.
```
This file contains the code to insert the ModelUnit menu in any Drafting based Tribon application. This Vitesse code must be incorporated into the Init Drafting Pre-trigger(trig_draft_init.py), or an appropriate Vitesse script, called from the trigger.
```
2. Create an attribute template for the user-defined attribute Model Unit. Use Tribon Toolkit Preferences - Attribute templates.
 Attribute name: Model Unit.
 Category: General
 Property: Name
 Data type: String
3. Copy the files below to the appropriate file catalogue. This file catalogue must be included in the PYTHONPATH definition.
 munDefineModelUnit.py
 munUnDefineModelUnit.py
 munHighlightModelUnit.py
 munUnHighlightModelUnit.py
 munModelUnitMenu.py
 munModel_Unit.py
4. If the Model Unit attribute is to be included in the customized Object Property page, use Tribon Toolkit Preferences - Object Properties. Define a new property "model unit" and link itto the Vitesse script munModel_Unit.py.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.10 Add-ins
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
3.10.1 General
Vitesse add-ins is a mechanism that supports user-defined Vitesse functions. A simple user-defined Vitesse function can be implemented in one file, and more complex functionality canbe implemented in many files.
Below the standard Vitesse directory, SB_PYTHON, there is a subdirectory named AddIns. This subdirectory is used as a storage location for Vitesse add-ins. All applications thatsupport the Vitesse interface search this subdirectory for Vitesse add-ins during startup. Each subdirectory in SB_PYTHON\AddIns represents a separate Vitesse add-in.
Each add-in will create a menu item in the Tools > Vitesse AddIns menu. The directory structure in the example above would result in the menu items in the figure below.
Selecting a Vitesse add-in from the Vitesse AddIns popup menu will run the Start.py file located in the add-in directory.
The user is responsible for providing the Start.py file for each add-in.
A Vitesse add-in is handled as a Python package. This means that the user must also provide a __init__.py file for each add-in. This file can be empty but must exist in the add-in
directory. It's existence indicates that the Vitesse add-in is a Python package.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
Vitesse
AddIns
WhereUsed  Vitesse WhereUsed add-in.
WebFrameRuler  Vitesse add-in for creating web frame rulers.
BracketList  Vitesse add-in for creating list of brackets
Vitesse
AddIns
WhereUsed  Vitesse WhereUsed add-in.
Start.py  Starter for WhereUsed add-in.
WebFrameRuler  Vitesse add-in for creating web frame rules.
Start.py  Starter for web frame ruler add-in.
BracketList  Vitesse add-in for creating list of brackets.
Start.py  Starter for brackets list add-in
Vitesse
AddIns
WhereUsed  Vitesse WhereUsed add-in.
Start.py  Starter for WhereUsed add-in.
__init__.py  Defines package.
WebFrameRuler  Vitesse add-in for creating web frame rulers.
Start.py  Starter for web frame ruler add-in.
__init__.py  Defines package.
BracketList  Vitesse add-in for creating list of brackets.
Start.py  Starter for brackets list add-in.
__init__.py  Defines package.
Copyright © 1993-2005 AVEVA AB
__init__.py file format
Some properties for Vitesse add-ins can be customized by the user. This is done in the __init__.py file.
Add-in name
The default name for the add-in is the name of the subdirectory it is stored in. It can be changed by defining the Menu variable in the __init__.py file.
This will result in the menu in the figure below.
If the user uses the Menu function to define menu position, the Menu variable has no meaning since the user must define the menu item himself and provide a name.
Menu position
The default location of the add-in menu item is in the Tools > Vitesse AddIns menu. It can be changed by defining the Menu function in the __init__.py file. This function will be
called to create the menu item for the add-in.
```
Result:
```
Start File
The default start file of the add-in is Start.py. It can be changed by defining the Start variable in the __init__.py file.
Selecting the add-in menu item will now run WhereUsedApp.py.
If the user uses the Menu function to define menu position, the Start variable has no meaning since the user must define the menu item himself and provide a file name.
Enabling and Disabling add-ins
The default is to enable all add-ins found in the AddIns subdirectory. Disable an add-in by defining an IsEnabled function in the __init__.py file. The function is called to check if the
add-in should be enabled or not.
User's Guide Vitesse
```
Chapter: Utilities
```
```
Example:
```
Vitesse\AddIns\WhereUsed\__init__.py
```
Menu = Where Used Add-In
```
```
Example:
```
Vitesse\AddIns\WhereUsed\__init__.py:
```
def Menu():
```
```
try:
```
```
main_menu = kcs_gui.menu_get(None, 0)
```
```
kcs_gui.menu_item_usr_add(main_menu, 5 , "Where Used Add-In", "AddIns.WhereUsed.Start")
```
```
except:
```
pass
```
Example:
```
Vitesse\AddIns\WhereUsed\__init__.py:
```
Start = "WhereUsedApp"
```
```
Example:
```
Vitesse\AddIns\WhereUsed\__init__.py:
```
def IsEnabled():
```
```
return kcs_util.app_planar_hull()
```
Copyright © 1993-2005 AVEVA AB
3.10.2 Vitesse Addin function: Where Used
Where Used could be used when searching for a component in a subset of Tribon models or searching for a Tribon model in a subset of drawings.
To start the application choose Tools > Vitesse AddIns > Where Used.
The main window is spit into two sides: the left one for component search and the right one for model search. It is possible to define some filters to speed up the search process. In caseof component search, the resulting models can be filtered by name and type of model. In case of model search in drawings it can be filtered by type of model we are looking for and
drawing name and databank.
The component and model can be selected directly from the screen by usage of the "..." button.
```
The search results are displayed on the lists located below the search criteria. It is possible to automatically use a found model (from component search) as input to the find model indrawing by double clicking the given model on the result list.
```
It is possible to open found drawing and zoom to given model object. If the model is used more then once in the drawing use Zoom button continuously.
User's Guide Vitesse
```
Chapter: Utilities
```
Copyright © 1993-2005 AVEVA AB
4 Python Classes
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
4.1 General
```
This section describes the General Python classes used in the different Vitesse interfaces. Class methods may be changed or added by the programmer. However, the class attributesmay NOT be changed. To use the classes, add 'import Kcs<classname>' in the vitesse program. The class attributes can be updated by using dot-notation (although methods exist for
```
```
this purpose).
```
User's Guide Vitesse
```
Chapter: Python Classes
```
Copyright © 1993-2005 AVEVA AB
4.2 Assembly
These python classes are used in connection with the kcs_assembly interface.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsAssembly.Assembly
```
The class holds information about assembly. It is used in Vitesse editing of assembly properties with functions assembly_properties_set and assembly_properties_get in modulekcs_assembly. The use of these functions requires that the _TB_ASS_DEFAULT object is stored on the assembly databank (SB_ASSDB). This object (and the level definitions) can be
```
created with the utility program ph015.
Parameters and attributes:
Name string Name of assembly object
Descrip string Description of assembly object
BuildStrat list of string Building strategy. Six strings.
PlanningUnit string Assembly planning unit
Type string Assembly type
WorkingLocation string Assembly working location
Destination string Assembly destination
DesignStatus string Assembly design status
ProductionStatus string Assembly production status
AssemblyOrientation string Assembly orientation. Can be one of:
 <empty string>
 'UpRight'
 'Upside Down'
 'Fore Down'
 'Aft Down'
 'Portside Down'
 'Starboard Down'
 'Automatic'
 'Specific Panel'
Names defined in Assembly.Orientation tuple
SpecificPanel string Assembly specific panel
Level integer Assembly level. Valid assembly levels are predefined in assembly default object
ShortLevelDesc string Short assembly level description
LongLevelDesc string Long assembly level description
PlannedStartDate date Assembly planned start date
PlannedEndDate date Assembly planned end date
ActualStartDate date Assembly actual start date
ActualEndDate date Assembly actual end date
EstimatedWeight real Assembly estimated weight
EstimatedCOG Point3D Assembly estimated centre of gravity
OrientationMatrix Transformation3d Assembly orientation matrix
```
CalculatedWeight real Assembly calculated weight (readonly)
```
```
CalculatedCOG Point3d Assembly calculated centre of gravity (readonly)
```
```
GlobalCoordBox box Assembly box in global coordinate system (readonly)
```
```
AssemblylCoordBox box Assembly box in local coordinate system (readonly)
```
```
Constructor:
```
```
Assembly() This constructor will create instance of Assembly class.
```
```
Methods:
```
```
SetBuildingStrategy(bldstrat, <index>)This method will set building strategy info.
```
bldstrat string Building strategy string.
```
<index> integer Building strategy info index. If it is given then only one line will be changed, otherwise given string bldstrat will be split to number (definedin Assembly.__BuildStrategyNum) of substrings based on separator string(defined in Assembly.__BuildStrategySep).
```
```
GetBuildingStrategy (<index>) This method will return building strategy string defined by given index.
```
```
<index> integer Building strategy info index. If no index is given then all strings will be joined using separator string(defined inAssembly.__BuildStrategySep).
```
```
SetLevel (<level>, <shortdesc>, <longdesc>) Sets level of assembly object. Valid assembly levels are predefined in assembly default object.
```
```
<level> integer 0 - level will not be set (default)
```
1-100 - level id
```
<shortdesc> string short level description ('' default)
```
```
<longdesc> string long level description ('' default)
```
```
GetLevel() (Integer, String,String)Returns level of assembly object as tuple: (levelid, shortdesc, longdesc)
```
Class protocols:
__cmp__ Used to compare two Assembly objects.
__repr__ Used to return string representation of Assembly object.
```
Example:
```
import KcsAssembly
```
a = KcsAssembly.Assembly()
```
a.Name = 'Name'
see also:
# Example: kcs_ex_ass01.py
Class KcsAssemblyKeyInItem.AssemblyKeyInItem
The class holds information about assembly key-in item. It is used in Vitesse functions i.e. assembly_keyin_ref_get, model_collect, model_decollect in module kcs_assembly.
Parameters and attributes:
Name string Name of assembly key-in item
ItemType string Assembly key-in item type:
'key-in part'
'key-in component'
All available types are defined in AssemblyKeyInItem.ItemTypes dictionary.
COG Point3d Centre of gravity
Quantity integer Quantity
PosNumber string Position number
Quality string Quality
Weight real Weight of assembly key-in item
Descrip string Description of assembly key-in item
Comment string Comment
```
Constructor:
```
```
AssemblyKeyInItem()This constructor will create instance of AssemblyKeyInItem() class.
```
```
Methods:
```
None
Class protocols:
```
__cmp__ Used to compare two AssemblyKeyInItem() objects.
```
```
__repr__ Used to return string representation of Assembly KeyInItem() object.
```
```
Example:
```
import KcsAssemblyKeyInItem
```
a = Kcs AssemblyKeyInItem.AssemblyKeyInItem()
```
a.Name = 'Name'
see als o:
# Example: kcs_ex_ass01.py
Copyright © 1993-2005 AVEVA AB
4.3 Geometry
These python classes handles different kinds of geometry.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsPoint2D.Point2D
The class holds information about a 2D point. It is the basic class for Vitesse 2D operations.
Parameters and attributes:
X real x-coordinate of the point
Y real y-coordinate of the point
```
Constructor:
```
```
Point2D (<x>, <y>) This constructor will create instance of Point2D class. Parameters are defined as above, default values are zeros.
```
```
Methods:
```
```
DistanceToPoint(p) real Calculates straight line distance between point and second point given as parameter.
```
p Point2D Point to get distance to
```
Move (xmove, ymove) Translates the point by given values
```
xmove real Change in x-coordinate
ymove real Change in y-coordinate
```
Round (decimals) Rounds coordinate values to a given number of decimals.
```
```
Example:
```
```
p = Point2D(103.67,203.73)
```
```
p.Round(1)
```
print p # [X Y:103.7,203.7]
decimals integer Number of decimals to round to
```
SetFromPoint (p) Set point as a copy of other point
```
p Point2D Point to copy coordinates from
```
SetFromMidpoint (p1, p2) Update the point to be the midpoint of two other points
```
p1 Point2D First point
p2 Point2D Second point
```
SetCoordinates(x,y) Update point coordinates. Parameters are defined as attributes above.
```
Class protocols:
__repr__ Used to return string representation of Point2D object
__cmp__ Used to compare two Point2D objects
```
Example:
```
```
point = KcsPoint2D.Point2D(10.0,0.0)
```
```
Class KcsVector2D.Vector2D(X,Y)
```
The class holds information about a 2D vector.
Parameters and attributes:
X real x-coordinate of the vector
Y real y-coordinate of the vector
```
Methods:
```
SetFromVector
SetLength
SetFromPoints
BlankProduct
CompareVector
SetFromVectorDifference
DotProduct
SetComponents
Length
LargestComponentAxis
Rotate
Round
ScalarComponentOnVector
SetFromVectorSum
SetToUnitVector
```
Example:
```
```
vec = KcsVector2D.Vector2D(1.0,0.0)
```
```
Class KcsRline2D.Rline2D(Start,End)
```
The class holds information about a restricted 2D line.
Parameters and attributes:
Start Point2D Start point of the line
End Point2D End point of the line
```
Methods:
```
None
```
Examples:
```
```
sp = KcsPoint2D.Point2D(0.0,0.0)ep = KcsPoint2D.Point2D(100.0,100.0)
```
```
line = KcsRline2D.Rline2D(sp,ep)
```
```
Class KcsRectangle2D.Rectangle2D(Corner1,Corner2)
```
The class holds information about a 2D axis-parallel rectangle.
```
NB: The rectangle is defined by two opposite corners.
```
Parameters and attributes:
Corner1 Point2D First corner of the rectangle
Corner2 Point2D Second corner of the rectangle
```
Methods:
```
None
```
Examples:
```
```
c1 = KcsPoint2D.Point2D(0.0,0.0)c2 = KcsPoint2D.Point2D(100.0,100.0)
```
```
rectangle = KcsRectangle2D.Rectangle2D(c1,c2)
```
Class KcsArc2D.Arc2D
The class holds information about a 2D arc segment. It is used in many Vitesse classes and functions i.e. arc_new, arc_highlight and dim_diameter_new in module kcs_draft.
Parameters and attributes:
Start Point2D Start point of the arc segment
End Point2D End point of the arc segment
Amplitude real Amplitude of the arc segment
```
Constructor:
```
```
Arc2D (start, end, amplitude) This constructor will create instance of Arc2D class. Parameters are defined as above.
```
```
Methods:
```
None
Class protocols:
__repr__ Used to return string representation of Arc2D object.
```
Examples:
```
```
sp = KcsPoint2D.Point2D(0.0,0.0)ep = KcsPoint2D.Point2D(100.0,100.0)
```
```
ampl = 30.0arc = KcsArc2D.Arc2D(sp,ep,ampl)
```
arc.Amplitude = 40
Class KcsCircle2D.Circle2D
The class holds information about a 2D circle. It is used in Vitesse kcs_draft module functions i.e. dim_diameter_new, circle_new or circle_highlight.
Parameters and attributes:
Centre Point2D Centre of the circle
Radius real Radius of the circle
```
Constructor:
```
```
Circle2D (centre, radius) This constructor will create instance of Circle2D class. Parameters are defined as above.
```
```
Methods:
```
```
HasPoint (point) integer Checks whether given point is inside the circle:
```
1 - point is inside the circle
0 - point is outside the circle or it is on the circle
point Point2D Point to test.
```
IsPointOnCircle (point) integer Checks whether given point is on the circle:
```
1 - point is on the circle
0 - point is inside or outside the circle
point Point2D Point to test
```
GetTangentPoints (tngPnt1,<tngPnt2>, <cle>)Point2Dor
```
[ Point2D,Point2D ]
No optional parameters given:
Method gets possible tangent points. Each of two returned tangent points on the circle and a point tngPnt1 outside the circle definestangent to the circle. If tngPnt1 is on the circle, method returns only one point equal to tngPoint1.
Optional parameters given:
Method returns one tangent point of the master circle and one tangent point of circle <cle>, both lying on one common tangent of two
```
circles. Points tngPnt1 and tngPnt2 define which variant of tangential line is considered (resulting points are possibly closest to given).
```
```
tngPnt1 Point2D A point outside the circle essential for main circle tangent point(s) calculation
```
<tngPnt2> Point2D An approximate tangent point to circle <cle> for common tangent calculation.
<cle> Circle2D Second circle for common tangent calculation
```
TangentAtPoint (pntExt,pntRef)Vector2D Method returns a vector which is a tangent to circle through point pntExt and the tangent point closest to approximate point pntRefselected by the user.
```
pntExt Point2D A point outside the circle
pntRef Point2D A point on the circle defining tangent vector variant
Class protocols:
__repr__ Used to return string representation of Circle2D object.
```
Examples:
```
```
cp = KcsPoint2D.Point2D(100.0,100.0)rad = 50.0
```
```
circle = KcsCircle2D.Circle2D(cp,rad)
```
```
Class KcsEllipse2D.Ellipse2D(Corner1,Corner2)
```
The class holds information about a 2D ellipse circumscribed by a rectangle.
```
NB: The circumscribing rectangle is defined by two opposite corners.
```
Parameters and attributes:
Corner1 Point2D First corner of the circumscribing rectangle
Corner2 Point2D Second corner of the circumscribing rectangle
```
Methods:
```
```
Examples:
```
```
c1 = KcsPoint2D.Point2D(100.0,100.0)
```
```
c2 = KcsPoint2D.Point2D(400.0,400.0)ellipse = KcsEllipse2D.Ellipse2D(c1,c2)
```
Class KcsPolygon2D.Polygon2D
```
The class holds information about a 2D polygon. Polygon is represented as a list of points. Polygons are used in Vitesse functions i.e. note_new() in module kcs_draft.
```
Parameters and attributes:
Polygon [ Point2D ] List of polygon points. Access to list is possible also by class protocols __len__, __getitem__ and __setitem__
```
Constructor:
```
```
Polygon2D(<startp>) This constructor will create instance of Point2D class. If startp is not None, it initiates the list of polygon points in Polygon attribute.
```
<startp> Point2D Start point of the polygon. None by default
```
Methods:
```
```
AddPoint(nextp) Adds a point at the end of the polygon
```
nextp Point2D The next point of the polygon
Class protocols:
__repr__ Used to return string representation of Polygon2D object
__cmp__ Used to compare two Polygon2D objects
```
__len__ Used to return the length of polygon (number of points in Polygon attribute)
```
__getitem__ Implements sequence type evaluation of self[key] to Point2D
__setitem__ Implements sequence type assignment of Point2D to self[key]
```
Examples:
```
```
sp = KcsPoint2D.Point2D(100.0,50.0)polygon = KcsPolygon2D.Polygon2D(sp)
```
sp.X = 30.0sp.Y = 120.0
```
polygon.AddPoint(sp)sp.Y = 400.0
```
```
polygon.Addpoint(sp)
```
```
point = polygon[1]
```
Class KcsContour2D.Contour2D
The class holds information about contour. It is used in Vitesse functions, i.e. contour_properties_get and hatch_new in module kcs_draft or pan_curve_create in module kcs_hull.
Parameters and attributes:
Contour [segment] List of contour segments. Each segment is a list of one or two arguments. The syntax is [startPoint, <amplitude>] where:
startPoint - Point2D at the end of the segment
```
amplitude - amplitude at the midpoint of segment (if 0 or none then segment is a straight line)
```
First segment always consists of one point only. The point is a start point of contour.
Visible integer Visibility:
1 : contour is visible
0 : contour is not visible.
Detectable integer Detect ability:
1 : contour is detectable
0 : contour is not detectable.
Colour Colour Colour of contour
LineType LineType Line type of contour. Line type must be defined in system.
Layer Layer Layer of contour
```
Constructor:
```
```
Contour2D (startp) This constructor will create an instance of Contour2D class
```
startp Point2D Start point of the contour
```
Methods:
```
```
AddLine (point) Add a line (straight) segment to the contour
```
point Point2D Point at end of line
```
AddArc (point, amplitude) Add an arc segment to the contour
```
point Point2D Point at the end of the arc
amplitude real Amplitude at the midpoint of segment
```
SetPoint (point) Reset the contour to one point
```
point Point2D Start point of the contour
```
IsPoint () integer Checks if contour is a point:
```
1 - Contour is a point
0 - Contour is not a point
```
IsClosed () integer Check whether the contour is closed:
```
1 - Contour is closed
0 - Contour is not closed
```
IsInside (point) integer Check whether the point is inside the contour:
```
1 - The point is inside the contour
0 - The point is outside or on the contour or the contour is not closed.
point Point2D Point to test
```
IsPointOnContour (point) integer Check whether the given point is on contour:
```
1 - The point is on the contour
0 - The point is not on the contour.
point Point2D Point to test
```
GetPointOnContour (point) Get a point on contour, which is nearest to the given point. New point is returned in input variable.
```
point Point2D Input/output point
```
GetCenterPoint (start, end,amplitude)Point2D Get the center point of a segment given at input
```
start Point2D Start point of the segment
end Point2D End point of the segment
amplitude real Amplitude of the segment
```
Distance (point) real Get the distance between given point on contour and the end point of the contour measured along contour
```
point Point2D Point on contour, whose distance to end point is to be calculated
```
Length() real Get the length of contour
```
```
Area() real Get the area inside contour
```
```
Direction() integer Get the direction (orientation) of the contour:
```
1 - Contour is clockwise
-1 - Contour is anticlockwise
Class protocols:
__repr__ Used to return string representation of Contour2D object.
__add__ Returns a sum of two contours, for example:
```
contC = contA + contB
```
Now contC is a new instance of Contour2D representing the sum of contA and contB where contA and contB are also instances of Contour2D.
__sub__ Returns a subtraction of two contours, for example:
```
contC = contA - contB
```
Now contC is a new instance of Contour2D representing the subtraction of contA and contB where contA and contB are also instances ofContour2D.
__mul__ Returns a common part of two contours, for example:
```
contC = contA * contB
```
Now contC is a new instance of Contour2D representing the common part of contA and contB where contA and contB are also instances ofContour2D.
Class KcsContourOperations. BooleanOperations:
The ContourOperations class holds information about two 2D dimensional# contours, which will be used to perfom operations on.
```
Attributes:
```
__contour1 Contour2D First contour
__contour2 Contour2D Second contour
__segments1 list Segments list of first contour
__segments2 list Segments list of second contour
```
Methods:
```
```
BooleanOperations(constructor) Creates an instance of the class
```
```
INPUT:
```
Contour2D First contour
Contour2D Second contour
ConvertContour Converts contour segments to the following representation:
```
(start point, end point, center point, amplitude)
```
```
INPUT:
```
Contour2D Contour to convert
GetInsideSegments Gets all segments that are inside the other contour.
```
INPUT:
```
list List of segments converted by ConvertContour
GetOuterSegments Gets all segments that are outside the other contour
```
INPUT:
```
list List of segments converted by ConvertContour
GetConditionalSegments Gets all segments that are in both contours.
```
INPUT:
```
list List of segments converted by ConvertContour
IsOuterSegment Checks if segment is an outer segment.
```
INPUT:
```
list Segment converted by ConvertContour
IsOuterPoint Checks if point is an outer point.
```
INPUT:
```
Point2D Point
ChooseNextSegment Chooses next segment used for adding contours.
```
INPUT:
```
list Segment converted by ConvertContour
list List of priority segments converted by ConvertContour
list List of secondary segments converted by ConvertContour
DifferNextSegment Chooses next segment used for substracing contours.
```
INPUT:
```
list Segment converted by ConvertContour
list List of priority segments converted by ConvertContour
list List of secondary segments converted by ConvertContour
CompositeContour Adds contours
```
INPUT:
```
list List of intersection points
ChooseDifStartPoint Chooses another start point when creating more than one contour.
```
INPUT:
```
list list of already used segments converted by ConvertContour
list list of segments converted by ConvertContour
```
CommonContour Finds common part(s) of two contours
```
```
INPUT:
```
list list of intersection points
DifferContour Subtracts contours.
list list of intersection points
Class KcsConic2D.Conic2D
The class holds information about a 2D conic segment. It is used in Vitesse kcs_draft module functions, i.e. conic_new or conic_highlight
Parameters and attributes:
Start Point2D The start point
End Point 2D The end point
Amplitude Vector2D The amplitude vector
Cff real The form factor. It controls the shape of the conic and should be 0 <= Cff < 1. In Mathematical terms, a value < 0.5 will yield a ellipse, a value > 0.5a hyperbola, while a value of exactly 0.5 will yield a parabola.
```
Constructor:
```
```
Conic2D (stp, endp,ampl, cff)This constructor will create instance of Conic2D class.Parameters are defined as above.
```
```
Methods:
```
None
Class protocols:
_repr_ Return string representation of Conic2D object
```
Examples:
```
```
sp = KcsPoint2D.Point2D(100.0,100.0)ep = KcsPoint2D.Point2D(300.0,300.0)
```
```
amp = KcsVector2D.Vector2D(1.0,2.0)cff = 0.1
```
```
con = KcsConic2D.Conic2D(sp,ep,amp,cff)
```
Class KcsPoint3D.Point3D
The class holds information about a 3D point. It is the basic class for Vitesse 3D operations.
Parameters and attributes:
X real x-coordinate of the point
Y real y-coordinate of the point
Z real z-coordinate of the point
```
Constructor:
```
```
Point3D (<x>, <y>, <z>) This constructor will create instance of Point3D class. Parameters are defined as above, default values are zeros.
```
```
Methods:
```
```
DistanceToPoint(p) real Calculates straight line distance between point and second point given as parameter
```
p Point3D Point to get distance to
```
Round (decimals) Rounds coordinate values to a given number of decimals.
```
```
Example:
```
```
p = Point3D(103.67,203.73, 300)
```
```
p.Round(1)
```
print p # [X Y:103.7,203.7, 300.0]
decimals integer Number of decimals to round to
```
SetFromPoint (p) Set point as a copy of other point
```
p Point3D Point to copy coordinates from
```
SetFromMidpoint (p1, p2) Update the point to be the midpoint of two other points
```
p1 Point3D First point
p2 Point3D Second point
```
SetCoordinates(x,y,z) Update point coordinates. Parameters are defined as attributes above.
```
```
Transform (tra) Transform the point using a transformation matrix
```
tra Transformation3D Transformation matrix
Class protocols:
__repr__ Used to return string representation of Point3D object
__cmp__ Used to compare two Point3D objects
```
Example:
```
```
point = KcsPoint3D.Point3D(0.0,0.0,0.0)
```
Class KcsVector3D.Vector3D
The class holds information about vector 3D.
```
Attributes:
```
X Float X-coordinate
Y Float Y-coordinate
Z Float Z-coordinate
```
Methods:
```
Class constructor: This constructor will create instance of Vector3D class.
```
Vector3D(<x>, <y>, <z>) Coordinates are optional. Default value for all coordinates is:
```
-32000
```
AngleToVector(v1) Returns angle (in radians) between self and another vector 3D v1.
```
```
AngleToVectorWithSign(v1) Returns angle (in radians) between self and another vector 3D v1 with sign.
```
```
BlankProduct (scale) Scale the vector length by scale value.
```
```
BoxProduct (v1, v2) Calculates the box product between self and other two vectors v1 and v2.
```
```
CompareVector(v1, tol) Compares with another vector v1 and tolerance tol.
```
```
DotProduct (v1) Returns scalar product between self and vector v1.
```
```
AbsoluteLargestComponentAxis() Returns axis with largest component absolute value. It returns:
```
0 for X axis,
1 for Y axis and
2 for Z axis.
```
Length () Returns length of vector.
```
```
ProjectOnLine(line3D) Projects vector on Line3D
```
```
ProjectOnVector(v1) Projects vector on another 3D vector v1.
```
```
ProjectOnPlane(plane) Projects vector on Plane3D.
```
```
Rotate(angle, v1) Rotates vector by given angle (in radians) around another vector.
```
```
Round(decimals) Rounds vector components to given number of decimals.
```
```
ScalarComponentOnLine(line) Performs scalar projection on Line3D.
```
```
SetComponents(x, y, z) Sets vectors components.
```
```
SetFromCrossProduct(v1, v2) Sets vectors components from cross product of another two vectors v1 and v2.
```
```
SetFromPoints(p1, p2) Sets vectors components from start and end 3D points p1 and p2.
```
```
SetFromVector(v1) Sets vectors components from another 3D vector v1
```
```
SetFromVectorDifference(v1, v2) Sets vectors components to difference of another two 3D vectors: v1-v2.
```
```
SetFromVectorSum(v1, v2) Sets vectors components to sum of another two 3D vectors: v1+v2.
```
```
SetLength(length) Update the vector to have a certain length.
```
```
SetToUnitVector() Update the length of vector to 1.
```
```
Transform(tra) Transforms vector by Transformation3D matrix.
```
Operators Operators: ==, !=, <=, <, >, >=, +, -, truth value testing
Sequential data type protocol You can use index for accessing vector components:
v1[0] returns X component,
v1[1] returns Y component,
v1[2] returns Z component.
```
Example:
```
from KcsPoint3D import Point3D
```
v1 = Point3D(12, 22, 24)
```
```
v1[v1.AbsolutLargestComponentAxis()] = 0.0
```
print v1
```
Class KcsLine3D.Line3D(Point,Direction)
```
The class holds information about an unlimited 3D line
Parameters and attributes:
Point Point3D A point on the line
Direction Vector3D A vector along the line
```
Methods:
```
ScalarComponentOfVector
VectorComponentOfVector
Transform
```
Examples:
```
```
pnt = KcsPoint3D.Point3D(100.0,100.0,100.0)
```
```
dir = KcsVector3D.Vector3D(0.0, 0.0, 1.0)
```
```
line = KcsLine3D.Line3D( pnt, dir)
```
```
Class KcsPolygon3D.Polygon3D(Start)
```
The class holds information about a 3D polygon.
```
Parameters:
```
Start Point3D Start point of the polygon
```
Methods:
```
AddPoint
```
ClassPolygon3D.GetNoOfPoints()
```
The function returns number of points in polygon.
```
ClassPolygon3D.GetPoint()
```
```
The function returns Point3D instance of polygon point selected by index (0 based).
```
```
Examples:
```
```
sp = KcsPoint3D.Point3D(100.0,50.0,0.0)polygon = KcsPolygon3D.Polygon3D(sp)
```
sp.X = 30.0sp.Y = 120.0
```
polygon.AddPoint(sp)sp.Y = 400.0
```
```
polygon.Addpoint(sp
```
```
Class KcsPlane3D.Plane3D)
```
```
The class holds information about an unlimited plane. It is used by Vitesse functions i.e view_slice_planes_get() in module kcs_draft.
```
Parameters and attributes:
Point Point3D A point on the plane
Normal Vector3D A vector perpendicular to the plane
```
Constructor:
```
```
Plane3D (pnt, norm) This constructor will create instance of Plane3D class. Parameters are defined as above.
```
```
Methods:
```
```
IntersectLine (line,point)integer Intersects the plane with a line. If the intersection is found it returns 0 and sets "point" parameter to intersection point, otherwise returns -1.
```
line Line3D The line to intersect the plane with
point Point3D The point to be updated with result
```
Transform (tra) Transforms a plane using transformation matrix.
```
tra Transformation3D The transformation matrix
Class protocols:
__repr__ Used to return string representation of Plane3D object.
```
Examples:
```
```
pnt = KcsPoint3D.Point3D(0.0,0.0,0.0)norm = KcsVector3D.Vector3D(0.0, 1.0, 0.0)
```
```
plane = KcsPlane3D.Plane3D( pnt, norm)
```
Class KcsCircle3D.Circle3D
The class holds information about a 3D circle.
Parameters and attributes:
Centre Point3D Centre of the circle
Normal Vector3D Normal vector to circle plane
Radius real Radius of the circle
```
Constructor:
```
```
Circle3D (centre, normal, radius) This constructor will create instance of Circle3D class. Parameters are defined as above.
```
Class protocols:
__repr__ Used to return string representation of Circle3D object.
Examples
```
cp = KcsPoint3D.Point3D(100.0,100.0, 50.0)rad = 50.0
```
```
norm = KcsVector3D.Vector3D(0,0,1)circle = KcsCircle2D.Circle2D(cp,norm,rad)
```
Class KcsBox.Box
The class holds information about a 3D box. It is used i.e. with classes KcsAssembly.Assembly, KcsVolPrimitiveBlock.VolPrimitiveBlock or with function view_symbolic_new in modulekcs_draft.
Parameters and attributes:
Origin Point3D Box origin
LengthDir Vector3D Length direction vector
HeightDir Vector3D Height direction vector
Length real Length along 'LengthDir' vector
Height real Height along 'HeightDir' vector
Width real Width along right normal of "length-height" plane
```
Constructor:
```
```
Box (origin, lengthDir, heightDir, length, height,width)This constructor will create instance of Box class. Parameters are defined as above.
```
```
Methods:
```
```
SetAxisParallelBox (lowCorner, upCorner) or
```
```
(x1, y1, z1, x2, y2, z2)
```
It will create axis parallel box. Height direction is parallel to Y axis and Length direction is parallel to Z axis.
```
lowCorner Point3d Lower-left (min z) corner of Bo
```
```
upCorner Point3d Upper-right (max z) corner of Box
```
```
x1, y1, z1, x2, y2, z2 real Corners in coordinate list format (first = lower-left, second = upper-right)
```
```
IsEmpty() integer 1 - Box is empty (three dimentions are equal 0)
```
0 - Box is not empty
Class protocols:
__repr__ Used to return string representation of Box object.
```
Examples:
```
import KcsBox
import KcsPoint3D
import KcsVector3D
```
origin = KcsPoint3D.Point3D(0,0,0)
```
```
lengthDir = KcsVector3D.Vector3D(0,1,2)
```
```
heightDir = KcsVector3D.Vector3D(0,2,1)box = KcsBox.Box(origin, lengthDir, heightDir, 45.7 , 10, 55.5)
```
Class KcsCap.Cap
The class holds information about a cap. The cap primitive describes a spherical segments, i.e. a part of a sphere, cut off with plane.
Parameters and attributes:
Origin Point3d Cap origin
Direction Vector3d Cap direction vector
Diameter real Cap diameter
Amplitude real Cap amplitude
```
Constructor:
```
```
Cap (orig, dir, diam, ampl) This constructor will create instance of Cap class. Parameters are defined as above.
```
Class protocols:
__repr__ Return string representation of Cap object.
```
Example:
```
import KcsCap
import KcsPoint3D
import KcsVector3D
```
origin = KcsPoint3D.Point3D(4,5,7.8)
```
```
direction = KcsVector3D.Vector3D(0,0,1)
```
```
cap = KcsCap.Cap(origin, direction, 4, 7.8)
```
cap.Diameter = 1
Class KcsCone.Cone
The class holds information about a cone. For the cone primitive at least one of the two defining radii must be greater than zero.
Parameters and attributes:
```
Origin Point3D Cone origin (centre of first end circle)
```
Direction Vector3D Cone direction vector
Length real Cone length.
Diameter1 real The diameter of first end circle
Diameter2 real The diameter of second end circle
```
Constructor:
```
```
Cone (orig, dir, len, diam1,<diam2>)This constructor will create instance of Cone class. Parameters are defined as above, by default <diam2> is equal to diam1. At least one of thediameters must be greater then zero.
```
Class protocols:
__repr__ Return string representation of Cone object.
```
Example:
```
```
origin = KcsPoint3D.Point3D(4,5,7.8)
```
```
direction = KcsVector3D.Vector3D(0,0,1)
```
```
cone = KcsCone.Cone(origin, direction, 20, 8, 0)
```
cone.Diameter2 = 1
Class KcsConnection.Connection
The class holds information about a connection.
Parameters and attributes:
Pos Point3D Origin of the connection
Dir Vector3D Direction of the connection
```
Type integer The type of the connection (1-9)
```
```
Number integer The number of the connection (1-199)
```
Descr string The description of the connection
```
Constructor:
```
```
Connection (pos, dir, type, number, <descr>) This constructor will create an instance of Connection class. Parameters are defined as above, description is an empty string by default.
```
Class protocols:
__repr__ Return string representation of Connection object.
```
Examples:
```
```
pos = KcsPoint3D.Point3D(100.0,100.0, 0.0)dir = KcsVector3D.Vector3D(1.0,2.0,3.0)
```
```
con = KcsConnection.Connection(pos, dir, 1, 50, 'description')
```
Copyright © 1993-2005 AVEVA AB
4.4 Date and Time
These python classes handle dates and time.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsDate.Date
The class holds information about date
Parameters and attributes:
_Year integer Year
_MonthY integer Month
_Day integer Day
```
Methods:
```
Class constructor:
```
Date(<integer year>, <integer month>, <integer day>)
```
This constructor will create instance of Date class.
__cmp__ Used to compare two Date objects.
__rpr__ Used to return string representation of Date object.
```
SetDate(year, month, day)
```
```
SetDate(Date)
```
Sets date.
```
GetDate() Returns date as tuple containing three integers:
```
```
(year, month, day)
```
```
Example:
```
import KcsDate
```
a = KcsDate.Date(2001, 10, 10)
```
print a
```
a.SetDate(2000, 10, 11)
```
```
print '%04i %02i %02i' %.GetDate()
```
see also:
# Example: kcs_ex_ass01.py
# Example: kcs_ex_db01.py
Class KcsTime.Time
The class holds information about time. It is used with other Vitesse classes.
Parameters and attributes:
Hour integer Hour part
Minute integer Minute part
Second integer Second part
Hundredths integer Hundredth of second
```
Constructor:
```
```
Time(<hour>,<min>,<sec>,<hund>) This constructor will create instance of Time class. Parameters are defined as above. Default values are 0.
```
```
Methods:
```
```
SetTime (hour, min, sec, hund) Sets time from four parts. Parameters are defined as above.
```
```
SetTime (time) Sets time from another Time instance.
```
time Time Time object to copy
```
GetTime () (integer, integer, integer, integer) Returns time as tuple:
```
```
(hour, minute, second, hundredths)
```
Class protocols:
__cmp__ Used to compare two Time objects.
__repr__ Used to return string representation of Time object.
```
Example:
```
import KcsTime
```
a = KcsTime.Time(05, 10, 10, 00)
```
print a
```
a.SetTime(05, 10, 11, 00)
```
```
print '%02i:%02i:%02i.%02i' %GetTime()
```
see also:
# Example: kcs_ex_db01.py
Class KcsDateTime.DateTime
The class holds information about date and time. This class inherits from Date and Time classes.
Parameters and attributes:
None.
```
Methods:
```
Class constructor:
```
DateTime(<integer year>, <integer month>, <integer day>, <integer hour>, <integer minute>, <integersecond>, <integer hundredths>)
```
This constructor will create instance of DateTime class.
__cmp__ Used to compare two DateTime objects.
__repr__ Used to return string representation of DateTime object.
```
SetDateTime(year, month, day, hour, min, sec, hund)
```
```
SetDateTime(DateTime)
```
Sets date time.
```
GetDateTime() Returns time as tuple containing seven integers:
```
```
(year, month, day, hour, minute, second, hundredths)
```
```
Examples:
```
import KcsDateTime
```
a = KcsDateTime.DateTime(2001, 10, 19, 05, 10, 10, 00)
```
print a
see also:
# Example: kcs_ex_db01.py
Copyright © 1993-2005 AVEVA AB
4.5 Pipe
```
These python classes are used in connection with the Vitesse Pipe / Ventilation (kcs_pipe) interface.
```
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsResultPipeStructConn.ResultPipeStructConn
```
The class holds information about structure connected to pipe part. Class is used as return value from function part_structure_get() in module kcs_pipe.
```
Parameters and attributes:
StructName string Structure name
AliasName string Structure alias name
```
Constructor:
```
```
ResultPipeStructConn(<StructName>,<AliasName>)This constructor creates an instance of ResultPipeStructConn class. Parameters are defined as above with empty strings as defaultvalues.
```
```
Methods:
```
None.
Class protocols:
__repr__ Used to return string representation of ResultPipeStructConn object.
```
Example:
```
```
result = KcsResultPipeStructConn.ResultPipeStructConn()
```
print result.StructName
print result.AliasName
result.StructName = "STR1"
result.AliasName = "Alias"
print result
see also:
# Example: kcs_ex_pipe12.py
Class KcsPipeProp.PipeProp
The class contains information about pipe properties
Parameters and attributes:
__BendRad Real Bending radius
__Color String Pipe colour
__SketchNote String Sketch note
__JointCode Integer Joint code
__WeldCode Integer Weld code
__HeatCode Integer HeatCode
__SurfTrCode Integer Surface treatment code
__TestPress Real Test pressure
__PlanUnit String Planning unit
```
Methods:
```
SetBendRadius
GetBendRadius
SetColor
GetColor
SetSketchNote
GetSketchNote
SetJointCode
GetJointCode
SetWeldCode
GetWeldCode
SetHeatCode
GetHeatCode
SetSurfaceTreatmentCode
GetSurfaceTreatmentCode
SetTestPressure
GetTestPressure
SetPlanningUnit
GetPlanningUnit
```
Example:
```
```
prop = KcsPipeProp.PipeProp()
```
```
prop.SetJointCode(2)
```
```
kcs_pipe.pipe_properties_set(prop)
```
see also:
# Example: kcs_ex_pipe09.py
Class KcsPipeCheck.PipeCheck
```
The class contains information about which checks have to be performed when calling pipe_check() function
```
Parameters and attributes:
PosNoCheck Integer Position name checking
ExcessCheck Integer Excess checking
BendingCheck Integer Bending checking
ExtrusionCheck Integer Extrusion checking
FeedCheck Integer Feed checking
FrameCheck Integer Frame checking
LengthCheck Integer Length checking
LooseCheck Integer Loose checking
RotationCheck Integer Rotation checking
JointCheck Integer Joint checking
NonConnCheck Integer Non connected connection checking
WeldGapsCheck Integer Weld gaps checking
```
Methods:
```
SetPosNoCheck
GetPosNoCheck
SetExcessCheck
GetExcessCheck
SetBendingCheck
GetBendingCheck
SetExtrusionCheck
GetExtrusionCheck
SetFeedCheck
GetFeedCheck
SetFrameCheck
SetLengthCheck
GetLengthCheck
SetLooseCheck
GetLooseCheck
SetRotationCheck
GetRotationCheck
SetJointCheck
GetJointCheck
SetNonConnCheck
GetNonConnCheck
SetWeldGapsCheck
GetWeldGapsCheck
```
Example:
```
```
check = KcsPipeCheck.PipeCheck()
```
```
check.SetPosNoCheck()
```
```
result = kcs_pipe.pipe_check( check )
```
see also:
# Example: kcs_ex_pipe05.py
Class KcsPipeCheck.Settings.PipeCheckSettings
```
The class is used as input parameter by function pipe_check_settings() to activate/deactivate pipe production check functions
```
Parameters and attributes:
PosNoCheck Integer Position name checking
BendingCheck Integer Bending checking
ExtrusionCheck Integer Extrusion checking
```
Methods:
```
SetPosNoCheck
GetPosNoCheck
SetBendingCheck
GetBendingCheck
SetExtrusionCheck
GetExtrusionCheck
```
Example:
```
```
settings = KcsPipeCheckSettings.PipeCheckSettings()
```
```
settings.SetPosNoCheck()
```
```
kcs_pipe.pipe_check_settings( settings )
```
see also:
# Example: kcs_ex_pipe05.py
Class KcsPipeJointAddCriteria.PipeJointAddCriteria
The class contains information defining criteria of joint insertion into pipe
Parameters and attributes:
JointType String Joint type
Direction Vector3D Angled joint direction
ExtPipeName PipeName External pipe name
Distance Real Distance from connection to insert node
```
Methods:
```
SetJointType
GetJointType
SetDirection
GetDirection
SetExternalPipe
GetExternalPipe
SetDistance
GetDistance
```
Example:
```
```
criteria = KcsPipeJointAddCriteria.PipeJointAddCriteria()
```
```
criteria.SetJointType("insert")
```
```
kcs_pipe.joint_add(PartId, Conn, Criteria)
```
see also:
# Example: kcs_ex_pipe10.py
Class KcsPipeMaterial.PipeMaterial
The class contains information about material components used by functions setting pipe material
Parameters and attributes:
AddType Integer Material type. Use SetType function to choose one of following types: 'pipe', 'straight', 'bend', 'mitre'
StraightMat String Straight material component
BendMat String Bend material component
```
Methods:
```
SetBendMaterial
GetBendMaterial
SetStraightMaterial
GetStraightMaterial
SetType
GetType
```
Example:
```
```
material = KcsPipeMaterial.PipeMaterial()
```
```
material.SetStraightMaterial("88.9-10-1330")
```
```
material.SetBendMaterial("88.9-10-1330")
```
```
kcs_pipe.pipe_material_set(material)
```
see also:
# Example: kcs_ex_pipe06.py
Class KcsPipeName.PipeName
The class contains pipe name string
Parameters and attributes:
_Name String Pipe name
```
Methods:
```
GetModule
GetSystem
GetLinNo
SetName
GetName
SplitName
```
Example:
```
```
name = kcs_pipe.pipe_name_get()
```
```
lineNo = name.GetLineNo()
```
```
systemName = name.GetSystem()
```
```
moduleName = name.GetModule()
```
Class KcsPipePartAddCriteria.PipePartAddCriteria
The class contains information defining criteria of part insertion into pipe
Parameters and attributes:
__AddType Integer Add type defining if part should be connected to another part or added on surface. Use SetConnType function to choose one of following types: 'part','surface'
__Component String
__SurfPoint Point3D
__Direction Vector3D
__Orientation Vector3D
__Length Real Part length
__ExtPipeName PipeName External pipe name
__Distance Real Distance of insert from connection
__Angle Real Cut angle
__CutBlenType Integer Cut building length type
```
(0=No cut, 1=Cut off building length)
```
```
Methods:
```
SetConnType
GetConnType
SetComponent
GetComponent
SetLength
GetLength
SetSurfPoint
GetSurfPoint
SetDirection
GetDirection
SetOrientation
GetOrientation
SetExternalPipe
GetExternalPipe
SetDistance
GetDistance
SetAngle
Get Angle
SetCutBlenType
GetCutBlenType
```
Example:
```
```
criteria = KcsPipePartAddCriteria.PipePartAddCriteria()
```
```
criteria.SetConnType( "part")
```
```
criteria.SetComponent("88.9-10-1330")
```
```
criteria.SetLength(200)
```
```
kcs_pipe.part_add( PartId, Conn, criteria)
```
see also:
# Example: kcs_ex_pipe08.py
Class KcsPipePartProp.PipePartProp
The class contains properties of pipe part
Parameters and attributes:
__AcqCode Integer Acquisition code
__InsulComp Integer Insulation Component
```
__InsulType Integer Insulation status (0/1 - no/yes insulation)
```
__JointCode Integer Joint code
__LooseCode Integer Loose code
__MatNote String Material note
__PlaceCode Integer Placing code
__WeldCode Integer Weld code
```
Methods:
```
SetAcquisitionCode
GetAcquisitionCode
SetMaterialNot
GetMaterialNot
SetJointCode
GetJointCode
SetWeldCode
GetWeldCode
SetPlacingCode
GetPlacingCode
SetLooseCode
GetLooseCode
SetInsulation
GetInsulation
```
Example:
```
```
prop = KcsPipePartProp.PipePartProp()
```
```
prop.SetAcquisitionCode(1)
```
```
prop.SetLooseCode(0)
```
```
prop.SetInsulation("Component")
```
```
kcs_pipe.part_properties_set(PartId, prop)
```
see also:
# Example: kcs_ex_pipe09.py
Class KcsPipeSpoolProp.PipeSpoolProp
```
The class contains properties of pipe spool. It is used by Vitesse function spool_properties_set() in module kcs_pipe.
```
Parameters and attributes:
PosNo string Position name
SketchNote string Sketch note
SketchType string Sketch type
HeatCode integer Heat code
SurfTrCode integer Surface treatment code
TestPress real Test pressure
PlanUnit string Planning unit
```
Constructor:
```
```
PipeSpoolProp() This constructor creates an instance of PipeSpoolProp class. By default all attributes are set to None (default system values are set to spool).
```
```
Methods:
```
None
Class protocols:
__repr__ Used to return string representation of PipeSpoolProp object.
```
Example:
```
```
prop = KcsPipeSpoolProp.PipeSpoolProp()
```
prop.PosNo = "POSNO"
prop.PlanUnit = "PU1"
```
kcs_pipe.spool_properties_set( PartId, prop )
```
see also:
# Example: kcs_ex_pipe09.py
Class PipeRoute.PipeRoute
The class contains information defining pipe routing criteria.
Parameters and attributes:
```
__AddType Integer Defines if routing is performed from/to part, surface or free point. Use SetRouteType() function to choose one of following options: 'part', 'surface', 'point'.
```
```
__FreePoint Point3D Free point (required when routing from free point).
```
```
__SurfPoint Point3D Point on surface (required when routing on surface).
```
```
__PartId Integer Part Id (required when routing from part).
```
```
__Conection Integer Connection number (required when routing from part).
```
```
__ExtPipeName Pipe Name External pipe name (required when routing from external pipe).
```
```
Methods:
```
SetRouteType
GetRouteType
SetSurfPoint
GetSurfPoint
SetFreePoint
GetFreePoint
SetPartId
GetPartId
SetConnection
GetConnection
SetExternalPipe
GetExternalPipe
```
Example:
```
```
criteria = KcsPipeRoute.PipeRoute()
```
```
criteria.SetRouteType('point')
```
```
criteria.SetFreePoint(point)
```
```
kcs_pipe.pipe_route_start(criteria)
```
see also:
# Example: kcs_ex_pipe07.py
Class KcsResultPipeCheck.ResultPipeCheck
```
The class objects contain messages returned by pipe production check functions i.e. pipe_check() or pipe_ready().
```
Parameters and attributes:
PartId integer Part id number
ConnNo integer Connection number
MsgNo integer Message number
MsgString string Message text
```
Constructor:
```
```
ResultPipeCheck(<PartId>, <ConnNo>, <MsgNo>,<MsgString>)This constructor creates an instance of ResultPipeCheck class. Parameters are defined as above with zeros and emptystring as default values.
```
```
Methods:
```
None.
Class protocols:
__repr__ Used to return string representation of ResultPipeCheck object.
```
Example:
```
```
check = KcsPipeCheck.PipeCheck()
```
```
check.SetPosNoCheck()
```
```
result = kcs_pipe.pipe_check( check )
```
print result
see also:
# Example: kcs_ex_pipe05.py
Class KcsSpecSearch.SpecSearch
```
The class contains search criteria and search results. Vitesse functions using SpecSearch parameter (i.e. part_add(), part_insert(), pipe_material_set() ) need valid SearchResultsettings. In other words, filling criteria and performing a search operation is needed before calling functions with SpecSearch object.
```
Parameters and attributes:
SCProject string Search criteria: project name. On value change SearchResult is cleared.
SCSpec string Search criteria: specification. On value change SearchResult is cleared.
SCFunction string Search criteria: function. On value change SearchResult is cleared.
SCNomDia integer Search criteria: nominal diameter. On value change SearchResult is cleared.
SCFlow real Search criteria: flow. On value change SearchResult is cleared.
SCPressClass string Search criteria: pressure class. On value change SearchResult is cleared.
```
SearchResult [string] Result list from a search (readonly)
```
```
Choice integer Indicates which component in SearchResult to use, in case of multiple components (default 0)
```
```
Constructor:
```
```
SpecSearch() This constructor creates an instance of SpecSearch class.
```
```
Methods:
```
```
Search() Perform a search and fill up SearchResult using the current parameters settings.
```
```
GetComponent(index) string Examines search result by returning string value pointed by an index from SearchResult table.
```
index integer Index of the claimed result in SearchResult table.
```
GetChoosenComponent()string Gets string value pointed by current setting of Choice attribute from SearchResult table.
```
Class protocols:
__repr__ Used to return string representation of SpecSearch object.
```
Example:
```
```
specSearch = KcsSpecSearch.SpecSearch()
```
specSearch.SCProject = "SP"
specSearch.SCSpec = "WW"
specSearch.SCFunction = "BALL"
specSearch.SCNomDia = 100
```
specSearch.Search()
```
```
criteria = KcsPipePartAddCriteria.PipePartAddCriteria()
```
criteria.AddType = "part"
criteria.Length = 200
```
kcs_pipe.part_add( PartId, Conn, criteria, specSearch)
```
Copyright © 1993-2005 AVEVA AB
4.6 User Interface
These python classes are of user interface type.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsButtonState.ButtonState
The class holds information about buttons states during interactive operations. It is used in interactive functions call i.e. point2D_req in module kcs_ui.
Parameters and attributes:
LockEnabled integer Lock buttons state:
0 - disabled,
1 - enabled
OptionsEnabled integer Options button state:
0 - disabled
1 - enabled
LockChecked string State of lock buttons:
None - no lock button checked
'U' - U lock checked
'V' - V lock checked
```
Constructor:
```
```
ButtonState() This constructor will create instance of ButtonState class. By default all buttons are disabled/unchecked.
```
Class protocols:
__cmp__ Used to compare two ButtonState objects.
__repr__ Used to return string representation of ButtonState object.
```
Example:
```
import KcsButtonState
import KcsPoint2D
import kcs_ui
```
point = KcsPoint2D.Point2D()
```
```
buttons = KcsButtonState.ButtonState()
```
buttons.LockEnabled = 1
buttons.OptionsEnabled = 1
buttons.LockChecked = 'U'
```
kcs_ui.point2D_req('Select 2D point', point, buttons)
```
Class KcsCursorType.CursorType
The class holds information about cursor type used in kcs_ui.point2D_req function
Parameters and attributes:
__nType integer Type of cursor. This variable should not be accessed directly.
__Arguments list Additional information for specified cursor type. This variable should not be accessed directly.
```
Methods:
```
```
SetCrossHairs() This function will set cursor type to CrossHair cursor.
```
```
SetRubberBand(point) This function will set cursor type to RubberBand cursor. Point specifies first point position.
```
```
SetRubberRectangle(point) This function will set cursor type to RubberRectangle. Point specifies first corner position.
```
```
SetRubberCircle(point) This function will set cursor type to RubberCircle. Point will specify centre of circle.
```
```
GetCursorType() This function will return current cursor type. It can be:
```
 'CrossHair'
 'RubberBand'
 'RubberRectangle'
 'RubberCircle'
```
SetDragCursor(highlight, point) This function will set cursor type to DragCursor.
```
 highlight
Instance of HighlightSet class containing drag cursor definition
 point
Point specifying cursor position.
```
Example:
```
```
center = KcsPoint2D.Point2D(0, 0)
```
```
Cursor = KcsCursorType.CursorType()
```
```
Cursor.SetRubberCircle(point)
```
```
print Cursor.GetCursorType()
```
Class KcsHighlightSet.HighlightSet
The class holds information defining drag cursor.
Parameters and attributes:
__Elements list List of elements defining highlight set.
```
Methods:
```
```
AddGeometry2D(element,
```
```
<linetype>)
```
Adds graphical 2D element to highlight set.
 element
instance of following classes: Arc2D, Contour2D, Point2D, Rrectangle2D
```
 linetype (KcsLinetype.Linetype )
```
optional parameter defining type of line used to draw the element
```
AddGeometry3D(element,
```
```
<handle>,<linetype>)
```
Adds graphical 2D element to highlight set.
 element
instance of following classes: Point3D, Polygon3D
```
 handle (KcsElementHandle.ElementHandle)
```
Handle to view in which element is drawn. If no handle given, element is drawn in all model views.
```
 linetype (KcsLinetype.Linetype )
```
optional parameter defining type of line used to draw the element
```
AddModel( model ) Adds model to highlight set.
```
```
 model (KcsModel.Model)
```
model information
```
AddSubpicture( handle ) Adds subpicture to highlight set.
```
```
 handle (KcsElementHandle)
```
handle to view, subview or component
```
Reset() Removes all elements from highlight set.
```
```
Example:
```
```
highlight = KcsHighlightSet.HighlightSet()
```
```
cursor = KcsCursorType.CursorType()
```
```
highlight.AddSubpicture( handle )
```
```
cursor.SetDragCursor( highlight, refpoint )
```
see also:
# Example: kcs_ex_ui1.py
Class KcsStat_point2D_req.Stat_point2D_req
The class holds information about point2D selection method.
Parameters and attributes:
__CursorType iCursorType Type of coursor. This variable should not be accessed directly.
__Point2dDefMode integer Point definition mode. This variable should not be accessed directly.
__HelpPoint Point2D Help point for ModeOffsetCurrent definition mode.
This attribute is optional.
__Scale Real Scale
```
Methods:
```
```
SetDefMode(mode) This function will set definition mode. Argument mode is a string that specifies point definition mode:
```
 'ModeKeyIn'
 'ModeCursor'
 'ModeNode'
 'ModeExist'
 'ModeSymbConnection'
 'ModeAuto'
 'ModeArcAtAngle'
 'ModeArcCentre'
 'ModeDistanceAlong'
 'ModeMidPoint'
 'ModeIntersect'
 'ModeOffsetCurrent'
 'ModeNearest'
 'ModeCOG'
 'ModeEvent'
These names are defined in KcsStat_point2D_req.Point2dDefModes dictionary.
```
GetDefMode() This function will return name of selected definition mode.
```
Look at KcsStat_point2D_req.Point2dDefModes dictionary for definition modes names.
```
SetCursorType(CursorType) This function will set cursor type to specified by CursorType instance of KcsCursorType.CursorType class.
```
```
GetCursorType() This function will return current cursor type as instance of KcsCursorType.CursorType class.
```
```
SetHelpPoint(point)
```
```
SetHelpPoint(None)
```
This function will set help point for ModeOffsetCurrent point definition mode.
```
Note: that user can select mode to ModeOffsetCurrent during selection so if this point will be None then mode will be greyed on point definitionmode toolbar.
```
```
Use SetHelpPoint(None) to delete existing help point.
```
```
GetHelpPoint() This function will return currently defined help point. If no point is defined it will return python None value.
```
```
SetScale(scale)
```
```
SetScale(None)
```
Set scale. If None scale will be fetched from current subpicture.
```
GetScale() Returns scale value.
```
```
Example:
```
```
CursorType = KcsCursorType.CursorType()
```
```
CursorType.SetRubberCircle(KcsPoint2D.Point2D(100, 100))
```
```
Status = KcsStat_point2D_req.Stat_point2D_req()
```
```
Status.SetCursorType(CursorType)
```
```
Status. SetDefMode('ModeOffsetCurrent')
```
```
Status.SetHelpPoint(KcsPoint2D.Point2D(0, 0))
```
```
point = KcsPoint2D.Point2D();
```
```
kcs_ui.point2D_req('Select point', point, Status)
```
```
print Status.GetDefMode()
```
```
Class KcsStat_point3D_req. Stat_point3D_req()
```
The class holds information about some initial status when defining a 3D point, using the point3D_req function.
```
Attributes:
```
Helpdef integer Help point defined?
```
= 0 No (default)
```
= 1 Yes
```
Helppnt Point3D The help point (if defined)
```
Lockstatic integer Initial lock protected?
```
= 0 No (default)
```
= 1 Yes
Locktype integer Type of lock:
```
= 0 No lock (default)
```
=1 Lock plane
= 2 Lock line
```
Lockpnt Point3D A point through the plane/line (if lock)
```
Lockvec Vector3D A vector perpendicular to the plane /
```
parallel to the line (normalised) (if lock)
```
Initial3D integer The initial way of defining the 3D point:
```
= 1 Pick line (by indicating in a view)
```
= 2 Key in
```
= 3 Indicate event point (default)
```
```
= 4 Offset from current (the help point)
```
```
Initial2D integer The initial way of defining a 2D point (used by Pick Line)
```
```
= 1 Key in (2D)
```
```
= 2 Cursor position (default)
```
= 3 End or node point
= 4 Existing point
= 5 Symbol connection
= 6 Auto point
= 7 Point on arc at angle
= 8 Arc centre
= 9 Point at distance along
= 10 Mid point
= 13 Intersecting point
= 20 Offset from current point
= 21 Closest segment point
= 22 Centre of gravity
```
= 23 Event point (2D)
```
```
Methods:
```
None
```
Examples (to enable lock line) :
```
```
status = KcsStat_point3D_req.Stat_point3D_req()status.Locktype = 2
```
```
status.Lockpnt = KcsPoint3D.Point3D(1000.0,2000.0,1500.0).Lockvec = KcsPoint3D.Point3D(1.0,0.0,0.0)
```
statusstatus.Initial3D = 1
status.Initial2D = 3 ## Pick line
## End/node point
Copyright © 1993-2005 AVEVA AB
4.7 Miscellaneous
These python classes are of miscellaneous types.
User's Guide Vitesse
```
Chapter: Python Classes
```
```
Class KcsTransformation3D.Transformation3D()
```
The class holds information about a 3D transformation matrix
```
Attributes:
```
Type integer Type of transformation matrix:
= 0 Unknown type of matrix
= 1 Matrix does not contain general scaling or projection
= 2 Matrix contains general scaling
= 3 Matrix contains projection
```
element(1,1) in the matrix
```
Matrix11 real
.
.
```
Matrix44 real element(4,4) in the matrix
```
```
Methods:
```
SetFromTransformation
Combine
GetByRow
SetByRow
SetFromPointAndTwoVectors
SetFromPointAndThreeVectors
Invert
ReflectX
ReflectY
ReflectZ
Rotate
Translate
```
Examples:
```
```
orig = KcsPoint3D.Point3D(0.0,0.0,0.0)Uvec = KcsVector3D.Vector3D(1.0, 0.0, 0.0)
```
```
Vvec = KcsVector3D.Vector3D(0.0, 1.0, 0.0)trvec = KcsVector3D.Vector3D(0.0, 1000.0, 2000.0)
```
```
trmat= KcsTransformation3D.Transformation3D()trmat. SetFromPointAndTwoVectors( orig, Uvec, Vvec)
```
```
trmat.Translate(trvec)
```
```
Class KcsStringlist.Stringlist(Initstring)
```
The class holds information about a list of strings.
```
Parameters:
```
Initstring string The first string in the list
```
Methods:
```
AddString
```
Examples:
```
```
str = 'First string'list = KcsStringlist.Stringlist(str)
```
```
str = 'Second string'list.AddString(str)
```
```
Class KcsSymbollist.Symbollist(FontId,SymbNo)
```
The class holds information about a list of symbols, each represented by an integer pair denoting the font identification and the symbol number within that font.
```
Parameters:
```
FontId integer First symbol: The font identification
SymbNo integer First symbol: The symbol number within the font
```
Methods:
```
AddSymbol
```
Examples:
```
```
fontid = 23symbno = 1
```
```
list = KcsSymbollist.Symbollist( fontid, symbno)
```
```
fontid = 66symbno = 16
```
```
list.AddSymbol(fontid, symbno)
```
```
Class KcsColour.Colour)
```
The class holds information about a specific colour. It is used in Vitesse functions i.e. colour_set in module kcs_draft or colour_select in module kcs_ui.
Parameters and attributes:
ColourString string The name of the colour
Valid colours are:
"White"
"Cyan"
"Blue"
"Magenta"
"Red"
"Yellow"
"Green"
"Black"
"Wheat"
"MediumAquamarine"
"NavyBlue"
"DarkOrchid"
"FireBrick"
"Orange"
"ForestGreen"
"DimGrey"
"Tan"
"Aquamarine"
"SlateBlue"
"Violet"
"IndianRed"
"Gold"
"LimeGreen"
"Grey"
"Sienna"
"Turquoise"
"LightBlue"
"BlueViolet"
"Pink"
"Coral"
"SpringGreen"
"LightGrey"
```
Constructor:
```
```
Colour (colourString) This constructor will create instance of Colour class. Parameter is defined as above.
```
Class protocols:
__repr__ Used to return string representation of Colour object.
```
Examples:
```
```
col1 = KcsColour.Colour("Violet")col1_str = col1.ColourString
```
```
col2 = KcsColour.Colour()col2.ColourString = col1_str
```
```
Class KcsLinetype.Linetype(LinetypeString)
```
The class holds information about a specific line type.
Parameters and attributes:
LinetypeString string The name of the line type.
```
Alias names can be used as well as system names. To get all linetype names use GetLinetypes() function in KcsLinetype module. It will return python dictionarycontaining pairs: system name - alias name. There are also two other useful functions in KcsLinetype module:
```
```
GetAliasName(name) - returns alias name for given system name,
```
```
GetSystemName(name) - returns system name for given alias name.
```
```
Methods:
```
SetName
Name
```
Examples:
```
# get system name for first alias name
```
aliases = KcsLinetype.GetLinetypes()
```
```
SysName = KcsLinetype.GetSystemName(aliases[0])
```
# create instances of Linetype class
```
lt1 = KcsLinetype.Linetype(SysName)
```
```
lt1_str = lt1.Name()
```
```
lt2 = KcsLinetype.Linetype()
```
```
lt2.SetName( lt1_str)
```
```
Class KcsModel.Model(Type,Name)
```
The class holds information about a specific model
Parameters and first two attributes:
Type string The model type.
Valid types are:
"plane panel"
"hull curve"
"pipe"
"pipe spool"
"equipment"
"cable way"
"cable"
"struct"
"placed volume"
"longitudinal"
"transversal"
"ventilation"
"subsurface"
"lines fairing curve"
"accommodation"
"curved panel"
"assembly"
Name string The model name.
Remaining attributes:
PartType string The model part type.
Valid types are:
"panel"
"boundary"
"hole"
"bracket"
"plate"
"notch"
"seam"
"stiffener"
"flange"
"pillar"
"bead"
"cutout"
"excess"
"hole/notch/cutout"
"point"
"curve"
"unknown"
PartId integer The model part ID
SubPartType string The model subpart type.
Valid types are:
""
"limit"
"crossmark"
SubPartId integer The model subpart ID
```
ReflCode integer Reflection code (relevant for Hull).
```
Valid codes are:
0 = not reflected
1 = reflected
```
Methods:
```
SetType
Type
SetName
Name
PartType
PartId
SubPartType
SubPartId
ReflCode
Class KcsModelDrawAssyCriteria. ModelDrawAssyCriteria
The class holds information about assembly that will be drawn.
Parameters and attributes:
__Name string Name of assembly object.
__Recursive integer Recursive/Parts mode flag.
__Criteria dictionary Selection criteria for model types.
```
Methods:
```
Class constructor: This constructor will create instance of
```
ModelDrawAssyCriteria(<name>)ModelDrawAssyCriteria class.
```
name - is an assembly name. This parameter is optional.
```
SetAssemblyName(name) Sets name of assembly object.
```
```
GetAssemblyName() Returns name of assembly object.
```
```
IsRecursive() Returns 1 if Recursive mode is selected. If it is 0 Parts mode is selected.
```
```
SetRecursive(mode) Sets mode flag to:
```
Recursive - if mode is 1
Parts - if mode is 0
```
EnableModelType(type, value) Enables(value=1) or disables(value=0) given model type. As type one of the following names should by used:
```
'PlanePanel', 'CurvedPanel', 'Pipe', 'Equipment', 'Cableway', Structure', 'PlacedVolume' or 'Ventilation'.
```
IsModelTypeEnabled(type) Returns 1 if given type is enabled, otherwise it will return 0.
```
```
Combine(transf) Performs combination of two transformations. Combines self with another transformation matrix given by transf which is another instance ofTransformation2D class.
```
```
Invert() Performs inversion of transformation matrix.
```
```
Example:
```
```
criteria = KcsModelDrawAssyCriteria. ModelDrawAssyCriteria ('BL-M902');
```
```
criteria.SetRecursive(1) # Recursive mode
```
```
criteria.EnableModelType('PlanePanel', 0)................ # Exclude PlanePanels from selection
```
```
kcs_draft.model_draw(criteria) .......................... # draw model
```
see also:
# Example: kcs_ex_draft33.py
```
Class KcsModelObjectRevision.ModelObjectRevision()
```
The class holds information about model object revision.
Parameters and attributes:
__revisionName string Name of revision
__revisionRemark string Revision remark.
__createdBy string Name of creator
__createdDate string Creation date
__modifiedBy string Name of modifier
__modifiedDate string Modified date
```
Methods:
```
```
setRevisionName(string) Sets __revisionName
```
```
getRevisionName() Returns __revisionName string
```
```
SetRevisionRemark(string) Sets __revisionRemark string
```
```
getRevisionRemark() Returns __revisionRemark string
```
```
getCreatedBy() Returns __createdBy string
```
```
getCreatedDate() Returns __createdDate string
```
```
getModifiedBy() Returns __modifiedBy string
```
```
getModifiedDate() Returns __modifiedDate string
```
```
Get() Returns tuple of__revisionName,
```
__revisionRemark,__createdBy,
__createdDate,__modifiedBy,
__modifiedDate
```
Examples:
```
```
revision = KcsModelObjectRevision.ModelObjectRevision()
```
```
revision.setRevisionName(revisionName)
```
See also:
# Example: kcs_ex_draft42.py
Class KcsObject.Object
The class holds information about database object.
Parameters and attributes:
__Name string Name of object.
__Code1 integer Object code 1.
__Code2 integer Object code 2
__DateTime DateTime Creation date and time.
```
__Size integer Size of object given in number of blocks (1 block = 512 bytes)
```
```
Methods:
```
Class constructor:
```
Object()
```
This constructor will create instance of Object class.
__cmp__ Used to compare two Object instances.
__repr__ Used to return string representation of Object instance.
```
SetName(string) Sets database object name.
```
```
GetName() Returns name of database object.
```
```
SetCode1(integer) Sets database object code 1.
```
```
GetCode1() Returns database object code 1.
```
```
SetCode2(integer) Sets database object code 2.
```
```
GetCode2() Returns database object code 2.
```
```
__SetSize(integer) For internal use only.
```
```
GetSize() Returns object size in blocks.
```
```
SetCreationDate(DateTime) Sets creation date.
```
```
GetCreationDate() Returns creation date as DateTime instance.
```
```
Example:
```
import KcsObject
```
a = KcsObject.Object(05, 10, 10, 00)
```
print a
```
a.SetName('SP162-2')
```
print a
see also:
# Example: kcs_ex_db01.py
Class KcsObjectCriteria.ObjectCriteria
The class holds information about database object selection criteria.
Parameters and attributes:
__Name string or None Name of object given with wildcards.
__Code1 integer or None Object code 1.
__Code2 integer or None Object code 2
__DateTime tuple or None Date and time criteria. Stored as:
1. (DateTime, DateTime)
2. (integer, DateTime)
3. None
__Size tuple or None Size criteria. Stored as:
1. (integer, integer)
2. None
```
Methods:
```
Class constructor:
```
ObjectCriteria()
```
This constructor will create instance of ObjectCriteria class. All criteria are set to None so all objects match criteria.
__cmp__ Used to compare two ObjectCriteria instances.
__repr__ Used to return string representation of ObjectCriteria instance.
```
SetName(string)
```
```
SetName(None)
```
Sets name criteria or deletes it.
```
GetName() Returns name criteria or None if not set.
```
```
SetCode1(integer)
```
```
SetCode1(None)
```
Sets code1 criteria or deletes it.
```
GetCode1() Returns code1 criteria or None if not set.
```
```
SetCode2(integer)
```
```
SetCode2(None)
```
Sets code2 criteria or deletes it.
```
GetCode2() Returns code2 criteria or None if not set.
```
```
SetSize(integer size)
```
```
SetSize(string type, integer size)
```
```
SetSize(None)
```
Sets size criteria:
1. Type will be set to '='
2. Size and type selected by user
3. Criteria will be deleted
Defined types for that criteria are in: ObjectCriteria.SignDefinition tuple.
```
GetSize() Returns tuple:
```
```
(string type, integer size)
```
or None if not defined.
```
SetCreationDate(DateTime start, DateTime end)
```
```
SetCreationDate(string type, DateTime date)
```
```
SetCreationDate(None)
```
Sets creation date criteria:
1. Between dates
2. Depending on type
3. No criteria
Defined types for that criteria are in: ObjectCriteria.SignDefinition tuple.
```
GetCreationDate() Returns tuple:
```
1. (DateTime, DateTime)
2. (string type, DateTime)
or None if not defined.
```
Example:
```
import KcsObjectCriteria
from KcsDateTime import DateTime
```
a = KcsObjectCriteria.ObjectCriteria()
```
print a
```
a.SetName("PLANE*")
```
```
a.SetCreationDate('>=', DateTime(2000, 10, 19, 23, 00, 00, 00))
```
```
a.SetSize('<', 100)
```
print a
see also:
# Example: kcs_ex_db01.py
```
Class KcsPrintOptions.PrintOptions(printername)
```
The class holds information about print options.
Parameters and attributes:
PrinterName string Printer name, empty means to use currently selected on
Orientation integer Page orientation,
0 - Currently selected
1 - Portrait
2 - Landscape
PrintToFile integer Activity of print-to-file option:
0 - print-to-file option set to false
1 - print-to-file option set to true
FileName String File name for print result if print-to-file option is active.
NoOfCopies integer Number of copies. If it is 0 than currently value will be used.
EffPrintArea integer Effective print area:
0 - Currently selected
1 - Drawing Form
2 - Drawing Extension
3 - Current Window
AutoOrient integer Auto-orientation flag:
0 - Use current state of flag
1 - Activate option
2 - Deactivate option
ScaleToFit integer Scale-to-fit flag:
0 - Use current state of flag
1 - Activate option
2 - Deactivate option
```
Scale real Scale value (valid only if Scale-to-fit is not selected):
```
Figure 4:1. 0 - Use current value
Figure 4:2. >0 - new value for scale
printername string Initial value for PrinterName
```
Methods:
```
SetPrinterName
GetPrinterName
SetOrientation
GetOrientation
SetPrintToFile
IsPrintToFile
SetNumberOfCopies
GetNumberOfCopies
SetEffectivePrintArea
GetEffectivePrintArea
SetAutoOrient
GetAutoOrient
SetScaleToFit
GetScaleToFit
SetScale
GetScale
SetFileName
GetFileName
```
Example:
```
```
options = KcsPrintOptions.PrintOptions('\\ntsvr7\p015');
```
```
options.SetOrientation(1)
```
```
options.SetScaleToFit(1)
```
```
kcs_draft.dwg_print(options)
```
see also:
# Example: kcs_ex_draft27.py
```
Class KcsTransformation2D.Transformation2D()
```
The class holds information 2D transformation.
Parameters and attributes:
__type integer Type of transformation matrix. It is for internal use so if any transformation methods will be added to this class take care of setting this variable to correctvalue.
0 = Undefined transformation
1 = Identity transformation
2 = Transformation may also consist of translations.
3 = Transformation may also consist of rotations.
4 = Transformation may also consist of uniform scalings.
5 = Transformation may also consist of reflections.
6 = Transformation may also consist of general scalings.
```
7 = Transformation may also consist of skews (shears).
```
8 = Transformation may also consist of parallel projection.
9 = Transformation may also consist of central projection.
__matrix list of reals Transformation matrix.
```
Methods:
```
```
__Set(Row, Col, Value) Sets matrix item at Row and Col to Value.
```
Row and Col must be value from 0 to 2.
```
__Get(Row, Col) Gets matrix item at Row and Col.
```
Row and Col must be value from 0 to 2.
```
__Decompose() Decomposes transformation matrix to linear transformations as: scale, rotation, translation etc.
```
```
IdentityTransf() Initializes identity matrix.
```
```
Translate(vector2D) Performs translation about vector vector2D which is an instance of Vector2D class.
```
```
Rotate(center, angle) Performs rotation about centre (instance of Point2D) and angle given in radians.
```
```
Scale(factor) Performs uniform scaling by given factor.
```
```
Reflect(point2D,vector2D)Performs reflection in a given line.
```
Line is given by point2D and direction vector vector2D.
```
Combine(transf) Performs combination of two transformations. Combines self with another transformation matrix given by transf which is another instance ofTransformation2D class.
```
```
Invert() Performs inversion of transformation matrix.
```
```
GetScale() Returns scale factors for x and y axis as tuple of two reals.
```
```
GetXYShear() Returns XY shear factor.
```
```
GetTranslation() Returns translation in x and y axis as tuple of two reals.
```
```
GetRotation() Returns rotation in radians.
```
```
GetReflection() Returns reflection factor.
```
```
Example:
```
```
transformation = KcsTransformation2D.Transformation2D();
```
```
center = KcsPoint2D.Point2D(10, 10)
```
```
angle = (3.1415/180) * 45........................... # 45 degrees
```
```
transformation.Rotate(center, angle)................ # rotate
```
```
transformation.Scale(2.0)........................... # and scale
```
```
kcs_draft.element_transform(handle, transformation). # transform element
```
see also:
# Example: kcs_ex_draft31.py
# Example: kcs_ex_draft34.py
```
Class KcsCaptureRegion2D.CaptureRegion2D()
```
The class holds information about 2D capture region. It is used in Vitesse capturing functions i.e. model_capture and geometry_capture in module kcs_draft.
Parameters and attributes:
Inside integer Side of capturing region. If 0 all inside of contour will be included, if 1 all outside will be included.
Cut integer Intersection flag. If 0 geometry intersecting the capturing region will not be included, if 1 geometry intersecting the capture region will be included.
Infinite integer Infinite flag. Set to 1 if region is infinite. Reset to 0 by SetRectangle and SetContour functions.
```
Rect integer Contour type flag. Set to 1 by SetRectangle function and reset to 0 by SetContour function (readonly as object variable).
```
```
Contour Contour2D Contour defining boundary of region. Set by SetRectangle and SetContour functions (readonly as object variable).
```
```
Constructor:
```
```
This constructor will create instance of CaptureRegion2D class (flags set to 1: Inside, Infinite, flags reset to 0: Cut, Rect).
```
```
CaptureRegion2D()
```
```
Methods:
```
```
SetRectangle (rect) Sets the region based on given rectangle. It sets Contour attribute with input rectangle contour, sets Rect flag to 1 and resets Infinite flag to 0.
```
rect Rectangle2D Capturing rectangle
```
SetContour (cont) Sets the region based on given contour. It sets Contour attribute with input contour, resets Rect and Infinite flags to 0.
```
cont Contour2D Capturing contour
Class protocols:
__repr__ Returns string representation of CaptureRegion2D object.
```
Example:
```
```
point1 = KcsPoint2D.Point2D(0, 0)
```
```
point2 = KcsPoint2D.Point2D(100, 100)
```
```
rectangle = KcsRectangle2D.Rectangle2D(point1, point2)
```
```
region = KcsCaptureRegion2D.CaptureRegion2D()
```
```
region.SetRectangle(rectangle)
```
region.Inside = 1
region.Cut = 0
```
Class KcsLayer.Layer(layerid)
```
The class holds information about layer element.
Parameters and attributes:
__LayerId
layerid
integer
integer
Layer id.
Initial value for __LayerId attribute.
```
Methods:
```
SetLayer
GetLayer
GetDescription
```
Example:
```
```
layer = KcsLayer.Layer(2)
```
```
print (layer.GetDescription())
```
```
Class KcsSymbol.Symbol(fontid, symbolid)
```
The class holds information about symbol element.
Parameters and attributes:
__Visible integer Visibility. If 1 symbol is visible, if 0 not.
__Detectable integer Detectability. If 1 symbol is detectable, if 0 not.
__Colour Colour Colour
__LineType LineType LineType
__Layer Layer Layer
__Position Point2D Position of symbol element.
__Height real Height of symbol element.
```
__Rotation real Rotation of symbol element (in degrees).
```
__Reflection integer Reflection of symbol element.
__SymbolId integer Symbol id of symbol element.
__FontId integer Font id of symbol element.
Fontid integer Initial value for __FontId attribute.
Symbolid integer Initial value for __SymbolId attribute.
```
Methods:
```
SetFontId
GetFontId
SetSymbolId
GetSymbolId
SetDetectable
IsDetectable
SetColour
GetColour
SetLineType
GetLineType
SetLayer
GetLayer
SetPosition
GetPosition
SetHeight
GetHeight
SetRotation
GetRotation
SetVisible
InVisible
SetReflectionInUAxis
IsReflectedInUAxis
SetReflectionInVAxis
IsReflectedInVAxis
SetNoReflection
IsReflected
```
Example:
```
```
symbolElement = KcsSymbol.Symbol(21, 2)
```
```
symbolElement.SetVisible(1)
```
```
reflectedInU = symbolElement.IsFeflectedInUAxis()
```
```
Class KcsText.Text(text)
```
The class holds information about text element.
Parameters and attributes:
__Visible integer Visibility. If 1 text is visible, if 0 not.
__Detectable integer Detectability. If 1 text is detectable, if 0 not.
__Colour Colour Colour
__LineType LineType LineType
__Layer Layer Layer
__Position Point2D Position of text element.
__Height real Height of text element.
```
__Rotation real Rotation of text element (in degrees).
```
__Aspect real Aspect ratio of text element.
__Slanting real Slant ratio of text element.
__Font string Font of text element.
__String string String of text element.
text string Parameter which defines initial __String value.
```
Methods:
```
SetString
GetString
SetVisible
IsVisible
SetDetectable
IsDetectable
SetColour
GetColour
SetLineType
GetLineType
SetLayer
GetLayer
SetPosition
GetPosition
SetHeight
GetHeight
SetRotation
GetRotation
SetAspect
GetAspect
SetSlanting
GetSlanting
SetFont
GetFont
```
Example:
```
```
text = 'example text'
```
```
textElement = KcsText.Text(text)
```
```
textElement.SetVisible(1)
```
```
aspect = textElement.GetAspect()
```
```
Class KcsDocumentReference. DocumentReference ()
```
The class holds information about document reference.
Parameters and attributes:
__Type integer Type of document reference. This member should be set only by SetType function.
__Document string Document name.
__Description string Document reference description
__Purpose Integer Purpose of the reference. In case if this is a drawing reference the purpose code should contain database where drawing is located. The database codecan be specified by kcs_draft constants.
```
Example:
```
```
SetPurpose(kcs_draft.kcsDWGTYPE_ASS_INSTR)
```
ReferenceTypes dictionary Dictionary mapping reference type string to its integer code.
```
Methods:
```
```
SetType(type) Sets document reference type. Argument type is a string. It can be one of values used as keys in ReferenceTypes dictionary:
```
 'unknown'
 'drawing'
 'file'
 'vitesse'
 'document'
```
GetType() Returns string representation of document reference type.
```
```
SetDocument(name) Sets __Document string.
```
```
GetDocument() Returns __Document string.
```
```
SetDescription() Sets __Description string.
```
```
GetDescription() Returns __Description string.
```
```
Example:
```
```
doc = KcsDocumentReference.DocumentReference();
```
```
doc.SetType('drawing')
```
```
doc.SetDocument('DwgTest1')
```
```
doc.SetPurpose(kcs_draft.kcsDWGTYPE_ASS_INSTR)
```
```
kcs_assembly.assembly_activate('-bl-m902-pipe')
```
```
kcs_assembly.assembly_reference_add(doc)
```
```
kcs_assembly.assembly_save()
```
see also:
# Example: kcs_ex_ass02.py
kcs_ex_pipe16.py
Class KcsInterpretationObject.SymbolicView
The class holds information about symbolic view
Parameters and attributes:
__ViewName string View name
__Looking constant Looking mode. Can be one of:
 SymbolicView.LOOKING_FOR
 SymbolicView.LOOKING_AFT
 SymbolicView.LOOKING_PS
 SymbolicView.LOOKING_SB
 SymbolicView.LOOKING_TOP
 SymbolicView.LOOKING_BOT
__PlaneType constant Plane type. Can be one of:
 SymbolicView.PLANE_BY_X
 SymbolicView.PLANE_BY_Y
 SymbolicView.PLANE_BY_Z
 SymbolicView.PLANE_BY_3POINTS
 SymbolicView.PLANE_BY_PANEL
 SymbolicView.PLANE_BY_CURVE
 SymbolicView.PLANE_BY_RSO
__Origin Point3D Origin point for plane definition
__UAxis Point3D Uaxis for plane definition
__VAxis Point3D Vaxis for plane definition
__DepthBefore real Depth before
__DepthAfter real Depth after
__ObjectName string Panel, curve or RSO object name
__CompType constant Object type. Can be one of:
 SymbolicView.TYPE_PANEL
 SymbolicView.TYPE_BRACKET
 SymbolicView.TYPE_STIFFENER
 SymbolicView.TYPE_FLANGE
__CompNo integer Number of component if object type different thanSymbolicView.TYPE_PANEL
__Reflect integer Reflection flag
__OnlyCurrent integer Only current panel flag
__LimMin Point3D Lower corner of box limits
__LimMax Point3D Upper corner of box limits
__ViewType constant View type. Can be one of:
 SymbolicView.VIEW_DESIGN
 SymbolicView.VIEW_ASSEMBLY
__ShellCurveType constant Shell curve type. Can be one of:
 SymbolicView.CURVE_EXISTING
 SymbolicView.CURVE_BY_NAME
 SymbolicView.CURVE_CUT
 SymbolicView.CURVE_NONE
__DrawRSO Integer Draw RSO flag
__ShellProfiles Integer Shell profiles flag
__ShellSeams Integer Shell seams flag
__DrawPlaneViews Integer Draw plane views flag
__DrawIntersections Integer Draw intersections flag
__AutomaticSelection Integer Automatic selection flag
__DrawAsPlate Integer Draw as plate flag
__PanelsFilter List List of panels
__PanelsExclude Integer Panels exclude flag
__BlocksFilter List List of blocks
__BlocksExclude Integer Blocks exclude flag
__ShellCurves List List of shell curves
__Assemblies List List of assemblies
```
Methods:
```
```
SetViewName(string) Sets to set view name.
```
```
GetViewName() Returns view name.
```
```
SetPlaneByX(real) Sets plane by X coordinate. X coordinate is stored in Origin point.
```
```
SetPlaneByY(real) Sets plane by Y coordinate. Y coordinate is stored in Origin point.
```
```
SetPlaneByZ(real) Sets plane by Z coordinate. Z coordinate is stored in Origin point.
```
```
SetPlaneBy3Points(Point3D, Point3D, Point3D) Sets plane by giving 3 points: origin, uaxis, vaxis.
```
```
SetPlaneByPanel(panel, object_type, reflect,onlycurrent)Sets plane giving panel name. Object type can be one of: see description of __CompType attribute. Reflect and only current aretrue/false flags.
```
```
SetPlaneByCurve(curve, reflect) Sets plane giving curve name. Reflect is a true/false flag.
```
```
SetPlaneByRSO(rsoobject, compno) Sets plane giving rso object name and component number.
```
```
GetPlaneType() Returns plane type. See description of __PlaneType attribute for possible values.
```
```
IsReflect() Returns status of __Reflect flag.
```
```
IsOnlyCurrent() Returns status of __OnlyCurrent flag.
```
```
GetComponentNo() Returns component number.
```
```
GetComponentType() Returns component type. See description of __CompType for possible values.
```
```
GetObjectName() Returns name of object (panel, curve, rsoobject)
```
```
SetLooking(looking) Sets looking mode. See description of __Looking attribute for possible values.
```
```
GetLooking() Returns looking mode. See description of __Looking attribute for possible values.
```
```
SetDepth(before, behind) Sets depth values.
```
```
GetDepth() Returns depth as tuple: (before, behind)
```
```
SetLimits(min3d, max3d) Sets box limits by two 3D points.
```
```
GetLimits() Returns box limits as tuple of two 3D points: (min3d, max3d)
```
```
SetViewType(viewtype) Sets view type. See description of __ViewType attribute for possible values.
```
```
GetViewType() Returns view type. See description of __ViewType attribute for possible values.
```
```
SetShellCurves(curvetype, curves=[]) Sets shell curves. See description of__ShellCurveType attribute for possible values of curve type. List of curves must be specifiedonly if type of curve is:
```
SymbolicView.CURVE_BY_NAME
```
GetShellCurveType() Returns curve type. See description of __ShellCurveType attribute for possible values.
```
```
GetShellCurves() Returns list of curve names.
```
```
SetDrawRSO(integer) Sets status of Draw RSO flag.
```
```
GetDrawRSO() Returns status of Draw RSO flag.
```
```
SetShellProfiles(integer) Sets status of Shell Profiles flag.
```
```
GetShellProfiles() Returns status of shell profiles flag.
```
```
SetShellSeams(integer) Sets status of Shell Seams flag.
```
```
GetShellSeams() Returns status of Shell Seams flag.
```
```
SetDrawPlaneViews(integer) Sets status of Draw Plane Views flag.
```
```
GetDrawPlaneViews() Returns status of Draw Plane Views flag.
```
```
SetDrawIntersections(integer) Sets status of Draw Intersections flag.
```
```
GetDrawIntersections() Returns status of Draw Intersections flag.
```
```
SetAutomaticSelection(integer) Sets Automatic Selection flag.
```
```
GetAutomaticSelection() Returns status of Automatic Selection flag.
```
```
SetDrawAsPlate(integer) Sets Draw As Plate flag.
```
```
GetDrawAsPlate() Returns status of Draw As Plate flag.
```
```
SetPanelsFilter(panels, exclude=0) Sets panels filter by list of panels name and exclude flag.
```
```
GetPanelsFilter() Returns status of panels filter. The method returns tuple: (list of panels names, exlude flag)
```
```
SetBlocksFilter(blocks, exlude=0) Sets blocks filter by list of blocks name and exclude flag.
```
```
GetBlocksFilter() Returns status of blocks filter. The method returns tuple: (list of blocks names, exlude flag)
```
```
SetAssemblies(assemblies) Sets assemblies list. Valid only for ASSEMBLY view.
```
```
GetAssemblies() Returns list of assemblies.
```
Class KcsInterpretationObject.CurvedPanelView
The class holds information about a curved panel view.
```
Parameters and attributes: ([]Default setting)
```
Seams integer Seams in view [1=Yes]/0=No
SeamNames integer Seam names in view [1=Yes]/0=No
Plates integer Plates in view [1=Yes]/0=No
Material integer Material specification in view 1=Yes/[0=No]
Stiffeners integer Stiffeners in view [1=Yes]/0=No
StiffNames integer Stiffener profile names in view 1=Yes/[0=No]
ShellStiffNames Integer Shell stiffener names in view 1=Yes/[0=No]
```
PartNames Integer Part names (stiffener) in view 1=Yes/[0=No]
```
Endcuts integer Display endcuts in view 1=Yes/[0=No]
Jigs integer Display jigs in view [1=Yes]/0=No
Heights integer Display jig heights in view 1=Yes/[0=No
FrameCurves integer Frame curves in view 1=Yes/[0=No]
FrameCurvesNames integer Names of frame curves in view 1=Yes/[0=No]
DirectionMarks integer Direction marks in view 1=Yes/[0=No]
HoleCrossMarks integer Hole crossmarks in view 1=Yes/[0=No]
```
Methods:
```
Property set/get methods.
```
SetSeams (integer)
```
```
GetSeams ()
```
```
SetSeamsNames (integer)
```
```
GetSeamsNames ()
```
```
SetPlates (integer)
```
```
GetPlates ()
```
```
SetMaterial (integer)
```
```
GetMaterial ()
```
```
SetStiffeners (integer)
```
```
GetStiffeners ()
```
```
SetStiffNames (integer)
```
```
GetStiffNames ()
```
```
SetEndcuts (integer)
```
```
GetEndcuts ()
```
```
SetJigs (integer)
```
```
GetJigs ()
```
```
SetHeights (integer)
```
```
GetHeights ()
```
```
Class KcsProjectCopyArg. ProjectCopyArg ()
```
The clas holds information about a 3D transformation matrix
```
Attributes:
```
__designStatus String Design Status
__manufactureStatus String Manufacture Status
__assemblyStatus String Assembly Status
__mtrlctrlStatus String Mtrlctrl Status
```
Methods:
```
GetDesignStatus
GetManufactureStatus
GetAssemblyStatus
GetMtrlctrlStatus
SetDesignStatus
SetManufactureStatus
SetAssemblyStatus
SetMtrlctrlStatus
```
Example:
```
```
a = ProjectCopyArg()
```
```
a.setDesignStatus(123)
```
```
a.setAssemblyStatus(456)
```
print a
Copyright © 1993-2005 AVEVA AB
4.8 Model
These python classes are used in connection with the kcs_model interface.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsCommonProperties. CommonProperties
The class holds information about model object.
Parameters and attributes:
TypeCode1 integer Type code
TypeCode2 integer Type code
TypeCode3 integer Type code
TypeCode4 integer Type code
PlanningUnit string Planning unit
Costcode string Cost code
Alias1 string Alias
Alias2 string Alias
Alias3 string Alias
Alias4 string Alias
Description string Description
Remarks string Remarks
```
Constructor:
```
```
CommonProperties() This constructor will create instance of CommonProperties class.
```
```
Methods:
```
```
SetTypeCode (no, code) Sets type code for given type code number
```
no integer Type code number
code integer Code to set
```
GetTypeCode() (integer, integer, integer, integer) Returns model type codes (from 1 to 4)
```
```
SetAlias (no, alias) Sets alias for number no
```
no integer Alias number
alias string Alias to set
```
GetAlias() (string, string, string, string) Returns model aliases (from 1 to 4)
```
Class protocols:
__repr__ Used to return string representation of CommonProperties object.
```
Example:
```
# kcs_ex_model04.py
Copyright © 1993-2005 AVEVA AB
4.9 Weld
These python classes are used in connection with the kcs_weld interface.
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsWeldTable.WeldTable
The class holds information about a weld table.
Parameters and attributes:
__WeldTableName String Name of weld table object
__WeldTableComment String Weld table comment
__TotalWeldLength Real Total weld length
__TotalSuspensionLength Real Total suspension length
__WeldedJoints list of WeldedJoint Welded joint data
```
Methods:
```
Class constructor: This constructor will create an instance of WeldTable class.
```
WeldTable()
```
```
SetWeldTableName(string) Sets weld table name
```
```
GetWeldTableName() Returns weld table name
```
```
SetWeldTableComment(string) Sets weld table comment
```
```
GetWeldTableComment() Returns weld table comment
```
```
SetTotalWeldLength(real) Sets the total weld length
```
```
GetTotalWeldLength() Returns total weld length
```
```
SetTotalSuspensionLength(real) Sets total suspension length
```
```
GetTotalSuspensionLength() Returns total suspension length
```
```
SetWeldedJoint(int,WeldedJoint) Sets the given welded joint
```
```
GetWeldedJoint(int) Returns the given welded joint
```
```
GetNumberWeldedJoints() Returns number of welded joints
```
```
AddWeldedJoint(WeldedJoint) Adds the welded joint
```
```
Example:
```
import KcsWeldTable
```
wt = KcsWeldTable.WeldTable()
```
```
wt.SetWeldTableComment("weld table comment")
```
Class KcsWeldedJoint.WeldedJoint
The class holds information about a welded joint.
Parameters and attributes:
__JointName string Name of joint
__JointComment string Joint comment
__WeldType string Weld type
__JointLength real Joint length
__SuspensionLength real Suspension length
__Assembly1 string Assembly name for first part
__Assembly2 string Assembly name for second part
__Part1 string First part
__Part2 string Second part
__Type1 integer Type for first part
__Type2 integer Type for second part
__Welds list of Weld Weld data
```
Methods:
```
Class constructor: This constructor will create an instance of WeldedJoint class
```
WeldedJoint()
```
```
SetJointName(string) Sets welded joint name
```
```
GetJointName() Returns welded joint name
```
```
SetJointComment(string) Sets welded joint comment
```
```
GetJointComment() Returns welded joint comment
```
```
SetWeldType(string) Sets weld type. Use one of the following types: 'fillet', 'butt'.
```
```
GetWeldType() Returns weld type
```
```
SetJointLength(real) Sets welded joint length
```
```
GetJointLength() Returns welded joint length
```
```
SetSuspensionLength(real) Sets welded joint suspension length
```
```
GetSuspensionLength() Returns welded joint suspension length
```
```
SetAssemblyName(int, string) Sets assembly name for the given part
```
```
GetAssemblyName((int) Returns assembly name for the given part
```
```
SetPartName(int, string) Sets name of the given part
```
```
GetPartName(int) Returns name of the given part
```
```
SetPartType(int) Sets type of the given part
```
```
GetPartType(int) Returns type of the given part
```
```
GetNumberWelds() Returns number of welds in welded joint
```
```
SetWeld(int, Weld) Sets the given weld
```
```
GetWeld(int) Returns the given weld
```
```
AddWeld(Weld) Adds the weld
```
```
Example:
```
import KcsWeldTable
import KcsWeldedJoint
```
wt = KcsWeldTable.WeldTable()
```
```
wj = wt.GetWeldedJoint( 1)
```
```
wj.SetJointComment("joint comment")
```
Class KcsWeld.Weld
This class holds information about a weld.
Parameters and attributes:
__WeldName string Name of weld
__WeldComment string Weld comment
__WeldLength real Weld length
__LegLength real Weld leg length
__Layers integer Number of weld layers
__Position string Weld position
__TestProcedure string Test procedure
__Process string Process
__StandardProcess string Standard process
__StartSuspension real Start suspension
__EndSuspension real End suspension
__ConnectionAngle real Connection angle
__RotationAngle real Rotation angle
__InclinationAngle real InclinationAngle
__TorchVector Vector3D Torch vector
__BevelPart1 real Bevel code, first part
__BevelPart2 real Bevel code, second part
__ThicknessPart1 real Thickness, first part
__ThicknessPart2 real Thickness, second part
__Geometry GeoContour3D Weld geometry
```
Methods:
```
```
ClassConstructor: This constructor will create an instance of Weld class
```
```
Weld()
```
```
SetWeldName(int, int) Set the weld name
```
```
GetWeldName() Returns the weld name
```
```
SetWeldComment(string) Sets weld comment
```
```
GetWeldComment() Returns weld comment
```
```
SetWeldLength(real) Sets the weld length
```
```
GetWeldLength() Returns weld length
```
```
SetLegLength(real) Sets weld leg length
```
```
GetLegLength() Returns weld leg length
```
```
SetLayers(int) Sets number of weld layers
```
```
GetLayers() Returns number of weld layers
```
```
SetPosition(string) Sets weld position
```
```
GetPosition() Returns weld position
```
```
SetTestProcedure(string) Sets weld test procedure
```
```
GetTestProcedure() Returns weld test procedure
```
```
SetProcess(string) Sets weld process
```
```
GetProcess() Returns weld process
```
```
SetStandardProcess(string) Sets weld standard process
```
```
GetStandardProcess() Returns weld standard process
```
```
SetStartSuspension(real) Sets start suspension
```
```
GetStartSuspension() Returns start suspension
```
```
SetEndSuspension(real) Sets end suspension
```
```
GetEndSuspension() Returns end suspension
```
```
SetConnectionAngle(real) Sets connection angle
```
```
GetConnectionAngle() Returns connection angle
```
```
SetRotationAngle(real) Sets rotation angle
```
```
GetRotationAngle() Returns rotation angle
```
```
SetInclinationAngle(real) Sets inclination angle
```
```
GetInclinationAngle() Returns inclination angle
```
```
SetTorchVector(Vector3D) Sets torch vector
```
```
GetTorchVector() Returns torch vector
```
```
SetBevelCode(int,real) Sets bevel code for the given part
```
```
GetBevelCode(int) Returns bevel code for the given part
```
```
SetThickness(int,real) Sets thickness for the given part
```
```
GetThickness(int) Returns thickness for the given part
```
```
Example:
```
import KcsWeldTable
import KcsWeldedJoint
import KcsWeld
```
wt = KcsWeldTable.WeldTable()
```
```
wj = wt.GetWeldedJoint( 1)
```
```
wld = wj.GetWeld( 1)
```
```
wld.SetWeldComment("weld comment")
```
```
wj.SetWeld( wld)
```
```
wt.SetWeldedJoint( 1, wj)
```
Copyright © 1993-2005 AVEVA AB4.10 Hull
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsBodyPlanViewOptions.BodyPlanViewOptions
The class holds information about Body plan View attributes.
Parameters and attributes:
BodyPlanName string Defines view name
```
bAutoSeams integer Auto Seams flag. If set, include all seams (longitudinal direction) and butts (transversal direction) inside the box.
```
bAutoLongTrace integer Auto Longitudal trace flag. If set, include traces of all profiles inside the box.
bAutoLongSection integer Auto longitudal section flag. If set, include cross-sections of all profiles inside the box
```
SurfacesFilter [ string ] List of surface for filtering (include/exclude depends on SurfacesExclude flag)
```
SurfacesExclude integer Surfaces exclude/include flag
Scale integer Defines view scale
AftLimits Point3d Defines coordinate of aft limit of the view
FwdLimits Point3d Defines coordinate of fwd limit of the view
bLooking constant Defines looking code. Can be one of:
```
LOOKING_PS = 1
```
```
LOOKING_SB = 2
```
```
LOOKING_FOR = 4
```
```
LOOKING_AFT = 3
```
```
LOOKING_TOP = 5
```
```
LOOKING_BOT = 6
```
LongSectionImage constant Defines how cross-sections of profiles should be drawn. Can be one of:
```
IMAGE_FULL = 0
```
```
IMAGE_MOULD = 1
```
```
IMAGE_THICK = 2
```
LongSectionFrame integer This attribute can be used to display the cross-section of the profiles at a single frame only.
```
DrawFrame integer Interval (number of frames) between sections to be drawn in the body plan view.
```
SeamColour colour Defines seam colour
LongColour colour Defines longitudal colour
FrameColour colour Defines frame colour
GridSpacing integer Defines grid spacing, if it should be drawn.
PanelFilter [ string ] Include/Exclude list
```
SeamsFilter [ string ] Include/Exclude list (depends on SeamsExclude flag)
```
SeamsExclude integer Except flag
```
TraceFilter [ string ] List of names of shell profiles whose traces will be included/excluded (depends on TraceExclude flag).
```
TraceExclude integer Except flag
```
SectionFilter [ string ] List of names of shell profiles whose sections will be included/excluded (depends on SectionExclude flag).
```
SectionExclude integer Except flag
```
SelectCurves dictionary Curve Name/LineType dictionary (name : line type). Line type must be defined in system.
```
```
Constructor:
```
```
BodyPlanViewOptions() This constructor will create instance of BodyPlanViewOptions () class.
```
```
Methods:
```
```
SetSection (image, frame) Sets longitudal section image and frame.
```
```
image constant Longintudal section image type (IMAGE_THICK, IMAGE_MOULD or IMAGE_FULL)
```
frame integer Longintudal section frame
```
GetSection () (constant, integer) Gets section image and frame (image, frame)
```
```
SetColours (long, seam, frame) Sets longitudal, seam and frame colours. Available colour strings are defined in KcsBodyPlanViewOptions.COLOURS table.
```
long colour Longitudal colour
seam colour Seam colour
frame colour Frame colour
```
GetColours () (Colour, Colour, Colour) Gets longitudal, seam and frame colours (long, seam, frame)
```
Class protocols:
```
__repr__ Used to return string representation of BodyPlanViewOptions() object.
```
Class KcsCopyPanOptions
The class holds information about Copy Panel Options : Inherits from KcsMovePanOptions
Parameters and attributes:
__Dictionary Dictionary Panel Names Dictionary
__BlockName string Block Name
```
Methods:
```
```
SetNameMapping (Ditcionary) Sets Dictionary used to change Panel Names. It defines names of panels to copy and names after copy operation.
```
Example call of Method:
```
SetNameMapping({'oldPanel' : 'newPanel'})
```
```
Where:
```
 OldPanel - is name of copied panel
 NewPanel - is name of panel created by copy function.
```
SetBlockName (string) Sets Block for copied Panel It defines name of block where panel will be copied.
```
Class KcsMovePanOptions
The class holds information about Move Panel Options
Parameters and attributes:
__LocationType Constant Type of Location. Can be one of:
```
PRINCIPAL_PLANE =1
```
```
THREE_POINTS =2
```
```
PLANE_OBJECT =3
```
__Coordinate Constant Defines Coordinate. Can be one of:
```
X =1
```
```
Y =2
```
```
Z =3
```
__RelativePosition Constant Defines Relative Position. Can be one of:
1 - Relative
0 - Not Relative
__CoordinateValue string Coordinate Value in String format
__Origin Point3D If defined by three points, Point of Origin
__Uaxis Point3D If defined by three points, Point of Uaxis
__Vaxis Point3D If defined by three points, Point of VAxis
__ObjectName string If Defined by Object, object name
```
Methods:
```
```
SetPrincipalPlane (integer, integer, string) Sets Principal Plane by giving cord, relpos, cordval. Example call:
```
```
SetPrincipalPlane(coordinate, relativePosition, coordinateValue)
```
```
Where:
```
coordinate - is coordinate definition, which defines plane of moving operation. See parameters and attributes definition.
relativePostion - is flag which defines if coordinateValue is relative postion or absolute. See parameters and attributes definition.
CoordinateValue - is, regarding to relativePosition flag, absolute coordinate value or relative coordinate value i.e. '1000' or 'FR1' .
```
SetThreePoints (Point3D, Point3D, Point3D) Sets three points by giving: origin, uaxis, vaxis
```
Defines moving operation by three points.
```
SetThreePoints(Origin, Uaxis, Vaxis)
```
```
Where:
```
Origin, Uaxis, Vaxis - are Point3D definitions in UVW coordinate sytem.
```
SetPlaneObject(string) Sets Plane Object by giving: name
```
Set moving operation by plane object where name is plane object name used to move panel.
Class KcsPanelSchema
The class contains functions operating on panel schema.
```
Methods:
```
```
SetValue(Group, Keyword, Value) Function to set value of keyword in panel schema statemen.
```
```
Parameters:
```
```
Group ( Integer/String ) : Index of statement in group or statement stringKeyword ( String ) : Name of keyword
```
```
Value ( String ) : Value of keyword
```
```
GetValue(Group, Keyword ) Function to get value of keyword in panel schema statement.
```
```
Group ( Integer/String ) : Index of statement in group or statement stringKeyword ( String ) : Name of keyword
```
```
Return value: ( String ) Value of keyword in given statement
```
Class KcsPanHoleOptions
The class holds information about PanHole Options.
Parameters and attributes:
__Axis Constant Defines axis by which hole is created:
```
BY_UNDEF = 0
```
```
BY_U = 1
```
```
BY_V = 2
```
```
BY_UV = 3
```
```
BY_X = 11
```
```
BY_Y = 12
```
```
BY_Z = 13
```
```
BY_YZ = 21
```
```
BY_XZ = 22
```
```
BY_XY = 23
```
```
BY_XYZ = 30
```
```
BY_X_Y_ZAP = 36
```
```
BY_X_YAP_Z = 34
```
```
BY_XAP_Y_Z = 32
```
```
BY_XRT = 40
```
```
BY_1 = 100
```
```
BY_2 = 200
```
```
BY_T = 500
```
____HasApprox Integer Defines if approximated coordinate.
0 - true
1- false
__Pt1 Point3D Defines the origin coordinates.
__Pt2 Point3D Defines the origin coordinates.
__AsStored integer Defines the origin of a hole "as stored".
This is used when the hole is created from an existing contour which has a transformation. The contour will be projected into the curved panel alongthe normal of the plane in which the countour is defined.
1 - true
0 - false
__Rotation Point3D In case of an asymmetrical hole, this defines the direction of the U-axis of the hole.
__Symm Constant Symmetry code.
```
SYMM_AS_PANEL = 0
```
```
SYMM_PS = 1
```
```
SYMM_SB = 12
```
__IsFictive integer Define if hole will be burnt or only marked.
1 - true
0 - false
__Develop integer Set the develop option for the hole.
1 - true
0 - false
__IsArbitrary integer Set the hole arbitrary, i.e. the hole designation is a curve.
1 - true
0 - false
__MarkType Constant Defines Marking Type
```
HOLE_MARK = 0
```
```
CROSS_MARK = 1
```
```
BOTH_MARK = 2
```
__CrossType Constant Defines Cross Type:
```
OVERHOLE_CROSS = 0
```
```
SMALL_CROSS = 1
```
```
SPECIAL_CROSS = 2
```
__MarkLen Float Defines Marking Length
```
Methods:
```
```
SetOriginAlongLine (Pt1, Pt2 ) Defines the origin of a hole in a curved panel, when defined "along line".
```
```
The (limited) line is defined by two 3d points. The origin will be the inersection point of the line and the panel.
```
```
Pt1 (Input). The start point of line intersecting the curved panel.
```
```
Pt2 (Input). The end point of the intersecting line.
```
```
SetOriginAlongAxis(Axis, Pt1,HasApprox)Defines the origin of a hole in a curved panel, when defined "along axis".
```
```
The (infinite)line is defined by two coordinates. The origin will be the intersection point of the line and the panel. An approximate coordinate must begiven. "Axis" selects which coordinate if "Pt1" is the approximate one.
```
```
Axis (Input). Selects the approximate coordinate
```
```
Pt1 (Input). The coordinates.
```
```
SetOriginAsStored(Axis, Pt1) Defines the origin of a hole "as stored". This is used when the hole is created from an existing contour which has a transformation. The contour will beprojected into the curved panel along the normal of the plane in which the countour is defined. You may given an approximate coordinate in case of
```
```
multiple intersection with the surface. Approx is: (axis+coordinate value)
```
```
SetDirection(Dir) In case of an asymmetrical hole, this selects the direction of the U-axis of the hole. "Dir" is either a vector or a point. Interpreted as a vector if thelength <= 1.0 If dir is a point the system will form a vector from origin the the point. The vector will then be projected into the tangent plane of the panel
```
```
( in the origin of the hole ).
```
```
Dir (Input). Point defining the direction of the U-axis of the hole.
```
```
SetArbitrary() Set the hole arbitrary, i.e. the hole designation is a curve.
```
```
SetFictive() Set "fictive" form the hole, ( A fictive hole will not be burnt, only marked.)
```
```
SetDevelop() Set the develop option for the hole.
```
```
SetMarkingType(type) Defines Marking Type
```
```
SetCrossType(self, type) Defines Cross Type
```
```
SetMarkLength(self, value) Defines Marking Length
```
```
GetOriginAlongLine(self) Gets the origin of a hole in a curved panel, when defined along line
```
```
GetOriginAlongAxis(self) Gets the origin of a hole in a curved panel, when defined along axis
```
```
GetOriginAsStored(self) Gets the origin of a hole in a curved panel
```
```
GetDirection(self) Gets Direction
```
```
GetDesign(self) Gets Design
```
```
IsFictive(self) Gets Fictive flag
```
```
IsDevelop(self) Gets Develop Flag
```
```
IsArbitrary(self) Gets Arbitrary Flag
```
```
GetMarkType(self) Gets Mark Type
```
```
GetCrossType(self) Gets Cross Type
```
```
GetMarkLen(self) Gets Mark Len
```
Class KcsRunModeOptions
The class holds information about planar hull scheme run mode options.
Parameters and attributes:
__ConfirmGeneration Integer Confirm generation option.
__TraceOn Integer Trace on option
```
Methods:
```
```
SetConfirmGeneration(Integer) Set Confirm Generation value.
```
Allowed values: [ 0,1, None ]
GetConfirmGeneration Get Confirm Generation value.
```
SetTraceOn (Integer) Set Trace On value.
```
Allowed values: [ 0,1, None ]
```
GetTraceOn () Get Trace On value.
```
Class KcsShPlateProp.ShPlateProp
The class holds information about a shell plate.
Parameters and attributes:
__PartList String An explicitly given parts list name.
__GPS_1 String General Purpose String.
__GPS_2 String General Purpose String.
__GPS_3 String General Purpose String.
__GPS_4 String General Purpose String.
__Surface Treatment String Surface Treatment.
__Destination String Destination.
```
__Thickness Float Material Thickness (inside).
```
```
__ThicknessOut Float Material Thickness (outside).
```
__Quality String Material Quality Code.
__Posno Integer Position Number.
__LaminateIn Integer Laminate code for inside of plate.
__LaminateOut Integer Laminate code for outside of plate. A value of 0 means same laminate code as for inside.
__LongitudinalShrinkage Float Longitudinal shrinkage.
__TransversalShrinkage Float Transversal shrinkage.
__RawPlate String Raw Plate Identification.
```
Methods:
```
GetDestination
GetGPS_1
GetGPS_2
GetGPS_3
GetGPS_4
GetLaminateIn
GetLaminateOut
GetLongitudinalShrinkage
GetPartsList
GetPosno
GetQuality
GetRawPlate
GetSurfaceTreatment
GetThickness
GetThicknessOut
GetTransversalShrinkage
SetDestination
SetGPS_1
SetGPS_2
SetGPS_3
SetGPS_4
SetLaminateIn
SetLaminateOut
SetLongitudinalShrinkage
SetPartsList
SetPosno
SetQuality
SetRawPlate
SetSurfaceTreatment
SetThickness
SetThicknessOut
SetTransversalShrinkage
ClassKcsShStiffProp.ShStiffProp
The class holds information about a shell stiffener.
Parameters and attributes:
_DummyInterval Integer = 1 The shell stiffener is a dummy interval.
_GPS_1 String General purpose string.
_GPS_2 String General purpose string.
_GPS_3 String General purpose string.
_GPS_4 String General purpose string.
_SurfaceTreatment String Surface treatment.
_Destination String Destination.
_UseStiffenerData Integer = 1 Use the profile data in this class.
= 0 Use the profile data in the shell profile this stiffener belongs to.
_Posno Integer Position number.
_PosnoPrefix String Position number prefix.
_PosnoSuffix String Position number prefix.
_Profile _Type
Profile type according to standards.
_Parameters
Profile parameters.
_Quality String Material quality code.
_End[0,1] _Connection
Connection code.
_Excess
Excess.
_Offset
The given length from the starting / ending point of the trace to the actual starting / ending point of the physical profile, measured as described below.This length should always be >=0.
_OffsetFrom
The physical end point of the shell stiffener will be located at a distance
_Offset from the plane described by
_OffsetFrom, measured perpendicularly to the plane.
Can be of type:
kcsCUTTING_PLANE
kcsFRAME_PLANE
kcsBUTTOCK_PLANE
kcsWATERLINE_PLANE
_EndCut
 _CalcWebAngle
The angle is calculated according to the values of _Connection.
 _CalcFrom
kcsCUTTING_PLANE
kcsFRAME_PLANE
kcsBUTTOCK_PLANE
kcsWATERLINE_PLANE
 _Type
End cut type.
 _Parameters
End cut parameters
_WebBevel
Bevel Code for profile web.
_FlaBevel
Bevel code for profile flange.
_InclAngle
Angle measure.
_InclAngelType
Angel type:
kcsX_AXIS,KcsY_AXIS,kcsZ-AXIs,
kcsPERPENDIUCULAR,
kcsPERP_WHOLe,
kcsCUTTING_PLANE
_TraceBevel Float Bevel code along the trace of this stiffener.
_Shrinkage Float Shrinkage of teh stiffener in millimeters per meter.
_FilletWeldDepth Float Depth of fillet weld when stiffener is mounted on a curved panel.
_Perpendicular Integer = 1 The stiffener is perpendicular to the surface at all positions along the trace.
= 0 Inclination is specified at both ends.
```
Methods:
```
GetDestination
GetDummyInterval
GetEnd1,GetEnd2 Get Connection
GetEndCut
GetCalcFrom
GetCalcWebAngle
GetParameter
GetType
SetCalcFrom
SetCalcWebAngle
SetParameter
SetTyp
GetExcess
GetFlaBevel
GetInclAngle
GetInclAngleType
GetOffset
GetOffsetFrom
GetWebBevel
SetConnection
SetExcess
SetFlaBevel
SetInclAngle
SetInclAngleType
SetOffset
SetOffsetFrom
SetWebBevel
GetFilletWeldDepth
GetGPS_1
GetGPS_2
GetGPS_3
GetGPS_4
GetPerpendicular
GetPosno
GetPosnoPrefix
GetPosnoSuffix
GetProfileParameter
GetProfileType
GetQuality
GetShrinkage
GetSurfaceTreatment
GetTraceBevel
GetUseStiffenerData
SetDestination
SetDummyInterval
SetFilletWeldDepth
SetGPS_1
SetGPS_2
SetGPS_3
SetGPS_4
SetPerpendicular
SetPosno
SetPosnoPrefix
SetPosnoSuffix
SetProfileParameter
SetProfileType
SetQuality
SetShrinkage
SetSurfaceTreatment
SetTraceBevel
SetUseStiffenerData
Class KcsShellXViewOptions
The class holds information about Shell Expansion View Options.
Parameters and attributes:
__ShellXName string Defines View Name
__DevelopedFromCode Constant Defines Coordinate. Can be one of:
```
X = 1
```
```
Y = 2
```
```
Z = 3
```
__DevelopedFromCoordinate Point3D Defines Developed From Coordinate
__SternLimtsCode string Defines Limits Code. Can be one of:
```
PLANE_BY_SEAMS = 1
```
```
PLANE_BY_X = -1
```
```
PLANE_BY_Y = -2
```
```
PLANE_BY_Z = -3
```
__SternLimitsSeams [ ] If defined by Seams, list of seams.
__SternLimitsCoordinate Point3D Defines Limits Coordinate.
__StemLimitsCode Point3D Defines Limits Code. Can be one of:
```
PLANE_BY_SEAMS = 1
```
```
PLANE_BY_X = -1
```
```
PLANE_BY_Y = -2
```
```
PLANE_BY_Z = -3
```
__StemLimitsSeams [ ] If defined by Seams, list of seams.
__StemLimitsCoordinate Point3D Defines Limits Coordinate.
__UpperLimitsCode Constant Defines Limits Code. Can be one of:
```
PLANE_BY_SEAMS = 1
```
```
PLANE_BY_X = -1
```
```
PLANE_BY_Y = -2
```
```
PLANE_BY_Z = -3
```
__UpperLimitsSeams [ ] If defined by Seams, list of seams.
__UpperLimitsCoordinate Point3D Defines Limits Coordinate.
__LowerLimitsCode Constant Defines Limits Code. Can be one of:
```
PLANE_BY_SEAMS = 1
```
```
PLANE_BY_X = -1
```
```
PLANE_BY_Y = -2
```
```
PLANE_BY_Z = -3
```
__LowerLimitsSeams [ ] If defined by Seams, list of seams.
__LowerLimitsCoordinate Point3D Defines Limits Coordinate.
__SideCode Constant Defines Side Code. Can be one of:
```
SIDE_PORT = 0
```
```
SIDE_STARBOARD = 1
```
__bExceptPanels Integer Except Flag
__SelectPanels [ ] Include/Exclude List
__bExceptBlocks Integer Except Flag
__SelectBlocks [ ] Include/Exclude List
__bExceptSeams integer Except Flag
__SelectSeams [ ] Include/Exclude List
__bExceptLongitudals integer Except Flag
__SelectLongitudals [ ] Include/Exclude List
__bExceptTransversals Integer Except Flag
__SelectTransversals [ ] Include/Exclude List
__SelectCurves Dictionary Select Curves Dictionary
```
Methods:
```
```
SetShelXViewName (string) Sets View Name
```
```
SetDevelopedFromX (Point3D) Sets plane defined by X coordinate
```
```
SetDevelopedFromY (Point3D) Sets plane defined by Y coordinate
```
```
SetDevelopedFromZ (Point3D) Sets plane defined by Z coordinate
```
GetShellXViewName Gets View Name
```
SetSternLimits Sets Limits defined by plane X, Y or Z) or seams and coordinate or seams list.
```
```
GetSternLimits Gets Stern Limits (code and coordinate or seam list)
```
```
SetStemLimits Sets Limits defined by plane X, Y or Z) or seams and coordinate or seams list.
```
```
GetStemLimits Gets Stem Limits (code and coordinate or seam list)
```
```
SetUpperLimits Sets Limits defined by plane X, Y or Z) or seams and coordinate or seams list.
```
```
GetUpperLimits Gets Upper Limits (code and coordinate or seam list)
```
```
SetLowerLimits Sets Limits defined by plane X, Y or Z) or seams and coordinate or seams list.
```
```
GetLowerLimits Gets Lower Limits (code and coordinate or seam list)
```
SetSideCode Sets Side Code.
GetSideCode Gets Side Code.
SetSelectPanels Sets select panels list.
GetPanels Gets select panels list
SetExceptPanels Sets except panels flag
SetSelectBlocks Sets select blocks list.
GetBlocks Gets select blocks list
SetExceptBlocks Sets except blocks flag
SetSelectLongitudals Sets select longitudals list.
GetLongs Gets select longitudals list
SetExceptLongitudals Sets except longitudals flag
SetSelectTransversals Sets select transversals list.
GetTrans Gets select transversals list
SetExceptTransversals Sets except transversals flag
```
SetLineTypes Sets dictionary with curves names and types (name : type)
```
GetCurves Gets dictionary with curves names and types.
Class KcsSplitPanOptions.SplitPanOptions
The class holds information about Split Panel Options
Parameters and attributes:
Plane3D Plane3D Cutting Plane used to split panel
PanelMapping [...] List of items defining new panels after split operation. Each item is an dictionary containing following keys:
'Name' - panel name
'Block' - block name
'SymetryCode' - symmetry code string
```
Constructor:
```
```
SplitPanOptions() This constructor will create an instance of SplitPanOptions class
```
```
Methods:
```
```
AddPanelMapping(PanelName, Block, Symetry)Define panel name, block and symmetry code for new panels generated by split operation. The function should be called once for each new panel.
```
PanelName String New panel name
Block <String> Panel block. If not defined panel block is remained.
Symetry <String> Panel symetry code. Possible values: 'S', 'P', 'SP', 'SBPS'. Default value is 'SBPS'.
Class protocols:
__repr__ Used to return string representation of SplitPanOptions object.
Copyright © 1993-2005 AVEVA AB
4.11 Volume
User's Guide Vitesse
```
Chapter: Python Classes
```
Class KcsVolPrimitiveBase. VolPrimitiveBase
The class holds information about properties of primitive.
Parameters and attributes:
Colour Colour Defines colour of primitive
Density real Defines density of primitive
Softness integer Defines softness of primitive
Class KcsVolPrimitiveBlock. VolPrimitiveBlock
The class holds information about Block Primitive.
Parameters and attributes:
```
Box Box (class ) Box defining the block
```
Class KcsVolPrimitiveGeneralCylinder. VolPrimitiveGeneralCylinder
The class holds information about General Cylinder Primitive.
Parameters and attributes:
Origin Point3D Origin point of the local uvw - coordinate system
UAxis Vector3D Define u-axis vector of the local coordinate system
VAxis Vector3D Defines v-axis vector of the local coordinate system.
Height real Define height of general cylinder to create. The height of the General Cylinder in the w direction.
ArcTol real Defines arc tolerance
Contour Contour2D Contour defining primitive, placed in u,v plane
Class KcsVolPrimitiveRevolution. VolPrimtiveRevolution
The class holds information about Revolution primitive.
Parameters and attributes:
Origin Point3D Origin point of the local uvw - coordinate system
UAxis Vector3D Define u-axis vector of the local coordinate system
ArcTol real Defines tolerance. Defines arc tolerance.
Contour Contour2D Defines the primitive's contour, which will be created in plane defined by u, v vectors.
Class KcsVolPrimitiveTorusSegment. VolPrimtiveTorusSegment
The class holds information about Torus segment Primitive.
Parameters and attributes:
ArcSeg Arc3D Defines Arc segment describing primitive
Radius Real Defines radius value
Class KcsArc3D.Arc3D
The class holds information about a 3D arc segment. It is used in Vitesse classes i.e. VolPrimtiveTorusSegment.
Parameters and attributes:
Start Point3d Start point of the arc segment
End Point3d End point of the arc segment
Amplitude real Amplitude of the arc segment
```
Methods:
```
None
Class protocols:
__repr__ Used to return string representation of Arc3D object.
```
Examples:
```
```
sp = KcsPoint3D.Point3D(0.0,0.0,0.0)ep = KcsPoint3D.Point3D(100.0,100.0,100.0)
```
```
ampl = 30.0arc = KcsArc3D.Arc3D(sp,ep,ampl)
```
Class KcsVolPrimitiveTruncatedCone. VolPrimitiveTruncatedCone
The class holds information about Truncated Cone Primitive.
Parameters and attributes:
Origin Point3D Origin point of the local uvw - coordinate system
UAxis Vector3D Define u-axis vector of the local coordinate system
Height real Define height of TruncatedCone in the u direction
BottomDiameter real Defines bottom diameter. The radius of the bottom circle.
TopDiameter real Defines top diameter. The radius of the top circle.
Class KcsVolPrimitiveSphericalCap. VolPrimitiveSphericalCap
The class holds information about Spherical Cap Primitive.
Parameters and attributes:
Origin Point3D Origin point of the local uvw - coordinate system.
UAxis Vector3D Define u-axis vector of the local coordinate system.
Amplitude real Define amplitude value
Radius real Defines radius value
Copyright © 1993-2005 AVEVA AB
5 Assembly
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
5.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_assembly. The functions are then referred to as kcs_assembly.<function name>.Before using a new function, please carefully read the function description.
The Vitesse Assembly interface contains functions for:
 Traversing the assembly structure.
 Creating, deleting and moving assembly nodes.
 Managing the attributes of an assembly.
 Collecting and decollecting model parts.
 Performing calculations like WCOG etc.
```
Note: Assembly nodes are identified by three types of identification which are used in different situations.
```
 Internal name, this is a unique name which is automatically generated by the system, example: _AS0000001234
 User given name, this is the name given by the user which must only be unique within the parent assembly, example: SBPH3. The top assembly has a fixed name, which is "-".
 Path name, this is the concatenation of all superior user given names together with the user given name of the indicated node, separated by "-" signs. This is very similar to a file
path, containing all superior directory levels, example: -BL4-WD23-SBPH3.
```
Note: Please note that the Path name must always begin with a "-", since this is the name of the top assembly node.
```
User's Guide Vitesse
```
Chapter: Assembly
```
Copyright © 1993-2005 AVEVA AB
5.2 Exception Handling
The Vitesse Assembly interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct ofthe Python language. The type of error can then be examined by checking the value of kcs_assembly.error. The exception is also displayed in the Vitesse Log window which is
available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Assembly
```
Copyright © 1993-2005 AVEVA AB
5.3 Functions
This chapter describes the functions in the kcs_assembly interface.
User's Guide Vitesse
```
Chapter: Assembly
```
```
assembly_activate(name)
```
Activates the given assembly. No assembly must be active.
Input parameters
name String Path name or internal name of the assembly to be activated.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
```
kcs_ValueError Delimiter missing in string (-) .
```
kcs_ModelNotFound Assembly was not found.
kcs_ModelLocked Assembly locked.
kcs_ModelIsCurrent An assembly is active.
```
assembly_exist(name)
```
Checks if the assembly with the specified path name exists.
Input parameters
name string Path name or internal name of the assembly.
Returned value:
[0] Integer 0 = Assembly does not exist
1 = Assembly exists
```
Exceptions:
```
```
assembly_new (parentName, name)
```
Creates a new assembly under the given parent. If no parent is given, the assembly will be created under the root assembly.
Input parameters
parentName String Path name or internal name of parent assembly.
name String Name of the assembly to be created. The parent path should not be included in this name.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid names.
```
kcs_ValueError Delimiter missing in string (-).
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_Error General error.
```
assembly_delete (name)
```
Deletes the given assembly. No assembly must be active. Note that all subordinate assemblies and model references also will be deleted.
Input parameters
name String Path name or internal name of the assembly to be activated.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing in string (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_ModelIsCurrent An assembly is active.
kcs_Error General error.
```
assembly_save()
```
Saves the active assembly.
Input parameters
None
Returned value:
None
```
Exceptions:
```
kcs_NoModelIsCurrent No active assembly to save.
kcs_Error General error.
```
assembly_cancel()
```
Cancels the changes to the active assembly.
Input parameters
Returned value:
```
Exceptions:
```
kcs_NoModelIsCurrent No active assembly to save.
kcs_Error General error.
```
assembly_move (newParentName)
```
Moves the active assembly and all subordinate assemblies and places it under the given new parent.
The involved assemblies, i.e. the assembly moved, its former parent and its new parent, are stored and scratched from internal workspace.
Input parameters
NewParentName String Path name or internal name of new parent.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid names
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_ModelIsCurrent Any assembly active.
kcs_Error General error.
```
assembly_parent_get (name)
```
Returns the name of the parent of the given assembly.
Input parameters
Name String Path name or internal name of the assembly whose parent should be returned.
Returned value:
[0] String Path name of parent assembly
[1] string Internal name of parent assembly.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing in string (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_Error General error.
```
assembly_sub_get(name)
```
Returns the name of the subordinates assembly to the given assembly.
Input parameters
Name String Path name or internal name of the assembly.
Returned value:
[0] String List path name of subordinates assembly. If empty string list is returned, no subordinateassemblies exist.
[1] string List internal name of subordinates assembly. If empty string list is returned, no subordinateassemblies exist.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_Error General error.
```
assembly_model_ref_get (name)
```
Returns the list of model reference of the given assembly.
Input parameters
name string Path name or internal name of assembly.
Returned value:
[0] KcsModel.Model List of model class instance containing the identification of the model.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_ModelIsCurrent Assembly is active.
kcs_Error General error.
kcs_PythonMethodNotFound Python class method not found.
```
assembly_keyin_ref_get (name)
```
Returns the list key-in reference for the assembly.
Input parameters
name string Path name or internal name of assembly.
Returned value:
[0] KcsModel.Model KcsAssemblyKeyInItem.AssemblyKeyInItemList of KcsAssemblyKeyInItem class instance containing the identification of the model.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_ModelIsCurrent Assembly is active.
kcs_Error General error.
kcs_PythonMethodNotFound Python class method not found.
```
assembly_properties_get(<name>)
```
Returns the properties for the given assembly or if not given the currently active assembly.
Input parameters
name string Path name or internal name of assembly.
Returned value:
[0] KcsAssembly. Assembly Assembly class instance containing the properties of the assembly.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing (-)
```
kcs_ModelNotFound Parent not found.
kcs_ModelLocked Assembly locked.
kcs_NoModelIsCurrent No active assembly.
kcs_Error General error.
kcs_PythonMethodNotFound Python class method not found.
kcs_PythonLibraryNotFound Python library not found.
```
assembly_properties_set (assembly)
```
Sets the properties for the active assembly.
Input parameters
assembly KcsAssembly.Assembly Instance of KcsAssembly class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid names
kcs_NoModelIsCurrent No active assembly.
kcs_Error General error.
kcs_PythonMethodNotFound Python class method not found.
```
Note: Function assembly_properties_set and assembly_properties_get requires that the _TB_ASS_DEFAULT object is stored on the assembly databank (SB_ASSDB). This object(and the level definitions) can be created with the utility program ph015.
```
```
assembly_wcog_calc()
```
Calculates the weight and centre of gravity for the current assembly.
Input parameters
None.
Returned value:
None
```
Exceptions:
```
kcs_NoModelIsCurrent No active assembly
kcs_Error General error.
```
model_collect(model)
```
```
model_collect(keyin)
```
Collects the model object, model part or key-in part indicated by the supplied model or key-in class to the current assembly.
Input parameters
Model KcsModel.Model Instance of KcsModel.Model class that identifies the object or part to be collected.
KeyIn KcsAssemblyKeyInItem. AssemblyKeyInItem Instance of KcsAssemblyKeyInItem class that identifies the object or part to be collected.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing(-)
```
kcs_NoModelIsCurrent No active assembly
kcs_ItemAlreadyExists Part reference already exists
kcs_Error General error
kcs_PythonMethodNotFound Python class method not found
```
model_decollect(model)
```
```
model_decollect(keyin)
```
Decollects the model object, part or key-in part indicated by the supplied class from the current assembly.
Input parameters
Model KcsModel.Model Instance of KcsModel.Model class that identifies the object or part to be decollected.
KeyIn KcsAssemblyKeyInItem. AssemblyKeyInItem Instance of KcsAssemblyKeyInItem class that identifies the object or part to be decollected.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid names
kcs_NoModelIsCurrent No active assembly to save
kcs_PartNotFound Part not found
kcs_PythonMethodNotFound Python class method not found
```
assembly_internal_name_get(pathName)
```
Returns the internal name for the given assembly.
Input parameters
pathName string Path name of assembly.
Returned value:
[0] string Internal name of assembly.
kcs_ArgumentError Invalid names
kcs_ModelNotFound Assembly not found
kcs_Error General error.
```
assembly_path_name_get(internalName)
```
Returns the path name for the given assembly.
Input parameters
InternalName string Internal name of assembly.
Returned value:
[0] string Path name of assembly.
```
Exceptions:
```
kcs_ArgumentError Invalid names
kcs_Error General error.
```
assembly_path_name_create(parentName, name)
```
Returns the path name for an assembly.
Input parameters
ParentName String Path name of parent assembly.
name string Name of assembly.
Returned value:
[0] String Path name of assembly.
```
Exceptions:
```
kcs_ArgumentError Invalid names
```
kcs_ValueError Delimiter missing (-)
```
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_ass01.py
```
document_reference_get()
```
The function returns a list of document references associated with the active assembly.
Input parameters
None
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active assembly not set
kcs_GeneralError List of result can't be created for some internal reason
```
document_reference_add(docRef)
```
The function adds a document reference to the active assembly object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active assembly not set
```
document_reference_remove(docRef)
```
The function removes document reference from active assembly object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active assembly not set
kcs_DoesNotExist Assembly document reference doesn't exist
Copyright © 1993-2005 AVEVA AB
6 Cable
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
6.1 General
The Vitesse Cable interfaces includes functions for handling Cables, Cableways and Cable Penetrations. The interfaces are available by import kcs_cable.
User's Guide Vitesse
```
Chapter: Cable
```
Copyright © 1993-2005 AVEVA AB
6.2 Exception Handling
The Vitesse Cable interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_cable.error. The exception is also displayed in the Vitesse Log window which is available by
the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Cable
```
Copyright © 1993-2005 AVEVA AB
6.3 Cable Functions
This chapter describes the functions in the kcs_cable interface..
User's Guide Vitesse
```
Chapter: Cable
```
```
cable_exist (system, name)
```
This function checks if a specified cable exists.
Input parameters
System String System name of cable.
Name String Name of cable.
Returned value:
[0] Integer 1 if it exists, 0 if not
```
Exceptions:
```
None.
```
cable_new (system, name)
```
Create a new cable.
Input parameters
System String System name of cable.
Name String Name of cable.
Returned value:
[0] Integer 1 if it exist 0 is not
```
Exceptions:
```
kcs_Error General error.
kcs_ItemAlreadyExists The cable does already exist.
kcs_ArgumentError Invalid arguments list.
kcs_AccessDenied User is not authorized to create cable.
```
cable_activate (system, name)
```
Activate an existing cable.
Input parameters
System String System name of cable.
Name String Name of cable.
Returned value:
None
```
Exceptions:
```
kcs_Error General error.
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelIsCurrent Another cable is already current.
kcs_ArgumentError Invalid arguments list.
kcs_AccessDenied User is not authorized to activate cable.
```
cable_delete(system, name)
```
Delete a cable. Connections are automatically removed.
Input parameters
System String System name of cable.
Name String Name of cable.
Returned value:
None.
```
Exceptions:
```
kcs_Error General error.
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelIsCurrent Cable is current.
kcs_ArgumentError Invalid arguments lists.
kcs_AccessDenied User is not authorized to create cable
```
cable_cancel()
```
Cancel modifications on current cable.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Error General error.
kcs_NoObjectActive No cable is current.
```
cable_save()
```
Save current cable.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Error General error.
kcs_NoObjectActive No cable is current.
```
cable_ready()
```
Save current cable with ready checks.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoObjectActive No cable is current
kcs_NoLength Length could not be calculated
kcs_CwayNotValid The status of referred cableways was not OK
kcs_ModelNotConnected The cable was not connected
kcs_IllegalFunction Cable transfer to PDI failed
kcs_Error General error
```
cable_system_get()
```
Returns the system of current cable.
Input parameters
None.
Returned value:
[0] String. Name of system.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoObjectActive No cable is current.
kcs_Error General error.
```
cable_name_get()
```
Returns the name of current cable.
Input parameters
None.
Returned value:
[0] String. Name of cable.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoObjectActive No cable is current.
kcs_Error General error.
```
cable_component_set (component name)
```
Set component reference to the cable component.
Input parameters
Component. String. Name of component.
Returned value:
[None.
```
Exceptions:
```
kcs_ComponentInvalid Component does not exist or is of wrong type.
kcs_NoObjectActive No cable is current.
kcs_Error General error.
```
cable_equipment_connect(equipment name, connection)
```
Connect the cable in end 'connection' to the equipment in the product model. The equipment shall not be current or locked by another user.
Input parameters
Equipment String Name of equipment
Connection Integer 1 is start and 2 is end point of cable.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments lists.
kcs_ReferenceNot Found Equipment is not found or locked.
kcs_ReferenceInvalid The equipment can not be connected by other reasons
kcs_NoObjectActive No cable is current.
kcs_IllegalFunction The cable end is already connected.
kcs_Error General error.
```
cable_equipment_disconnect(connection)
```
Disconnected the cable in end 'connection' to the equipment in the product model. The equipment shall not be current or locked by another user.
Input parameters
Connection. Integer. 1 is start and 2 is end point of cable.
Returned value:
None.
```
Exceptions:
```
kcs_ReferenceNot Found Equipment is locked.
kcs_NoObjectActive
No cable is current.
kcs_IllegalFunction The cable end is not connected.
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_cable_01.py
# Example: kcs_ex_cable_02.py
```
cable_document_reference_get ()
```
The function returns a list of document references associated with the active cable.
Input parameters
None.
Returned value:
[0] list List of DocumentReference instances.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active cable not set
kcs_GeneralError List of result can't be created for some internal reason.
```
cable_document_reference_add (docRef)
```
The function adds a document reference to the active cable object.
Input parameters
DocRef DocumentReference. Instance of Python DocumentReference class.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active cable not set
```
cable_document_reference_remove (docRef)
```
The function removes document reference from active cable object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference. Instance of Python DocumentReference class.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active cable not set
kcs_DoesNotExist Cable document reference doesn't exist.
```
cable_markpoint_set (mark point name)
```
Set mark point information to the current cable. Please note that any penetration can be used without any error but the general check function, when saving the cable, will only keep realpenetration passed y the cable route. Only two mark points can be defined.
Input parameters:
mark point name String Name of penetration
Returned value:
None.
```
Exceptions:
```
kcs_NoObjectActive No cable is current
kcs_Error General error, example to may markpoints
Copyright © 1993-2005 AVEVA AB
6.4 Cableway Object Functions
This chapter describes methods to handle the cableway on object level in the kcs_cable interface.
User's Guide Vitesse
```
Chapter: Cable
```
```
cway_exist (name)
```
The function returns true or false depending on if the cableway exists.
Input parameters
Name. String. Name of cableway.
Returned value:
[0] Integer. 1 if it exists, 0 if not.
```
Exceptions:
```
None.
```
cway_name_get()
```
Returns name of current cableway.
Input parameters
None.
Returned value
[0] String Name of cableway.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway is current.
kcs_Argument Error Invalid arguments list
```
cway_new (name, module, colour)
```
Create a new cableway. The cableway will be current. The cableway will be green if the colour is invalid.
Input parameters
Name String Name of cableway.
Module String Name of module.
Colour String String defining the colour.
Returned value:
None.
```
Exceptions:
```
kcs_Error General error.
kcs_ItemAlreadyExists The cable does already exist.
kcs_ModelIsCurrent Another cable is already current.
kcs_ModuleNotFound The module not found.
kcs_NameInvalid Model name has invalid syntax
kcs_ArgumentError Invalid arguments list.
```
cway_activate (name)
```
Activate an existing cableway.
Input parameters
Name. String. Name of cableway.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelIsCurrent Another cableway is already current.
```
cway_delete(name)
```
Delete a cableway. No cableway shall be current. No cables are allowed to be routed on it. Penetrations defined on cableway will be removed.
Input parameters
Name. String. Name of cableway.
Returned value:
None.
```
Exceptions:
```
kcs_Error General error.
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelIsCurrent Another cableway is already current.
kcs_CableRouted Cables are routed on the cableway.
kcs_ReferenceLock Object has assembly, cableway or penetration references.
kcs_ArgumentError Invalid arguments list.
```
cway_cancel()
```
Cancel modifications on current cableway.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway is current.
kcs_ArgumentError Invalid arguments list.
```
cway_save()
```
Save current cableway.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway is current.
kcs_AccessDenied User is not authorized to save current cableway.
kcs_ArgumentError Invalid arguments list.
```
cway_ready()
```
The current cableway will be checked against user defined settings. The cableway will be saved in db and transferred to PDI if this is set up.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway is current.
kcs_NoPlanningUnit The planning unit is not valid.
kcs_NoPositionNumber The user has not assigned a position number to cableway, or it is duplicated.
kcs_NoAssembly No assembly reference defined.
kcs_IllegalFunction The system setup says that the cableway should be transferred to PDI but it failed.
kcs_ArgumentError Invalid arguments list.
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_cway_01.py
# Example: kcs_ex_cway_02.py
```
cway_document_reference_get ()
```
The function returns a list of document references associated with the active cableway.
Input parameters
None.
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active cableway not set
kcs_GeneralError List of result can't be created for some internal reason
```
cway_document_reference_add (docRef)
```
The function adds a document reference to the active cableway object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active cableway not set
```
cway_document_reference_remove (docRef)
```
The function removes document reference from active cableway object. If there are more than one document reference, the first found will be deleted
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active cableway not set
kcs_DoesNotExist Cableway document reference doesn't exist
Copyright © 1993-2005 AVEVA AB
6.5 Cableway Default and Modelling Functions
This chapter describes methods for modelling the cableway using the kcs_cable interface.
User's Guide Vitesse
```
Chapter: Cable
```
```
default_value_set (statement)
```
These functions are used to set and get the default values valid in cable modelling.
Input parameters
Statement. String. Starement string in format 'KEYWORD=VALUE'.
Returned value:
None.
```
Exceptions:
```
```
kcs_ArgumentError Invalid parameter value (more than 80 characters or invalid format).
```
kcs_DefKeywordInvalid Invalid default keyword.
kcs_DefValueInvalid Invalid default value.
```
default_value_get (statement)
```
The function gets given default value.
Input parameters
Statement. String. The default keyword.
Returned value:
```
[0] String. The default statement (: is delimiter).
```
```
Exceptions:
```
kcs_DefKeywordInvalid Invalid default keyword.
kcs_ArgumentError Invalid argument format.
```
cway_cwenv_clear ()
```
Reset the list of cableways allowed to connect to.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invallid arguments list.
```
cway_cwenv_incl (name)
```
Add a cableway to the list of cableways allowed to connect to.
Input parameters
```
Name. String. Name of cableway (without project name).
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound The cableway is not found.
kcs_ItemAlreadyExists The cableway is already on the list.
```
cway_cwenv_connect ( )
```
The current cableway is connected to other cableways in the environment.
Input parameters
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
kcs_IllegalFunction No cableways selected in the environment
```
cway_transform ( T )
```
Transform current cableway.
Input parameters
T. kcstransformation3D. Transformation matrix.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
kcs_MatrixInvalid The values in the matrix was invalid.
kcs_ReferenceInvalid The cableway could not be used since it had references to other objects that not could be updated.
```
cway_duplicate (from cableway)
```
All parts of given cableway will be copied into current. No parts shall be defined in current cableway before calling this function.
Input parameters
from. String Name of cableway to copy from.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
kcs_ModelNotFound The cableway to copy from was not found.
kcs_IllegalFunction The current cableway was not empty or the cableway to copy from was empty.
```
cway_route_start_point ( <point> )
```
The method scratches the preliminary route and optionally adds the point to it.
```
cway_route_start_point() - only initialises the routing process, and clears the list of route points (routingsequence).
```
```
cway_route_start_point(point) - does the initialisation as above, additionally adds the first point to the routing sequence, so that: cway_route_start_point (point) is an equivalent ofcway_route_start_point()
```
```
cway_route_point(point)
```
Input parameters
```
point. Point3D A 3D coordinate point. (May be omitted) .
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
```
cway_route_point ( point )
```
Intermediate point in route sequence.
Input parameters
Point. Point3D A 3D coordinate point.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_PointInvalid Point is the same as previous one.
kcs_NoModelIsCurrent No cableway was current.
```
cway_route_end_point ( <point> )
```
The preliminary route will be added to the current cableway.
```
cway_route_end_point() - marks the routing process as finished, and does not modify the routing sequence, as defined so far.
```
```
cway_route_end_point(point) - first adds another (final) point to the routing sequence, and additionally does the finalisation as above, so that:
```
```
cway_route_end_point(point) is an equivalent of:
```
```
cway_route_point(point) cway_route_end_point()
```
Input parameters
Point. Point3D A 3D coordinate point.
Returned value:
[0] Integer Id of the first part that has been created by this statement.
[1] Integer Id of the last part that has been created by this statement.
[2] Integer Direction,
+1 means that the id[0] is stored before id[1] in the cableway model.
-1 is the opposite,
0 is only one part created.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
kcs_PointInvalid No enough point given to create a part.
```
cway_route_delete ( start_id, end_id )
```
Delete part of cableway route in current cableway.
Input parameters
Start_id Integer Id of part to start delete.
End_id Integer Id of part to end delete.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelIsCurrent No cableway was current.
kcs_ReferenceInvalid The parts could not be deleted since the path defined by them referred to other objects, cables or cableways, that not could be updated.
kcs_PartNotFound The parts was not found.
kcs_CableRouted Cableway had cables routed.
kcs_IllegalFunction The parts did not belong to the same branch.
```
cway_material_set ( start_id, end_id, straight_material, <bend_material>,<start_distance>, <intermediate_distance>, <end_distance> )
```
Start, end and straight given:
The branch piece will be dressed with straight material.
Start, end, straight and bend given:
The corners will be dressed with bent material, the rest with straight. Parameter straight may be empty string.
Start, end, straight, bend, start_distance orStart, end, straight, bend, start_distance and intermediate:
As previous case but a distance after each straight part will be reserved for frame. Parameter bent may be empty string.
Start, end, straight, bend, start_distance intermediate and end distance given:
As previous case but a distance first and last in branch is reserved for frame. Parameter bent may be empty string and intermediate may be 0.
```
Note: Please note also that this function will create new parts if the length exceeds the material length, see result parameters.
```
Input parameters
Start_id Integer Id of part to start dress.
End_id Integer Id of part to end dress.
Straight String Component defining the straight material.
Bend String Component defining the bent material.
Start_dist Real Length of frame part in first end.
Interm_dist Real Intermediate distance between the straight parts.
End_dist. Real Distance between start and end point to first material part.
Returned value:
[0] Integer Id of the first part that has been dressed.
[1] Integer Id of the last part that has been dressed.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway was current.
kcs_ComponentInvalid The component was not found or the fill level was exceeded.
kcs_AreaInvalid Material area too small.
kcs_FrameInvalid No parts dressed depending components and shape.
kcs_PartIsDressed Pars already dressed.
kcs_IllegalFunction The parts did not belong to the same branch or parts not found.
kcs_ValueError The distance values were invalid.
kcs_ArgumentError Invalid arguments list.
```
cway_material_rotate ( part_id, angle )cway_material_rotate ( part_id, vector )
```
1. Rotate cableway material, a specific part about an angle.
2. Rotate cableway material, a specific part about a vector
Input parameters
Part_id Integer Id of part to rotate.
Angle Real Angle in degrees
Vector Vector 3D Vector used to define the rotation of material.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
kcs_ComponentInvalid No straight component was found to be rotated.
kcs_PartNotFound The parts was not found.
kcs_IllegalFunction The parts did not belong to the same branch.
```
kcs_ValueInvalid The angle (or vector) was invalid.
```
```
cway_material_remove (start_id, end_id,)
```
The material from start_id until end_id is removed on current cableway.
Input parameters:
Start_id Integer Id of part to start undress
End_id Integer Id of part to end undress
Returned value:
None
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway was current
kcs_IllegalFunction The parts did not belong to the same branch or parts not found.
kcs_ArgumentError Invalid arguments lists
```
cway_material_rotate_branch ( part_id, angle )cway_material_rotate_branch ( part_id, vector )
```
1. Rotate all cableway material belonging to a straight part of the branch identified by a part about an angle.
2. Rotate all cableway material belonging to a straight part of the branch identified by a part about a vector.
After this operation all parts of the branch are in the same plane.
Input parameters
Part_id Integer Id of part that identifies part of branch to rotate.
Angle Real Angle in degrees.
Vector Vector 3D Vector used to define the rotation of material.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway was current.
kcs_ComponentInvalid No straight component was found to be rotated.
kcs_PartNotFound The parts was not found.
kcs_IllegalFunction The parts did not belong to the same branch.
```
kcs_ValueError The angle (or vector) was invalid.
```
```
cway_check_cables()
```
Returns the number of cables placed on the cableway.
Input parameters
None.
Returned value:
[0] Integer Number of cables placed on the cableway.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
```
cway_remove_cable(<cable system>, <cable name>)
```
Remove the cable from the current cableway. All cables will be removed if both parameters are omitted. All cables belonging to a specific system is removed if only one parameter isgiven.
System String System name of cable.
Name String Name of cable.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelIsCurrent No cableway was current.
kcs_ReferenceInvalid The cableway route could not be removed, cased by locked references.
```
Example:
```
# Example: kcs_ex_cway_03.py
# Example: kcs_ex_cway_04.py
# Example: kcs_ex_cway_05.py
Copyright © 1993-2005 AVEVA AB
6.6 Cableway Production Functions
This chapter describes methods for handling production functions for cableways using the kcs_cable interface.
User's Guide Vitesse
```
Chapter: Cable
```
```
cway_planning_unit_set (plu)
```
Set or replace the planning unit for the cableway.
Input parameters
plu String Planning unit. The planning unit will be removed if the string is empty.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
```
cway_interference_exclude (class)
```
Exclude the interference class for this cableway. Cables with this interference class may not be routed on the cableway.
Input parameters
Class String Name of interference class.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway was current.
kcs_NameInvalid Interference class name invalid or already excluded or cableway has no branches
kcs_CableRouted A cable with this interference class is already routed on cway.
kcs_ArgumentError Invalid arguments list.
```
cway_interference_permit (<class>)
```
Permit the interference class again, which means that previously excluded interference classes will be permitted. No attribute means permit all.
Input parameters
Class String Name of interference class.
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No cableway was current.
kcs_ValueError Interference class not previously excluded.
kcs_ArgumentError Invalid arguments list.
```
cway_part_posno_set (posno, <id>)
```
Set position number for part. The position number will be automatically updated with prefix, given as input parameter posno, followed by an increasing number starting on 1 if id isomitted.
Input parameters
Id Integer Id of part to put position number on.
posno String Position number. Prefix if id is omitted.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No cableway was current.
```
Example:
```
# Example: kcs_ex_cway_06.py
Copyright © 1993-2005 AVEVA AB
6.7 Cable Penetration Functions
This chapter describes functions for modelling of Cable Penetrations.
User's Guide Vitesse
```
Chapter: Cable
```
```
cpen_real_new(name, cableway name, point, <component name>,<height>, <width>)
```
A real penetration will be created. The cableway shall not be current, either component or height and width shall be given. Insert blocks are handled automatically, see the PUT_GLANDkeyword.
Input parameters
Name String Name of penetration.
```
Cableway String Name of cableway to place the penetration on (without project name).
```
Point Point3D Point to place the penetration.
Component String Component used for penetration.
Height Real Height of penetration.
Width Real Width of penetration.
Returned value:
None.
```
Exceptions:
```
kcs_NameInvalid The penetration name had illegal signs, existed or was longer than 10 signs.
kcs_ModelNotFound The cableway was not found.
kcs_ModelIsCurrent The cableway was current.
kcs_ReferenceInvalid The owning cableway was locked by another user.
kcs_ComponentInvalid The component was not found or was of illegal type.
kcs_PartNotFound The parts was not found at this point.
kcs_ArgumentError The length or width was invalid.
kcs_ItemAlreadyExist The penetration exist.
```
cpen_real_transform (name, T)
```
Transform a real penetration.
Input parameters
Name String Name of Penetration.
T KcsTransformation3D Transformation matrix.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound The penetration not found.
kcs_ModelIsCurrent The owning cableway was current.
kcs_ReferenceInvalid The owning cableway was locked by another user.
kcs_MatrixInvalid The values in the matrix was invalid.
```
cpen_imag_new (name, cableway name, point)
```
An imaginary penetration will be created.
Input parameters
Name String Name of Penetration.
```
Cableway String Name of cableway to place the penetration on (without project name).
```
Point Point3D Point to place the penetration.
Returned value:
None.
```
Exceptions:
```
kcs_NameInvalid The penetration name had illegal signs, existed or was longer than 10 signs.
kcs_ModelNotFound The cableway was not found.
kcs_ModelIsCurrent The cableway was current.
kcs_ReferenceInvalid The owning cableway was locked by another user.
kcs_PartNotFound The parts was not found at this point.
kcs_ArgumentError The length or width was invalid.
kcs_ItemAlreadyExist The penetration exist.
```
cpen_delete (name)
```
Any kind of penetration will be deleted from db.
Input parameters
Name String Name of penetration.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound The penetration was not found.
kcs_ModelIsCurrent The owning cableway was current.
kcs_ReferenceInvalid The owning cableway was locked by another user.
```
Example:
```
# Example: kcs_ex_cway_07.py
```
cpen_document_reference_get (name)
```
The function returns a list of document references associated with the penetration.
Input parameters
Name String Name of penetration
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Penetration not exist
kcs_GeneralError List of result can't be created for some internal reason
```
cpen_document_reference_add (docRef, name)
```
The function adds a document reference to the penetration object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Name String Name of penetration
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Penetration not exist
```
cpen_document_reference_remove (docRef,name)
```
The function removes document reference from the penetration object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Name String Name of penetration
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Penetration not exist
kcs_DoesNotExist Penetration document reference doesn't exist
Copyright © 1993-2005 AVEVA AB
7 Drafting
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
7.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_draft. The functions are then referred to as kcs_draft.<function name>. Before usinga new function, please carefully read the function description.
Vitesse for Drafting contains functions for many different purposes. There are functions for e.g. create a new drawing, place text in drawing, create geometric entities, create drawingcomponents, and highlighting. The functions are divided into the following sections:
 Drawing Functions
 Modal Properties
 Default Values
 View Functions
 Model handling functions
 Creation of basic geometric entities
 Creation of texts
 Creation of symbols
 Creation of drawing components
 Property changing and Retrieving Functions
 Identifying and Capturing Functions
 Deleting functions
 Highlighting functions
 Subpicture and Element Navigation
 Drawing element functions
 Subpicture functions
 Visual Area functions
Every function in the interface will be explained and some examples have been included to show how the functions can be used.
User's Guide Vitesse
```
Chapter: Drafting
```
Copyright © 1993-2005 AVEVA AB
7.2 Exception Handling
The Vitesse Drafting interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_draft.error. The exception is also displayed in the Vitesse Log window which is available by
the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below. .
User's Guide Vitesse
```
Chapter: Drafting
```
```
Example:
```
import kcs_draft
import KcsColour
```
new_colour = KcsColour.Colour("Red")
```
```
try:
```
```
kcs_draft.colour_set(new_colour)
```
```
except:
```
print kcs_draft.error
Copyright © 1993-2005 AVEVA AB
7.3 Classes
Some of the functions in the Vitesse Drafting interface take objects as input. These objects are instances of Python classes. The classes used in this interface are described in General.
User's Guide Vitesse
```
Chapter: Drafting
```
Copyright © 1993-2005 AVEVA AB
7.4 Drawing Functions
This section describes functions that handle drawings on object level. The default data bank for drawings is the Drawing Data Bank, SB_PDB.
```
Note: Only one drawing at a time may be current. This means that no drawing may be current before creating a new or opening an existing drawing. If a drawing is current it first hasto be closed.
```
User's Guide Vitesse
```
Chapter: Drafting
```
```
document_reference_get ()
```
The function returns a list of document references associated with the active drawing.
Input parameters
None
Returned value:
[0] List List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_DrawingNotCurrent Active drawing not set Active drawing not set
kcs_GeneralError List of result can't be created for some internal reason
```
document_reference_add (docRef)
```
The function adds a document reference to the active drawing object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_DrawingNotCurrent Active drawing not set
```
document_reference_remove (docRef)
```
The function removes document reference from active drawing object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_DrawingNotCurrent Active drawing not set
kcs_DoesNotExist Drawing document reference doesn't exist
```
dwg_properties_set (PropRef)
```
The function sets common properties for drawing.
Input parameters
PropRef CommonProperties Instance of Python CommonProperties class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_DrawingNotCurrent Active drawing not set
```
dwg_new(DwgName, <FormName>, <DwgType>)
```
The function creates a new drawing and makes it the current one. The optional FormName gives the name of the drawing form.
Input Parameters:
```
DwgName string Name of drawing (maximum 25 characters)
```
```
<FormName> string Name of drawing form (optional)
```
<DwgType> Constant or string Drawing type. It can be defined by using:
1. drawing types constants(see chapter: "Drafting Constants"):
e.g. kcs_draft.kcsDWGTYPE_ASSEMBLY
2. logical databank names: e.g. "SB_PDB"
User defined drawing databanks can be specified also by:
1. constantkcs_draft.kcsDWGTYPE_USER_DEFINEDand database index
e.g. kcs_draft.kcsDWGTYPE_USER_DEFINED + 2
2. logical databank names: e.g. "SB_PDB002"
A list of all drawing databanks defined in the Tribon system can be obtained by using kcs_draft.dwg_type_list_getfunction.
This parameter is optional. If not given, the standard drawing databank will be used.
Returned value:
None
```
Exceptions:
```
kcs_DbError Databank error
kcs_DrawingCurrent A drawing is already current
kcs_DrawingExist A drawing named DwgName already exists in the data bank
kcs_FormLocked The drawing form is locked in the data bank.
kcs_FormNotFound The drawing form was not found in the data bank.
kcs_NameError Invalid name of drawing
kcs_NameOccupied The name DwgName or FormName is used by the system.
kcs_CouldNotOpenDatabank Not possible to open databank. Probably because of wrong user database name or id.
kcs_VolumeCurrent A volume is already current.
```
dwg_open(DwgName, <DwgType>, <OpenMode>, <DwgRevision>), <EnvelopeMode>)
```
The function opens an existing drawing and makes it the current one. It is possible to specify a Drawing Type, an Open Mode and a Drawing Revision Name.
Input Parameters:
DwgName string Name of drawing
<DwgType> constant or string Drawing type. It can be defined by using:
1. drawing types constants(see chapter: "Drafting Constants")
e.g. kcs_draft.kcsDWGTYPE_ASSEMBLY
2. logical databank names: e.g. "SB_PDB"
User defined drawing databanks can be specified also by:
1. constantkcs_draft.kcsDWGTYPE_USER_DEFINED
and database indexe.g. kcs_draft.kcsDWGTYPE_USER_DEFINED
2. logical databank names: e.g. "SB_PDB002"
A list of all drawing databanks defined in the Tribon system can be obtained by using kcs_draft.dwg_type_list_getfunction.
This parameter is optional. If not given, the standard drawing databank will be used.
<OpenMode> constant Drawing Open Mode. It can be one of the following constants:
 kcs_draft.kcsOPENMODE_READONLY
 kcs_draft.kcsOPENMODE_READWRITE
This parameter is optional. If it is not given, the drawing will be opened in read-write mode.
<DwgRevision> string Drawing Revision Name. This parameter is valid only in case of TDM usage. If an empty string is given, the latestrevision of the drawing will be opened. To open the Base Revision, use the kcs_draft.kcsBASE_REVISION constant.
This parameter is optional. If not given the latest revision of drawing will be opened.
<EnvelopeMode> constant Drawing views envelope mode. It can be one of the following constants:
 kcs_draft.kcsENVELOPE_NONE
 kcs_draft.kcsENVELOPE_INITIAL
 kcs_draft.kcsENVELOPE_PERMANENT
This parameter is optional. If it is not given, the drawing views will be opened without envelope.
Returned value:
None
```
Exceptions:
```
kcs_Error General error
kcs_DbError Databank error
kcs_DrawingCurrent A drawing is already current
kcs_DrawingLocked The drawing is locked in the databank.
kcs_DrawingNotFound The drawing was not found in the databank.
kcs_NameOccupied The name is used by system.
kcs_VolumeCurrent The volume mode is active.
Kcs_RevisionNotFound The revision not found for given drawing.
Kcs_CouldNotOpenDatabank Not possible to open databank. Probably because of wrong user database name or id.
```
dwg_pack()
```
The function packs the current drawing.
```
Arguments:
```
None.
Returned value:
None.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
kcs_ArgumentError Invalid arguments list.
```
dwg_purge()
```
The function purges the current drawing. I.e. Removes any empty subpictures down to subcomponent level.
Input parameters:
None.
Returned value:
[] None
```
Exceptions:
```
kcs_DrawingNotCurrent
kcs_Error
```
dwg_reference_show (show, <views>)
```
This function expands or collapses drawing references in current drawing.
Input Parameters:
show true/false Boolean value. If true then reference will be expanded otherwise collapsed.
<views> List, tuple of ElementHandle orinstance of ElementHandle.Handles to views that should be expanded/collapsed. This parameter is optional. If not given then all reference viewswill be considered.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Argument Error
kcs_DrawingNotCurrent There is no current drawing.
kcs_HandleInvalid Given handle is not a valid handle.
kcs_ValueError Given handle is not an instance of ElementHandle.
kcs_DrawingNotFound Reference drawing not found.
kcs_DrawingLocked Reference drawing locked.
kcs_ReferenceDrawingInvalid Reference drawing invalid.
kcs_DrawingEmpty Reference drawing empty.
```
dwg_revision_freeze()
```
The function freezes latest revision of current drawing.
Input parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_CouldNotOpenDatabank Invalid database ID.
kcs_DrawingNotCurrent Active drawing not set.
kcs_DrawingNotFound The drawing not found in the data bank.
kcs_FunctionNotSupported Function not supported on current Tribon Data Management level.
kcs_Error General error.
```
dwg_revision_new()
```
The function creates new revision for current drawing. Previous 'current' revision is frozen.
Input parameters:
RevName string Drawing revision name.
RevRemark string Drawing revision remark.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_CouldNotOpenDatabank Invalid database ID.
kcs_DrawingNotCurrent Active drawing not set.
kcs_DrawingNotFound The drawing not found in the data bank.
kcs_FunctionNotSupported Function not supported on current Tribon Dta Management level.
kcs_NameOccupied The revision name is already used.
kcs_ValueError The revision name string is empty.
kcs_Error General error.
```
dwg_revision_unfreeze()
```
The function unfreezes latest revision of current drawing.
Input parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_CouldNotOpenDatabank Invalid database ID.
kcs_DrawingNotCurrent Active drawing not set.
kcs_DrawingNotFound The drawing not found in the data bank.
kcs_FunctionNotSupported Function not supported on current Tribon Data Management level.
kcs_Error General error
```
dwg_save()
```
The function saves the current drawing in the data bank. Note: An already existing version in the data bank will be overwritten!
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_DbError Data bank error
kcs_DrawingLocked The drawing is locked in the data bank
kcs_DrawingNotCurrent No drawing was current
kcs_ReadOnlyMode Drawing was opened in read-only mode
```
dwg_save_as('NewDwgName', <Databank>)
```
This function saves the current drawing with a new name in the given databank.
Input Parameters:
```
NewDwgName string The new drawing name (max. 25 characters)
```
Databank string Optional databank name. If not given then standard drawing databank will be used. Allowed values are: 'SB_ASSPDB' -for automatic assembly drawings databank and 'SB_PDB' - for standard drawings databank
Returned value:
None
```
Exceptions:
```
kcs_DbError Databank error.
kcs_DrawingExist Drawing already exists in databank.
kcs_DrawingNotCurrent No drawing was current
kcs_DrawingLocked The drawing is locked in the databank
kcs_NameError Invalid name of drawing
kcs_NameOccupied The name is used by the system
```
dwg_size_get()
```
The function returns the size of the current drawing.
Input Parameters:
None.
Returned value:
[0] integer The size, in Kbyes.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
```
dwg_close()
```
The function closes the current drawing The drawing is not stored and will not be the current one any more.
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
```
dwg_exist(DwgName, <DwgType>)
```
The function checks if a drawing of given type exists in the data bank.
Input Parameters:
```
DwgName string Name of drawing (maximum 25 characters)
```
<DwgType> Constant or string Drawing type. It can be defined by using:
1. drawing types constants(see chapter: "Drafting Constants"):
e.g. kcs_draft.kcsDWGTYPE_ASSEMBLY
2. logical databank names: e.g. "SB_PDB"
User defined drawing databanks can be specified also by:
1. constantkcs_draft.kcsDWGTYPE_USER_DEFINED
and database index e.g.kcs_draft.kcsDWGTYPE_USER_DEFINED + 2
2. logical databank names: e.g. "SB_PDB002"
A list of all drawing databanks defined in the Tribon system can be obtained by using kcs_draft.dwg_type_list_getfunction.
This parameter is optional. If not given, the standard drawing databank will be used.
Returned value:
[0] integer 0: The drawing does not exist in the data bank
1: The drawing exists in the data bank.
```
Exceptions:
```
kcs_CouldNotOpenDatabank Not possible to open databank. Probably because of wrong user database name or id.
```
dwg_delete(DwgName, <DwgType>)
```
The function deletes a drawing of a given type in the databank.
Input Parameters:
```
DwgName string Name of drawing (maximum 25 characters)
```
<DwgType> Constant or string Drawing type. It can be defined by using:
1. drawing types constants(see chapter: "Drafting Constants"):e.g. kcs_draft.kcsDWGTYPE_ASSEMBLY
2. logical databank names: e.g. "SB_PDB"
User defined drawing databanks can also be specified by
1. constantkcs_draft.kcsDWGTYPE_USER_DEFINEDand database indexe.g.
kcs_draft.kcsDWGTYPE_USER_DEFINED + 2
2. logical databank names: e.g. "SB_PDB002"
Returned value:
None
```
Exceptions:
```
kcs_DbError Data bank error
kcs_DrawingLocked The drawing is locked in the data bank.
kcs_DrawingNotFound The drawing is not found in the data bank.
kcs_CouldNotOpenDatabank Not possible to open databank. Probably because of wrong user database name or id.
```
dwg_current()
```
The function checks if a drawing is current.
Input Parameters:
None
Returned value:
[0] integer 0: No drawing is current
1: A drawing is current
```
Exceptions:
```
None
```
dwg_name_get()
```
The function returns the name of the current drawing.
Input Parameters:
None
Returned value:
[0] string The name
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
```
dwg_print(options)
```
The function prints current drawing using selected print options.
Input Parameters:
options PrintOptions Python class describing print options.
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_PrinterNotFound Selected printer not found.
kcs_PrintError Print error: e.g. wrong file name for print-to-file printing.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
dwg_dxf_export(FileName, <ACVersion>, <Mode>, <nElemVisibility>, <nLayerVisibility>)
```
The function exports the current drawing to a 2D DXF file.
Input Parameters:
FileName string Name of file to be created. The file must not exist before. If no path is given, the file is created in current directory. If noextension is given, the default extension .dxf will be used.
<ACVersion> integer Version of AutoCAD in which exported file will be open. It can be one of the following values:
12 - for R12
13 - for R13
14 - for R14
```
15 - for R15 (AutoCAD 2000) (default)
```
```
18 - for R18 (AutoCAD 2004)
```
This parameter is optional.
<Mode> integer Type of dxf file:
```
0 - text dxf file (default)
```
1 - binary dxf file
This parameter is optional.
<nElemVisibility> integer Type of exports hidden elements:
```
0 - hidden elements are invisible in exported file (default)
```
1 - hidden elements are visible in exported file
<nLayerVisibility> integer Type of exports hidden layers:
```
0 - idden layers are invisible in exported file (default)
```
1 - hidden layers are visible in exported file
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
kcs_AlreadyExist Version is not valid.
kcs_ValueError For some reasons file can not be opened. For example file on read only drive.
kcs_Error Internal error. Drawing can not be exported.
```
dwg_dxf_import(FileName, DrawingName , <MapFileName>)
```
The function imports the drawing from a 2D DXF file. No drawing must be current before.
Input Parameters:
FileName string Name of file to be opened. If no extension is given, the default extension .dxf will be used.
DrawingName string Name for new drawing that will be created.
<MapFileName> string Name of file with import map definition. This parameter is optionaly. Default import map is defined in dxfimport.def
file located in directory described by SBGD_DEF.
The format of this file is as follows:
It is divided in three sections:
```
One for mapping layers, one for mapping linetypes and one for mapping fonts. These sections have specified headers([LAYERS], [LTYPES], [FONTS]) followed by pairs of DXF objects and corresponding Drafting objects to be used, every
```
value in a new line. The example here shows how such mapping file could look like.
[LAYERS]dxflayer1
34dxflyer2
55[LTYPES]
BYLAYERSYSTEM32
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingIsCurrent There is current drawing.
kcs_DoesNotExist Source file doesn't exist.
kcs_ValueError For some reasons file can not be opened or illegal drawing name.
kcs_NameOccupied Drawing name is already in use.
kcs_Error Internal error. Drawing can not be imported.
Example
#Example:kcs_ex_draft32.py
```
dwg_dxf_2d3d_export(FileName, ViewSubviewsList, Paper, Margins <DetailLevel>, <ACVersion>, <Mode>, <nElemVisibility>, <nLayerVisibility>)
```
The function exports selected views/subviews to 2d3d dxf file. Model parts are exported to ModelSpace block as 3D entities. Non-model parts are exported to PaperSpace block as 2Dentities.
Input Parameters:
FileName string Name of file to be created. The file must not exist before. If no path is given, the file is created in current directory. If noextension is given, the default extension .dxf will be used.
ViewSubviewsList list of Element Handle List of views and/or subviews handles. Specified views/subviews must be model views/subviews.
Paper Vector2D Paper size
Margins Vector2D Margins size
<DetailLevel> integer Level of dxf file detail. It can be one of the following:
1 - Low detail
2 - Medium detail
```
3 - High detail (default)
```
4 - Extra detail
This parameter is optional.
<ACVersion> integer Version of AutoCAD in which exported file will be open. It can be one of the following values:
12 - for R12
13 - for R13
14 - for R14
```
15 - for R15 (AutoCAD 2000) (default)
```
```
18 - for R18 (AutoCAD 2004)
```
This parameter is optional.
<Mode> integer Type of dxf file:
```
0 - text dxf file (default)
```
1 - binary dxf file
This parametr is optional.
<nElemVisibility> integer Type of exports hidden elements:
```
0 - hidden elements are invisible in exported file (deault
```
1 - hidden elements are visible in exported file
<nLayerVisibility> integer Type of exports hidden layers:
```
0 - hidden layers are invisible in exported file (default
```
1 - hidden layers are visible in exported file
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
kcs_AlreadyExist Destination file already exsist.
kcs_HandleInvalid List of views/subviews is empty or there are handles for not model views/subviews.
kcs_ValueError This exception is generated if:
 detail level or version is not valid
 for some reasons output file can't be opened. For example file on read only drive.
kcs-Error Internal error. Drawing canot be exported.
```
dwg_dxf_3d_export(FileName, ViewSubviewsList, <DetailLevel>, <ACVersion>, <Mode>)
```
The function exports all models in the given views and subviews to a 3D DXF Facet format.
Input Parameters:
FileName string Name of file to be created. The file must not exist before. If no path is given, the file is created in current directory. If noextension is given, the default extension .dxf will be used.
ViewSubviewsList list of List of views and/or subviews handles. Specified
Element Handle views/subviews must be model views/subviews.
<DetailLevel> integer Level of dxf file detail. It can be one of the following:
1 - Low detail
2 - Medium detail
```
3 - High detail (default)l
```
4 - Extra detail
This parameter is optional.
<ACVersion> integer Version of AutoCAD in which exported file will be open. It can be one of the following values:
12 - for R12
13 - for R13
14 - for R14
```
15 for R15 (AutoCAD 2000) (default)
```
```
18 - for R18 (AutoCAD 2004)
```
This parameter is optional.
<Mode> integer Type of dxf file:
```
0 - text dxf file (default
```
1 - binary dxf file
This parameter is optional.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
kcs_AlreadyExist Destination file already exists.
kcs_HandleInvalid List of views/subviews is empty or there are handles for not model views/subviews.
kcs_ValueError This exception is generated if:
 detail level or version is not valid
 for some reasons output file can't be opened. For example file on read only drive.
kcs_Error Internal error. Drawing can not be exported.
```
dwg_wmf_export(FileName)
```
The function exports the current drawing to a metafile.
Input Parameters:
FileName string Name of file to be created. The file must not exist before. If no path is given, the file is created in current directory. If noextension is given, the default extension .wmf will be used.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
kcs_AlreadyExist Destination file already exists.
kcs_ValueError For some reasons file can not be opened. For example file on read only drive.
kcs_Error Internal error. Drawing can not be exported.
```
dwg_preview_bmp_export(FileName,DwgType,DwgName)
```
The function exports the preview of the given drawing to a bitmap file. Please note that a preview of this drawing must exist in the preview image database.
Input Parameters:
FileName string Name of file to be created. If no path is given, the file is created in current directory.
DwgType integer The drawing type code for the drawing. This can be found in Tribon Toolkit Preferences.
DwgName string Name of the drawing to create a bitmap file from.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter.
kcs_FileError The file could not be created.
kcs_PreviewError The preview object could not be found in the preview image database.
```
Example:
```
#kcs_ex_draft43.py
```
form_name_get()
```
The function returns form name of current drawing.
Input Parameters:
None
Returned value:
[0] string Name of drawing form
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Drawing has no form.
kcs_Error General error
```
dwg_type_list_get()
```
The function returns all drawing types registered in the Tribon system as a Python dictionary.
Input Parameters:
None
Returned value:
[0] dictionary The dictionary contains drawing types as keys and pairs: description and logical databank name as values. Example:
```
kcsDWGTYPE_GEN : ('General drawing', 'SB_PDB')
```
```
You can find all registered types using keys() function of the returned dictionary.
```
User defined drawing types
Any of user defined drawing types are equal to:
kcsDWGTYPE_USER_DEFINED + database index
where index starts from 1. It means that each type which has a value higher thankcsDWGTYPE_USER_DEFINED is a user defined drawing type.
```
Exceptions:
```
kcs_Error General error
```
Example:
```
#kcs_ex_draft01.py
```
dwg_status_set (StatusType, StatusValue)
```
The function changes status for current drawing.
Input Parameters:
StatusType constant Status type. It can be defined by using constants defined in kcs_model module:
 kcsSTATTYPE_DESIGN
 kcsSTATTYPE_MANUFACTURING
 kcsSTATTYPE_ASSEMBLY
 kcsSTATTYPE_MATERIAL_CONTROL
```
StatusValue constant New status value. To get all possible values use kcs_model.status_values_get() function.
```
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Argument error.
kcs_ValueError Argument value not valid.
kcs_FunctionNotSupported Function not supported. Tribon Data Management not enabled.
kcs_CouldNotChangeStatus It is not possible to change status. Probably you don't have permission to do this.
kcs_DrawingNotCurrent No current drawing.
```
dwg_validate(OutOfDate, NotFound)
```
The function validates the current drawing and returns two lists of KcsModel.Model instances. The first list contains model objects that have been updated on the databank after thisdrawing was saved. List two contains model objects in the drawing that cannot be found on the databank. Only one instance of the object is returned and always as un-reflected.
Input parameters:
OutOfDate List
NotFound List
Returned value:
[0] OutOfDate List of KcsModel objects
[1] NotFound List of KcsModel objects
```
Exceptions:
```
kcs_DrawingNotCurrent
kcs_Error
```
dwg_layers_is_shown ()
```
The function tests if application display mode is show layers. If show layers mode is active the function returns true otherwise false.
Input Parameters:
None
Returned value:
[0] integer 0: Show layers mode is not active
1: Show layers mode is active
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing is current
```
dwg_layers_is_hidden()
```
The function tests if application display mode is hide layers. If hide layers mode is active the function returns true otherwise false.
Input Parameters:
None
Returned value:
[0] integer 0: Hide layers mode is not active
1: Hide layers mode is active
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing is current
```
dwg_layers_shown_get ()
```
The function returns list of layers that are displayed when application mode is show layers.
Input Parameters:
None
Returned value:
[0] list List of KcsLayer objects
```
Exceptions:
```
kcs_DrawingNotCurrentkcs_LayersDisplayModeInvalid No drawing is current. Application is not in show layers mode
```
dwg_layers_hidden_get ()
```
The function returns list of layers that are hidden when application mode is hide layers.
Input Parameters:
None
Returned value:
[0] list List of KcsLayer objects
```
Exceptions:
```
kcs_DrawingNotCurrentkcs_LayersDisplayModeInvalid No drawing is current. Application is not in hide layers mode
```
Example:
```
kcs_ex_draft26.py
```
Examples:
```
These are examples on how to use the drawing functions.
# Example: kcs_ex_draft1.py
# Example: kcs_ex_draft27.py
# Example: kcs_ex_draft30.py
Copyright © 1993-2005 AVEVA AB
7.5 Functions for Modal Properties
This chapter describes functions to access different modal properties used in the Drafting system. See also the functions for Functions for Default Values access.
User's Guide Vitesse
```
Chapter: Drafting
```
Copyright © 1993-2005 AVEVA AB
7.5.1 General Properties
User's Guide Vitesse
```
Chapter: Drafting
```
```
colour_set(ModalColour)
```
The function sets the modal colour for ordinary geometry.
Input Parameters:
ModalColour Colour The colour
Returned value:
None
```
Exceptions:
```
kcs_ColourInvalid Invalid colour
```
colour_get(ModalColour)
```
The function gets the modal colour.
Output Parameters:
ModalColour Colour The colour
Returned value:
[0] Colour The colour
```
Exceptions:
```
None
```
linetype_display_settings_get()
```
The function returns the line type display settings.
Input Parameters:
None.
Returned value:
[0] LineTypeDisplaySettings The current line type display settings - instance of KcsLineTypeDisplaySettings.LineTypeDisplaySettings class.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
```
linetype_display_settings_set (modelLTDSettings)
```
The function sets the line type display settings.
Input Parameters:
ModalLTDSettings LineTypeDisplaySettings Instance of KcsLineTypeDisplaySettings.LineTypeDisplaySettings class
Returned value:
None.
```
Exceptions:
```
kcs_AgrumentError Invalid parameter type
```
linetype_set(ModalLinetype)
```
The function sets the modal line type.
Input Parameters:
ModalLinetype Linetype The line type.
Returned value:
None
```
Exceptions:
```
kcs_LinetypeInvalid Invalid line type
```
linetype_get(ModalLinetype)
```
The function gets the modal line type.
Output Parameters:
ModalLinetype Linetype The line type
Returned value:
[0] Linetype The line type
```
Exceptions:
```
None
```
layer_set(Layer)
```
The function sets the modal layer.
Input Parameters:
Layer integer The layer
Returned value:
None
```
Exceptions:
```
Kcs_ArgumentError Invalid arguments list.
```
layer_get()
```
The function gets the modal layer.
Input Parameters:
None
Returned value:
[0] integer The layer
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_draft2.py
Copyright © 1993-2005 AVEVA AB
7.5.2 Hatch Pattern
Functions for setting the modal hatch pattern type.
User's Guide Vitesse
```
Chapter: Drafting
```
```
hatch_pattern_set(Angle, Distance)
```
The function sets the modal hatch pattern to a given angle and line distance.
Input Parameters:
Angle real The angle of the hatch pattern lines, between -90 and 90 degrees.
```
Distance real The distance between the hatch pattern lines (>0.0)
```
Returned value:
None
```
Exceptions:
```
kcs_Argument Error Invalid arguments list.
kcs_ValueError Invalid parameter value
```
std_hatch_pattern_set(Type)
```
The function sets the modal hatch pattern to one of the three standard patterns:
1. Single hatching with hatch angle defined by the default parameter HATCH_ANG_PAT1.
2. Single hatching with hatch angle defined by the default parameter HATCH_ANG_PAT2.
3. Cross hatching with hatch angle defined by the default parameter HATCH_ANG_CROSS.
Input Parameters:
```
Type integer The standard hatch pattern type (1, 2 or 3)
```
Returned value:
None
```
Exceptions:
```
kcs_StdHatchPatternInvalid Invalid standard hatch pattern type
```
userdef_hatch_pattern_set(Page, Detail)
```
The function sets the modal hatch pattern to a user defined pattern found in the standard hatch pattern book.
Input Parameters:
Page integer The page in the standard hatch pattern book
Detail integer The detail in the selected page
Returned value:
None
```
Exceptions:
```
kcs_PageNotFound The page was not found
kcs_DetailNotFound The detail within the page was not found
```
Example:
```
# Example: kcs_ex_draft3.py
Copyright © 1993-2005 AVEVA AB
7.5.3 Note and Position Number Symbols
Functions for accessing modal properties for notes and position numbers.
See Creating Note and Position Number symbols in Drafting User's Guide for further information.
.
User's Guide Vitesse
```
Chapter: Drafting
```
```
note_symbol_set(Symbol)
```
The function sets the modal note symbol.
Input Parameters:
```
Symbol integer The modal note symbol in the font for Note symbols (range [31-60] in the standard font, range [1-400] in the alternative font).
```
```
(to suppress the note symbol, give -1)
```
Returned value:
None
```
Exceptions:
```
SymbolInvalid
```
note_symbol_get()
```
The function gets the modal note symbol.
Input Parameters:
None
Returned value:
[0] integer The modal note symbol in the font for Note symbols
```
Exceptions:
```
None
```
posno_symbol_set(Symbol)
```
The function sets the modal position number symbol.
Input Parameters:
```
Symbol integer The modal position symbol in the font for Position Number symbols (range [61-80] in the standard font, range [601-999] in the alternative font).
```
Returned value:
None
```
Exceptions:
```
SymbolInvalid
```
posno_symbol_get()
```
The function gets the modal position number symbol.
Input Parameters:
None
Returned value:
[0] integer The modal position symbol in the font for Position Number symbols
```
Exceptions:
```
None
```
posno_height_set(Height)
```
The function sets the modal height of position number symbols.
Input Parameters:
```
Height real The height of position number symbols (> 0.0)
```
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
posno_height_get()
```
The function gets the modal height of position number symbols.
Input Parameters:
None
Returned value:
[0] real The height of position number symbols
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_draft4.py
Copyright © 1993-2005 AVEVA AB
7.5.4 Text Attributes
This section describes text attributes functions.
User's Guide Vitesse
```
Chapter: Drafting
```
```
text_height_set(Height)
```
The function sets the modal text height.
Input Parameters:
```
Height real The text height (> 0.0)
```
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
text_height_get()
```
The function gets the modal text height.
Input Parameters:
None
Returned value:
[0] real The text height
```
Exceptions:
```
None
```
text_rotation_set(Rot)
```
The function sets the modal text rotation angle.
Input Parameters:
Rot real The text rotation angle, in degrees.
Returned value:
None
```
Exceptions:
```
None
```
text_rotation_get()
```
The function gets the modal text rotation angle.
Input Parameters:
None
Returned value:
[0] real The text rotation angle, in degrees
```
Exceptions:
```
None
```
text_aspect_set(Aspect)
```
The function sets the modal text aspect, i.e. the width/height ratio.
Input Parameters:
Aspect real The text aspect. A negative value means proportional text.
Returned value:
None
```
Exceptions:
```
None
```
text_aspect_get()
```
The function gets the modal text aspect.
Input Parameters:
None
Returned value:
[0] real The text aspect
```
Exceptions:
```
None
```
text_slant_set(Slant)
```
The function sets the modal text slanting angle
Input Parameters:
```
Slant real The text slanting angle, in degrees (90 means standard slant).
```
Returned value:
None
```
Exceptions:
```
None
```
text_slant_get()
```
The function gets the modal text slanting angle.
Input Parameters:
None
Returned value:
[0] real The text slanting angle, in degrees
```
Exceptions:
```
None
```
text_ascii_font_set(Font)
```
The function sets the modal ASCII text font.
Input Parameters:
Font integer The ASCII text font.
Valid fonts are:
```
0-7 (system fonts)
```
```
8-99 (user-defined fonts)
```
```
101,105 (ISO8859 fonts)
```
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
```
text_ascii_font_get()
```
The function gets the modal ASCII text font.
Input Parameters:
None
Returned value:
[0] integer The ASCII text font
```
Exceptions:
```
None
```
text_vector_font_set(Vfont)
```
```
The function sets the modal text vector (multi-byte) font, e.g. Japanese.
```
```
Note: that the validity of given font is not checked here.
```
Input Parameters:
Vfont integer The text vector font
Returned value:
None
```
Exceptions:
```
None
```
text_vector_font_get()
```
The function gets the modal text vector font.
Input Parameters:
None
Returned value:
[0] integer The text vector font
```
Exceptions:
```
None
```
text_ilsp_set(Ilsp)
```
The function sets the modal text interline space factor, used for multiple line texts. The distance between two text lines will then be Interline space factor * text height. Note that anegative value means "negative" growth direction.
Input Parameters:
Ilsp real The text interline space factor
Returned value:
None
```
Exceptions:
```
None
```
text_ilsp_get()
```
The function gets the modal text interline space factor.
Input Parameters:
None
Returned value:
[0] real The text interline space factor
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_draft5.py
Copyright © 1993-2005 AVEVA AB
7.5.5 Symbol Attributes
This section describes symbol attribute functions.
User's Guide Vitesse
```
Chapter: Drafting
```
```
symbol_height_set(Height)
```
The function sets the modal symbol height.
Input Parameters:
Height real The symbol height.
> 0: height of symbol space
```
< 0: height of symbol (absolute value)
```
Returned value:
None
```
Exceptions:
```
None
```
symbol_height_get()
```
The function gets the modal symbol height.
Input Parameters:
None
Returned value:
[0] real The symbol height
```
Exceptions:
```
None
```
symbol_rotation_set(Rot)
```
The function sets the modal symbol rotation angle.
Input Parameters:
Rot real The symbol rotation angle, in degrees
Returned value:
None
```
Exceptions:
```
None
```
symbol_rotation_get()
```
The function gets the modal symbol rotation angle.
Input Parameters:
None
Returned value:
[0] real The symbol rotation angle, in degrees
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_draft6.py
Copyright © 1993-2005 AVEVA AB
7.6 Functions for Default Values
Refer to Tribon M3 Drafting, Model Viewing and General Drafting for general information about the Default handling in Drafting.
This chapter describes functions to access the default settings in drafting, see also Drafting Default File Keywords.
User's Guide Vitesse
```
Chapter: Drafting
```
```
default_value_set(DefStatement)
```
The function updates a default value by a given default statement.
Input Parameters:
```
DefStatement string The default statement (max 80 characters). Statement string in format 'KEYWORD=VALUE' or 'KEYWORD:VALUE'.
```
Returned value:
None
```
Exceptions:
```
kcs_Error Invalid arguments list
kcs_ValueError Invalid parameter value
kcs_DefKeywordInvalid Invalid default keyword
kcs_DefValueInvalid Invalid default value
```
default_value_get(DefKeyword)
```
The function returns a default statement, given a default keyword.
Input Parameters:
```
DefKeyword string The default keyword (max 40 characters).
```
Returned value:
[0] string The default statement
```
Exceptions:
```
kcs_Error Invalid arguments list.
kcs_DefKeywordInvalid Invalid default keyword
```
Example:
```
# Example: kcs_ex_draft18.py
Copyright © 1993-2005 AVEVA AB
7.7 View Functions
This chapter describes functions to create and handle views in the current drawing.
User's Guide Vitesse
```
Chapter: Drafting
```
```
model_object_revision_save(model, revision, view_handle, save_spools)
```
The function will save a revision of a model object.
Input Parameters:
model KcsModel.Model Instance of Model class.
revision KcsModelObjectRevision. ModelObjectRevision Instance of ModelObjectRevision class.
view_handle ElementHandle Handle to model view where model should be saved.
save_spools Integer If spools should be saved.
1=Yes
0 = No.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Arguments types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_GeneralError General error.
```
model_object_revision_get(model, view_handle, list)
```
This function returns a list with revisions of a model object.
Input Parameters:
model KcsModel.Model Instance of Model class.
view_handle ElementHandle Handle to the view.
list List of ModelObjectRevision instances. List of ModelObjectRevision is returned
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_GeneralError General error.
```
model_object_revision_set(model, revision, view_handle)
```
This function displays a model object revision.
Input Parameters:
model KcsModel.Model Instance of Model class.
revision KcsModelObjectRevision. ModelObjectRevision Instance of ModelObjectRevision class.
view_handle ElementHandle Handle to the view.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_GeneralError General error.
```
Examples:
```
# Example: kcs_ex_draft19.py
# Example: kcs_ex_draft33.py
# Example: kcs_ex_draft42.py
```
view_new(ViewName, <Uvect>, <Vvect>)
```
The function creates a new view in the current drawing. The projection plane is defined by two non-parallel 3D vectors. The cross product of these vectors defines the direction towardsthe viewer.
Input Parameters:
```
ViewName String The name of the view (max 25 characters). An empty string is accepted. If view name is not empty and there is anotherview with such name exception will be raised.
```
```
Uvect Vector3D The u-vector defining the projection plane (optional; default the x-axis)
```
```
Vvect Vector3D The v-vector defining the projection plane (optional; default the y-axis)
```
Returned value:
[0] ElementHandle Handle to the created view.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_NameOccupied There is already view with specified name.
```
view_move(ViewHandle, DeltaVec)
```
The function moves a view by a delta vector.
Input Parameters:
ViewHandle integer Handle to the view
DeltaVec Vector2D The delta vector
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to given view
```
view_reflect(ViewHandle, Reflect, Centre)
```
The function reflects a view in a given line.
Input Parameters:
ViewHandle integer Handle to the view
Reflect integer The reflection line:
1 = the u-axis through given centre
2 = the v-axis through given centre
```
Centre Point2D Centre of reflection (optional; default the centre of the circumscribed rectangle of the view)
```
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to given view
```
view_rotate(ViewHandle, RotAngle, Centre)
```
The function rotates a view around a given centre.
Input Parameters:
ViewHandle integer Handle to the view
RotAngle real The rotation angle, in degrees
```
Centre Point2D Centre of rotation (optional; default the centre of the circumscribed rectangle of the view)
```
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to given view
```
view_scale(ViewHandle, ScaleFac, Centre)
```
The function scales a view around a given centre.
Input Parameters:
ViewHandle integer Handle to the view
```
ScaleFac real The scale factor (relative)
```
```
Centre Point2D Centre of scaling (optional; default the centre of the circumscribed rectangle of the view)
```
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to given view
```
view_identify(ViewName, <PictWinExt>)
```
```
view_identify(IdPnt, <PictWinExt>)
```
The function returns a handle to a view, identified by name or closest to a given point in the current drawing.
Input Parameters:
ViewName string The name of the view
IdPnt Point2D The identification point
<PictWinExt> KcsPictWinExt.PictWinExt Picture element window extension.
Returned value:
[0] integer Handle to the view.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_ViewNotFound No view was found
```
view_hl_remove(ViewHandle)
```
The function removes hidden lines from a view.
Input Parameters:
ViewHandle integer Handle to the view
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_HandleInvalid Invalid handle to given view
```
point_transform(ViewHandle, ModelPnt, DwgPnt)
```
The function transforms a 3D point to a 2D point in a given view.
Input Parameters:
ViewHandle integer Handle to the view
ModelPnt Point3D The 3D point
Output Parameters:
DwgPnt Point2D The resulting 2D point
Returned value:
[0] Point2D The resulting 2D point
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to given view
```
view_symbolic_new(ViewName, LocPoint, Uvect, Vvect, Forward, Backward, box)view_symbolic_new(SymbolicView)
```
The function creates a new symbolic view in the current drawing. The projection plane is defined by two non-parallel 3D vectors. The cross product of these vectors defines the directiontowards the viewer. An instance of the KcsInterpretationObject.SymbolicView class can also be used.
Input Parameters:
```
ViewName string The name of the view (max 25 characters). An empty string is accepted. If view name is not empty and there is anotherview with such name exception will be raised.
```
```
LocPoint Point3D Location (origin) of view projection.
```
Uvect Vector3D The u-vector defining the projection plane.
Vvect Vector3D The v-vector defining the projection plane.
Forward real Forward depth of slice for projection in relation to plane defined by location.
Backward real Backward depth of slice for projection in relation to plane defined by location and vectors.
box Box Axis parallel restriction box for display of models. Any model items or parts of model items outside this box will not be drawnwhen using the model_draw function.
Returned value:
[0] ElementHandle Handle to the created view.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
kcs_ValueError Invalid U and V vectors.
kcs_NameOccupied There is already view with specified name.
kcs_ArgumentError Invalid arguments list.
kcs_Error General error. View can not be created.
kcs_ObjectNotFound Can't create interpretation object.
kcs_ViewNotFound View can't be created.
```
view_projection_get (ViewHandle, Transf3D)
```
The function retrieves the defined projection for a given view.
Input Parameters:
ViewHandle ElementHandle Handle to view
Transf3D Transformation3D Instance of KcsTransformation3D.Transformation3D class
Returned value:
[0] Transf3D Instance of KcsTransformation3D.Transformation3D class
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
```
kcs_HandleInvalid Given handle is invalid. (e.g. doesn't point to view)
```
kcs_Error General error
kcs_PythonMethodNotFound Method in Transformation3D python class not found.
```
view_projection_set(ViewHandle, uVector, vVector, <DefaultDrawCode>)
```
The function sets the projection of a given view.
Input Parameters:
ViewHandle ElementHandle Handle to view
uVector Vector3D U-Vector
vVector Vector3D V-Vector
```
<DefaultDrawCode> integer If DefaultDrawCode==, the draw codes stored in the model subview are used. If DefaultDrawCode=1 (default), the defaultdraw codes are used.
```
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
```
kcs_HandleInvalid Given handle is invalid. (e.g. doesn't point to view)
```
kcs_Error General error
kcs_ModelViewNotFound View given by handle is not a model view.
```
view_slicedepth_get (ViewHandle)
```
The function retrieves the defined forward and backward distance for slice planes in relation to the view plane for a given view. The view can either be a symbolic view or a sliced modelview. For a symbolic view forward and backward slice depth from the projection plane is returned. For a sliced model view, a single depth is returned.
Input Parameters:
ViewHandle ElementHandle Handle to view
Returned value:
[0] integer Return code:
0 - no slice depth returned, view is not sliced
1 - slice depth returned for model view
2 - forward and backward slice depth returned
[1] real Slice depth for model view or forward slice depth for symbolic view
[2] real Backward slice depth for symbolic view
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
```
kcs_HandleInvalid Given handle is invalid. (e.g. doesn't point to view)
```
kcs_Error General error
kcs_ModelViewNotFound Given handle doesn't point to model view
```
view_slice_planes_get(handle)
```
This function returns slice planes for symbolic view.
Input Parameters:
handle ElementHandle Symbolic view handle.
Returned value:
[0] Plane3D Tuple with slice planes represented by 2 instances of Plane3D class.
[1] Plane3D
```
Exceptions:
```
kcs_ArgumentError Argument Error
kcs_DrawingNotCurrent Drawing not current
kcs_HandleInvalid Handle invalid
kcs_ModelViewNotFound Given handle doesn't specify model view
kcs_GeneralError Given handle doesn't specify symbolic view
```
view_symbolic_model_tra(ViewHandle,Transf3D)
```
The function retrieves the model transformation matrix for a given symbolic view.
Input Parameters:
View Handle ElementHandle Handle to symbolic view.
Transf3D Transformation3D Instance of KcsTransformation3D.Transformationd3D class
Returned value:
[0] Transf3D Instance of KcsTransformation3D.Transformation3D class
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
```
kcs_HandleInvalid Given handle is invalid. (e.g. doesn't point to view)
```
kcs_Error General error.
kcs_PythonMethodNotFound Method in Transformation3D python class not found.
```
view_restriction_area_get(ViewHandle)
```
This function returns area that has been defined for a view in a modelling drawing form.
Input Parameters:
ViewHandle ElementHandle Handle to the view.
Returned value:
[0] KcsRectangle2D Defined area of view.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_HandleInvalid Given handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_PythonLibraryNotFound Python library KcsRectangle2D not found.
kcs_PythonMethodNotFound Error in python definition of KcsRectangle class.
kcs_DoesNotExist Restriction area for specified view is not defined.
```
Examples:
```
# Example: kcs_ex_draft17.py
# Example: kcs_ex_draft16.py
# Example: kcs_ex_draft34.py
# Example: kcs_ex_draft30.py
# Example: kcs_ex_draft31.py
Copyright © 1993-2005 AVEVA AB
7.8 Model Handling Functions
This chapter describes functions handling models in the current drawing.
User's Guide Vitesse
```
Chapter: Drafting
```
```
model_draw(model, <viewhandle>)
```
```
model_draw(AssemblyCriteria, <viewhandle>)
```
This function draws whole model object, part or assembly. Valid model types are: plane panel, pipe, cable way, shell profiles, equipment, struct, hull curve, placed volume andventilation. In case of plane panels parts like: holes and cutouts cannot be separately drawn.
Input Parameters:
```
model Model Instance of KcsModel.Model class (name, type and part).
```
AssemblyCriteria ModelDrawAssyCriteria Instance of KcsModelDrawAssyCriteria class.
viewhandle ElementHandle Optional parameter. Handle to model view where model should be placed. If not given model will be placed in all modelviews.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments.
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Given handle is not valid.
kcs_DrawingNotCurrent No drawing was current
kcs_ModelViewNotFound No model view is found.
kcs_Error Specified model or assembly cannot be drawn.
```
model_delete(Model, <ViewHandle>)
```
The function deletes a given model in given view in the current drawing.
Input Parameters:
```
Model Model The model to delete (type & name)
```
ViewHandle ElementHandle Optional view handle. If no view specified then all views will be used.
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
kcs_ModelNotFound The model was not found in the drawing
```
model_colour_set(Model, Colour, <ViewHandle>)
```
The function changes the colour of a model in given view in the current drawing.
Input Parameters:
```
Model Model The model (type & name
```
Colour Colour The colour
ViewHandle ElementHandle Optional view handle. If no view specified then all views will be used.
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
kcs_ModelNotFound The model was found in the drawing
kcs_ColourInvalid Invalid colour
```
model_layer_set(Model, Layer, <ViewHandle>)
```
The function changes the colour of a model in given view in the current drawing.
Input Parameters:
```
Model Model The model (type & name
```
Layer Layer The layer
ViewHandle ElementHandle Optional view handle. If no view specified then all views will be used.
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
kcs_ModelNotFound The model was found in the drawing
kcs_ColourInvalid Invalid colour
```
model_properties_get(handle, model)
```
```
This function returns the properties of a model or part (subpicture on subview or component level or geometry handle)
```
Input Parameters:
handle ElementHandle Handle to the subview, component or geometry.
model Model Instance of KcsModel.Model class.
Returned value:
[0] Model Instance of KcsModel.Model class.
```
Exceptions:
```
kcs_HandleInvalid Invalid handle.
kcs_ArgumentError Invalid parameter.
kcs_DrawingNotCurrent No drawing was current.
kcs_ModelNotFound Model not found.
```
kcs_draft.model_handle_get(model)
```
```
The function will return list of all subviews containing given model or list of all components containing given model part (if KcsModel.Model.PartId <> 0)
```
Input Parameters:
mdel KcsModel.Model Instance of Model class.
Returned value:
[0] List of ElementHandle instances List of:
- subviews' handles if PartId = 0
- components' handles if PartId <> 0
```
Exceptions:
```
kcs_ArgumentError Arguments types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_ValueError Model name and type are to long strings.
kcs_GeneralError General error.
```
Example:
```
# Example: kcs_ex_draft19.py
# Example: kcs_ex_draft33.py
Copyright © 1993-2005 AVEVA AB
7.9 Functions for Creation of Basic Geometric Entities
```
This section describes functions to create geometric entities (elements) in the current drawing. These functions take an instance of a "geometric" class as input. For further informationabout such geometric classes, see the documentation of General.
```
```
Each function returns a handle to the created entity, used for identification in subsequent processing of the entity (e.g. the delete function).
```
User's Guide Vitesse
```
Chapter: Drafting
```
```
arc_new(Arc)
```
The function creates a circular arc.
Input Parameters:
Arc Arc2D The arc definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_AmplitudeTooBig The amplitude was too big
```
circle_new(Circle)
```
The function creates a circle.
Input Parameters:
Circle Circle2D The circle definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
conic_new(Conic)
```
The function creates a conic segment.
Input Parameters:
Conic Conic2D The conic segment definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
contour_new(Contour)
```
The function creates a contour.
Input Parameters:
Contour Contour2D The contour definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_AmplitudeTooBig The amplitude in at least one segment was too big
```
ellipse_new(Ellipse)
```
The function creates an ellipse.
Input Parameters:
Ellipse Ellipse2D The ellipse definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
line_new(Line)
```
The function creates a restricted line.
Input Parameters:
Line Rline2D The line definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
point_new(Point)
```
The function creates a point.
Input Parameters:
Point Point2D The point definition
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
rectangle_new(rectangle, <radius>)
```
The function creates regular or with rounded-corners rectangle.
Input Parameters:
Rectangle Rectangle2D Description of rectangle.
radius real It is used for rounded corners rectangle and specifies radius for corners arcs. Valid values are from 0.0 to half length of minimal rectangle side. Thisparameter is optional.
Returned value:
[0] ElementHandle Handle to new element.
```
Exceptions:
```
```
kcs_ValueError Invalid parameter value. (e.g. radius not valid)
```
kcs_DrawingNotCurrent No drawing was current
kcs_Error General error. Can't create element.
```
spline_new(Spline)
```
The function creates a spline, defined by a number of points. The spline is created with no tangent conditions.
Input Parameters:
Polygon Polygon2D The points defining the spline
Returned value:
[0] integer Handle to the created entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
Example:
```
# Example: kcs_ex_draft7.py
Copyright © 1993-2005 AVEVA AB
7.10 Functions for Creation of Texts
```
This section describes functions to create text entities (elements) in the current drawing. Each function returns a handle to the created entity, used for identification in subsequentprocessing of the entity (e.g. the delete function).
```
Multiple line texts are handled. The character '\n' is used as separator between two lines.
User's Guide Vitesse
```
Chapter: Drafting
```
```
text_length(Text)
```
The function calculate the text length in specified font format.
Input Parameters:
Text KcsText.Text The text definition.
None.
Returned value:
[0] float The length of the text.
```
Exceptions:
```
kcs_ArgumentError Invalid argument.
```
text_new(String, Pos)
```
```
text_new(Text)
```
The function creates a text, with modal attributes, in the current drawing.
Input Parameters:
String String Element handle.
Pos Point2D Position of the text.
Text KcsText Instance of KcsText.Text class.
Returned value:
[0] Integer Handle to the created text
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current
kcs_Error General error.
kcs_PythonLibraryNotFound Program can't find python library.
kcs_PythonMethodNotFound Python module error.
```
rule_text_new(Text, RuleNo)
```
The function creates a text according to a given rule number, in the drawing form of the current drawing. If such a text already exists, it will be replaced.
Input Parameters:
```
Text string The text value (maximum 512 characters)
```
RuleNo integer The rule number
Returned value:
[0] integer Handle to the created text
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_NoFormInDrawing The drawing contains no form
```
kcs_RuleNoInvalid Invalid rule (not found in form)
```
kcs_FormNotFound The drawing form was not found in the data bank
```
Example:
```
# Example: kcs_ex_draft11.py
# Example: kcs_ex_draft24.py
# Example: kcs_ex_draft25.py
Copyright © 1993-2005 AVEVA AB
7.11 Functions for Creation of Symbols
```
This section describes functions to create symbol entities (elements) in the current drawing. Each function returns a handle to the created entity, used for identification in subsequentprocessing of the entity (e.g. the delete function).
```
User's Guide Vitesse
```
Chapter: Drafting
```
```
symbol_new(Font, SymbNo, Pos)
```
```
symbol_new(Symbol)
```
The function creates a symbol, with modal attributes, in the current drawing.
Input Parameters:
Font integer Font number.
SymbNo integer Symbol number.
Pos Point2D Position of the symbol.
Symbol KcsSymbol Instance of KcsSymbol.Symbol class.
Returned value:
[0] integer Handle to the created symbol.
```
Exceptions:
```
kcs_FontInvalid Invalid font id
kcs_SymbolInvalid Invalid symbol id.
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current
kcs_Error General error.
kcs_PythonLibraryNotFound Program can't find python library.
kcs_PythonMethodNotFound Python module error.
```
Example:
```
# Example: kcs_ex_draft12.py
# Example: kcs_ex_draft24.py
# Example: kcs_ex_draft25.py
```
pipe_restr_symbol_new(Parent, StartPt, EndPt )
```
The function creates a new pipe restriction symbol primitive.
Parent ElementHandle Parent subview handle. The created component will belong to given subview.
StartPt Point2D Starting point of symbol
EndPt Point2D Ending point of symbol
Returned value:
[0] ElementHandle Handle to the created component.
```
Exceptions:
```
ks_DrawingNotCurrent No drawing was current
kcs_HandleInvalid Invalid handle of subview.
kcs_ArgumentError Invalid arguments list.
kcs_DistanceTooShort Distance between points is to short.
kcs_Error General error. Pipe restriction symbol can't be created.
```
general_restr_symbol_new(Parent, StartPt, EndPt, Soft )
```
The function creates a new general restriction symbol primitive.
Parent ElementHandle Parent subview handle. The created component will belong to given subview.
StartPt Point2D Starting point of symbol
EndPt Point2D Ending point of symbol
Soft boolean If true restriction symbol will be generated using spline. Otherwise contour will be used.
Returned value:
[0] ElementHandle Handle to the created component.
```
Exceptions:
```
ks_DrawingNotCurrent No drawing was current
kcs_HandleInvalid nvalid handle of subview.
kcs_ArgumentError Invalid arguments list.
kcs_ValueError Distance between points is to short.
kcs_Error General error. General restriction symbol can't be created.
Copyright © 1993-2005 AVEVA AB
7.12 Functions for Creation of Drawing Components
```
This chapter describes functions that create drawing components, such as dimensionings and notes. Each function returns a handle to the created component, used for identification insubsequent processing of the component (e.g. the delete function).
```
User's Guide Vitesse
```
Chapter: Drafting
```
Copyright © 1993-2005 AVEVA AB
7.12.1 Dimensioning Components
It is possible to create four different kinds of 2D dimensionings: Linear, Angle, Diameter and Radius. See Tribon M3 Drafting, Model Viewing and General Drafting for layout details. Seealso Tribon M3 Drafting, Appendices for default keywords ruling the layout.
User's Guide Vitesse
```
Chapter: Drafting
```
```
dim_linear_new(Measpnts, Type, Dir, Pos)
```
The function creates a linear 2D dimensioning component, given a number of points. The dimension lines will be parallel to Dir and pass through the point Pos.
Input Parameters:
Measpnts Polygon2D Polygon containing the measure points
Type integer Type of measure:
1 = Normal
2 = Chain
3 = Staircase
Dir Vector2D The direction of the measure
Pos Point2D The location of the measure
Returned value:
[0] integer Handle to the created component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_OwnerNotFound No structural owner to the dimensioning component could be derived
kcs_MeasureNotCreated Failure creating the dimensioning component
```
dim_angle_new(Line1, Line2, ArcPos, TextPos)
```
The function creates an 2D angular dimensioning component, given two non-parallel lines.
Input Parameters:
Line1 Rline2D The first line
Line2 Rline2D The second line
ArcPos Point2D The location of the measure arc
TextPos Point2D The location of the measure text
Returned value:
[0] integer Handle to the created component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_LinesParallel The two lines are parallel
kcs_OwnerNotFound No structural owner to the dimensioning component could be derived
kcs_MeasureNotCreated Failure creating the dimensioning component
```
dim_diameter_new(CircleOrArc, Pos1, Pos2)
```
The function creates a 2D diameter dimensioning component, given a circle or an arc.
```
Note: Pos1 and Pos2 are optional.
```
 If neither Pos1 nor Pos2 are not given, the reference line will start at:
 if arc object: the middle of the arc
 if circle object: the middle of the upper right quadrant of the circle
The reference line will aim towards the centre of the arc or the circle
```
 If Pos1, but not Pos2, is given, the reference line is defined by Pos1 and the centre of the arc or the circle. If Pos1 is a point inside the circle or the imagined circle defined by thearc, the reference line will aim away from the centre; otherwise it will aim towards the centre.
```
 If both Pos1 and Pos2 are given a "knuckled" measure is created. The reference line will pass through Pos1 and the horizontal line will pass through Pos2.
Input Parameters:
CircleOrArc Circle2D/Arc2D Object containing the arc/circle to be measured
```
Pos1 Point2D The location of the measure (optional)
```
```
Pos2 Point2D The location of the horizontal part in a "knuckled" measure (optional)
```
Returned value:
[0] integer Handle to the created component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_OwnerNotFound No structural owner to the dimensioning component could be derived
kcs_MeasureNotCreated Failure creating the dimensioning component
```
dim_radius_new(CircleOrArc, Pos1, Pos2)
```
The function creates a 2D radius dimensioning component, given a circle or an arc.
```
Note: Pos1 and Pos2 are optional.
```
 If neither Pos1 nor Pos2 are not given, the reference line will start at:
 if arc object: the middle of the arc
 if circle object: the middle of the upper right quadrant of the circle
The reference line will aim towards the centre of the arc or the circle.
```
 If Pos1, but not Pos2, is given, the reference line is defined by Pos1 and the centre of the arc or the circle. If Pos1 is a point inside the circle or the imagined circle defined by thearc, the reference line will aim away from the centre; otherwise it will aim towards the centre.
```
 If both Pos1 and Pos2 are given a "knuckled" measure is created. The reference line will pass through Pos1 and the horizontal line will pass through Pos2
Input Parameters:
CircleOrArc Circle2D/Arc2D Object containing the arc/circle to be measured
```
Pos1 Point2D The location of the measure (optional)
```
```
Pos2 Point2D The location of the horizontal part in a "knuckled" measure (optional)
```
Returned value:
[0] integer Handle to the created component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_OwnerNotFound No structural owner to the dimensioning component could be derived
kcs_MeasureNotCreated Failure creating the dimensioning component
```
dim_linear_new(polygon3D, type, projDir, locPoint2D, witnDir, <modelsubview>, <basepoint>)
```
The function creates a new 3D linear dimension.
Input Parameters:
polygon3D Polygon3D 3D polygon which contains 3D points for dimensioning.
type integer Type of dimension:
1 - Normal
2 - Chain
3 - Staircase
projDir Vector3D Projection direction vector.
locPoint2D Point2d 2D point in drawing where the coordinate dimension should be placed.
witnDir Vector3D Direction vector for witness lines.
```
modelsubview ElementHandle Handle to a subview where dimension will be placed. It must be a model subview (optional).
```
```
basepoint integer Index of measure point (0 based) which will be used to define dimension element plane. This parameter is optional. If no index is given thefirst point will be used.
```
Returned value:
[0] integer Handle to created dimension component.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_SubviewNotFound Subview not found.
kcs_MeasureNotCreated Dimension element not created.
kcs_Error General error.
```
dim_point_3d(point3D, locPoint, height, rotation, annotation, <modelsubview>)
```
The function creates a new point 3D dimension.
Input Parameters:
point3D Point3D 3D point for which the coordinates should be displayed.
locPoint Point2d 2D point in drawing where the coordinate dimension should be placed.
height real Height of dimension text.
rotation real Rotation of dimension box.
annotation string Annotation text. If empty no annotation will be added.
```
modelsubview integer Handle to a subview where dimension will be placed. It must be a model subview (optional).
```
Returned value:
[0] integer Handle to created dimension component.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_SubviewNotFound Subview not found.
kcs_MeasureNotCreated Dimension element not created.
kcs_Error General error.
kcs_HandleInvalid Invalid handle to given subview.
```
dim_shell_new(Viewhandle,From, Along, To, <Type>, <Colour>)
```
The function adds dimensioning from one model object to another along a third in a given view. The model objects have to intersect the same surface. Valid model types are:longitudinal, transversal, hull curve, seam and stiffener.
Input Parameters:
Viewhandle Element Handle Handle to model view.
From List List of KcsModel.Model
Along List List of KcsModel.Model
To List List of KcsModel.Model
Type Integer = 0: only the dimension text will be created.
= 1: Arrow at end point and circle at start point also displayed.
= 2: The dimension trace are also displayed.
Colour KcsColour.Colour The colour of the dimension
Returned value:
[0] List Handles to the created components
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_ArgumentError Invalid arguments list
kcs_GeneralError List of result can't be created for some internal reason
kcs_ ModelViewNotFound Specified view not found
```
Examples:
```
# Example: kcs_ex_draft8.py
# Example: kcs_ex_draft29.py
# Example: kcs_ex_draft28.py
Copyright © 1993-2005 AVEVA AB7.12.2 Hatch Components
User's Guide Vitesse
```
Chapter: Drafting
```
```
hatch_new(Contour)
```
```
hatch_new(ContHandle)
```
The function creates a hatch pattern component, given a closed 2D contour.
Input Parameters:
Contour Contour2D The contour definition
ContHandle integer Handle to the contour
Returned value:
[0] integer Handle to the created component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to contour
kcs_AmplitudeTooBig The amplitude in at least one segment was too big
kcs_OwnerNotFound No structural owner to the hatch pattern component could be derived
```
hatch_island_new(HatchHandle, Island)
```
```
hatch_island_new(HatchHandle, IslandHandle)
```
The function removes the part of the given hatch pattern that lies inside a given island, defined by a closed 2D contour.
Input Parameters:
HatchHandle integer Handle to the given hatch pattern component
Island Contour2D The island contour definition
IslandHandle integer Handle to the island contour
Returned value:
[0] integer Handle to the resulting hatch pattern component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_HandleInvalid Invalid handle to hatch pattern/island contour
kcs_AmplitudeTooBig The amplitude in at least one segment in the island contour was too big
kcs_OwnerNotFound No structural owner to the resulting hatch pattern component could be derived
```
Example:
```
# Example: kcs_ex_draft9.py
Copyright © 1993-2005 AVEVA AB
7.12.3 Note and Position Number Components
User's Guide Vitesse
```
Chapter: Drafting
```
```
note_new(Text, RefLine)
```
The function creates a note component. The reference line is defined by a 2D polygon.
Input Parameters:
Text string The text of the note
RefLine Polygon2D The reference line
Returned value:
[0] integer Handle to the created note component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_SymbolError The modal note symbol was not found
kcs_OwnerNotFound No structural owner to the resulting note component could be derived
```
posno_new(Text, RefLine)
```
The function creates a position number component. The reference line is defined by a 2D polygon.
Input Parameters:
Text string The text of the position number
RefLine Polygon2D The reference line
Returned value:
[0] integer Handle to the created position number component
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
kcs_SymbolError The modal position number symbol was not found
kcs_OwnerNotFound No structural owner to the resulting position number component could be derived
```
Example:
```
# Example: kcs_ex_draft10.py
Copyright © 1993-2005 AVEVA AB
7.12.4 Other Drawing Components
User's Guide Vitesse
```
Chapter: Drafting
```
```
cloud_new(Parent, Shape)
```
The function creates a new cloud primitive.
Parent ElementHandle Parent subview handle. The created cloud component will belong to given subview.
Shape Rectangle2D or Polygon2D Contour for cloud symbol.
Returned value:
[0] ElementHandle Handle to the created cloud component.
```
Exceptions:
```
ks_DrawingNotCurrent No drawing was current
kcs_ValueError Values of input parameters are invalid. For example: given polygon has only 2 vertexes.
kcs_ArgumentError Invalid arguments list.
kcs_Error General error. Cloud component can't be created.
kcs_HandleInvalid Invalid handle of subview.
```
cross_new(Parent, String, Line1, Line2)
```
The function creates a new cross primitive.
Parent ElementHandle Parent subview handle. The created cross component will belong to given subview.
String Text Instance of Text class. Members of Text class like: Visible, Detectable, Colour, Layer, Position are ignored.
Line1 Rline2D First line for cross symbol.
Line2 Rline2D Second line for cross symbol.
Returned value:
[0] ElementHandle Handle to the created cross component.
```
Exceptions:
```
ks_DrawingNotCurrent No drawing was current.
kcs_ValueError Values of input parameters are invalid. For example: lines are parallel.
kcs_ArgumentError Invalid arguments list.
kcs_Error General error. Cross component can't be created.
kcs_HandleInvalid Invalid handle of subview
```
ruler_new(Parent, StartPt, TickLen, FirstTick, LastTick, LabelTick, TextProp)
```
The function creates a new ruler primitive.
Parent ElementHandle Parent subview handle. The created component will belong to given subview.
StartPt Point2D Starting point of ruler
TickLen Real Distance between ticks
FirstTick Integer First ruler tick value
LastTick Integer Last ruler tick value
LabelTick Integer Value which identifies to which ticks add label with tick value. The labeled tick is determined by dividing total number of ticks by LabelTickvalue.
TextProp Text Class defining properties of ruler label texts. The following properties are used: font, test height, rotation, aspect ratio, slanting.
Returned value:
[0] ElementHandle Handle to the created component.
```
Exceptions:
```
ks_DrawingNotCurrent No drawing was current.
kcs_HandleInvalid Invalid handle of subview.
kcs_ArgumentError Invalid arguments list.
kcs_Error General error. Ruler component can't be created.
```
position_ruler_new (Act, View, StartPt, EndPt)
```
This function creates different kinds of rulers in model view and generates the complete dimensioning components automatically.
Act integer Ruler type:
1 - Base Line
2 - Center Line
3 - Fram Ruler
4 - Longitudinal Horizontal Ruler
5 - Longitudinal Vertical Ruler
View ElementHandle View handle. The created component will belong to given view.
StartPt Point2D Starting point of ruler.
EndPt Point2D Ending point of ruler.
Returned value:
[0] ElementHandle Handle to the created measure component.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
kcs_ArgumentError Invalid arguments list.
kcs_HandleInvalid Invalid handle to view.
kcs_RulerTypeInvalid Invalid ruler type. Creation not possible in given view,
kcs_ValueError Invalid point.
kcs_BasicLineToCloseToViewPlane The base line plane is too close to the view plane.
kcs_CenterLineToCloseToViewPlane The center line plane is too close to the view plane.
Copyright © 1993-2005 AVEVA AB
7.13 Property Changing and Retrieving Functions
This chapter describes functions that change properties of arbitrary entities in the current drawing
Layer Functions
```
There is a possibility to use the Drafting layer show/hide mechanism in Vitesse. The user can specify layers to show (other layers will be hidden) or layers to hide other layers will bevisible). It is not allowed to specify layers to hide and show at the same time.
```
```
To reset the layers show/hide mode, the function layer_show_all() should be used.
```
.
Properties Get Functions
This chapter describes functions used to get properties of text, symbol and contour. The properties get functions described in this chapter use the Text, Symbol and Contour2D classes toget properties of element. These classes hold information about a text, symbol and contour..
User's Guide Vitesse
```
Chapter: Drafting
```
```
layer_show(layer)
```
```
layer_show(layersList)
```
```
The function will show layer (layers). It will set show mode if it is not selected yet. If application is in show mode than this layer will be added to previously selected layers. If hide modeis active it will be reset and than changed to show mode.
```
Input Parameters:
layer Layer Instance of KcsLayer. Layer class.
layersList [Layer, ...] List of KcsLayer. Layer class instances.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Argument type is not valid.
kcs_DrawingNotCurrent No drawing is current.
```
layer_hide(layer)
```
```
layer_hide(layersList)
```
```
The function will hide layer (layers). It will set hide mode if it is not selected yet. If application is in hide mode than this layer will be added to previously selected layers. If show mode isactive it will be reset and than changed to show mode.
```
Input Parameters:
Layer Layer Instance of KcsLayer. Layer class.
layersList [Layer, ...] List of KcsLayer. Layer class instances.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Argument type is not valid.
kcs_DrawingNotCurrent No drawing is current.
```
layer_show_all()
```
The function will reset layers show/hide mode. All layers will be visible.
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError This function requires no arguments.
kcs_DrawingNotCurrent No drawing is current.
kcs_GeneralError General error.
```
element_layer_get(handle, layer)
```
The function will return element layer.
Input Parameters:
handle ElementHandle Handle to element.
layer Layer Instance of Layer class.
Returned value:
[0] Layer Instance of Layer class.
```
Exceptions:
```
kcs_ArgumentError Argument types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_HandleInvalid Given handle is not valid.
kcs_PythonMethodNotFound Python method not found. Check your KcsLayer implementation file.
```
element_layer_set(handle, layer)
```
The function will set layer of element given by handle.
Input Parameters:
handle ElementHandle Handle to element.
layer Layer Instance of Layer class.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Argument types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_HandleInvalid Given handle is not valid.
kcs_PythonMethodNotFound Python method not found. Check your KcsLayer implementation file.
kcs_GeneralError General error. Layer can not be set.
```
model_layer_set(model, layer)
```
The function changes the layer of a model in all views in the current drawing.
Input Parameters:
```
model Model The Model (type & name)
```
layer Layer Instance of Layer class.
Returned value:
None
```
Exceptions:
```
kcs_ValueError Argument value error.
kcs_DrawingNotCurrent No drawing is current.
kcs_ModelNotFound Model not found.
kcs_GeneralError General error. Layer can not be set.
```
element_colour_get(handle, colour)
```
The function will get colour of geometry element given by handle.
Input Parameters:
handle ElementHandle Handle to geometry element.
colour Colour Instance of Colour class.
Returned value:
[0] Colour Instance of Colour class.
```
Exceptions:
```
kcs_ArgumentError Argument types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_HandleInvalid Given handle is not valid.
kcs_PythonMethodNotFound Python method not found. Check your KcsColour implementation file.
```
element_linetype_get(handle, linetype)
```
The function will get linetype of geometry element given by handle.
Input Parameters:
handle ElementHandle Handle to geometry element.
linetype Linetype Instance of Linetype class.
Returned value:
[0] Linetype Instance of Linetype class.
```
Exceptions:
```
kcs_ArgumentError Argument types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_HandleInvalid Given handle is not valid.
kcs_PythonMethodNotFound Python method not found. Check your KcsLinetype implementation file.
```
element_linetype_set(handle, linetype)
```
The function will set linetype to element given by handle.
Input Parameters:
handle ElementHandle Handle to geometry element.
linetype Linetype Instance of Linetype class.
Returned value:
```
Exceptions:
```
kcs_ArgumentError Argument types are not valid.
kcs_DrawingNotCurrent No drawing is current.
kcs_HandleInvalid Given handle is not valid.
kcs_PythonMethodNotFound Python method not found. Check your KcsLinetype implementation file.
kcs_GeneralError General error. Linetype can not be changed.
```
text_properties_get(handle, text)
```
The function returns a properties of text selected by handle.
Input Parameters:
handle integer Element handle
text KcsText Instance of KcsText.Text class.
Returned value:
[0] KcsText Instance of KcsText. Text class.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_HandleInvalid Given handle is not valid or was not found in drawing.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
kcs_PythonLibraryNotFound Program can't find python library.
kcs_PythonMethodNotFound Python module error.
```
contour_properties_get(handle, contour)
```
The function returns a properties of contour selected by handle.
Input Parameters:
handle integer Element handle
contour KcsContour2D Instance of KcsContour2D.Contour2D class.
Returned value:
[0] KcsContour2D Instance of KcsContour2D.Contour2D class.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_HandleInvalid Given handle is not valid or was not found in drawing.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
kcs_PythonLibraryNotFound Program can't find python library.
kcs_PythonMethodNotFound Python module error.
```
symbol_properties_get(handle, symbol)
```
The function returns a properties of symbol selected by handle.
Input Parameters:
handle integer Element handle
symbol KcsSymbol Instance of KcsSymbol. Symbol class.
Returned value:
[0] KcsSymbol Instance of KcsSymbol. Symbol class.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_HandleInvalid Given handle is not valid or was not found in drawing.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
kcs_PythonLibraryNotFound Program can't find python library.
kcs_PythonMethodNotFound Python module error.
```
element_colour_set(Handle, Colour)
```
The function changes the colour of an arbitrary entity.
Input Parameters:
Handle integer Handle to the entity
Colour Colour The colour
Returned value:
None
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
kcs_HandleInvalid Invalid handle to given entity
kcs_ColourInvalid Invalid colour
```
Example:
```
# Example: kcs_ex_draft26.py
# Example: kcs_ex_draft23.py
```
reference_move ()
```
This function moves reference symbol together with associated text to a new location.
Input Parameters:
Handle ElementHandle Handle to reference element.
Position Point2D New position where reference text should be placed.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_HandleInvalid Invalid element handle.
kcs_DrawingNotCurrent No drawing was current.
Copyright © 1993-2005 AVEVA AB
7.14 Identifying and Capturing Functions
Identify Functions
```
This chapter describes functions to identify the nearest element in the current drawing, based on a given drawing coordinate or name (identification by name is only for views, subviewsand components).
```
Capture Functions
This chapter describes functions to capture elements in the current drawing. The capture functions described in this chapter use the CaptureRegion2D as input parameter. ThisCaptureRegion2D class holds information about a 2D capture region. Region can be described by a Contour2D or Rectangle2D.
This chapter describes functions to identify arbitrary entities in the current drawing.
User's Guide Vitesse
```
Chapter: Drafting
```
```
element_identify(Name)
```
The function returns a handle to the entity in the current drawing, identified by a given name. If there are more than one entity with this name, the first one encountered will be returned.
Input Parameters:
Name string The name of the entity
Returned value:
[0] KcsElementHandle Handle to the entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ElementNotFound The entity was not found in the drawing
```
model_identify(IdPnt, Model)
```
The function identifies a model, closest to a given point in the current drawing.
Input Parameters:
IdPnt Point2D The identification point
```
Model Model The model to identify (type & name)
```
Output Parameters:
Model Model The model identified
Returned value:
[0] Model The model identified
[1] integer Handle to the model subview
[2] integer Handle to the model component
```
Exceptions:
```
kcs_ValueError Invalid parameter value
kcs_DrawingNotCurrent No drawing was current
kcs_ModelNotFound No model identified
```
subview_identify(point)
```
```
subview_identify(name)
```
The function returns a handle to the subview on 2:nd level closest to the given point or with a given name. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
name string The name of the subview.
Returned value:
[0] integer Handle to identified subview.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_SubviewNotFound Subview not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
component_identify(point)
```
```
component_identify(name)
```
The function returns a handle to the component on 3:nd level closest to the given point or with a given name. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
name string The name of the component.
Returned value:
[0] integer Handle to identified component.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_ComponentNotFound Component not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error
General error.
```
volume_prim_identify(point)
```
The function returns the volume primitive closest to the given point in the current drawing.
Input Parameters:
Point Point2D Point in drawing.
Returned value:
[0] integer The subvolume number.
[1] integer The primitive number.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_PrimitiveNotFound Primitive not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
dim_identify(point)
```
The function returns a handle to the dimension component closest to the given point. Please note that only visible layers are considered.
Input Parameters:
Point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified dimension component.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Dimension not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
note_identify(point)
```
The function returns a handle to the note component closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified note component.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Note not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
posno_identify(point)
```
The function returns a handle to the position number component closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified position number component.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Position number not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
hatch_identify(point)
```
The function returns a handle to the hatch component closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified hatch component.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Hatch not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
text_identify(point)
```
The function returns a handle to the text closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified text.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Text not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
symbol_identify(point)
```
The function returns a handle to the symbol closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified symbol.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Symbol not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error
General error.
```
contour_identify(point)
```
The function returns a handle to the contour closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] Integer Handle to identified contour.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Contour not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
point_identify(point)
```
The function returns a handle to the point closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified point.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Point not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
geometry_identify(point)
```
The function returns a handle to the geometry closest to the given point. Please note that only visible layers are considered.
Input Parameters:
point Point2D Point in drawing.
Returned value:
[0] integer Handle to identified geometry.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Geometry not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
model_capture(region)
```
The function returns a list of handles to models captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured models
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
dim_capture(region)
```
The function returns a list of handles to dimensions captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured dimensions
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
note_capture(region)
```
The function returns a list of handles to notes captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured notes
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
posno_capture(region)
```
The function returns a list of handles to position numbers captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured position numbers.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
hatch_capture(region)
```
The function returns a list of handles to hatches captured by given region. Please note that only visible layers are considered.
Input Parameters:
Region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured hatches
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
text_capture(region)
```
The function returns a list of handles to texts captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured texts
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
symbol_capture(region)
```
The function returns a list of handles to symbols captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured symbols
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
contour_capture(region)
```
The function returns a list of handles to contours captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured contours
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
point_capture(region)
```
The function returns a list of handles to points captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of KcsElementHandle Handles to captured points
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
geometry_capture(region)
```
The function returns a list of handles to geometries captured by given region. Please note that only visible layers are considered.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
List of KcsElementHandle Handles to captured geometries
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound Entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
view_capture(region)
```
The function returns a list of handles to views captured by given region.
Input Parameters:
region CaptureRegion2D Region in drawing.
Returned value:
[0] List of element handles. Handles to captured views.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound The entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
subview_capture(region)
```
The function returns a list of handles to subviews captured by given region.
Input Parameters:
region CaptureRegion2D. Region in drawing.
Returned value:
[0] List of element handles. Handles to captured subviews.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound The entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
component_capture(region)
```
The function returns a list of handles to components captured by given region.
Input Parameters:
region CaptureRegion2D. Region in drawing.
Returned value:
[0] List of element handles. Handles to captured components.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_NotFound The entities not found.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_draft20.py
# Example: kcs_ex_draft21.py
# Example: kcs_ex_draft22.py
Copyright © 1993-2005 AVEVA AB
7.15 Deleting Functions
User's Guide Vitesse
```
Chapter: Drafting
```
```
element_delete(Handle)
```
The function deletes an arbitrary entity in the current drawing. The entity is given by a handle.
Input Parameters:
Handle KcsElementHandle Handle to the entity
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_HandleInvalid Invalid handle to given entity
```
Example:
```
# Example: kcs_ex_draft14.py
```
delete_by_area (handles, act, contour)
```
This function deletes everything inside or outside specified area.
Input Parameters:
handles List or tuple of element handles Handles of elements that should be considered.
act Constant kcs_draft.kcsDEL_INSIDE or kcs_draft.kcsDEL_OUTSIDE
contour Contour2D Contour defining deletion area
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Argument Error
kcs_ValueError Handle invalid or not an instance of ElementHandle class.
kcs_DrawingNotCurrent There is no current drawing.
kcs_GeneralError General error
Copyright © 1993-2005 AVEVA AB
7.16 Highlighting Functions
This section describes functions to highlight certain geometric entities in the current drawing. All such functions return a handle to the highlighted entity, used when turning off thehighlighting by the function highlight_off.
User's Guide Vitesse
```
Chapter: Drafting
```
```
Example:
```
```
hl_handle = arc_highlight(arc)<do something>
```
```
highlight_off(hl_handle)
```
```
arc_highlight(Object)
```
The function highlights a circular arc.
Input Parameters:
Object Arc2D The arc definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
circle_highlight(Object)
```
The function highlights a circle.
Input Parameters:
Object Circle2D The circle definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
conic_highlight(Object)
```
The function highlights a conic segment.
Input Parameters:
Object Conic2D The conic segment definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
contour_highlight(Object)
```
The function highlights a contour.
Input Parameters:
Object Contour2D The contour definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
ellipse_highlight(Object)
```
The function highlights an ellipse.
Input Parameters:
Object Ellipse2D The ellipse definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
line_highlight(Object)
```
The function highlights a restricted line.
Input Parameters:
Object Rline2D The line definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
point_highlight(Object,<Type>)
```
The function highlights a point.
Input Parameters:
Object Point2D The point definition
```
Type =1 A cross will be drawn that stays the same size regardless of zoom.
```
Else A circle will be drawn as before.
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
rectangle_highlight(Object)
```
The function highlights a rectangle.
Input Parameters:
Object Rectangle2D The rectangle definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError kcs_ValueError
```
spline_highlight(Object)
```
The function highlights a spline.
Input Parameters:
Object Polygon2D The spline definition
Returned value:
[0] KcsElementHandle Handle to the highlighted entity
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_ValueError Invalid parameter value
```
element_highlight(Handle) or element_highlight([Handles])
```
The function highlights an arbitrary entity/entities given by a handle/list of handles.
Input Parameters:
Handle KcsElementHandle Single handle or a list of handles.
Returned value:
[0] KcsElementHandle Handle to the highlighted entity/entities.
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current
kcs_HandleInvalid Invalid handle to given entity
```
highlight_off(Handle)
```
The function turns off a given highlighting.
Input Parameters:
```
Handle KcsElementHandle Handle to a highlighted entity (no validity check.
```
If zero is given, all highlighted entities are turned off.
Returned value:
None
```
Exceptions:
```
None
```
Example:
```
# Example: kcs_ex_draft13.py
Copyright © 1993-2005 AVEVA AB
7.17 Subpicture and Element Navigation Functions
User's Guide Vitesse
```
Chapter: Drafting
```
```
element_parent_get(elementHandle)
```
The function returns handle to the parent subpicture of the given element.
Input Parameters:
elementHandle KcsElementHandle Handle to element
Returned value:
[0] KcsElementHandle Handle of parent subpicture.
```
Exceptions:
```
kcs_ArgumentError Parameter is not expected.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element has no parent. This exception is raised when an attempt is made to get the parent of a view.
kcs_Error General error.
```
element_child_first_get(<subpictureHandle>)
```
The function returns handle to the first child of the given subpicture handle. If no argument is given, a handle to the first view in the drawing is returned.
Input Parameters:
subpictureHandle KcsElementHandle Handle to subpicture
Returned value:
[0] KcsElementHandle Handle of the first child element.
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element has no children.
kcs_Error General error.
```
element_sibling_next_get(elementHandle)
```
The function returns handle to the next sibling of the given element.
Input Parameters:
elementHandle KcsElementHandle Handle to element
Returned value:
[0] KcsElementHandle Handle of the next sibling element.
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound There is no next sibling element.
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_draft30.py
Copyright © 1993-2005 AVEVA AB
7.18 Drawing Element Functions
User's Guide Vitesse
```
Chapter: Drafting
```
```
element_transform(elementHandle, <transf2d>)
```
The function transform element by given transformation data.
Input Parameters:
elementHandle KcsElementHandle Handle to the element.
<transf2d> Transformation2D Transformation data. If not given then transformation toolbar will be displayed and the user will be prompted totransform given element manually.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
```
element_transformation_get (ElemHandle, Transf2D)
```
The function retrieves the defined transformation for a given element.
Input Parameters:
ElemHandle ElementHandle Handle to element
Transf2D Transformation2D Instance of KcsTransformation2D.Transformation2D class
Returned value:
[0] Transf2D Instance of KcsTransformation2D.Transformation2D class
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DrawingNotCurrent No drawing was current.
```
kcs_HandleInvalid Given handle is invalid. (e.g. doesn't point to view)
```
kcs_Error General error
kcs_PythonMethodNotFound Method in Transformation2D python class not found.
```
element_copy(elementHandle, <targetSubpictureHandle>)
```
The function copies an element and places it under the given target subpicture. If no target subpicture is given, the new element will belong to the same subpicture as the sourceelement. If the element is subpicture and the target parent subpicture already has a subpicture with this name, the name will be blanked. Space that when copying and subsequently
```
transforming an element, the original element will be temporarily erased from the display. Please call the dwg_repaint() function to repaint the display so that the original element willappear again.
```
Input Parameters:
ElementHandle ElementHandle Handle to source element.
targetSubpictureHandle ElementHandle Handle to target parent subpicture.
Returned value:
[0] ElementHandle Handle to new element.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_HandleInvalid Given handles are not valid. There are no elements in current drawing with these handles.
```
kcs_OwnerNotFound Owner subpicture not found. (e.g. view handle for component copy)
```
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error. Can't copy elements.
```
element_extent_get(<ElementHandle>)
```
```
This function returns the current extent (occupied area) of an element in the current drawing. For subpictures method IsEmpty of returned Rectangle2D instance should be use todetermine if subpicture has elements and it is possible to obtain its extent. If ElementHandle is not specified extension of whole drawing will be returned.
```
Input Parameters:
ElementHandle ElementHandle Handle to the element. This parameter is optional.
Returned value:
[0] KcsRectangle2D Current extent area.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_HandleInvalid Given handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_PythonLibraryNotFound Python library KcsRectangle2D not found.
kcs_PythonMethodNotFound Error in python definition of KcsRectangle class.
```
Example:
```
# Example: kcs_ex_draft30.py
# Example: kcs_ex_draft31.py
# Example: kcs_ex_draft35.py
```
element_transformation_redefine (Handle, Transf2d)
```
This function redefines transformation for given element.
Input Parameters:
Handle ElementHandle Handle to element
Transf2d Transformation2D New transformation
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_HandleInvalid Invalid element handle.
kcs_DrawingNotCurrent No drawing was current.
```
element_visibility_get (elementHandle)
```
This function sets visibility of element specified by handle.
Input Parameters:
elementHandle KcsElementHandle Handle to the element.
Returned value:
[0] integer 1 - if element is visible
0- otherwise
```
Exceptions:
```
kcs_ArgumentError Argument error
kcs_DrawingNotCurrent There is no current drawing.
kcs_HandleInvalid Given handle is not a vlid handle.
```
element_visibility_set (elementHandle, Visibility)
```
This function sets visibility of element specified by handle.
Input Parameters:
elementHandle KcsElementHandle Handle to the element.
Visibility integer If Visibility = 1 element will be visible, if 0 not.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Argument error.
kcs_DrawingNotCurrent There is no current drawing.
kcs_HandleInvalid Given handle is not a valid handle.
Copyright © 1993-2005 AVEVA AB
7.19 Element type functions
This chapter describes functions to get element type.
User's Guide Vitesse
```
Chapter: Drafting
```
```
element_is_contour(elementHandle)
```
The function checks if an element is a contour.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_view(elementHandle)
```
The function checks if an element is a view.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_subpicture(elementHandle)
```
The function checks if an element is a subpicture.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_subview(elementHandle)
```
The function checks if an element is a subview.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_component(elementHandle)
```
The function checks if an element is a component.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_text(elementHandle)
```
The function checks if an element is a text.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_symbol(elementHandle)
```
The function checks if an element is a symbol.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_note(elementHandle)
```
The function checks if an element is a note component.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_posno(elementHandle)
```
The function checks if an element is a position number component.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_dimension(elementHandle)
```
The function checks if an element is a dimension component.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_hatch(elementHandle)
```
The function checks if an element is a hatch component.
Input Parameters:
elementHandle KcsElementHandle Handle to the element
Returned value:
[0] integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
Example:
```
# Example: kcs_ex_draft30.py
```
element_is_nesting(elementHandle)
```
The function checks if an subpicture is a nesting subview or component which belongs to it.
Input Parameters:
elementHandle ElementHandle Handle to the component or subview.
Returned value:
[0] Integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_burning_sketch(elementHandle)
```
The function checks if an subpicture is a burning sketch subview or component which belongs to it.
Input Parameters:
elementHandle ElementHandle Handle to the component or subview.
Returned value:
[0] Integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
element_is_detail_sketch (elementHandle)
```
The function checks if an subpicture is a detail sketch subview or component which belongs to it.
Input Parameters:
elementHandle ElementHandle Handle to the component or subview.
Returned value:
[0] Integer 1 if element matches type, otherwise 0
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_HandleInvalid Invalid handle.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound Element not found.
```
Example:
```
# Example: kcs_ex_draft30.py
```
element_is_bodyplan_view (ViewPtr)
```
This function checks whether the current picture is a BodyplanView.
Input parameters
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a BodyplanView
1==If the model is a BodyplanView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_curpanel_view (ViewPtr)
```
This function checks whether the current picture is a CurpanelView.
Input parameters
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a CurpanelView
1==If the model is a CurpanelView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_detail_view (ViewPtr)
```
This function checks whether the current picture is a Detail View.
Input parameters
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a Detail View
1==If the model is a Detail View
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_devpla_view (ViewPtr)
```
This function checks whether the current picture is a DevplaView.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a DevplaView
1==If the model is a DevplaView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_devsti_view (ViewPtr)
```
This function checks whether the current picture is a DevstiView.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a DevstiView
1==If the model is a DevstiView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_general_view (ViewPtr)
```
This function checks whether the current picture is a General View.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a General View
1==If the model is a General View
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_shellx_view (ViewPtr)
```
This function checks whether the current picture is a ShellxView.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a ShellxView
1==If the model is a ShellxView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_symbolic_view (ViewPtr)
```
This function checks whether the current picture is a Symbolic View.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a Symbolic View
1==If the model is a Symbolic View
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
```
element_is_templ_view (ViewPtr)
```
This function checks whether the current picture is a TemplView.
Input parameters:
ViewPtr Integer Handle to the view
Returned value:
[0] Integer 0==If the model is not a TemplView
1==If the model is a TemplView
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_Value_Error Invalid parameter value.
kcs_DrawingNotCurrent Active drawing not set.
kcs_GeneralError List of result can't be created for some internal reason.
Copyright © 1993-2005 AVEVA AB
7.20 Subpicture Functions
Management of subpictures
This chapter describes functions to create new subview and component, traverse subpictures, elements tree and change current subpicture.
User's Guide Vitesse
```
Chapter: Drafting
```
```
subview_new (<name>)
```
The function creates a new subview. The subview will be placed within the current view. Current subpicture cannot be set to "automatic" when this function is executed.
Input Parameters:
```
name string Name for new subview (optional).
```
Returned value:
[0] KcsElementHandle Handle to created subview.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_NameOccupied Name is already in use in current view.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
component_new (<name>)
```
The function creates a new component. The component will be placed within the current subview. Current subpicture cannot be set to "automatic" when this function is executed.
Input Parameters:
```
name string Name for new component (optional).
```
Returned value:
[0] KcsElementHandle Handle to created component.
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_NameOccupied Name is already in use in current subview.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
subpicture_current_set (subpictureHandle)
```
```
The function sets a subpicture to be current for the creation of new geometry. If a component subpicture element handle is give, this will be set as current. If a handle to view or subviewis given, the component (and subview) will be chosen by the system. If no argument is given the subpicture will be automatically chosen each time geometry is created.
```
```
Note: If you will try to set a view or a subview which has no children as current then system will create component (and subview) and set it current.
```
Input Parameters:
```
subpictureHandle KcsElementHandle Handle to subpicture (optional).
```
Returned value:
[0] KcsElementHandle Handle to created component.
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
subpicture_current_get ()
```
The function returns the current subpicture status. If an empty result list is returned, this means that the current subpicture setting is set to "automatic".
```
Note: If you will use that function when current subpicture settings is not set to "automatic" and there are no views, subviews or components system will create one at set is ascurrent. Handles of created subpictures will be returned.
```
Input Parameters:
None
Returned value:
```
[0] List of ElementHandle If not empty then handles to current view (first list item), subview (second list item) and component (third list item).
```
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
subpicture_name_set(subpictureHandle, name)
```
The function sets new name for existing subpicture. Name of form view can't be changed. If name is not empty and there is another subpicture on this level with the same nameexception will be raised.
Input Parameters:
subpictureHandle KcsElementHandle Handle to subpicture element
name String New name for subpicture
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_NameOccupied There is another subpicture on this level with the same name.
kcs_CantChangeFormViewName Form view name can't be changed.
```
subpicture_name_get(subpictureHandle)
```
The function gets name of existing subpicture.
Input Parameters:
subpictureHandle KcsElementHandle Handle to element.
Returned value:
[0] String Name of existing subpicture.
```
Exceptions:
```
kcs_ArgumentError Invalid parameters list.
kcs_HandleInvalid Specified handle is not valid.
kcs_DrawingNotCurrent No drawing was current.
kcs_NotFound There is no next sibling element.
kcs_Error General error.
```
Example:
```
# Example: kcs_ex_draft30.py
```
subpicture_save(subpHandle)
```
The function saves subpicture given by handle to standard subpicture databank. Subpicture name will be used for saving so it must be set first.
Input Parameters:
subpHandle ElementHandle Subpicture handle
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_HandleInvalid Given handle is not valid.
kcs_SubpictureNotValid Given subpicture is not valid.
kcs_NameInvalid Given subpicture has invalid name.
kcs_NameOccuppied Subpicture's name is already in use in standard subpicture databank
kcs_NameUsedInWorkspace There is another object in the workspace with the same name as given subpicture's name.
kcs_DrawingNotCurrent There is no current drawing.
kcs_GeneralError General error. Subpicture can not be saved.
```
subpicture_insert(subpName, <parentHandle>), <databank='SBD_PICT'>)
```
```
The function inserts a subpicture from the SBD_PICT (default) or SBD_STD databank under given parent given by handle. It is required to use the parent subpicture on the correctlevel. If the given subpicture is a view no parent must be given. Only subpictures with 001=102 are handled.
```
```
Note: The sample function SubpictureInsert defined in CommonSample.py module takes care of missing parent subpicture creation. It extends possibilities of subpicture_insertfunction allowing user to specify any subpicture handle as parent for inserting one. It will find the correct subpicture level and create missing subpictures if needed.
```
Input Parameters:
subpName string Subpicture name.
parentHandle ElementHandle Handle to parent subpicture. Should be specified only if subpicture stored in standard subpicture databank is a subview or component.
Databank integer Valid types:
 kcsSBD_PICT
 kcsSBD_STD
Returned value:
[0] ElementHandle Handle to inserted subpicture.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_HandleInvalid Given handle is not valid.
kcs_SubpictureNotValid Given subpicture is not valid.
kcs_NameInvalid Given subpicture has invalid name.
kcs_NameOccuppied Subpicture's name is already in use in standard subpicture databank
kcs_NameUsedInWorkspace There is another object in the workspace with the same name as given subpicture's name.
kcs_DrawingNotCurrent There is no current drawing.
kcs_GeneralError General error. Subpicture can not be saved.
```
Example:
```
#Example:
kcs_ex_draft37.py
CommonSample.py
Copyright © 1993-2005 AVEVA AB
7.21 Visual Area Functions
User's Guide Vitesse
```
Chapter: Drafting
```
```
dwg_repaint()
```
The function repaints entire drawing.
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
```
dwg_zoom()
```
The function zooms the display to the specified rectangle.
Input Parameters:
rectangle KcsRectangle2D New display area
Returned value:
None
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
kcs_ArgumentError Invalid parameter type.
kcs_ValueError Specified rectangle is empty.
kcs_PythonMethodNotFound Python Rectangle2D class method not found.
```
zoom_extent_get()
```
```
The function returns currently displayed area of drawing. Note that if the drawing is empty this function can return empty rectangle. The IsEmpty() method of Rectagle2D class shouldbe use for test.
```
Input Parameters:
rectangle KcsRectangle2D Instance of Rectangle2D class.
Returned value:
rectangle KcsRectangle2D Displayed area of drawing
```
Exceptions:
```
kcs_DrawingNotCurrent No drawing was current.
kcs_ArgumentError Invalid parameter type.
kcs_Error General error.
kcs_PythonMethodNotFound Python Rectangle2D class method not found.
```
Example:
```
# Example: kcs_ex_draft35.py
Copyright © 1993-2005 AVEVA AB
7.22 Shading Functions
User's Guide Vitesse
```
Chapter: Drafting
```
```
shd_new(ViewHandle)
```
The function creates a shaded view given a handle to a view. If a shaded view already exists then an exception is set, as only one shaded view can exist at a time.
Input parameters:
ViewHandle The handle to the view to show in shaded mode.
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError
kcs_DrawingNotCurrent
kcs_HandleInvalid
kcs_Error
kcs_ShadedViewExists
```
shd_projection_set(TransformationMatrix)
```
The function sets the projection for a shaded view given a tranformation matrix. If no shaded view exists then an exception is set.
Input parameters:
TransformationMatrix KcsTransformation3D.Transformation3D The transformation matrix
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError
kcs_DrawingNotCurrent
kcs_Error
kcs_NoShadedViewExists
```
shd_autoscale()
```
The function auto scales a shaded view. If no shaded view exists then an exception is set.
Input parameters:
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError
kcs_DrawingNotCurrent
kcs_Error
kcs_NoShadedViewExists
```
shd_zoom_box(BoxMinPoint, BoxMaxPoint)
```
The function zooms a shaded view given the min and max points of a 3D box. If no shaded view exists then an exception is set.
Input parameters:
BoxMinPoint KcsPoint3D.Point3D
BoxMaxPoint KcsPoint3D.Point3D
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError
kcs_DrawingNotCurrent
kcs_Error
kcs_NoShadedViewExists
Copyright © 1993-2005 AVEVA AB
7.23 Common Sample
This module contains some useful Python functions used by Tribon samples. These functions can be used by users as well.
Functions in the CommonSample.py module are the following:
```
 ReportTribonError(module, output=0)
```
Displays tribon module error on selected output:
 0 - console and command window,
 1 - only console window,
 2 - only command window.
```
 SelectView(prompt)
```
```
Allows the user to select a view in current drawing. Returns tuple: (status, viewhandle) where status is equal to:
```
 1 - view selected
 0 - selection cancelled
```
 SelectSubview(prompt)
```
```
Allows the user to select a subview in current drawing. Returns tuple: (status, subviewhandle) where status is equal to:
```
 1 - subview selected or
 0 - selection cancelled
```
 SelectComponent(prompt)
```
```
Allows the user to select a component in current drawing. Returns tuple: (status, comphandle) where status is equal to:
```
 1 - component selected or
 0 - selection cancelled
```
 SelectSubpicture(prompt, level=3)
```
Select subpicture function. It displays "user choice" dialog box to select subpicture type and then allows the user to select chosen subpicture type in current drawing.
Level specifies what kind of subpicture is allowed:
 1 - view
 2 - view and subview
 3 - view, subview and component
```
Function returns tuple: (status, subpicture handle) where status can be:
```
 0 - subpicture not selected
 1 - view selected
 2 - subview selected
 3 - component selected
```
 SelectGeometry(prompt)
```
```
This function is used for interactive selection of geometry. It returns tuple: (status, geometry handle) where status can be:
```
 0 - geometry not selected,
 1 - geometry selected.
```
 SubpictureInsert(name, parenthandle=None)
```
This function is an extension of vitesse subpicture_insert function from kcs_draft module. Since kcs_draft.subpicture_insert requires parent subpicture to be on correct level theCommonSample.SubpictureInsert function will find/create correct subpicture based on given handle. If no handle is given function will create new subpictures path.
```
Tip: Let's suppose that the subpicture given by name is a component and parenthandle points to any view. The function will then create the missing subview and it will be usedas parent for inserted component.
```
The function returns:
 1 - if subpicture was inserted successfully or,
 0 - otherwise.
```
 Point2DLockReq(prompt, point, status, buttons)
```
This function is an extension of the Vitesse point2d_req function from kcs_ui. It has the same input and results as point2d_req. Its main purpose is handling locking buttons. It drawshelp lines and modifies result point corresponding to selected locking direction.
User's Guide Vitesse
```
Chapter: Drafting
```
Copyright © 1993-2005 AVEVA AB
8 Equipment
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
8.1 General
The functions are made available in the Python program by the insertion of the import kcs_equip statement. The functions are then referred to as kcs_equip.<function name>.
Before using a new function, please carefully read the function description.
Vitesse for Equipment contains functions for creating, manipulation and deleting equipment items. Every function in the interface is documented and some examples have been includedto show how the functions can be used.
User's Guide Vitesse
```
Chapter: Equipment
```
Copyright © 1993-2005 AVEVA AB
8.2 Exception Handling
The Vitesse Equipment interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct ofthe Python language. The type of error can then be examined by checking the value of kcs_equip.error. The exception is also displayed in the Vitesse Log window which is available
by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Equipment
```
Copyright © 1993-2005 AVEVA AB
8.3 Functions
Below are the Equipment Vitesse functions described.
User's Guide Vitesse
```
Chapter: Equipment
```
```
equip_exist(name)
```
The function checks if the specified equipment exists or not.
Input Parameters:
```
name string Name of equipment in presentation format (not including project and delimiter)
```
Returned value:
[0] Integer 0 = Equipment does not exist
1 = Equipment exists
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_ArgumentError Incorrect arguments given
```
equip_new(module, name)
```
The function creates a new equipment item.
Input Parameters:
module string Name of module
```
name string Name of equipment in presentation format (not including project and delimiter)
```
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_ArgumentError Incorrect arguments given
kcs_ModuleNotFound Given module does not exist
kcs_NameInvalid Given name is invalid
kcs_ItemAlreadyExists Equipment item with given name already exists
```
equip_activate(name)
```
The function activates an existing equipment item and makes it current.
Input Parameters:
```
name string Name of equipment in presentation format (not including project and delimiter)
```
Returned value:
None
```
Exceptions:
```
kcs_ModelNotFound Equipment Item not found
kcs_ModelIsCurrent An equipment item is already current
kcs_ModelLocked Equipment item is locked by another user
kcs_InternalError Internal error has occurred, check log file
kcs_ArgumentError Incorrect arguments given
```
equip_delete(name)
```
The function deletes an equipment item from the databank. No equipment shall be current. Connections are automatically removed.
Input Parameters:
```
name string Name of equipment in presentation format (not including project and delimiter)
```
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_ArgumentError Incorrect arguments given
kcs_ModelIsCurrent Equipment item is current
kcs_ModelNotFound Equipment Item not found
kcs_ObjectLocked Equipment object is locked
kcs_ConnectedToPipeOrVent Equipment is connected to pipe / ventilation
```
equip_cancel()
```
Cancel modifications on current equipment item.
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
```
equip_save()
```
The function saves the current equipment item.
Input Parameters:
None
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_NameInvalid Equipment name is invalid
kcs_ModuleUpdateError Module object cannot be updated
```
equip_module_get()
```
Returns the module of current equipment item.
Input Parameters:
None
Returned value:
[0] string Name of module
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
```
equip_name_get()
```
```
Returns the name of current equipment in presentation format (without project and delimiter)
```
Input Parameters:
None
Returned value:
[0] string Name of equipment
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
```
equip_component_set(compname)
```
The function sets the component reference for the current equipment item.
Input Parameters:
compname string Name of component
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
kcs_ComponentNotFound Given component does not exist
```
equip_description_set(description)
```
The function sets the description for the current equipment item.
Input Parameters:
description string Description of equipment
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
```
equip_room_set(room)
```
The function sets the room for the current equipment item.
Input Parameters:
room string Room of equipment
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
```
equip_alias_set(alias)
```
The function sets the alias name for the current equipment item.
Input Parameters:
alias string Alias name of equipment
Returned value:
None
Exceptions
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
```
equip_place(point, uvector, vvector)
```
The function places the current equipment item in the 3D model
Input Parameters:
point kcsPoint3D Point for placement
uvector kcsVector3D U vector for orientation
vvector
kcsVector3D V vector for orientation
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
kcs_VectorsNotOrthogonal U and V Vectors are not orthogonal
kcs_AlreadyPlaced Equipment item is already placed
kcs_ConnectedToPipeOrVent Equipment is connected to pipe / ventilation
```
equip_transform(transformation)
```
The function transforms an equipment item in the 3D model. It is not allowed to use a transformation that incorporates any other operations than translations and rotations.
Input Parameters:
transformation kcsTransformation3D Transformation that should be applied to the equipment item.
Returned value:
None
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_ArgumentError Incorrect arguments given
kcs_ NotPlaced Equipment item is not placed
kcs_TransformationInvalid Transformation is not valid
kcs_ConnectedToPipeOrVent Equipment is connected to pipe / ventilation
```
equip_ready()
```
The function makes an equipment item ready. The checks and actions performed during ready operation are the same as for the interactive function.
Input Parameters:
None.
Returned value:
[0] integer Result code:
0 = OK, equipment has been made ready
Other codes = Equipment could not be made ready because:
1 = Room not given
2 = Subproject not given
3 = Planning unit not given
4 = Description not given
5 = Not placed
```
Exceptions:
```
kcs_InternalError Internal error has occurred, check log file
kcs_NoModelIsCurrent No model is current
kcs_EquipDefaultFileError Equipment default file could not be found or has invalid format
kcs_EquipPDITransferFailed Equipment is ready and stored OK, but PDI transfer failed
```
document_reference_get ()
```
The function returns a list of document references associated with the active equipment.
Input parameters
None
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentErrorI Invalid arguments list
kcs_NoModelCurrent Active equipment not set
kcs_GeneralError List of result can't be created for some internal reason
```
document_reference_add (docRef)
```
The function adds a document reference to the active equipment object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active equipment not set
```
document_reference_remove (docRef)
```
The function removes document reference from active equipment object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exeptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active equipment not set
kcs_DoesNotExist Equipment document reference doesn't exist
```
Example:
```
```
# Example: kcs_ex_equip01.py (New)
```
```
# Example: kcs_ex_equip02.py (Update)
```
```
# Example: kcs_ex_equip03.py (Delete)
```
```
# Example: kcs_ex_equip04.py (Place, Transform, Ready)
```
Copyright © 1993-2005 AVEVA AB
9 Hull
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
9.1 General
Vitesse functions in hull can be use to create planar as well as curved model objects. The functions are divided into two modules one for planar hull and one for curved hull: kcs_hullpanand kcs_chm.
The basic feature of these Vitesse interfaces is that objects/components may be created from an input file. In the planar case the input file is the plane panel scheme and in the curvedcase the input file is the XML based description file which may be used to generate objects by the Batch Curved Hull program. In this way all types of plane panels/components and all
types of curved model objects can be created via the Vitesse Hull interfaces.
The input languages of the planar and curved input file will not be explained here, please refer to Tribon M3 Hull \ Planar Modelling \ Design Language of Tribon Hull Modelling and TribonM3 Hull \ Curved Modelling \ User's Guide Batch \ Input Language of Curved Hull Modelling.
Although the basic feature is to generate object/components via an input file, the Vitesse interfaces also have functions for "direct" modification. In the planar module you will also findpowerful methods to copy/move/split panels, split stiffeners and remove seams.
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.2 Exception Handling
```
The Vitesse Hull interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_hullpan.error (planar modelling) or kcs_chm.error (curved modelling). The exception is
```
also displayed in the Vitesse Log window which is available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be foundin the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set.
```
Note: The kcs_Error exception is a general exception and will not be further described below.
```
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.3 Planar Modelling Functions
Vitesse features access to the modelling functionality in planar hull modelling. This means that all kinds of planar panels can be created. For more information on Planar Hull Modelling,see Tribon M3 Hull Planar Modelling.
The module has the following features:
 function to initiate a new panel.
 function to activate existing panels.
 function to add/modify components to a panel by the full power of the plane panel input scheme syntax.
 functions to change existing components: delete components, split stiffeners and remove a seam
 function to copy, move and split one or several panels.
 functions to recreate, store and terminate panels.
The functions are made available in the Python program by the insertion of the statement import kcs_hullpan. The functions are then referred to as kcs_hullpan.<function name>. Beforeusing a new function, please carefully read the function description.
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.3.1 Hull Default Functions
User's Guide Vitesse
```
Chapter: Hull
```
```
default_value_set(statement)
```
These functions are used to set and get the default values valid in planar-, curved modelling and basic design.
Input Parameters:
Statement String Statement string in format KEYWORD=VALUE.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_DefKeywordInvalid Invalid default keyword.
kcs_DefValueInvalid Invalid default value.
```
default_value_get(statement)
```
The function gets given default value.
Input Parameters:
Statement String The default keyword.
Returned value:
[0] String The default statement.
```
Exceptions:
```
kcs_DefKeywordInvalid Invalid default keyword.
kcs_ArgumentError Invalid argument format.
Copyright © 1993-2005 AVEVA AB
9.3.2 Activate/Store/Skip/Delete/Recreate
User's Guide Vitesse
```
Chapter: Hull
```
```
pan_activate(ListOfPanels)
```
Activate a number of panels
Input Parameters:
ListOfPanels list of strings The names of the panels to be activated.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_ModelNotFound The panel was not found.
kcs_ModelLocked The panel was locked by another user.
```
pan_skip(ListOfPanels)
```
Skip the panels indicated by "ListOfPanels". Each panel in "ListOfPanels" must one of the currently activated panels. An empty list means all currently activated panels.
Input Parameters:
ListOfPanels list of strings The names of the panels to be skipped.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_ModelNotFound The panel is not active or does not exist
```
pan_store(ListOfPanels)
```
Store the panels indicated by "ListOfPanels". Each panel in "ListOfPanels" must one of the currently activated panels, otherwise it will be ignored. An empty list means all currentlyactivated panels.
Input Parameters:
ListOfPanels list of strings The names of the panels to be stored.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_ModelNotFound The panel is not active or does not exist
```
pan_delete(ListOfPanels)
```
Delete the panels indicated by "ListOfPanels". Each panel in "ListOfPanels" must one of the currently activated panels. An empty list means all currently activated panels.
Input Parameters:
ListOfPanels list of strings The names of the panels to be stored.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_NoModelIsCurrent The panel is not active or does not exist
```
pan_list_active( )
```
Get a list of all currently activated panels
Input Parameters:
none
Returned value:
[0]PanelNames list of strings The names of the panels that are currently activated.
```
Exceptions:
```
none
```
pan_recreate(<ListOfPanels>)
```
Recreate panels from list in topological order. The panels must be activated. If no parameter is given then all activated panels will be recreated..
Input Parameters:
ListOfPanels list of strings Optional list of names of the panels to be recreated.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_NoModelIsCurrent Panel is not active
Copyright © 1993-2005 AVEVA AB
9.3.3 Scheme Handling
```
The exceptions kcs_InterpretationError and kcs_GenerationError are special scheme generation exceptions that can be raised by some of the functions described below. For theseexceptions additional information can be fetched by the functions kcs_hullpan.nerr (nerr()), kcs_hullpan.err_code (err_code(error_ind)) and kcs_hullpan.err_mess (err_mess
```
```
(error_ind)) described below.
```
User's Guide Vitesse
```
Chapter: Hull
```
```
pan_init(scheme,ident)
```
Initialize a new panel. This function also starts a new scheme with the given name and adds an 'ident' statement first in the scheme. The directory path need not be given. It is thenfetched from the global variable SB_SHIPSCH. If another scheme is already active a control question appears.
Input Parameters:
scheme string name of scheme.
ident string the ident statement in the schema
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_InterpretationError Hull Planar Scheme interpretation error
kcs_GenerationError Hull Planar Scheme generation error
kcs_Error Other error
```
pan_modify(panel,mode)
```
Activate an existing panel. As for kcs_hullpan.pan_init the belonging scheme is also activated.
Input Parameters:
panel string giving the name of the panel
mode integer 1: create new
2: update existing
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_InterpretationError Hull Planar Scheme interpretation error
kcs_GenerationError Hull Planar Scheme generation error
kcs_Error Other error
```
stmt_exec(group,statement)
```
Add the statement given as input to current scheme and run it. The components are generated into the current panels.
Input Parameters:
group integer number of the group to replace. For addition the group number should be set to zero.
statement string containing the statement to be executed.
Should be in standard Tribon Hull Plane Modelling format.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_InterpretationError Hull Planar Scheme interpretation error
kcs_GenerationError Hull Planar Scheme generation error
kcs_Error Other error
```
stmt_exec_single(group,statement,panel)
```
Add the statement given as input to the scheme of the given panel and run it. The components are generated into the given panel.
Input Parameters:
```
group integer (as stmt_exec)
```
```
statement string (as stmt_exec)
```
panel string the name of the panel
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_InterpretationError Hull Planar Scheme interpretation error
kcs_GenerationError Hull Planar Scheme generation error
kcs_Error Other error
```
group_get(panel,part_id)
```
Get the group number for a given component within a panel.
Input Parameters:
panel string the name of the panel
part_id integer the component identity to get the group number for
Returned value:
group integer the group number
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_ModelNotFound Panel or group not found
kcs_Error Other error
```
group_next(panel,act,group)
```
Get the number of the group according to input. Either the first group number can be returned. In this case the input parameter group has no meaning. Or the group following the givenone can be returned. The last option is to check the validity of an existing group number. If it is valid the same group number is returned. In case of failure, an exception is raised just as
for the other functions.
Input Parameters:
panel string the name of the panel
act integer -2: get first group
0: get this group
1: get next group
group integer the component identity to get the group number for
Returned value:
group integer the resulting group number
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_ModelNotFound Panel or group not found
kcs_Error Other error
```
stmt_get(panel,group)
```
Get the statement text for a given group within a panel. The statement text can be changed and used in the "kcs_hullpan.stmt_exec" function to change a group of components.
Input Parameters:
panel string the name of the panel containing the group
group integer the number of the group to get the statement text for
Returned value:
statement string the statement text
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters
kcs_SystemError Tribon system error
kcs_ModelNotFound Panel of group not found
kcs-Error Other error
```
pan_scheme_runmode_get( )
```
Get the current run mode options. These are the same options as you can view/change with the interactive function "Planar\Scheme\Run Mode" of planar hull modelling.
Input Parameters:
none
Returned value:
RunModeOptions Instance of KcsRunModeOptions The current run mode options.
```
pan_scheme_runmode_set(RunModeOptions)
```
Set the current run mode options. These are the same options as you can view/change with the interactive function "Planar\Scheme\Run Mode" of planar hull modelling. You maymodify current settings for "Confirm Generation" and "Trace On".
Input Parameters:
RunModeOptions Instance of KcsRunModeOptions The current run mode options.
Returned value:
none
```
nerr()
```
Number of interpretation and generation errors when the exceptions kcs_InterpretationError or kcs_GenerationError was raised. If kcs_SystemError was raised 1 is returned.
Input Parameters:
none
Returned value:
nerr interger number of errors
```
Exceptions:
```
none
```
err_code(error_ind)
```
Get the error code after any of the exceptions kcs_InterpretationError, kcs_GenerationError or kcs_SystemError.
Input Parameters:
```
error_code interger index number between 1 and nerr(). For kcs_SystemError set error_ind to zero.
```
Returned value:
error_code interger the error code
```
Exceptions:
```
kcs_ArgumentError incorrect number of, or type of, parameters or value out of bounds.
```
err_mess(error_ind)
```
Get the error message after any of the exceptions kcs_InterpretationError, kcs_GenerationError or kcs_SystemError.
Input Parameters:
```
error_ind interger index number between 1 and nerr(). For kcs_SystemError set error_ind to zero.
```
Returned value:
error_mess string the error message
```
Exceptions:
```
kcs_ArgumentError Incorrect number of, or type of, parameters or value out of bounds.
```
editor(panel)
```
Invoke the editor with a scheme for the given panel. Can be used after the exceptions kcs_InterpretationError or kcs_GenerationError to show the erroneous statement in its context.
Input Parameters:
panel string the name of the panel
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Incorrect number of , or type of, parameters.
Copyright © 1993-2005 AVEVA AB
KcsPanelSchema Class
The KcsPanelSchema python can help you to modify the schema of a panel. You initiate this class by giving the name of the panel for which you want to do scheme updates. There aretwo methods SetValue and GetValue that will get/set the value of a specific keyword in a specific statement
User's Guide Vitesse
```
Chapter: Hull
```
```
Example:
```
KcsPanelSchema
import KcsPanelSchema
import kcs_ui
```
panelName = 'JUMBO-GIR11700'
```
```
sch = KcsPanelSchema.PanelSchema( panelName )
```
```
group = 8
```
```
val = sch.GetValue(group, 'SID')
```
```
es = sch.SetValue(group, 'SID', 'OS')
```
```
val = sch.GetValue(group, 'SID')
```
Copyright © 1993-2005 AVEVA AB
Panel Scheme Syntax Dictionaries
In the hullpan module there are also two variables kcsSCHEME_STATEMENTS and kcsSCHEME_KEYWORD_TYPES. They are both "dictionaries" and may be used to find statementsand keywords that are available in the design language of planar hull.
```
The kcsSCHEME_STATEMENTS dictionary contains list of statements used in planar hull application. Each dictionary item consists of pair {Statement: Keywords} , where Statement is astring with statement name and Keywords is a dictionary containing allowed keywords for given statement. Each Keywords dictionary item consist of pair{ Keyword: Properties }, where
```
```
Keyword string with keyword name and Properties is a dictionary containing statement properties. The properties dictionary contains the following entries: { 'TYPE': TypeValue } whereTypeValue is an index of kcsSCHEME_KEYWORD_TYPES dictionary.
```
```
The kcsSCHEME_KEYWORD_TYPES dictionary contains description of schema keyword types. The dictionary consist of pairs {TypeValue: TypeDescription}, where TypeValue is aninteger number, and TypeDescription is a string describing given type. The following type codes exist:
```
User's Guide Vitesse
```
Chapter: Hull
```
0 Standalone keyword
1 Integer
2 Real
102 Coordinate value: real, FR- or LP-term, reference to topological point
202 Real or topological point direction
3 Orientational string: FOR, AFT, TOP, BOT, PS, SB, 1, -1
4 Integer, real or string. The keyword is basically a integer or real value but may also be expressed with a string description: QUA=A32, LEN=H-20, CUT=ABC
```
5 Number, string or description name. (A description name is always surrounded by single quotes)
```
8 Description name
9 Reference to topological point
Copyright © 1993-2005 AVEVA AB
9.3.4 Copy/Move/Split/Topology
These are functions that operates on the panel object level. You can copy or move whole panels, split panels and get topology information about the panel.
User's Guide Vitesse
```
Chapter: Hull
```
```
pan_copy(ListOfPanels, CopyPanOptions)
```
Copy some of the currently activated panels. The new panels will also be activated.
Input Parameters:
```
ListOfPanels string or list or strings List of panels to copy. It can be a single panel name or a list of names. Every panel in the list must be among the activates onesotherwise an exception is return (kcs_NoModelIsCurrent).
```
CopyPanOptions Instance ofKcsCopyPanOptionsDetailed information about the copy operation
Returned value:
[None
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_NoModelIsCurrent One or more of the selected panels are not activated.
```
pan_move(ListOfPanels, MovePanOptions)
```
Move all currently selected panels
Input Parameters:
```
ListOfPanels string or list or strings List of panels to copy. It can be a single panel name or a list of names. Every panel in the list must be among the activates onesotherwise an exception is return (kcs_NoModelIsCurrent).
```
MovePanOptions KcsMovePanO ptions. Instance of KcsMovePanOptions. Detailed information about the move operation.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_NoModelIsCurrent One or more of the selected panels are not activated.
```
pan_split(ListOfPanels, SplitPanOptions)
```
Split all the currently activated panels.
Input Parameters:
```
ListOfPanels string or list or strings List of panels to copy. It can be a single panel name or a list of names. Every panel in the list must be among the activates onesotherwise an exception is return (kcs_NoModelIsCurrent).
```
SplitPanOptions Instance ofKcsSplitPanOptionsThis object contains all the detailed information for the split operation.
Returned value:
none
```
Exceptions:
```
kcs_Error General error.
```
pan_topology(Model, Act)
```
Calculate the dependencies to/from a given model object.
Input Parameters:
Model Instance of KCSModel The model object The "Root" object.
Act string Activity indicating how to calculate the dependencies:
"Dependent primary" - List all objects that depends on "Model". Only search one level.
"Dependent all" - List all objects that depends on "Model". Search all levels.
```
"Defining" - List all object that defines "Model" (i.e. a list of all objects that "Model" depends on)
```
Returned value:
[0]TopoList List of instances ofKcsModelThe list of all model objects that depend on or defines "Model".
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
kcs_Error Topology calculation failed.
Copyright © 1993-2005 AVEVA AB
9.3.5 Modify Components
This group is a number of functions that modify components in a panel. The vitesse function modifies the model components "directly", i.e. NOT via the input scheme. The functionality issimilar to that of the corresponding interactive function of planar hull modelling.
User's Guide Vitesse
```
Chapter: Hull
```
```
pan_remove_seam(panel_name, component)
```
Remove a seam from a panel. This function corresponds to the function "Remove seam" of the interactive planar hull modelling. It removes the seam an "glues" all components that aresplit by the seam.
Input Parameters:
panel_name The name of the panel
component The seam component number
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters, e.g. the group number does not exist.
kcs_NoModelIsCurrent The panel is not activated.
```
pan_group_delete(panel_name,group)
```
Delete a group of components from a panel.
Input Parameters:
panel_name The name of the panel
group The group number
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters, e.g. the group number does not exist.
kcs_NoModelIsCurrent The panel is not activated.
```
pan_group_divide(panel_name, group, ListOfModels)
```
Move some components from a group into a new group.
Input Parameters:
Group integer The group to be divided.
ListOfModels List of instances ofKcsModelThe components to be moved from "group" to a new group.
Returned value:
new_group integer The number of the new group.
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters, e.g. the group number does not exist.
kcs_NoModelIsCurrent The panel is not activated.
```
pan_sti_split_by_model(group, component_id)
```
Split a group of stiffeners where they intersect another model, i.e. a hole, a stiffener or a seam in the current panel. This function operates on all active panels.
Input Parameters:
group integer The group to be split.
component_id integer Selected the "splitting" component. The function will be split the group of stiffeners where this component intersect the stiffeners. Thecomponent may be a stiffener, a seam, a hole, a flange or a bracket.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters.
```
pan_sti_split_by_plane(group, plane)
```
Split a group of stiffeners where they intersect a plane. This function operates on all active panels.
Input Parameters:
Group integer The group to be divided.
Plane string The group will be divided where this plane intersects the stiffeners. Plane is a string describing a principal plane. It can be a string like"X=FR50+200", "Y=8000" or Z="LP23-100".
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters.
kcs_Error The split failed: no intersection or other error.
Example
# Example: kcs_ex_hullpan03.py
```
component_id_translate (act, component_id)
```
Translate id between panel component number and picture element id.
Input Parameters:
Act integer 0 - translate panel to picture id
1 - translate picture to panel id
component_id integer Id to translate
Returned value:
Integer - Translated Id
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters
Copyright © 1993-2005 AVEVA AB
9.3.6 View Handling
User's Guide Vitesse
```
Chapter: Hull
```
```
view_detail_new(act, component_handle)
```
When a handle to a component is given, and create a detail view.
Input Parameters:
act integer Selects the type of component:
2 - Flange
3 - Stiffener
4 - Bracket
5 - Seam
component_handle KcsElementHandle Handle to the component in the drawing. The component handle must be in a symbolic view.
Returned value:
ViewHandle Handle to the new view
```
Exceptions:
```
kcs_ArgumentError Invalid input parameters.
kcs_DrawingNotCurrent There is no current drawing.
kcs_ValueError comnponent_handle is invalid
```
view_symbolic_modify(ViewHandle, SymbolicViewOptions)
```
```
This function will get all view options from an existing symbolic view and deliver them in a KcsInterpretationObject (Python object).
```
Input Parameters:
ViewHandle ElementHandle Handle to the view.
Returned value:
SymbolicViewOptions KcsInterpretationObject Instance of the "KcsInterpretationObject" object. The object will be filled with all the view options that were set when the view wascreated.
```
Exceptions:
```
kcs_InvalidView The given view is not a symbolic view or view data is missing.
```
view_symbolic_recreate(ViewHandle)
```
Recreate a symbolic view.
Input Parameters:
ViewHandle ElementHandle Handle to the view.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError The given view is not a symbolic view or view data is missing.
kcs_DrawingNotCurrent The is no current drawing
Examples
```
# Example: kcs_ex_hullpan04.py (view_detail_new)
```
Copyright © 1993-2005 AVEVA AB
9.3.7 Curve Functions
This chapter describes function to identify an existing contour in the current drawing and create a curve statement to add to the current panel
User's Guide Vitesse
```
Chapter: Hull
```
```
pan_curve_create( )
```
The function returns a curve statement to add in the current panel.
Input Parameters:
plane code integer The code of the plane.
view handle handle The handle of the current view
curve name string The name of created curve
panel name string The name of the current panel
contour contour2D The contour object
Returned value:
[0] integer Result code
[1] string Curve statement
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
```
pan_curve_store( )
```
The function makes curve object out of the contour and saves it on the TRIBON databank.
Input Parameters:
dwg handle handle The handle of the current drawing.
view handle handle The handle of the current view.
curve name string The name of created curve.
cont handle handle The handle of the contour.
contour contour2D The contour object.
Returned value:
[0] integer Result code
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error.
Examples
# Example: kcs_ex_hullcurve1.py
# Example: kcs_ex_hullcurve2.py
Copyright © 1993-2005 AVEVA AB
9.3.8 Document Reference Handling
User's Guide Vitesse
```
Chapter: Hull
```
```
document_reference_get () =>document_reference_get (PanelName)
```
The function returns a list of document references associated with the panel.
Input parameters
PanelName Name of the panel to get references for
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Panel not found
kcs_GeneralError List of result can't be created for some internal reason
```
document_reference_add (docRef) =>document_reference_add (docRef, PanelName)
```
The function adds a document reference to the panel object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
PanelName Name of the panel to add reference for
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Panel not found
```
document_reference_remove (docRef) =>document_reference_remove (docRef, PanelName)
```
The function removes document reference from panel object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
PanelName Name of the panel to remove reference for
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_ModelNotFound Panel not found
kcs_DoesNotExist Equipment document reference doesn't exist
Copyright © 1993-2005 AVEVA AB
9.3.9 Examples
```
Example on using the plane panel modelling interface. All error handling has been left out to keep the example small. A slash (\) at the end of lines mean that the statement continues onthe next line.
```
1. Get the position of the sideweb
2. Indicate the upper deck
3. Initiate a new panel. A scheme is created and the editor started.
4. Create a panel statement containing a name generated (automatically) elsewhere and the given position.
5. Add the panel statement to the scheme and execute it.
6. Create a topological point statement to be used to define the boundary.
7. Create the boundary statement from a hullcurve derived from the position, the two indicated decks and the topological points.
8. Store the panel.
9. Terminate the scheme.
The rest of the components such as seams, plates, notches, brackets, flanges and/or stiffeners are added in the same way as the topological points and the boundary. The topologicalpoint is very useful in Vitesse program in order to reuse input that is combined into new geometry by referring the surrounding model items.
User's Guide Vitesse
```
Chapter: Hull
```
```
Example:
```
import kcs_ui
import kcs_hullpan
```
position = kcs_ui.req_int('Side web position') 1
```
```
upper_deck = kcs_ui.req_pick_mod('Indicate upper deck') 2
```
```
lower_deck = kcs_ui.req_pick_mod('Indicate lower deck')
```
```
kcs_hullpan.pan_init( panel_name, ident) 3
```
```
stmt = "PAN, '" + panel_name + "', SBP, DT=123, X=FR"+\
```
```
str(position[1]) + ";" 4
```
```
kcs_hullpan.stmt_exec( 0, stmt) 5
```
```
stmt = "POI, NO=1, INT, " + upper_deck[2] + "',\
```
```
SID=BOT, M1=-" + str(depth) + "/ '" + hcx +\
```
```
str(position[1]) + "';" 6
```
```
kcs_hullpan.stmt_exec( 0, stmt)
```
```
stmt = "POI, NO=2, INT, " + lower_deck[2] + "', SID=TOP,
```
```
M1=-" + str(depth) + "/ '" + hcx + str(position[1]) + ';"
```
```
kcs_hullpan.stmt_exec( 0, stmt)
```
```
stmt = "BOU, '" + hcx + str(position[1]) + "'/ '"+\
```
```
upper_deck[2] + "'/ XYZ=P1, XTY=P2/ '" +lower_deck[2]\+"';" 7
```
```
kcs_hullpan.stmt_exec( 0, stmt)
```
```
kcs_hullpan.pan_store() 8
```
```
kcs_hullpan.pan_skip() 9
```
Copyright © 1993-2005 AVEVA AB
9.4 Curved Modelling Functions
These functions deals with generation of curved hull model objects. The functions are made available in a Vitesse program by the insertion of the statement import kcs_chm.The
functions are then referred to as kcs_chm.<function name>. Before using a new function, please carefully read the function description.
The kcs_chm module has the following features:
 Create curved model objects from an XML description file.
 Create various kinds of curved hull modelling views: shell expansion, body plan, curved panel and shell profile view
 Store, delete, skip and recreate model objects.
 Split and combine shell profiles.
 Dimensioning of curved models.
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.4.1 Generate Hull Objects from XML file
You can model all curved hull objects via Vitesse by creating a input file in XML format and then run this file. The input language of the input file is identical to that of "Batch Curved Hull".This input language is thoroughly described in Tribon M3 Hull \ Curved Modelling \ User's Guide Batch \ Input Language of Curved Hull Modelling. It will not be further explained here.
```
The XML input file may be created by using methods in PyXML. PyXML is an extension to Python that handle XML document. One features of PyXML is that it implements the DOMinterface and standard interface (defined by W3C) to handle the tree structure of an XML. You may create a new document, add element and attributes. PyXML and DOM will not be
```
documented here.
For PyXML, please refer to the Python web site
www.pythonlabs.com
You will find documentation on DOM on the web site of the World Wide Web Consortium,
www.w3c.org
PyXML will be delivered together with Tribon Vitesse, version M3 or later. You will also find an example of how to use PyXML/DOM, kcs_ex_hull_XML.py
User's Guide Vitesse
```
Chapter: Hull
```
```
run_XML(XmlFileName, LogFileName)
```
Generates a number of curved hull object described in the XML document. The objects described in the XML file will be created and also stored in the data bank.
Input Parameters:
XmlFileName string The full path name of the XML input file.
LogFileName string The full path name of a log file, where you will find detailed information about the XML generation. If empty string, log messages will appear inthe standard output log file of curved hull modelling application.
Returned value:
[0]SuccessList List of KcsModelobjectsA list of all successfully created curved model objects. Each KcsModel object contains type and name.
```
Exceptions:
```
kcs_ArgumentError Invalid input parameter.
kcs_Error XML generation failed, see log file.
```
output_XML(ModelList, OutputFileName)
```
Get the XML description of existing curved hull model objects.
Input Parameters:
ModelList List of KcsModelobjectsSelects the objects for which an XML description will be created. Each object in the list is an instance of KcsModel. Type and name must begiven.
OutputFileName string The XML output file. Full path name of the file. An existing file will be overridden a non-existing file will be created.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input parameter.
kcs_ObjNotFound Object not found
Example
# Example: kcs_ex_hull_XML.py
Copyright © 1993-2005 AVEVA AB
9.4.2 View Handling
User's Guide Vitesse
```
Chapter: Hull
```
```
view_shellexp_new(ViewOptions)
```
Create a shell expansion view.
Input Parameters:
ViewOptions Instance of KcsShellExpView. An object with all the options to set up a shell expansion view
Returned value:
[0]ViewHandleElementHandle Handle to the new shell expansion view.
```
Exceptions:
```
kcs_Error Failed to create the view.
kcs_DrawingNotCurrent There is no current drawing.
```
view_bodyplan_new(ViewOptions)
```
Create a body plan view
Input Parameters:
ViewOptions Instance of KcsBodyPlanView. An object with all the options to set up a bodyplan view
Returned value:
[0]ViewHandleElementHandle Handle to the new view.
```
Exceptions:
```
kcs_Error Failed to create the view.
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
```
view_curvedpanel_new(Panel, ViewOptions)
```
Create a curved panel view
Input Parameters:
Panel Model The curved panel to create the view for.
ViewOptions KcsInterpretationOb ject .CurvedPanelViewOptions for the view.
Returned value:
[0]ViewHandleElementHandle Handle to the new view.
```
Exceptions:
```
kcs_Error Failed to create the view.
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
```
kcs_NameOccupied A view of this panel exists in current drawing (same view name).
```
kcs_ObjectNotFound No view with expected name created.
kcs_SubpictureNotValid View created on wrong level.
```
view_shprof_new(Stiffener)
```
Create a shell profile view
Input Parameters:
Stiffener KcsModel Instance of KcsModel. Name of the profile to create a view for.
Returned value:
[0]ViewHandleElementHandle Handle to the new view.
```
Exceptions:
```
kcs_Error Failed to create the view.
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
```
view_devpla_new(Plate)
```
Create a shell profile view
Input Parameters:
Plate KcsModel Instance of KcsModel. Name of the shell plate to create a view for.
Returned value:
[0]ViewHandleElementHandle Handle to the new view.
```
Exceptions:
```
kcs_Error Failed to create the view.
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
```
view_modify(ViewHandle)
```
Get the view options data for a given view
Input Parameters:
ViewHandle ElementHandle Handle to the view.
Returned value:
ViewOptions Instance of any of the hull "view option" classes: KcsCurvedPanelView, KcsShellExpView, KcsBodyPlaneView orKcsInterpretationObject. The view option object will be filled with all the view options that was set when the view was created.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
kcs_HandleInvalid The view handle is invalid or view data is missing.
```
view_recreate(ViewHandle)
```
Recreate a given view.
Input Parameters:
ViewHandle ElementHandle Handle to view.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_DrawingNotCurrent There is no current drawing.
Examples
# Example: kcs_ex_hullcurved_views01.py
Copyright © 1993-2005 AVEVA AB
9.4.3 Other Modelling Functions
User's Guide Vitesse
```
Chapter: Hull
```
```
plate_prop_get(Obj)
```
To get properties of a shell plate.
Input Parameters:
Obj Instance of KcsModel. Type, name and part id must be given. This is the shell plate to get data for.
Returned value:
Properties Instance of KcsShPlateProp carrying the dta extracted.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_ObjectNotFound Obect not found.
kcs_Error There was a problem in extracting data from the object.
```
plate_prop_set(Obj, Prop)
```
Sets properties for a shell plate. This function will lock the shell plate. To unluck you must call either "kcs_chm.store" or "kcs_chm.skip".
Input Parameters:
Obj KcsModel Instance of KcsModel. Type, name and part id must be given. This is the shell plate to set data for.
Prop KcsShPlateProp Instance of KcsShPlateProp carrying the data to set.
Returned value:
ResProp Instance of KcsShPlateProp carrying the updated plate data.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_ObjectNotFound Object not found.
kcs_ObjectLocked Object locked.
kcs_AccessDenied Access denied.
kcs_Error There was a problem in setting data in the object.
```
stiffener_split(ObjToSplit, SplittingObj)
```
Split a shell profile or a shell stiffener at a given position. This function will lock the whole shell profile. To unlock you must either call "kcs_chm.store" or "kcs_chm.skip".
Input Parameters:
ObjToSplit Instance of KcsModel. Type and name must be given. This is the shell profile or the shell stiffener to split
SplittingObj Instance of KcsModel or KcsPlane3D. This object gives the position for the split.
Returned value:
none
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_Error The split failed: Objects do not exist, no intersection or other error.
```
stiffener_combine(Stiff1, Stiff2)
```
Combines two shell stiffeners into one. This function will lock the whole shell profile. To unlock you must call either "kcs_chm.store" or "kcs_chm.skip".
Input Parameters:
Stiff1 KcsModel Instance of KcsModel. Stiff1 will be combine with Stiff2.
Stiff2 KcsModel Instance of KcsModel
Returned value:
ResultStiff Instance of KcsModel. If the combine operation succeeded this is the resulting stiffener.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_Error The combine failed: Objects do not exist, the stiffeners are not neighbouring stiffeners or other error.
```
stiffener_prop_get(Obj)
```
To get properties of a shell stiffener.
Input Parameters:
Obj Instance of KcsModel. Type, name and part id must be given. This is the shell stiffener to get data for.
Returned value:
Properties Instance of KcsShStiffProp carrying the data extracted.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_ObjectNotFound Object not found.
kcs_Error There was a problem in extracting data from the object.
```
stiffener_prop_set(Obj, Prop)
```
Sets properties for a shell stiffener. This function will lock the shell stiffener. To unlock you must call either "kcs_chm.store" or kcs_chm.skip".
Input Parameters:
Obj KcsModel Instance of KcsModel. Type, name and part id must be given. This is the shell stiffener to set data for.
Prop KcsShStiffProp Instance of KcsShStiffProp carrying the data to set.
Returned value:
ResProp Instance of KcsShStiffProp carrying the updated stiffener data.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_ObjectNotFound Object not found.
kcs_ObjectLocked Object locked.
kcs_AccessDenied Access denied.
kcs_Error There was a problem in setting data in the object.
```
curve_principal_create(CurveName, Plane, MinPt, MaxPt, SurfName)
```
Creates a shell curve or a shell seam. The curve/seam is the intersection between a surface and a principal plane. The resulting curve will created and locked on the data bank. Useeither "kcs_chm.store" or "kcs_chm.skip" to unlock the curve.
Input Parameters:
CurveName string The name of the curve/seam. If the name is a valid seam name a seam object is created otherwise a hull curve is created.
Plane string A string describing the principal plane, e.g "X=FR50+200", "Y=LP10", "Z=LP25-100".
MinPt KcsPoint3D MinPt and MaxPt is the limit box for the curve/seam. MinPt holds the minimum values of the box.
MaxPt KcsPoint3D MaxPt holds the maximum values of the box limitbox.
SurfName string Optional parameter. The name of the surface the should be intersected. If SurfName is omitted, the default surface will be used
```
cpan_hole_create(PanelName, HoleOptions)
```
Creates a new hole in a curved panel object. The panel will be locked in the data bank. Use store kcs_chm.store" to store and unlock the panel or "kcs_chm.skip" to discard thechanges and unlock the panel.
Input Parameters:
PanelName string The name of the curved panel.
HoleOptions KCSPanHoleOptions This python object contains all the data that specifies the shape and position of the new hole. Please see this python file fordocumentation.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_Error Failed to create the hole.
Examples
# Example: kcs_ex_hull_shellstiff.py
# Example: kcs_ex_hull_shellcurves.py
# Example: kcs_ex_hull_cpanhole.py
# Example: kcs_ex_hull_sh_stiff_prop.py
Copyright © 1993-2005 AVEVA AB
9.4.4 Store/Skip/Delete/Recreate
User's Guide Vitesse
```
Chapter: Hull
```
```
store(Model)
```
Store a curved hull object. This store method works as the store in interactive curved hull. It is an "intelligent" store, i.e. it will update all related objects.If you choose to store a shellprofile for instance, this function will also store shell stiffeners and trace curves and update limit tables.
Input Parameters:
Model A KcsModel object.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input
kcs_Error Storing failed: Model objects does not exist, is locked by another user or other error.
```
skip(Model)
```
```
Skips a curved hull object, i.e. removes any locks set on the object and related objects. (If you choose to skip a shell profile for instance, the function will also unlock shell stiffeners andtrace curves that belong to the profile.)
```
Input Parameters:
Model A KcsModel object.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input
kcs_Error Skip failed: Model objects does not exist, is locked by another user or other error.
```
delete(Model)
```
Delete a curved hull object. This store method works as the delete function in interactive curved hull. It is an "intelligent" delete, i.e. it will also delete/update related objects.If youchoose to delete a shell profile for instance, this function will also delete all shell stiffeners and trace curves and remove the profile from the limit tables.
Input Parameters:
Model A KcsModel object.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input
kcs_Error Delete failed: Model objects does not exist, is locked by another user or other error.
```
recreate(Model)
```
Recreate a curved hull object.
Input Parameters:
Model A KcsModel object.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid input
kcs_Error Recreate failed: Model object does not exist or other error.
Examples
# Example: kcs_ex_hull_shellcurves.py
# Example: kcs_ex_hull_shellstiff.py
Copyright © 1993-2005 AVEVA AB
9.4.5 Dimensioning of Curved Models
These functions calculate distances between objects placed on or attached to curved panel surface. No markup is done on view. The object types that are accepted by this function are:
 Hull curves
 Seams and butts
 Shell stiffeners
 Curves along Jig rows and columns
 Frame curves
 Planar panel limits
 Hole crossmarks
```
Hole cross-marks are identified by the curved panel (Model class "Name" attribute, "Type" attribute), hole part ID (Model class "PartId" attribute), subpart type ("SubPartType" attribute"crossmark") and subpart ID corresponding to horizontal or vertical crossmark position ("SubPartId" attribute 666 or 667). Correct Model class instances are returned by
```
```
kcs_draft.model_identify() function.
```
User's Guide Vitesse
```
Chapter: Hull
```
```
remarking_length(ObjectFrom, ObjectAlong, ObjectTo)
```
Function returns length between two objects along a third. For accepted object types see Dimensioning from Hull Tools Menu.
Input Parameters:
ObjectFrom Model Object to measure from.
ObjectAlong Model Object to measure along.
ObjectTo Model Object to measure to.
Returned value:
[0] Length float The measured distance between objects.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_Error The dimensioning failed: Objects do not exist, no intersection or other error.
```
remarking_length_ext(Activity, PanelName, ObjectFrom, ObjectAlong, ObjectTo)
```
```
This function returns length between two objects along a third with adjustments according to set flags. In case the objects intersection point is located at a panel boundary, the measureis optionally adjusted with bevel gap, excess, compensation and shrinkage compensation of intersecting plate(s). For accepted object types see Dimensioning from Hull Tools Menu.
```
Input Parameters:
Activity integer Sum of the following flags:
1 - bevel gap considered,
2 - excess type 1 considered,
4 - excess type 2 considered,
8 - excess type 3 considered,
16 - excess type 4 considered,
32 - excess type 5 considered,
64 - compensation considered,
128 - shrinkage considered.
```
PanelName string Curved panel name (intersection surface).
```
ObjectForm Model Object to measure from.
ObjectAlong Model Object to measure along.
ObjectTo Model Obect to measure to.
Returned value:
[0] Length float The measured distance between objects.
```
Exceptions:
```
kcs_ArgumentError Invalid input.
kcs_Error The dimensioning failed: general error.
kcs_DatabankReadError Failed to read from databank.
kcs_ObjectNotFound Object not found in databank.
kcs_DevelopedPlateObjectNotFound Failed to retrieve developed plate data needed for calculations.
kcs_ObjectNotInPanel Seam or intersection point not in the panel.
kcs_BevelError Error while calculating bevel gap, e.g. bevel control object not found or wrong name of the object.
kcs_ShrinkageObject Error Error while getting data from shrinkage object.
kcs_UnableToCalculate Error in calculations.
Copyright © 1993-2005 AVEVA AB
9.5 Customised Holes via Vitesse
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.5.1 General
```
.Traditionally there have been two options to create holes in Tribon hull. By use of the inbuilt hole standards (parameter controlled) or to use any closed curve as hole. A facility has beendeveloped that allows the customer to set up his own parameter controlled hole standard to be used in principle the same way as the built-in standard. From a user's point of view such
```
```
holes are defined in exactly the same way as the standard holes, i.e. by a hole type (name) followed by a number of parameters separated by asterisks.
```
The option to develop a customer specific hole standard is implemented by means of the Python language. On top Tribon hull has a "hole hook" with the fixed name _TBhookCustHole.
This may branch into several sub-scripts for different hole types. How this is organised is up to the customer to decide. The customer developed holes are handled by the Tribon userinterface in the same way as the in-built standard holes, using the drawing _ _SBH_HOLE_MENU_ _ to create the user dialogue.
A picture, organized as a view of its own and named as the added hole type, must be added to this drawing. Further details can be found in Setup and Customisation / CustomisingDialog in Tribon Hull.
```
A Vitesse script is delivered in the release , _TBhookCustHole, with two example holes that have the format FH<par1>*<par2> and HOS<par1>*<par2>*<par3>*<par4> (suitable
```
```
values for test are FH150*30 and HOS600*400*50*25).
```
```
Additional holes can be implemented by expanding this script (or invoking sub-scripts from it). The name of the script is fixed and it must be placed in the directory indicated by the globalvariable PYTHONPATH.
```
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.5.2 Interface Function
A number of functions with predefined names and parameter list must exist in the script. These functions should never be changed regarding the input parameters and the result values.
User's Guide Vitesse
```
Chapter: Hull
```
```
getHoleName(HoleNo):
```
The function returns the name of the hole from the list of holes.
Input Parameters:
HoleNo integer Index to hole list.
Returned value:
HoleList[HoleNo] string Hole name.
```
getHoleSegment(SegNo):
```
The function returns a hole segment from the hole contour.
Input Parameters:
Segno integer Hole segment number.
Returned value:
HoleData[SegNo] reals Segment part R,U,V.
```
setHoleContour(HoleName, NPar, Par1, Par2, Par3, Par4, Par5, Par6, Par7, Par8):
```
```
The function creates a customer defined hole by creating hole segments to the HoleData list. The function should define a hole contour in the UV co-ordinate system whose origin willbe the reference point of the hole. Up to 8 number of hole parameters are allowed. The breakpoints of the holecontour should be defined as a number of segments (R, U, V), where R is
```
equal to 0.0 for a line segment, positive for a counterclock radius and negative for a clockwise radius. The hole code should be implemented with an exception handling mechanism sothat a failure to run the code will always be signalled by the return code.
Input Parameters:
Holename string The name of the customer hole.
Npar real Number of parameters.
Par1 real Hole parameter 1.
Par2 real Hole parameter 2.
Par3 real Hole parameter 3.
Par4 real Hole parameter 4.
Par5 real Hole parameter 5.
Par6 real Hole parameter 6.
Par7 real Hole parameter 7.
Par8 real Hole parameter 8.
Returned value:
HoleRes integer Result code. The predefined values should be used.
0 OK
1 Unrecognized hole type
2 Wrong number of parameters
3 Unreasonable parameter values
4 Hole geometry could not be generated
Copyright © 1993-2005 AVEVA AB
9.6 Customised Brackets via Vitesse
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.6.1 General
Non standard brackets have in Tribon traditionally had to be generated as bracket panels. This means that the panel bracket must have been generated as a panel of its own first andthen its "mother" panel must have been activated to enable the panel bracket to be connected.
A feature has been implemented which makes it possible to integrate the modelling of panels brackets with the normal panel modelling under certain circumstances. Characteristics ofthis implementation are:
```
 It makes use of a Vitesse script in the Pyhton language with the fixed name " _TBhookCustBracket". This script may contain the definition of any number of panel brackets (or
```
```
calls on sub-scripts performing the same task). It is the responsibility of the customer to develop and maintain this script.
```
```
 The hook is activated by a new option in the bracket selection menu with a bracket symbol and the text "Other brackets". The Vitesse based brackets are selected by picking (or
```
```
keying in the short name "V") the Vitesse symbol in the bracket syntax selection dialogue.
```
 When this alternative has been selected, another symbol menu will pop-up containing symbols, each corresponding to a Vitesse script for an panel bracket. The number of the
```
selected bracket will be supplied to the bracket hook so that the corresponding script may be activated. A new symbol font (with number 95) is used to contain these symbols. It isthe responsibility of the customer to update this font as new scripts are added. A picture representing the new bracket shall be added to the drawing _ _SBH_BKT_MENU_ _. The
```
added picture shall be organized as a view of its own and be named in a way that makes it simple to select also by keying in the name. Further details can be found in Setup andCustomisation / Customising Dialog in Tribon Hull.
 After picking control is transferred to the script that will be executed. After execution control will be returned to the main panel and the generated bracket will automatically be
connected to it.
 It is the responsibility of the customer to see to it the called script generates a proper panel bracket. Otherwise, the customer has the same options available for generating bracket
panels as when panels otherwise are generated via Vitesse.
The beauty of this implementation is that panel brackets that are so "standardised" that it makes sense to develop a Vitesse script for them can be generated as belonging to the panelaccording to a routine that is similar to that of ordinary standard brackets.
A simple example of the Vitesse hook _TBhookCustBracket is delivered together with Tribon. The name of the script is fixed and it must be placed in the directory indicated by the
global variable PYTHONPATH. Condition for this option is that a license for Hull Vitesse is available.
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.6.2 Interface Functions
A number of functions with predefined names and parameter list must exist in the script.
These functions should never be changed regarding the input parameters and the result values.
User's Guide Vitesse
```
Chapter: Hull
```
```
getBracketName(BraInd)
```
The function connects the bracket symbol to a bracket name.
Input Parameters:
BraInd integer Bracket number.
Returned values:
BracketList[BraInd] string Bracket name.
```
setBracketContour(BracketNo, BracketName):
```
The bracket defining function. New bracket scripts are added in this function.
Input Parameters:
BracketNo integer Bracket number.
BracketName string Bracket name
Returned value:
BraRes integer Result code. The predefined values should be used.
0 Ok
1 The bracket could not be generated
Copyright © 1993-2005 AVEVA AB
9.7 Customised Notches
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.7.1 General
```
This is a facility which allows the customer to set up his own parameter controlled notch standard to be used in principally the same way as the built-in standard. From a user's point ofview such notches are defined in exactly the same way as the standard notches, i.e. by a notch type (name) followed by a number of parameters separated by asterisks.
```
The option to develop a customer specific notch standard is implemented by means of the Python language. On top Tribon hull has a "notch hook" with the fixed name_TBhookCustNotch. This may branch into several sub-scripts for different notch types. How this is organised is up to the customer to decide. The customer developed notches are
handled by the Tribon user interface in the same way as the in-built standard notches, using the drawing _ _SBH_EDGE_NOTCH_MENU_ _ to create the user dialogue.
A picture, organized as a view of its own and named as the added notch type, must be added to this drawing. Further details can be found in Setup and Customisation / CustomisingDialog in Tribon Hull.
A Vitesse script is delivered in the release , _TBhookCustNotch, with two example nocthes that have the format NOTA<par1>*<par2> and NOTB<par1>*<par2>.
```
Additional notches can be implemented by expanding this script (or invoking sub-scripts from it). The name of the script is fixed and it must be placed in the directory indicated by theglobal variable PYTHONPATH.
```
User's Guide Vitesse
```
Chapter: Hull
```
Copyright © 1993-2005 AVEVA AB
9.7.2 Interface Function
A number of functions with predefined names and parameter list must exist in the script. These functions should never be changed regarding the input parameters and the result values.
User's Guide Vitesse
```
Chapter: Hull
```
```
getNotchName(notchNo):
```
The function returns the name of the notch from the list of notches.
Input Parameters:
NotchNo integer Index to notch list.
Returned value:
NotchList[NotchNo] string Notch name.
```
getNotchSegment(SegNo):
```
The function returns a notch segment from the notch contour.
Input Parameters:
Segno integer Notch segment number.
Returned value:
NotchData[SegNo] reals Segment part R,U,V.
```
setNotchContour(NotchName, NPar, Par1, Par2, Par3, Par4, Par5, Par6, Par7, Par8):
```
```
The function creates a customer defined notch by creating segments to the NotchData list. The function should define a notch contour in the UV co-ordinate system whose origin will bethe reference point of the notch. Up to 8 number of parameters are allowed. The breakpoints of the contour should be defined as a number of segments (R, U, V), where R is equal to
```
0.0 for a line segment, positive for a counter clock radius and negative for a clockwise radius. The notch code should be implemented with an exception handling mechanism so that afailure to run the code will always be signaled by the return code.
Input Parameters:
Notchname string The name of the customer notch.
Npar real Number of parameters.
Par1 real Notch parameter 1.
Par2 real Notch parameter 2.
Par3 real Notch parameter 3.
Par4 real Notch parameter 4.
Par5 real Notch parameter 5.
Par6 real Notch parameter 6.
Par7 real Notch parameter 7.
Par8 real Notch parameter 8.
Returned value:
NotchRes integer Result code. The predefined values should be used.
0 OK
1 Unrecognized notch type
2 Wrong number of parameters
3 Unreasonable parameter values
4 Notch geometry could not be generated
Copyright © 1993-2005 AVEVA AB
10 Pipe / Ventilation
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
10.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_pipe. The functions are then referred to as kcs_pipe.<function name>. Before usinga new function, please carefully read the function description. The kcs_pipe interface is used for both pipe and ventilation and there are functions to switch between pipe and ventilation
mode.
The Vitesse Pipe interface includes the following functionality:
 Handling of Pipe Objects, Pipe Spools, Parts and Joints.
 Production functions like Checking, Ready and Splitting.
 Traversing functions to find Spools and Parts within Pipe.
 Routing and Material functions.
 Default handling.
 Pipe / Vent mode functions.
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
Copyright © 1993-2005 AVEVA AB
10.2 Exception Handling
The Vitesse Pipe / Ventilation interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except"construct of the Python language. The type of error can then be examined by checking the value of kcs_pipe.error. The exception is also displayed in the Vitesse Log window which
is available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
Copyright © 1993-2005 AVEVA AB
10.3 Pipe Object Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_activate(Name)
```
The function activates a pipe object. If the function is successful the pipe will be current.
Input Parameters:
Name PipeName The name of the pipe.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound Invalid name, pipe not found or locked.
kcs_ModelIsCurrent Another pipe is already current.
kcs_ArgumentError Invalid arguments list.
kcs_AccessDenied User is not authorized to activate pipe.
```
pipe_delete (Name)
```
The function deletes a pipe object from data bank. The function requires that no pipe is current.
Input Parameters:
Name PipeName The name of the pipe.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelCurrent A pipe is current
```
pipe_duplicate(Name, NewName)
```
The function creates a copy of a pipe and stores it in the databank. No pipe must be current and new pipe will not be left current.
Input Parameters:
Name String Name of pipe to duplicate parts from.
New Name String Name of target pipe.
Returned value:
None.
```
Exceptions:
```
kcs_Error General error. Another pipe may be current.
```
pipe_exist (Name)
```
The function returns true or false depending on if the pipe exists in data bank.
Input Parameters:
Name PipeName The name of the pipe.
Returned value:
[0] integer 0 = pipe does not exists
1 = pipe exists
```
Exceptions:
```
None.
```
pipe_list ()
```
The function lists pipe to result file in SB_SHIPPRINT named <subsystem><module>.res
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_new(Name, Colour, <UserId>, <Maincomp>, <SpecSearch>)
```
The function creates a new pipe object
The colour may be defined either by using the class KcsColour or by a string. The colours are documented in Tribon Basic User's Guide in the Colour chapter. If a colour is used, notknown by the system, the default green colour is chosen.
User identification string can be given as a parameter to be stored in the pipe. When parameter is not defined or string is empty, default user identification name is used.
Main component can be given as a parameter. When the component is not defined system tries to fetch the component from diagram list.
When component name is defined UserId parameter must be given. Passing an empty string as UserId tells system to use default value.
Input Parameters:
Name PipeName The name of the pipe.
Colour String/Object String defining the colour or a KcsColour object.
<UserId> String User identification string can be empty string.
<Maincomp> String Name of main component.
<SpecSearch> Object KcsSpecSearch object containing a valid search.
Returned value:
None.
```
Exceptions:
```
kcs_NameError Invalid name.
kcs_ModelFound The pipe already exist.
kcs_ModelCurrent Another pipe is already current.
kcs_ComponentInvalid Component does not exist.
```
pipe_cancel()
```
The function cancels current pipe object. Modifications of the pipe are not stored and the pipe will not be current any more.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_name_get ()
```
Returns name of current pipe
Input Parameters:
None.
Returned value:
[0] PipeName Pipe name class.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_save()
```
The function saves current pipe. If the function is successful the pipe will not be current any more.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current
```
pipe_regenerate ()
```
The function regenerates modelling information for current pipe to a PML file named <subsystem><module>.prg in SB_PIPESCH.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_properties_set (Prop)
```
Set pipe production information
Input Parameters:
Prop PipeProp Pipe properties class.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_weldgap_set (GapSize)
```
Add weld gaps to pipe
Input Parameters:
GapSize Real Size of weld gap.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
kcs_pipe.document_reference_get()
```
The function returns a list of document references associated with the active pipe.
Input Parameters:
None.
Returned value:
[0] list List of DocumentReference instances.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active pipe not set.
kcs_GeneralError List of result can't be created for some internal reasons.
```
kcs_pipe.document_reference_add(docRef)
```
The function adds a document reference to the active pipe object.
Input Parameters:
DocRef DocumentReference Instance of Python DocumentReference class.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active pipe not set.
```
kcs_pipe.document_reference_remove(docRef)
```
The function removes document reference from the active pipe object. If there are more then one document reference, the first found will be deleted.
Input Parameters:
docRef DocumentReference Instance of Python DocumentReference class.
Returned value:
None.
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NoModelCurrent Active pipe not set.
kcs_DoesNotExist Pipe document reference doesn't exist.
```
Example:
```
```
Example: kcs_ex_pipe 01.py
```
kcs_ex_pipe 02.py
kcs_ex_pipe 09.py
kcs_ex_pipe 14.py
kcs_ex_pipe 16.py
Copyright © 1993-2005 AVEVA AB
10.4 Spool Functions
.
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_auto_spool_name_delete()
```
The function automatic deletes position names in current pipe.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current
```
pipe_auto_spool_name_set()
```
The function automatic updates position names in current pipe. All spools without position names are updated. The syntax in SBP_MODEL_DEF is used.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
spool_properties_set (SpoolId, Prop)
```
Set pipe production information.
Input Parameters:
SpoolId Integer Id of spool.
Prop PipeSpoolProp Spool properties class.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_SpoolNotFound Spool with given Id was not found.
kcs_ArgumentError Invalid arguments.
kcs_ValueError Invalid values spool properties object's members.
```
spool_weldgap_delete (PartId)
```
Delete all weld gaps in spool
Input Parameters:
PartId Integer Id of spool part.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
spool_weldgap_edit (PartId, GapSize)
```
Change size of all existing weld gaps in spool
Input Parameters:
PartId Integer Id of spool part.
GapSize Real Size of weld gap.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
spool_weldgap_set (PartI, GapSize)
```
Add weld gaps to spool
Input Parameters:
PartId Integer Id of spool part.
GapSize Real Size of weld gap.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current
kcs_PartNotFound Part with given Id was not found
```
Example:
```
```
Example: kcs_ex_pipe 03.py
```
kcs_ex_pipe 09.py
kcs_ex_pipe 13.py
Copyright © 1993-2005 AVEVA AB
10.5 Part Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
part_add (PartId, Criteria, <SpecSearch>)
```
```
part_add (PartId, Conn, Criteria, <SpecSearch>)
```
The function adds component to pipe part.
Input Parameters:
PartId Integer Part Id number.
Conn Integer Connection number.
Criteria PipePartAddCriteria Add criteria.
SpecSearch SpecSearch Valid SpecSearch object
Returned value:
[0] Integer Id of created part.
```
Description:
```
Set PipePartAddCriteria type to specify how part will be connected to pipe.
Parameter connection is used when adding component to part connection.
Depending on component type fill information in PipePartAddCriteria required to add part.
```
When part has to be connected to external pipe define external pipe name. PartId and Conn must belong to that external pipe.)
```
```
Exceptions:
```
kcs_NoModelIsCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_ComponentInvalid Component does not exist.
kcs_PointNotInPart Point is outside part.
kcs_ModelNotFound External pipe does not exist.
kcs_ArgumentError Invalid arguments list.
```
part_boss_conn_type_set (PartId, Conn, Code)
```
Change the boss connection code
Input Parameters:
Part Id Integer Part Id number.
Conn Integer Connection number.
Code Integer Boss connection code.
1 = on surface
2 = insert
3 = extrude
4 = saddle
5 = none
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PartIsNotDressed Boss connection not allowed for frame part.
kcs_ConnectionNotBossJoint Connection is not boss joint.
kcs_ValueError Invalid connection code.
```
part_branch_get (PartId)
```
The function returns branch number of part.
```
(Function name will be changed in next delivery to pipe_part_branch_get())
```
Input Parameters:
PartId Integer Part Id number.
Returned value:
[0] Integer Branch number.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_conn_coord_get(PartId, Conn, Point)
```
Get pipe part connection coordinates.
Input Parameters:
PartId Integer Id of part in spool.
Conn Integer Connection number.
Point Point3D Returns connection coordinates.
Returned value:
[0] Integer 1 - success, point contains connection coordinates
0 - failure
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
```
part_conn_find (PartId, Point)
```
The function gets closest connection of part to a given point.
Input Parameters:
PartId Integer Part Id number.
Point3D Point Given point.
Returned value:
[0] Integer Connection number.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_connect (PartId1, Conn1, PartId2, Conn2)
```
```
part_connect (PartId1, Conn1, Name, PartId2, Conn2)
```
Connects two parts. The first part has to belong to current pipe. If the second part belongs to an external pipe/equipment, external pipe name has to be given.
Input Parameters:
PartId1 Integer Id of first part.
Conn1 Integer Connection number of first part.
Name PipeName Name of external pipe/equipment.
PartId2 Integer Id of second part.
Conn2 Integer Connection number of second part.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Invalid connection number.
kcs_ConnectionIsUsed Connection already connected.
kcs_ConnectionError Connection was not possible.
kcs_ModelNotFound External pipe not found.
```
part_delete (PartId)
```
The function deletes a part
The part has to be "deletable", use part to frame otherwise
Input Parameters:
PartId Integer Part Id number.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartNotDeletable Part is not "deletable".
```
part_disconnect (PartId, Conn)
```
Disconnect the part connection from another part in current pipe, a part in another pipe or an equipment
Input Parameters:
PartId Integer Id of part.
Conn Integer Connection number.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Invalid connection number.
kcs_ArgumentError Invalid arguments.
kcs_ConnectionNotConnected Connection is not connected.
kcs_DisconnectionError Connected to locked object or connected to on-connection, cannot disconnect.
```
part_end_excess_set (PartId, Conn, Excess, <Enable>)
```
Set end excess at part connection.
Input Parameters:
Part Id Integer Part Id number.
Conn Integer Connection number.
Excess Real Excess length.
```
Enable Integer Set when Enable=1 (default), reset when Enable=0.
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PartNotStraight End excess not allowed, part is not straight.
kcs_PartNotMaterialEnd End excess not allowed, part connection is not end of material.
```
part_ext_structure_connect (PartId, Point, Structure)
```
Connect a pipe part to a structure at a specific point on the structure part. The reference is a true 2-way connection stored in both pipe and structure. The pipe has to be current.
Input Parameters:
PartId Integer Id of pipe part.
Point Point3D Connection point on pipe part frame.
Structure String Structure Name.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionError Connection was not possible.
kcs_ObjectLocked Structure is locked by another user.
kcs_ArgumentError Invalid arguments.
```
part_ext_structure_disconnect (PartId, Structure)
```
```
part_ext_structure_disconnect (PartId)
```
Disconnect the part from structure. The connection shall be the kind described in the part_ext_structure_connect function. The pipe has to be current.
Input Parameters:
PartId Integer Id of part.
Structure String Structure name. All structures connected to this part will be disconnected.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection between this part and structure not exist.
kcs_ObjectLocked Structure is locked by another user
kcs_ArgumentError Invalid arguments.
```
part_feed_excess_set (PartId, <Enable>)
```
Permit feed excess between bends.
Input Parameters:
Part Id Integer Part Id number.
```
Enable Integer Set when Enable=1 (default), reset when Enable=0.
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartNotStraight Feed excess not allowed, part is not straight.
```
part_feed_min_set (PartId, Length, <Enable>)
```
Sets minimum feed excess for a straight pipe.
Fetched from bending machine if not given.
Input Parameters:
Part Id Integer Part Id number.
Length Real Minimum feed excess length.
```
Enable Integer Set when Enable=1 (default), reset when Enable=0.
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartNotStraight End excess not allowed, part is not straight.
```
part_flip(PartId)
```
The function flips a part.
Input Parameters:
PartId Integer Id of part to flip.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_FlipNotPossible Flip operation is not possible.
```
part_incline(PartId, Vect)
```
This function inclines an existing part. Part has to be flange type 2601.
Input Parameters:
PartId Integer Id of part.
Vect Vector3D Vector
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ComponentInvalid Component is not flange type 2601.
kcs_ArgumentError Invalid arguments.
```
part_insert (PartId, Conn, Criteria, <SpecSearch>)
```
Inserts a new part in an existing part.
Input Parameters:
PartId Integer Id of part.
Conn Integer Connection number.
Criteria PipePartAddCriteria Criteria class defining:
- part component
- distance from connection to node point of inserted part.
<SpecSearch> SpecSearch Valid SpecSearch object
Returned value:
[0] Integer Id of inserted part.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Invalid connection number
kcs_PointNotInPart Placing point is outside part.
```
part_properties_set (PartId, Prop)
```
Set pipe production information.
Input Parameters:
PartId Integer Id of part.
PipePartProp Prop Part properties class.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ArgumentError Invalid arguments.
```
part_resize (Option, PartId, NomDia, [NomDia2])
```
Resize a part.
Input Parameters:
Option Integer Ignored. Set this to 0. For future use.
PartId Integer Id of part.
NomDia Integer New nominal diameter.
NomDia2 Integer Optional. New nominal diameter for connection 2.
Returned value:
[0] Integer Operation result
0 = Success
```
1 = Secondary DN needed (Multidimensional component and more than one hit in the specification)
```
[1] Integer Id of previous part. Use for iteration.
-1 = No more parts in branch
[2] Integer New Id of this part.
[3] Integer Id of succeding part. Use for iteration.
-1 = No more parts in branch
[4] String Operation information.
```
Description:
```
The method resizes one part giving part id's of neighbour's back for iteration purpose. If Operation result is 1, call again with NomDia2 given to limit the search result in the specification.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_respec (Option, PartId, SpecName, [NomDia2])
```
Respec a part.
Input Parameters:
Option Integer Ignored. Set this to 0. For future use.
PartId Integer Id of part.
SpecName String New specification.
NomDia2 Integer Optional. New nominal diameter for connection 2.
Returned value:
[0] Integer Operation result
0 = Success
```
1 = Secondary DN needed (Multidimensional component and more than one hit in the specification)
```
[1] Integer Id of previous part. Use for iteration.
-1 = No more parts in branch
[2] Integer New Id of this part.
[3] Integer Id of succeding part. Use for iteration.
-1 = No more parts in branch
[4] String Operation information.
```
Description:
```
The method respecifies one part giving part id's of neighbour's back for iteration purpose. If Operation result is 1, call again with NomDia2 given to limit the search result in thespecification.
```
Exceptions:
```
kcs_NoModeIIsCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_selection_criteria_get (PartId)
```
The function get selection criteria from pipe part.
Input Parameters:
PartId Integer Part Id number
Returned value:
SpecSearch SpecSearch Valid SpecSearch object
```
Description:
```
The function gets the selection criteria from the part.
```
Exceptions:
```
kcs_NoModelIsCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ArgumentError Invalid arguments list.
```
part_selection_criteria_set (Partld,<SpecSearch>)
```
The function get selection criteria from pipe part.
Input Parameters:
Partld Integer Part Id number
SpecSearch SpecSearch Valid SpecSearch project
Description
The function sets the selection criteria of the part.
```
Exceptions:
```
kcs_NoModellsCurrent No pipe is curent.
kcs_PartNotFound Part with given Id was not found.
kcs_ArgumentError Invalid arguments list.
```
part_spool_get (Spoold)
```
The function gets spool name of the spool that the part belongs to.
Input Parameters:
SpoolId Integer Part Id number.
Returned value:
[0] String Spool name.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_spool_limit_set (PartId, Conn, <Enable>)
```
Sets spool limit at given connection of part.
Input Parameters:
Part Id Integer Part Id number.
Conn Integer Connection number.
```
Enable Integer Set when Enable=1 (default), reset when Enable=0.
```
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_LimitHasToExist Limit has to exist at the end of part.
kcs_OnSurfaceLimitNotAllowed Spool limit not allowed for boss connection.
kcs_ContMaterialLimitNotAllowed Spool limit not allowed for continuous material.
```
part_structure_connect (PartId, Structure, Alias)
```
Connects a part to a structure. Pipe has to be current.
Input Parameters:
PartId Integer Part Id number.
Structure String Structure name.
Alias String Structure alias name.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_StructureNotFound Structure does not exist.
kcs_ConnectionExist Connection already exist.
kcs_ArgumentError Invalid arguments.
```
part_structure_disconnect (PartId, Structure)
```
Disconnects a part from a structure. Pipe has to be current.
Input Parameters:
PartId Integer Part Id number.
Structure String Structure name.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent
No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Part is not connected to structure.
kcs_ObjectLocked Structure is locked.
kcs_ArgumentError Invalid arguments.
```
part_structure_get (PartId)
```
Returns the names of all connected structures.
Input Parameters:
PartI Integer Part Id number.
Returned value:
[...] ResultPipeStructConn List of ResultPipeStructConn objects containing name and alias name of connected structure.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_weldgap_delete (PartId)
```
Delete weld gap at given connection of part.
Input Parameters:
PartId Integer Id of part.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartNotWeldgap Part has not weld gap.
kcs_ArgumentError Invalid arguments.
```
part_weldgap_edit (PartId, GapSize)
```
Modify size of weld gap.
Input Parameters:
PartId Integer Id of part.
GapSize Real Size of weld gap.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartNotWeldGap Part has not weld gap.
kcs_ArgumentError Invalid arguments.
```
part_weldgap_set (PartId, Conn, GapSize)
```
Add weld gap at given connection of part.
Input Parameters:
PartId Integer Id of part.
Connection Integer Connection number.
GapSize Real Size of weld gap.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_WeldGapNotAllowed Not possible to inser weld gap at this connection.
kcs_ArgumentError Invalid arguments.
```
part_conn_part_get (PartId, Conn)
```
The function returns Id of part connected to given connection of part.
Input Parameters:
PartId Integer Id of part in spool.
Conn Integer Connection number.
Returned value:
[0] Integer Id of connected part.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectedPartNotFound No part connected to given connection.
```
part_rotate (PartId, Conn, Angle)
```
The function rotates given connection of part.
Input Parameters:
PartId Integer Id of part in spool.
Conn Integer Connection number.
Angle Real Rotation angle in degrees.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PartRotateError Rotation is not possible.
```
part_turn (PartId, Conn, Angle)
```
The function turns given connection of part.
Input Parameters:
PartId Integer Id of part in spool.
Conn Integer Connection number.
Angle Real Turn angle in degrees.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PartTurnError Turn is not possible.
kcs_ArgumentError Invalid arguments.
```
pipe_transform(T)
```
The function transforms pipe.
Input Parameters:
T Transformation3D. Transformation matrix.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_MatrixInvalid Transformation matrix is invalid.
kcs_PipeConnected Pipe is connected.
```
Example:
```
```
Example: kcs_ex_pipe 04.py
```
kcs_ex_pipe 08.py
kcs_ex_pipe 09.py
kcs_ex_pipe 12.py
kcs_ex_pipe 13.py
kcs_ex_pipe 15.py
kcs_ex_pipe 17.py
Copyright © 1993-2005 AVEVA AB
10.6 Joint Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
joint_add (PartId, Conn, Criteria)
```
Adds a joint to part connection.
Input Parameters:
PartId Integer Id of part.
Conn Integer Connection number.
Criteria PipeJointAddCriteria Joint add criteria.
Returned value:
[0] Integer Id of added par.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Invalid connection number.
kcs_ComponentInvalid Invalid component type.
kcs_ModelNotFound External pipe does not exist.
```
joint_insert (PartId, Conn, Criteria)
```
Inserts a joint in an existing part.
Input Parameters:
Integer PartId Id of part.
Integer Conn Connection number.
Criteria PipeJointAddCriteria Criteria class defining:
- joint type ("insert" or "weld")
- distance from connection to node point of insert
Returned value:
[0] Integer Id of inserted part.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Invalid connection number.
kcs_PointNotInPart Placing point is outside part.
kcs_ComponentNotFound Invalid component type.
```
Example:
```
```
Example: kcs_ex_pipe 10.py
```
Copyright © 1993-2005 AVEVA AB
10.7 Production Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_check (Check)
```
Check if current pipe complies with the production requirements
Input Parameters:
Check PipeCheck PipeCheck class which specifies what kind of checks should be performed
Returned value:
[0] Integer 1 = OK
2 = OK with warnings
3 = not OK, due to controls
4 = not OK, due to other reasons
[1] Integer Number of messages
[...] ResultPipeCheck. List of ResultPipeCheck objects containing pipe check results.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_check_settings (Settings)
```
```
pipe_check_settings (Settings, PartId)
```
Activating or deactivating pipe production check functions.
If Settings has activated bending or extrusion checking. PartId Must be given.
Input Parameters:
Settings PipeCheckSettings Check functions state.
PartId Integer Id of part to modify production checking options, used to change settings related to part.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ArgumentError Invalid arguments.
```
pipe_ready ()
```
The function makes current pipe ready.
The pipe will be checked. If the checks are successful the pipe will be marked "ready" and saved in data bank.
Input Parameters:
None.
Returned value:
[0] Integer Pipe check result:
= 1 - OK
= 2 - OK with warnings
= 3 - not OK, due to control checks
= 4 - not OK, due to other reason
[1] Integer Number of messages generated during pipe checks
[...] ResultPipeCheck List of ResultPipeCheck objects containing pipe check results
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
Message number: Message description:
1 Position name missing.
2 Multiple position names.
3 Position control failed.
4 Position control deactivated.
5 Manual bending, the bending radius is not supported.
6 Manual bending, no straight pipe was found between two bends.
7 Manual bending, the straight pipe between two pipes is too short
8 Manual bending, bending angle is too big.
9 Manual bending, collision occurred.
10 Manual bending, Straight pipe at start or end too short.
11 Bending not allowed to the pipe material.
12 Possible autoweld ignored, no proceeding flange was found.
13 Possible autoweld ignored, no succeeding flange was found.
14 First flange, no autoweld.
```
15 Last flange, no autoweld User defined excess exists (PSG_PART_EXC2).
```
16 User defined excess exists.
17 Manual extrusion.
18 Feed excess permitted.
19 Frame pipe exists.
20 Pipe is longer that one pipe material.
21 Loose part.
22 Conflicting rotation of neighbours.
23 Given rotation conflicts with neighbour.
24 Joint has empty connection.
25 Non connected connections.
26 Feed excess.
27 Joint excess.
28 Fabrication excess.
29 Second sleeve not autoweld, only one allowed.
```
pipe_split(Name)
```
The function starts a background splitting job for a pipe. The pipe has to be "ready", and no pipe should be current.
Input Parameters:
Name PipeName. The name of the pipe.
Returned value:
None.
```
Exceptions:
```
kcs_ModelCurrent There is a current pipe.
kcs_ModelNotFound Pipe not found.
kcs_PipeNotReady Pipe is not ready.
```
Example:
```
```
Example: kcs_ex_pipe 05.py
```
Copyright © 1993-2005 AVEVA AB
10.8 Traversing Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_part_find (Act, <PartId>)
```
The function returns Id number of first/next/previous part.
Part Id must be given if previous or next part is requested.
that this function also returns non-physical parts like joints and connections. It is currently not possible in Vitesse to distinguish between the different types of parts.
Input Parameters:
Act Integer 1 = get first part
2 = get next part
3 = get previous part
```
PartId Integer Part Id number, required when getting next\previous part (Act = 2, 3).
```
Returned value:
[0] Integer 0 = failure, there is no next/previous part
1 = success, second argument contains part Id.
[1] Integer Requested part Id.
[2] Integer Connection number in found part that is connected to given part, only if act = 2 or act = 3. When act=1 the value is set to 0.
```
Exceptions:
```
kcs_NoModelIsCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ArgumentError Invalid arguments list.
Example
# Example: kcs_ex_pipe04.py
```
pipe_part_find_all()
```
Returns all part Ids in the pipe per branch. I.e. [[Branch 1], [Branch 2], [Branch 3]...]
[Branch] = [-1013, -1004, -1003, -1001, -1008, -1006, -1007, -1005, -1015]
Input Parameters:
None
Returned value:
[0] List [[Branch 1], [Branch 2], [Branch 3]...][Branch] = [-1013, -1004, -1003, -1001, -1008, -1006, -1007, -1005, -1015]
```
Exceptions:
```
kcs-Error Not able to initiate piping.
kcs-NoModellsCurrent No pipe is current.
kcs_BranchNotFound Branch not found.
kcs-ArgumentError Invalid arguments list.
```
pipe_part_data_get(<PartId>)
```
```
Returns a dictionary containing data for all the parts in the pipe, the part Ids are the keys for the data connected to each part.{partID:{DATA}, partID:{DATA}, partID:{DATA}...}
```
Input Parameters:
None
```
PartId (optional) integer A part id in the current pipe
```
Returned value:
```
[0] Dictionary {partID:{DATA}, partID:{DATA}, partID:{DATA}....where {DATA} is a dictionary with the following keys:
```
CompName - StringConnIn - Integer
ConnOut - IntegerNconn - Integer
Nom Dia - [ND at conn 1, ND at conn 2...] - IntegerPartType - Integer
Radius -RealRotation - Real
SpecCmpGroup - StringSpecCmpName - String
SpecFlow - RealSpecFuncType - Integer
SpecName - String
SpecNomDia - RealSpecPrClass - String
SpecProject - StringSpecShortName - String
SpecVelocity - RealTotBuildLength - Real
TypeString - String
```
If a part id is given as input then only the {DATA} dictionary for that part will be returned.
```
```
Exceptions:
```
kcs_Error Not able to initiate piping.
kcs_NoModellsCurrent No pipe is current.
kcs_SpoolNotFound Spool with given Id was not found.
kcs-ArgumentError Invalid arguments list.
```
pipe_spool_find (Act, <SpoolId>)
```
The function returns Id number of first/next/previous pipe spool.
Spool Id must be given if previous or next spool is requested.
Input Parameters:
Act Integer 1 = get first spool
2 = get next spool
3 = get previous spool
```
SpoolId Integer Spool Id number, required when getting next\previous spool (Act = 2, 3)
```
Returned value:
[0] Integer 0 = failure, there is no next/previous spool
1 = success, second argument contains spool Id
[1] Integer Requested spool Id.
```
Exceptions:
```
kcs_NoModelIsCurrent No pipe is current.
kcs_SpoolNotFound Spool with given Id was not found.
kcs_ArgumentError Invalid arguments list.
```
pipe_spool_part_find (Act, <PartId>)
```
The function returns Id number of first/next/previous part.
```
(Note that this function also returns non-physical parts like joints and connections).
```
Input Parameters:
Act Integer 1 = get first part
2 = get next part
3 = get previous part
```
PartId Integer Spool Id number when getting first part (Act = 1)
```
```
Part Id number when getting next\previous part (Act = 2, 3)
```
Returned value:
[0] Integer 0 = failure, there is no next/previous part
1 = success, second argument contains part Id
[1] Integer Requested part Id.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_SpoolNotFound Spool with given Id was not found.
Example
# Example: kcs_ex_pipe04.py
```
pipe_spool_part_find_all(<SpoolId> or <PartId>)
```
Returns all part Ids in the pipe per spool. I.e. [[Spool 1], [Spool 2], [Spool 3]...][Spool 1] = [-1004, -1013, -1004, -1003, -1001, -1008] where the first Id is the spool id. The same resultwill be returned if a part id is given, but then only for one spool. As an option a specific spool id can be given as input. Then only the parts in this spool will be returned.
```
kcs_pipe.pipe_spool_part_find_all(-1004)
```
[-1013, -1004, -1003, -1001, -1008]
Input Parameters:
None
Spool id interger The id of the spool to return part ids for.
PartId integer The id of a part belonging to a spool to return part ids for
Only one of the optional parameters can be given. If a part id shall be given then the named argument has to be used, e.g.
```
kcs_pipe.pipe_spool_part_find_all(PartId=-1013)
```
Only giving an integer will be interpreted as a spool id.
Returned value:
[0] List [[Spool 1], [Spool 2], [Spool 3]...][Spool 1] = [-1004, -1013, -1004, -1003, -1001, -1008]
or
[-1013, -1004, -1003, -1001, -1008]
```
Exceptions:
```
kcs_Error Not able to initiate piping.
kcs_NoModellsCurrent No pipe is current.
kcs_SpoolNotFound Spool with given Id was not found.
```
kcs:ArgumentError Invalid arguments list.
```
```
Example:
```
```
Example: kcs_ex_pipe 04.py
```
Copyright © 1993-2005 AVEVA AB
10.9 Routing and Material Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_route_end (Prop)
```
The function ends routing
Input Parameters:
Prop PipeRoute Routing criteria.
Returned value:
[0] Integer Id of first created part.
[1] Integer Id of last created part.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PointNotInPart Point is outside part.
kcs_ModelNotFound External pipe does not exist.
```
pipe_route_point (Prop)
```
The function adds intermediate point in route sequence.
Input Parameters:
Prop PipeRoute Routing criteria.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_route_start (Prop)
```
The function starts routing
Input Parameters:
Prop PipeRoute Routing criteria.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_ConnectionNotFound Connection number is invalid.
kcs_PointNotInPart Point is outside part.
kcs_ModelNotFound External pipe does not exist.
```
pipe_material_remove ()
```
The function removes all material from current pipe
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
pipe_material_set (<BranchId>, Prop, <SpecSearch>)
```
The function dresses branch with material. If no BranchId is given all branches in the pipe will be dressed with pipe material.
Input Parameters:
BranchId Integer Branch Id number.
Prop PipeMaterial Material properties. Operation type must be set to 'pipe'.
SpecSearch SpecSearch Valid SpecSearch object
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No pipe is current.
kcs_ArgumentError Invalid arguments list.
kcs_BranchNotFound Branch with given Id was not found.
kcs_ComponentInvalid Component does not exist.
kcs_ComponentTypeInvalid Invalid component type.
kcs_ComponentNotFit Component does not fit.
kcs_ValueError Invalid material properties.
kcs_SpecArgumentError SpecSearch object must be used.
```
part_material_remove (PartId)
```
The function removes all material from current pipe.
Input Parameters:
PartId Integer Part Id number.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
```
part_material_set (PartId1, <PartId2>, Prop, <SpecSearch>)
```
The function dresses frame with material.
When part is straight only one Id is needed.
When part is bend, the part can be defined in two ways.
If only one id is given, that should be the id of the frame bend.
If two ids are given that should be the two straight frame parts that connect to the bend
Input Parameters:
PartId1 Integer Part Id number.
PartId2 Integer Part Id number.
Prop PipeMaterial Material properties.
SpecSearch SpecSearch Valid SpecSearch object
Returned value:
[0] Integer Id of created part in place of frame part.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_PartNotFound Part with given Id was not found.
kcs_PartIsDressed Part already has material.
kcs_ComponentInvalid Component does not exist.
kcs_ComponentTypeInvalid Invalid component type.
kcs_ComponentNotFit Component does not fit.
```
Example:
```
```
Example: kcs_ex_pipe 06.py
```
kcs_ex_pipe 07.py
Copyright © 1993-2005 AVEVA AB
10.10 Default and Miscellaneous Functions
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
default_value_get (Keyword)
```
The function gets given default value.
Input Parameters:
Keyword String Keyword indicating default value.
Returned value:
[0] String Requested default keyword value.
```
Exceptions:
```
kcs_DefKeywordInvalid Invalid keyword.
```
default_value_set (Statement)
```
The function sets given default value.
Input Parameters:
Statement String Statement string in format 'KEYWORD=VALUE'
Returned value:
None.
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
```
default_bendobj_id_get()
```
The function returns Id number of bending machine object currently in use.
Input Parameters:
None.
Returned value:
[0] Integer Bending machine object Id.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
```
default_bendobj_id_set(bendObjId)
```
The function sets the Id number of bending machine object currently in use.
Input Parameters:
bendObjId Integer Bending machine object Id.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent No pipe is current.
kcs_ArgumentError Invalid argument given.
kcs_MultipleBendingObjectNotUse Multiple bending machines cannot be used.
kcs_BendingObjectNotFound Bending object cannot be found.
```
Example:
```
```
Example: kcs_ex_pipe 03.py
```
kcs_ex_pipe 011.py
Copyright © 1993-2005 AVEVA AB
10.11 Ventilation / Pipe Mode Functions
The kcs_pipe interface can operate in either pipe or ventilation mode. The following functions are used to switch mode.
User's Guide Vitesse
```
Chapter: Pipe / Ventilation
```
```
pipe_mode_activate()
```
Sets system in pipe modelling mode.
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelIsCurrent A ventilation duct is current.
```
vent_mode_activate()
```
Sets system in ventilation modelling mode
Input Parameters:
None.
Returned value:
None.
```
Exceptions:
```
kcs_ModelIsCurrent A pipe is current.
kcs_VentDatabankNotFound Ventilation data bank is not assigned.
kcs_LicenceError Licence authorization error.
```
Example:
```
```
Example: kcs_ex_pipe 11.py
```
Copyright © 1993-2005 AVEVA AB
11 Specifications
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
11.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_spec. The functions are then referred to as kcs_spec.<function name>. Before usinga new function, please carefully read the function description.
 Perform a SpecSearch
User's Guide Vitesse
```
Chapter: Specifications
```
Copyright © 1993-2005 AVEVA AB
11.2 Exception Handling
The Vitesse Pipe / Ventilation interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except"construct of the Python language. The type of error can then be examined by checking the value of kcs_spec.error. The exception is also displayed in the Vitesse Log window which is
available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Specifications
```
Copyright © 1993-2005 AVEVA AB
11.3 Specification Search Functions
User's Guide Vitesse
```
Chapter: Specifications
```
```
Spec_search(SpecSearch)
```
```
The function performs a search in the specifications using the current set search criterias in SpecSearch object (parameter). The result is passed back in SpecSearch__ResultList (seeKcsSpecSearch).
```
Input Parameters:
SpecSearch SpecSearch object A SpecSearch object with set search criterias.
Returned value:
None.
```
Exceptions:
```
kcs_ComponentNotFound No component match found.
Copyright © 1993-2005 AVEVA AB
12 Volume
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
12.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_vol. The functions are then referred to as kcs_vol.<function name>. Before
using a new function, please carefully read the function description.
The Vitesse Volume interface contains functions for:
 Placing a volume in the model.
 Creating volumes
 Modifying volumes
 Deleting volumes
 Creating connections
 Modifying connections
 Deleting connections
User's Guide Vitesse
```
Chapter: Volume
```
Copyright © 1993-2005 AVEVA AB
12.2 Exception Handling
The Volume interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of the Pythonlanguage. The type of error can then be examined by checking the value of kcs_vol.error. The exception is also displayed in the Vitesse Log window, which is available by the
Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Volume
```
Copyright © 1993-2005 AVEVA AB
12.3 Functions
This chapter describes functions for Volumes..
User's Guide Vitesse
```
Chapter: Volume
```
```
placvol_new(unplacedName, point, uVector, vVector, <placedName>)
```
The function creates an instance and places a volume in the product model.
Input Parameters:
unplacedName String Name of unplaced volume.
point KcsPoint3D 3D point where the volume should be placed.
uVector KcsVector3D U vector for placement
vVector KcsVector3D V vector for placement
placedName String Optional parameter. Name of the placed volume to be created. If no name is given or given name is empty, a name is generated automatically.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter value.
kcs_ValueError Given vectors are empty or parallel.
kcs_NameTooLong Given name is too long.
kcs_NameOccupied Given name for placed volume is already used.
kcs_ObjectLocked Unplaced volume is locked by another user.
kcs_ObjectNotFound Unplaced volume with given name not found.
kcs_Error General error. Can't copy elements.
```
placvol_exist (VolName)
```
The function checks if a volume exists in the data bank.
Input Parameters:
VolName string The name of the placed volume
Returned value:
[] integer 0 = Volume doesn't exist
1 = Volume exists
```
Exceptions:
```
kcs_ArgumentError Invalid arguments lists.
kcs_CouldNotOpenDatabank Failure opening Volume databank.
Example
# Example: kcs_ex_draft36.py
```
vol_new (VolName, <MaxExt>)
```
The function initializes a new volume and makes it the current one.
Input Parameters:
VolName string The name of the volume
<VolType> contant or string Volume type. It can be defined by using:
 volume type constants
 logical databank names
See the function kcs_vol.vol_type_list_get for a list of all volume types and corresponding databanks defined in the Tribon system.
```
his parameter is optional. If not given, the project volume data bank (SBD_VOLUME) will be used.
```
```
<MaxExt> real Max extension of the volume (optional)
```
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeCurrent Volume is already current.
kcs_NameUsedInWorkspace Name already used in workspace.
kcs_ArgumentError Invalid arguments list.
kcs_NameError Name invalid.
kcs_ExtensionError Invalid Extension.
```
vol_open (VolName, <MaxExt>)
```
The function opens an existing volume and makes it the current one..
Input Parameters:
Vol_Name string The name of the volume
<VolType> constant orstringVolume type. It can be defined by using:
 volume type constants
 logical databank names
See the function kcs_vol.vol_type_list_get for a list of all volume types and corresponding databanks defined in the Tribon system.
```
This parameter is optional. If not given, the project volume databank (SBD_VOLUME) will be used.
```
```
<MaxExt> real Max extension of the volume (optional)
```
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeCurrent Volume is already current
kcs-CouldNotOpenDatabank Failure opening Volume databank
kcs_VolumeNotFound Volume not found
kcs_VolumeLocked Volume is locked
kcs_DrawingLocked Drawing is locked
kcs_NameUsedInWorkspace Name already used in workspace
kcs_InvalidMode Not In Volume Mode
kcs_ArgumentError Invalid arguments list
kcs_NameError Name invalid
kcs_ExtensionError Invalid Extension
```
vol_exist (VolName, <VolType>)
```
The function checks if a volume exists in the data bank.
Input Parameters:
VolName string The name of the volume
<VolType> constant orstringVolume type. It can be defined by using:
 volume type constants
 logical databank names
See the function kcs_vol.vol_type_list_get for a list of all volume types and corresponding databanks defined in the Tribon system.
```
This parameter is optional. If not given, the project volume databank (SBD_VOLUME) will be used
```
Returned value:
[] integer 0 = Volume doesn't exist
1 = Volume exists
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_CouldNotOpenDatabank Failure opening Volume databank.
```
vol_cancel()
```
The function cancels the current volume
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent Volume was not current.
kcs_NotIntVolumeMode Not in Volume Mode
kcs_ArgumentError Invalid arguments list.
```
vol_save ()
```
The function saves the current volume in its original data bank.
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NameError Name of volume must be user-defined.
kcs_VolumeNotCurrent No volume is current.
kcs_NotInVolumeMode Not In Volume Mode.
kcs_CouldNotOpenDatabank Failure opening Volume databank.
kcs_ObjectLocked Object locked.
kcs_AccessDenied Access denied in data bank.
```
vol_save_as (Vol_Name, <VolType>)
```
The function saves the current volume under another name.
Input Parameters:
Vol_Name string The new name of the volume
<VolType> constant orstringVolume type. It can be defined by using:
 volume type constants
 logical databank names
See the function kcs_vol.vol_type_list_get for a list of all volume types and corresponding databanks defined in the Tribon system.
This parameter is optional. If not given, the original volume data bank will be used.
Returned Value:
[] None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_NameError Name invalid.
kcs_VolumeNotCurrent No volume is current.
kcs_NotInVolumeMode Not In Volume Mode.
kcs_CouldNotOpenDatabank Failure opening Volume databank.
kcs_VolumeExist Name clash in data bank.
kcs_NameUsedInWorkskpace Name clash in work space.
kcs_ObjectLocked Object locked.
kcs_AccessDenied Access denied in data bank.
```
vol_close()
```
The function cancels the current volume
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent Volume was not current.
kcs_NotInVolumeMode Not in Volume Mode.
kcs_ArgumentError Invalid arguments list.
```
vol_delete(VolName, <VolType>)
```
The function deletes a volume in the data bank.
Input Parameters:
VolName string The name of the volume
<VolType> constant orstringVolume type. It can be defined by using:
 volume type constants
 logical databank names
See the function kcs_vol.vol_type_list_get for a list of all volume types and corresponding databanks defined in the Tribon system.
```
This parameter is optional. If not given, the project volume databank (SBD_VOLUME) will be used
```
Returned value:
[] None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list.
kcs_CouldNotOpenDatabank Failure opening Volume databank.
kcs_VolumeNotFound Volume not found.
kcs_VolumeLocked Volume is locked.
kcs_AccessDenied Access denied in data bank.
```
vol_type_list_get()
```
The function returns all volume types registered in the Tribon system as a Python dictionary.
Input Parameters:
None
Returned value:
[0] dictionary The dictionary contains volume types as keys and pairs: description and logical databank name as values. The following volume types areimplemented:
```
kcsVOLTYPE_NONSTD : ('Project volume', 'SBD_VOLUME')
```
```
kcsVOLTYPE_STD : ('Component volume', 'SBE_GENVOLDB)
```
```
You can find all registered types using keys() function of the returned dictionary.
```
```
Exceptions:
```
kcs_Error General error
```
subvol_add ()
```
The function creates new subvolume on current volume
Returned value:
nSubVolNumber Integer Subvolume Number
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
```
subvol_list ()
```
The function returns list of subvolumes for current volume.
Returned value:
PyList List List of found subvolumes
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
```
subvol_delete (nSubVolNumber)
```
The function deletes subvolume in current volume
nSubVolNumber Integer Subvolume Number
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_SubvolumeNotFound Subvolume not found.
```
Primitive_add(nSubVolNumber, PyObject)
```
The function gets primitive properties.
nSubVolNumber Integer Subvolume Number
PyObject PyObject Primitive Creation Class Instance. Valid classes are:
 KcsVolPrimitiveBlock
 KcsVolPrimitiveGeneralCylinder
 KcsVolPrimitiveRevolution
 KcsVolPrimitiveTorusSegment
 KcsVolPrimitiveTruncatedCone
Returned value:
nPrimNumber Integer Number of created primitive
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_SubvolumeNotFound Subvolume not found.
kcs_PrimitiveNotFound Primitve not found.
kcs_Error General error. View can't be created.
```
Primitive_list(nSubVolNumber)
```
The function gets primitive properties.
nSubVolNumber Integer Subvolume Number
Returned value:
PyList List List of found primitves
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_SubvolumeNotFound Subvolume not found.
kcs_PrimitiveNotFound Primitve not found.
```
Primitive_properties_get (nSubVolNumber, nPrimNumber )
```
The function gets primitive properties.
nSubVolNumber Integer Subvolume Number
nPrimNumber Integer Primitive Number
Returned value:
KcsVolPrimitiveBase PyObject The primitive properties class instance
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_SubvolumeNotFound Subvolume not found.
kcs_PrimitiveNotFound Primitve not found.
```
Primitive_properties_set (nSubVolNumber, nPrimNumber, PyKcsPrimVolProp)
```
The function gets primitive properties.
nSubVolNumber Integer Subvolume Number
nPrimNumber Integer Primitive Number
KcsVolPrimitiveBase PyObject The primitive properties class instance
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_SubvolumeNotFound Subvolume not found.
kcs_PrimitiveNotFound Primitve not found.
```
conn_add (KcsVolConnection)
```
The function adds connection in current volume.
KcsVolConnection Class Instance KcsVolConnection class instance
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_ConnectionExist Connection already exists.
```
conn_list ()
```
The function returns connection properties in current volume.
Returned value:
PyList List List containing connections id's
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
```
conn_properties_get (KcsVolConnection)
```
The function returns connection properties in current volume
KcsVolConnection Class Instance KcsVolConnection class instance, Input fields: ConnNo, ConnType
Returned value:
KcsVolConnection Class Instance Class containing connection properties
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_ConnectionNotFound Connection not found.
```
conn_properties_set (KcsVolConnection)
```
The function sets connection properties in current volume
KcsVolConnection Class Instance KcsVolConnection class instance
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_ConnectionNotFound Connection not found.
```
conn_delete (KcsVolConnection)
```
The function deletes connection in current volume.
KcsVolConnection Class Instance KcsVolConnection class instance
Returned value:
[] None
```
Exceptions:
```
kcs_VolumeNotCurrent No volume was current.
kcs_ConnectionNotFound Connection not found.
kcs_Error General error. View can't be created.
Copyright © 1993-2005 AVEVA AB
13 Structure
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
13.1 General
This section describes Tribon Vitesse for Structure. The purpose of Tribon Vitesse for Structure is to supply the customer with simple tools to create and handle Structures in an easyway. This tool, in combination with the Data Extraction interface, is very efficient for creating general Structures that are dependent on other model objects, as pipe or cableway hangers.
The production may also be supported by automatic assembly drawings made by Drafting Vitesse.
Vitesse for Structure contains functions in the following areas:
 Functions handling a Structure object.
 Functions handling a Structure part.
The functions in Vitesse for Structure are developed to be used in python programs, which are started from the Vitesse button on the application independent part of the applicationwindow in the structure, cable and pipe application. A specific License for this interface is checked out when any function in this interface is used. The functions are made available in a
Vitesse program by the insertion of the statement import kcs_struct. All functions are accessed by kcs_struct.<function name>. Before using a new function, please carefully
read the function description.
User's Guide Vitesse
```
Chapter: Structure
```
Copyright © 1993-2005 AVEVA AB
13.2 Exception Handling
The Vitesse Structure interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct ofthe Python language. The type of error can then be examined by checking the value of kcs_struct.error. The exception is also displayed in the Vitesse Log window which is
available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Structure
```
```
Example:
```
import kcs_struct
```
try:kcs_struct.struct_new("struct01", "mod01", "green")
```
```
except:
```
print kcs_struct.error
Copyright © 1993-2005 AVEVA AB
13.3 Classes
Some of the functions in Vitesse for Structure take objects as input. These objects are instances of Python Classes. The classes used in Vitesse for Structure are described in sectionGeneral.
User's Guide Vitesse
```
Chapter: Structure
```
Copyright © 1993-2005 AVEVA AB
13.4 Functions on Object Level
Structure Vitesse is using the same current handling system as the interactive application. This means that if the user has created a structure by vitesse and left it current, he maycontinue to model it interactively. This is the same for the Cable, Pipe and Structure modelling application.
User's Guide Vitesse
```
Chapter: Structure
```
```
struct_new (Structure, Module, Colour)
```
The function creates a new structure object. The module has to be initiated in the system. If a colour is used, not known by the system, the default green colour is chosen. If the functionis successful the structure will be current.
The colour may be defined either by using the class Tribon Colour or by a string. The colours are documented in Tribon M3 Drafting, Appendices, Colour Tables.
```
Parameters:
```
Structure String Name of the structure
Module String Name of module
Colour String/Tribon Colour Colour of structure
```
Result:
```
None
```
Exceptions:
```
kcs_NameError Invalid names.
kcs_ModuleError Module does not exist.
kcs_ModelFound The model is already locked for update.
kcs_ModelCurrent Another model is already current
```
struct_activate (Structure)
```
The function activates a structure object. If the function is successful the structure will be current.
```
Parameters:
```
Structure String Name of the structure
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelCurrent Another model is already current.
```
struct_delete (Structure)
```
The function deletes a structure object from databank. The function requires that no structure is current.
```
Parameters:
```
Structure String Name of the structure.
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotFound Invalid name, not found or locked.
kcs_ModelCurrent Another model is already current.
struct_cancel
The function cancels current structure object. The changed parts of the structure are not stored and the structure will not be current any more.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
struct_save
The function saves current structure. If the function is successful the structure will not be current any more. The test for restriction file or multiple defined position numbers are made byseparate functions.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
```
struct_name_get ()
```
The function returns the name of current structure object.
```
Parameters:
```
None
```
Result:
```
[0] String Name of current structure
```
Exceptions:
```
kcs_ModelNotCurrent No model is current.
```
struct_transform (T)
```
The function transforms current structure by using a transformation matrix.
```
Parameters:
```
T kcstransformation3D Transformation matrix.
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_MatrixInvalid The values in the matrix was invalid
```
struct_duplicate (Structure)
```
The function duplicates all parts from given structure into current. The structure, from which the parts are duplicated, is not affected by this function.
```
Parameters:
```
Structure String Name of structure to duplicate parts from. It is allowed to key in the name of current structure.
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_ModelNotFound Invalid name of structure to duplicate from,
not found or locked.
kcs_FunctionInvalid Not allowed function. Example standard
reference exist
```
struct_check_restrict ()
```
The function checks if the profile endcuts in current structure matches the hull profile restriction file SBH_PROF_RESTRICT . It is possible to check a specific part by using theprofile_check_restrict function.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_EndcutInvalid At least one endcut was invalid
```
struct_check_posno ()
```
The function checks if any position number is defined twice.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_PosnoDuplicate A position number was defined twice.
```
struct_marking_lines_on ()
```
The function sets the marking line on for current structure.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
```
struct_marking_lines_off ()
```
The function sets the marking line off for current structure.
```
Parameters:
```
None
```
Result:
```
None
Exceptions
kcs_ModelNotCurrent No structure was current
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
```
struct_assembly (Assembly)
```
The function assigns the whole current structure to an assembly.
```
Parameters:
```
Assembly String Assembly name, if empty the assembly reference will be removed.
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
kcs_AssemblyNotFound The assembly was not defined.
```
struct_split ()
```
The function transfers the structure to the production preparation environment. The structure is stored in databank but is still current after call. The structure is transferred to PDI ifapplicable.
```
Parameters:
```
None
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
kcs_SplitInvalid Databanks needed for split are not connected.
```
document_reference_get ()
```
The function returns a list of document references associated with the active structure.
Input parameters
None
Returned value:
[0] list List of DocumentReference instances
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active structure not set
kcs_GeneralError List of result can't be created for some internal reason
```
document_reference_add (docRef)
```
The function adds a document reference to the active structure object.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active structure not set
```
document_reference_remove (docRef)
```
The function removes document reference from active structure object. If there are more than one document reference, the first found will be deleted.
Input parameters
DocRef DocumentReference Instance of Python DocumentReference class
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active structure not set
kcs_DoesNotExist Equipment document reference doesn't exist
```
Example:
```
#Example: kcs_ex_struct_2.py
Copyright © 1993-2005 AVEVA AB
13.5 Functions on Part Level
These functions handle parts in 'current' structure. The modified parts are saved when the whole structure is saved.
```
Functions to handle profiles;
```
User's Guide Vitesse
```
Chapter: Structure
```
```
pseudoname_profile (Type, a, b, s, t, c, u)
```
The function creates the pseudo component name used for a profile. The different measures are documented for each profile type in the Tribon documentation. Measures not neededfor the specific type may be omitted. This function does not update the structure object.
```
Parameters:
```
Type String Type of profile.
a Real Measure in mm.
b Real Measure in mm.
s Real Measure in mm.
t Real Measure in mm.
c Real Measure in mm.
u Real Measure in mm.
```
Result:
```
[0] String The pseudo name.
```
Exceptions:
```
kcs_SyntaxInvalid The syntax is invalid
```
profile_new_2 point3D (Name, Start point, End point, Material vector)
```
The function adds a profile part in the current structure. If the function is successful, the id of the new part will be returned.
```
Parameters:
```
Name String The component or pseudo component name.
Start point point3D A 3D co-ordinate start point
End point point3D A 3D co-ordinate end point
Material vector vector3D A 3D vector defining the material direction
Result
[0] Integer Id of new part
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
kcs_ModelNotCurrent No structure was current
kcs_ComponentInvalid The component name was not valid
kcs_NoPart It was not possible to create a part
```
profile_endcut (Id, Point, Type, Param1, Param2,Param3,Param4, Param5, Param6)
```
The function adds an endcut to a profile part with a specific id in the current structure. Parameters not needed for the specific endcut type may be omitted
```
Parameters:
```
Id Integer Id of profile part to put endcut on
Point coord3D A 3D co-ordinate point defining the end of profile
Type Integer Type of endcut, see Tribon M3 Setup and Customisation.
Param1 Real Parameters to define the endcut
Param2 Real Parameters to define the endcut
Param3 Real Parameters to define the endcut
Param4 Real Parameters to define the endcut
Param5 Real Parameters to define the endcut
Param6 Real Parameters to define the endcut
```
Result:
```
None
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current.
kcs_PartNotFound The part was not found
kcs_EndcutInvalid The endcut was not predefined
```
pseudoname_plate (t)
```
The function creates the pseudo component name used for a plate. The function does not update the current structure object.
```
Parameters:
```
t Real Thickness in mm
```
Result:
```
[0] String The pseudo name
```
Exceptions:
```
kcs_SyntaxInvalid The syntax is invalid
```
plate_new_contour2D (Name, Origo, Material,Rotation,Contour)
```
The function adds a plate part in the current structure. The plate is defined by a 2D contour placed in the model co-ordinate system. If the function is successful, the id of the new partwill be returned.
```
Parameters:
```
Name String The component or pseudo component name.
```
Origo point3D A 3D co-ordinate point defining where the origo point (0,0) for the contour is placed in the model.
```
Material vector3D A 3D vector, perpendicular to the plate contour plane, defining material direction.
Rotation vector3D A 3D vector, defining the direction of the x -axis in the plate contour co-ordinate system.
Contour contour2D A 2 contour, defining the shape of the plate. The contour has to be closed.
```
Result:
```
[0] Integer Id of new part
Exceptions
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current.
kcs_ComponentInvalid The component name was not valid.
kcs_NoPart It was not possible to create a part.
```
pseudoname_hole (h,w,r)
```
The function creates the pseudo name used for a hole. The function does not update the current structure object.
Parameters
h Real Height of hole in mm
w Real Width of hole in mm, if omitted the width will be the same as height.
r Real Radius of corners in hole in mm.
If omitted the radius is 0.
```
Result:
```
[0] String The pseudo name.
```
Exceptions:
```
kcs_SyntaxInvalid The syntax is invalid
```
hole_new (comp_name, id, point, vector)hole_new (contour2D, id, point, vector)
```
```
hole_new (comp_name, id, point, vector, side)hole_new (contour2D, id, point, vector, side)
```
1. Create general hole in plate part.
2. Create general hole in structure plate part defined by contour2D.
3. Create general hole in profile part.
4. Create general hole in structure part (plate or profile) defined by contour2D.
Input Parameters:
Contour2D Contour2D Contour instance to be a boundary hole
Comp_named String A pseudo component name.
id Integer Id part of structure plate or profile.
```
point Point3D Origin point of hole (midpoint of hole).
```
vector Vector3D A 3D vector, defining the direction of height.
side Integer Parameter indicating Flange or Web.
0: hole is located in Web side of a profile
1: hole is located in Flange side of a profile
2: hole is located in opposite flange side of a profile in case of I-bar.
Returned value:
[] Integer. Id of hole.
```
Exceptions:
```
kcs_FunctionInvalid Invalid names.
kcs_PartNotFound The parts does not exists.
kcs_Contour Invalid Contour is invalid.
kcs_ModelNotCurrent A structure is not current.
```
Example:
```
#Example:kcs_ex_struct2.py
```
misc_comp_new (Name, Point, Route, Rotation)
```
The function adds a miscellaneous component part to the current structure. If the function is successful, the id of the part will be returned
```
Parameters:
```
Name String The component name.
Point point3D A 3D co-ordinate point defining where the plate is placed
Route vector3D A 3D vector, defining the route direction
Rotation vector3D A 3D vector, defining the rotation
```
Result:
```
[0] Integer Id of new part
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current
kcs_ComponentInvalid The component name was not valid
kcs_NoPart It was not possible to create a part
```
part_delete (ID)
```
The function deletes a part or hole in the current structure. The part may be a profile, plate with holes or a miscellaneous component
```
Parameters:
```
Id Integer Id of part to delete
```
Result:
```
None
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current
kcs_PartNotFound The part was not found
```
part_transform (id, T)
```
The function transforms a part in current structure. Holes may not be transformed as single parts.
```
Parameters:
```
Id Integer Id of part to delete
T kcstransformation3D
Transformation matrix
```
Result:
```
None
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current
kcs_MatrixInvalid The values in the matrix was invalid
kcs_PartNotFound The part was not found
```
part_duplicate (Structure, Id)
```
The function duplicates a parts from given structure into current. The structure, from which the parts are duplicated, is not affected by this call.
```
Parameters:
```
Structure String Name of structure to duplicate parts from
It is allowed to give the name of current structure.
Id Integer The id of part to duplicate
```
Result:
```
[0] Integer Id of new part
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_ModelNotFound Invalid name of structure to duplicate from, not found or locked.
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_PartNotFound The part was not found
```
Functions in the production information area;
```
```
profile_check_restrict (id)
```
The function checks if a specific profile's endcuts matches the hull profile restriction file SBH_PROF_RESTRICT . It is possible to check the whole structure with one function.
```
Parameters:
```
Id Integer Id of part to check
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_EndcutInvalid At least one endcut was invalid
kcs_PartNotFound The part was not found
```
part_posno (Id, Posno)
```
The function adds or exchanges a position number for a specific part. A specific function may be called to verify that the same position number not is defined twice. When settingposition number on a bent plate, use part id from any of the plate parts.
```
Parameters:
```
Id Integer Id of part to put position number on
Posno String Position number
```
Result:
```
None
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_ModelNotCurrent No structure was current
kcs_PartNotFound The part was not found
```
part_assembly (Id, Assembly)
```
The function assigns the part in current structure to an assembly.
```
Parameters:
```
Id Integer Id of part to put assembly reference on.
Assembly String Assembly name. The assembly reference will be removed if an empty string is used.
```
Result:
```
None
```
Exceptions:
```
kcs_ModelNotCurrent No structure was current
kcs_FunctionInvalid Not allowed function.
Example standard reference exist.
kcs_AssemblyNotFound The assembly was not defined.
kcs_PartNotFound The part was not found
```
plate_bent_new(id1, point1, id2, point2, radii)
```
The function creates a bent plate group in the current structure given the id's of two plates the bending radii and two points indicating the parts of the plates to keep. Both can belong toplate groups, but not to the same bent plate group.
Input Parameters:
Id1 Integer Id of first plate part to be a bent plate
Point1 Point3D Point3D indicating side of part to be kept and deciding the direction of fillet
Id2 Integer Id of second plate part to be a bent plate
point2 Point3D Point3D indicating side of part to be kept and deciding the direction of fillet
radii Real Radius of bent part
Returned value:
[0] Integer Id of bent plate group
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
kcs_ModelNotCurrent No structure was current.
kcs_NoPart It was not possible to create a bent plate group.
```
profile_new_contour2D(compName, contour, origo, normal, rotation)
```
The function adds a bent profile part in the current structure. The bent profile is defined by a 2D contour placed in the model co-ordinate system by means of an origo and an normaland rotation. If the function is successful, the id of the new part will be returned. Note that the direction of the material and flange is always to the left from the mould line in the direction
of the contour definition.
Input Parameters:
Name String The component or pseudo component name.
Contour2D Contour2D A 2D contour, defining the centre line of the profile.
```
Origo Point3D A 3D co-ordinate point defining the where the origo point (0,0) for the contour is placed in the model.
```
```
Normal Vector3D A 3D vector, defining the direction of the x-axis in the profile contour co-ordinate system.(The normal vector for the profile (perpendicular to theprofile))
```
Rotation Vector3D A 3D rotation vector for the contour
Returned value:
[0] Integer Id of new part
```
Exceptions:
```
kcs_FunctionInvalid Not allowed function. Example standard reference exist.
kcs_ModelNotCurrent No structure was current.
kcs_ArgumentError Part is not created, invalid data
kcs_ComponentInvalid Invalid component name.
```
Example:
```
```
Example: kcs_ex_struct_4.py
```
Copyright © 1993-2005 AVEVA AB
13.6 Functions for Standard Structures
This chapter describes functions to handle standard structures.
User's Guide Vitesse
```
Chapter: Structure
```
set_standard_origin
Function to set standard-origin point for structure.
Input parameters:
Origin as KcsPoint3D
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No model is current.
```
Example:
```
```
point = KcsPoint3D.Point3D(1000,200,300)
```
```
kcs_struct.set_standard_origin(point)
```
get_standard_origin
Function to get standard-origin point for structure.
Input parameters:
Point as KcsPoint3D
Returned value:
Origin Point as KcsPoint3D
```
Exceptions:
```
kcs_NoModelIsCurrent No model is current.
```
Example:
```
```
point = KcsPoint3D.Point3D()
```
```
kcs_struct.get_standard_origin(point)
```
set_standard_desc
Function to set description about standard structure.
Input parameter:
Description as String
Returned value:
None.
```
Exceptions:
```
kcs_NoModelIsCurrent No model is current.
```
Example:
```
```
desc = "my standard struct"
```
```
kcs_struct.set_standard_desc(desc)
```
get_standard_desc
Function to get description about standard structure.
Input parameter:
None.
Returned value:
Description as String
```
Exceptions:
```
kcs_NoModelIsCurrent No model is current.
```
Example:
```
```
s = kcs_struct.get_standard_desc()
```
```
standard_input (StdName, NewMod, NewName, PlacePoint)
```
Function to create a structure from a standrad structure object. Now the user can also give a placing point.
Input Parameters:
StdName String Name of standard structure.
NewMod String Name of new module.
NewName String Name of new structure.
PlacePoint KcsPoint3D Point where the new structure should be placed. This parameter is optional.
Returned value:
None.
```
Exceptions:
```
kcs_NameInvalid Invalid names.
kcs_StandardModelNotFound The standard model was not found.
kcs_ItemAlreadyExist. The structure does already exist.
kcs_ModelIsCurrent Another model is already current.
```
Example:
```
```
placePoint = KcsPoint3D.Point3D(1000, 2000, 1000)
```
#input standard structure UNISTD3 as UNIDEL3 at placePoint
```
kcs_struct.standard_input("UNISTD3","TEST","UNIDEL3",point);
```
```
standard_output (name, stdname)
```
Save structure as standard structure.
Input Parameters:
name String Name of structure model to be a standard structure.
stdname String Name of standard structure.
Returned value:
None.
```
Exceptions:
```
kcs_NameError Invalid names.
kcs_StandardModelExists The standard structure already exists.
kcs_ModelCurrent Another model is already exists.
kcs_ModelNotFound Module not found.
```
standard_replace (name, stdname)
```
Save structure as standard structure.
Input Parameters:
name String Name of structure model to be a standard structure.
stdname String Name of standard structure.
Returned value:
None.
```
Exceptions:
```
kcs_Error Invalid names.
kcs_StdModelNotFound The standard structure does not exists.
```
Example:
```
#Example: kcs_ex_struct2.py
Copyright © 1993-2005 AVEVA AB
13.7 Functions for Structure Reference
This chapter describes functions to handle structure reference.
User's Guide Vitesse
```
Chapter: Structure
```
```
struct_cway_connect (cway name, part_id, point, struct name)
```
A reference to the structure will be created. The height and width is used for fill level check. The structure has to exist when the reference is set.
Input Parameters:
Cway name String Name of cableway
Id Integer Id of part to which the structure refers. O means any part.
Point Point3D Point to place the structure reference.
Struct Name String Name of new structure.
Returned value:
None.
```
Exceptions:
```
kcs_ModelIsCurrent The structure or cableway is current.
kcs_ModelNotFound The structure was not found.
kcs_ReferenceNotFound The cableway not found.
kcs_ReferenceInvalid Connection not could be done or already exist.
```
Struct_cway_disconnect (cway name, structure name)
```
The reference to the structure will be removed
Input Parameters:
Cway Name String Name of cableway
structure name String Name of structure.
Returned value:
None.
```
Exceptions:
```
kcs_ModelIsCurrent The structure or cableway is current.
kcs_ModelNotFound The structure was not found.
kcs_ReferenceNotFound The cableway not found.
kcs_ReferenceInvalid Connection not could be done or already exist.
```
struct_cway_data (node, route, rotation, length, width, height)
```
The cableway data for current structure is updated.
Input Parameters:
Node Coord3D Coordinate for node point for cableway material.
Route Vector3D Vector used to define the route direction for cway part
Rotation Vector3D Vector used to define the rotation of material.
Length Real The length of cableway part to be occupied by this material.
Width Real Cross section measure used for fill level check.
Height Real Cross section measure used for fill level check.
Returned value:
None.
```
Exceptions:
```
kcs_ModelNotCurrent The cableway was not current.
```
Example:
```
#Example: kcs_ex_cway_08.py
Copyright © 1993-2005 AVEVA AB
13.8 Examples
The Structure Vitesse Interface could be used in many applications such as:
Structures made by subcontractor could easily be modelled by Vitesse if the construction was delivered as data on file, to be read by a vitesse program.
Pipe hangers, cableway hangers, stairs, railings and engine foundations can be generated automatically by writing Vitesse programs.
 Indicate the model objects.
 Fetch data by Data Extraction.
 Calculate the geometry by the using the Geometry classes.
 Create the structure using Vitesse.
The following example is enclosed in the normally delivery of Tribon Structure Vitesse called kcs_ex_struct1.py. It is a simple example of creating a structure from user input, the examplecan be found by following this link:
struct1_example.txt
User's Guide Vitesse
```
Chapter: Structure
```
Copyright © 1993-2005 AVEVA AB
14 Weld
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
14.1 General
Vitesse features access to the functionality in Weld Planning. For more information, see Tribon M3 Weld Planning.
The interface has the following features:
 function to perform a weld calculation and create a weld table
 function to get the calculation result
 functions to change some data in an existing weld table
 function to delete an existing weld table
The functions are made available in the Python program by the insertion of the statement import kcs_weld. The functions are then referred to as kcs_weld.<function name>. Before usinga new function, please carefully read the function description.
User's Guide Vitesse
```
Chapter: Weld
```
Copyright © 1993-2005 AVEVA AB
14.2 Exception Handling
The Vitesse Weld interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct of thePython language. The type of error can then be examined by checking the value of kcs_weld.error. The exception is also displayed in the Vitesse Log window which is available by the
Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Weld
```
Copyright © 1993-2005 AVEVA AB
14.3 Weld Planning Functions
These functions handle functionality within Tribon Vitesse that deals with weld planning calculations. The functions are made available in a Vitesse program by the insertion of thestatement "import kcs_weld".
User's Guide Vitesse
```
Chapter: Weld
```
```
weld_calculation(assembly_name,recursive)
```
Starts the weld detection for the given assembly, and optionally also for all its sub-assemblies.
Input parameters:
assembly_name string Path name of the assembly
recursive integer 0 = only the given assembly
1 = include all sub-assemblies
Returned value:
0 Error in weld calculation
1 Weld calculation OK
```
Exceptions:
```
kcs_ModelNotFound Assembly not found
kcs_Error General error
```
weld_properties_get(assembly_name, weld_table)
```
Returns the result of the weld detection.
Input parameters:
assembly_name string Path name of the assembly
Output parameters:
weld_table WeldTable Instance of KcsWeldTable.WeldTable class
Returned value:
[0] integer 1 = Success
```
Exceptions:
```
kcs_AssemblyNotFound Assembly not found
kcs_PythonMethodNotFound Python method not found. Check your KcsWeldTable implementation file.
kcs_ArgumentError Invalid arguments list.
```
weld_properties_set(assembly_name, weld_table)
```
Updates an existing weld table.
Input parameters:
assembly_name Path name of the assembly
Weld_table Instance of KcsWeldTable.WeldTable
Returned value:
0 Error updating weld table
1 OK
```
Exceptions:
```
kcs_ModelNotFound Assembly not found
```
weld_delete(assembly_name)
```
Deletes the weld table object on data bank
Input parameters:
assembly_name Path name of the assembly
Returned value:
0 Error deleting weld table
1 OK
```
Exceptions:
```
kcs_ModelNotFound Assembly not found
kcs_Error General error
Copyright © 1993-2005 AVEVA AB
15 Model Handling
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
15.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_model. The functions are then referred to as kcs_model.<function name>. Beforeusing a new function, please carefully read the function description.
The Vitesse Common Model interface contains functions for:
 Retrieving information about hull panels in contact with specified equipment or structure item.
User's Guide Vitesse
```
Chapter: Model Handling
```
Copyright © 1993-2005 AVEVA AB
15.2 Exception Handling
The Model Common Handling interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except"construct of the Python language. The type of error can then be examined by checking the value of kcs_model.error. The exception is also displayed in the Vitesse Log window which
is available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Model Handling
```
Copyright © 1993-2005 AVEVA AB
15.3 Functions
User's Guide Vitesse
```
Chapter: Model Handling
```
```
model_hull_contact (Model)
```
The Vitesse API function model_hull_contact extracts the hull panel objects touched by given structure or given equipment objects. The current drawing serves as a basis for the set ofhull panels examined. Adjacent objects not separated with respect to their extensions define the implication of touched. Returned from model_hull_contact API is a list of objects
defined by the KcsModel class.
Input Parameters:
Model Model The model. Valid model types are: "equipment", "struct", "pipe", "ventilation" and "cable".
Returned Value:
```
Model(s) List of KcsModel List of hull models found.
```
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error. View can't be created
```
Example:
```
# Example: kcs_ex_model01.py
```
model_hull_interference_check (Model, Type, Range )
```
For a specified hull model, this function returns list of touched outfitting models of given type. The touch check is done with a specified tolerance.
Input Parameters:
Model Instance of KcsModel The hull model.
Type string The type of outfitting models to check for. Valid types are: "equipment", "struct", "pipe", "ventilation" and "cable"
Range float Distance from "Model" which is accepted by touch check.
Returned Value:
```
Model(s) List of KcsModels List of touched outfitting models.
```
```
Exceptions:
```
kcs_ValueError Invalid parameter value.
kcs_DrawingNotCurrent No drawing was current.
kcs_Error General error. View can't be created
```
Example:
```
# Example: kcs_ex_model05.py
```
model_properties_set (model, properties)
```
The function sets parameters of a model object.
Input parameters
Model Model KcsModel.Model
Properties CommonProperties KcsCommonProperties.CommonProperties
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid arguments list
kcs_NoModelCurrent Active structure not set
kcs_NameInvalid Object not exist or not current. Object will be not current for penetration and hull object.
```
model_status_set(Model, StatusType, StatusValue)
```
The function changes status for given model.
Input Parameters:
Model Model Instance of KcsModel.Model class.
StatusType constant Status type. It can be defined by using constants defined in kcs_model module:
 kcsSTATTYPE_DESIGN
 kcsSTATTYPE_MANUFACTURING
 kcsSTATTYPE_ASSEMBLY
 kcsSTATTYPE_MATERIAL_CONTROL
```
StatusValue integer New status value. To get all possible values use kcs_model.status_values_get() function.
```
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Argument error.
kcs_ValueError Argument value not valid.
kcs_FunctionNotSupported Function not supported. Tribon Data Management not enabled.
kcs_CouldNotChangeStatus It is not possible to change status. Probably you don't have permission to do this.
```
status_values_get(StatusType)
```
The function returns possible status values for given status type.
Input Parameters:
StatusType constant Status type. It can be defined by using constants defined in kcs_model module:
 kcsSTATTYPE_DESIGN
 kcsSTATTYPE_MANUFACTURING
 kcsSTATTYPE_ASSEMBLY
 kcsSTATTYPE_MATERIAL_CONTROL
Returned value:
[0] dictionary Dictionary containing pairs: status value : status value string
```
Exceptions:
```
kcs_ArgumentError Argument error.
kcs_ValueError Argument value not valid.
kcs_FunctionNotSupported Function not supported. Tribon Data Management not enabled.
```
tdm_strings_get (StatusType)
```
The function returns either the Planning Units or Cost Codes as specified by the user.
Input Parameters:
StatusType integer = 1 for getting Planning Units
= 0 for getting Cost Codes
Returned value:
[0] tuple python tuple containing either Planning Units or Cost Codes
```
Exceptions:
```
kcs_ArgumentError Argument error.
kcs_ValueError Argument value not valid.
Copyright © 1993-2005 AVEVA AB
16 Model Structures
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
16.1 General
The functions are made available in the Python program by the insertion of the statement import kcs_modelstruct. The functions are then referred to as kcs_modelstruct.<functionname>. Before using a new function, please carefully read the function description.
The Vitesse Model Structures interface contains functions for:
 Creating and Deleting Hull blocks
 Creating and Deleting Outfit Systems.
 Creating and Deleting Outfit Modules.
User's Guide Vitesse
```
Chapter: Model Structures
```
Copyright © 1993-2005 AVEVA AB
16.2 Exception Handling
The Model Structures interface uses exception handling. This means that if a run time error occurs an exception is set. The exception can be caught using the "try - except" construct ofthe Python language. The type of error can then be examined by checking the value of kcs_modelstruct.error. The exception is also displayed in the Vitesse Log window which is
available by the Vitesse Log Window command and can optionally be written to the log file. The meaning of the exception can be found in the description of the corresponding function.
The default error is kcs_Error. If no specific exception occurs, this error is set. Note that the kcs_Error exception is a general exception and will not be further described below.
User's Guide Vitesse
```
Chapter: Model Structures
```
Copyright © 1993-2005 AVEVA AB
16.3 Functions
User's Guide Vitesse
```
Chapter: Model Structures
```
```
block_new(name, MinPt3d, MaxPt3d)
```
The function creates new hull block.
Input Parameters:
name string Name of hull block
MinPt3d Point3D Lower left corner of extension box.
MaxPt3d Point3D Upper right corner of extension box
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_ValueError Argument value is not valid.
kcs_NameInvalid Block name is not valid. For example: empty name.
kcs_NameTooLong Block name is too long. Max. 25 characters.
kcs_NameOccupied Block name is already in use.
kcs_Error General error. Block can not be created.
```
block_delete(name)
```
The function deletes existing hull block.
Input Parameters:
name string Name of hull block
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DoesNotExist Specified block does not exist.
kcs_Error General error. Block can not be deleted.
```
system_new(name, description, <SurfPrepCode>)
```
The function creates new system.
Input Parameters:
name string Name of new system.
description string Description for new system.
SurfPrepCode integer Surface preparation code. This parameter is optional.
Default value is -1.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_NameInvalid System name is invalid. For example: empty system name.
kcs_NameTooLong System name is too long. Max. 25 characters.
kcs_NameOccupied System name is already in use.
kcs_Error General error. System can not be created.
```
system_delete(name)
```
The function deletes existing system.
Input Parameters:
name string Name of system
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DoesNotExist Specified system does not exist.
kcs_NameTooLong Name of specified system is too long. Max. 25 characters.
kcs_ObjectNotEmpty Specified system is not empty. It can't be delete.
kcs_NameInvalid System name is invalid. For example: empty system name.
kcs_Error General error. System can not be deleted.
```
module_new(name)
```
The function creates new module.
Input Parameters:
name string Name of new module.
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_NameInvalid Module name is invalid. For example: empty module name.
kcs_NameTooLong Module name is too long. Max. 25 characters.
kcs_NameOccupied Module name is already in use.
kcs_Error General error. Module can not be created.
```
module_delete(name)
```
The function deletes existing module.
Input Parameters:
name string Name of module
Returned value:
None
```
Exceptions:
```
kcs_ArgumentError Invalid parameter type.
kcs_DoesNotExist Specified module does not exist.
kcs_NameTooLong Name of specified module is too long. Max. 25 characters.
kcs_ObjectNotEmpty Specified module is not empty. It can't be delete.
kcs_NameInvalid System module is invalid. For example: empty name.
kcs_Error General error. Module can not be deleted.
Example
# Example: kcs_ex_modelstruct01.py
Copyright © 1993-2005 AVEVA AB
17 The Tribon Geometry Macro Facility
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
17.1 General
The Tribon Geometry Macro Facility is a program used to create predefined geometry. The main purpose of using geometry macros in Tribon M3 is to create design standards. Exampleof such standards are profile cutouts in Tribon Hull and ventilation volumes in Tribon Ventilation.
```
Note: Previous versions of Tribon further allowed any user to define geometry macros creating drawings and sub-pictures. However, this is in Tribon M3 no longer supported. InsteadTribon Vitesse functions for Drafting should be used.
```
The geometry is put into the current drawing or volume.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.2 Introduction
In interactive Tribon applications, 2D drawings are built up by different interactive functions of the applications. Similarly, 3D figures can be created by the combination of volumeprimitives. These operations normally work on entity level, i.e. by the addition of lines, arcs, texts, etc. or by the duplication of information of the drawing.
However, in many situations the drawing or volume to be created is parenthesized, i.e. controlled by a relatively small number of parameters and/or conditions.
The Tribon Geometry Macro Facility has been developed as a tool to create such drawings/volumes by defining a number of parameters in calls of geometry macros.
A geometry macro is written as a text in a format like a programming language.
The elements of the language are:
 the geometrical entities that can be created
 "program logic", like branching and loops
 basic arithmetics, logical and trigonometrical operations
Details about all these things can be found below.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3 Functions
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.1 Entities of the Geometry Macro
A geometry macro used for a drawing or a sub-picture may generate the following entities:
 point
 vector
 line
 arc
 circle
 contour
 spline
 symbol
 text
 text file
 layer
 line type
 attribute
 note
 hatch pattern
A geometry macro used for volumes may generate the following entities:
 point
 vector
 parallelepiped
 cylinder
 cone
 spherical segment
 general cylinder
 toroid
 polygon
 rotational primitive
 attribute
One geometry macro can define either a 2D drawing/sub-picture or a 3D volume. However, some of the volume primitives use 2D entities as parameters.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.2 Additional Functions
The following functions can be used in any macro:
 assign
 colour
 branching: if..
.
.
.
else
.
.
.
endif
 loop
 conditional loop: while..
.
.
.
endwhile
```
 table (formatted output)
```
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.3 Operators and System Functions
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
AND logical and
- add
- change sign
& concatenate strings
% division
** exponentiation
== qual
> greater than
greater equal
< less than
less equal
- multiplication
NOT logical not
... not equal
OR logical or
- subtraction
XOR logical exclusive or
AB absolute value
```
ACO arcus cosine (radians)
```
```
ACOSD arcus cosine (degrees)
```
```
ASIN arcus sine (radians)
```
```
ASIND arcus sine (degrees)
```
```
ATAND arcus tangent (radians)
```
```
ATAND arcus tangent (degrees)
```
BYTE character whose ASCII code is the argument of BYTE
```
COS cosine (radians)
```
```
COSD cosine (degrees)
```
DEGREE angle in degrees to angle in radians
```
SIN sine (radians)
```
```
SIND sine (degrees)
```
SQRT square root
```
TAN tangent (radians)
```
```
TAND tangent (degrees)
```
SUBSTR substrings
LENGTH length of a string
INDEX position of a specified sub-string within a string
NRCHAR number of character with specified number of decimals
Copyright © 1993-2005 AVEVA AB
17.3.4 Creation of a Geometry Macro
The geometry macro is created by writing a geometry macro source text in a special macro language. This language is similar to other languages used for input to various Tribonapplications. The syntax of the Tribon Geometry Macro Language is given in Syntax of Tribon Geometry Macro Language. The source text is stored in an ordinary text file with an
```
arbitrary name (= the name of the macro). It can thus be created using an ordinary editor. Only capital letters, digits and _ (underscore) are allowed characters in the macro and file name.
```
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.5 Execution of a Geometry Macro
The geometry macro can be executed either from Tribon Drafting or as a stand alone program. The following is valid for both cases.
```
The first time the macro is to be executed, the file name must be given, including the file type. It is assumed that the geometry macro is stored on the directory given by the logicalvariable SBB_GEO_MACRO_SRC. The interpreter will then check the syntax of the macro in the source file (the macro is "compiled").
```
The result of the interpretation is given in a list file containing a list of the syntax together with possible error messages. The name of the list file is <source_file>.LST and the list file
will be created on the directory given by the logical variable SBB_GEO_MACRO_LST.
If the interpretation was successful, a "compiled" version of the syntax will be stored on a directory given by the logical variable SBB_GEO_MACRO_BIN. The name of the "compiled"version of the syntax is <source_file>.GLB. At the subsequent executions of the geometry macro, it is sufficient to give the macro name and the "compiled" version will be read, after
which the execution will start.
Note, the following paragraph is only valid when a project is shared between Windows and UNIX/VMS.
```
In case that the Tribon Geometry Macro is used in a project that is shared between platforms, and the project is located on a UNIX or VMS machine, the file handling differs a bit fromwhat is described above. The list file emanating from a compilation on Windows (<source_file>.LST) will be placed in the directory indicated by the operating system environment
```
```
variable TEMP, e.g. c:\Temp. Since the compiled format differs between platforms, it is necessary to have the compiled files (<source_file>.GLB) stored on each platform
```
respectively. This also means that the macros have to be compiled once on each platform. The logical variable SBB_GEO_MACRO_BIN_NT is used to indicate the directory used forcompiled binary files on the Windows platform. Note that the source files are still fetched from the directory indicated by SBB_GEO_MACRO_SRC, even if that is on another platform. If
you do not share projects, that is, you run only on the Windows platform, you do not have to set the variable SBB_GEO_MACRO_BIN_NT, and the compiled files will end up in thedirectory SBB_GEO_MACRO_BIN.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Stand Alone Program
If the Geometry Macro is run as a stand alone program, the result can be presented in a number of different ways. The following activities are available:
1. Print on terminal
2. Create 2D geometry and store on data bank
3. Create 3D volume model and store on data bank
4. Create 3D volume model + picture and store on data bank
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.6 Parameters of a Geometry Macro
The geometry macro can be parameterised, i.e. some parameters are given values at the time of execution. A parameter can be an integer number, a decimal number, a text string or a2D or 3D position in the drawing/volume. It is possible to define a command string to each parameter. This string will be displayed at the workstation and the operator is prompted to give
the parameter value.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Submacros in a Geometry Macro
```
It is possible to call another geometry macro (submacro) from any macro. Data is transferred from the macro to the submacro by parameters. These parameters can have any type.
```
The submacro parameters will be assigned the values of the corresponding macro parameters and the submacro will be executed. When the submacro execution is finished the macroparameters will be assigned the values of the corresponding submacro parameters and the execution of the macro is continued. See also The Facility of Using Conditional Statements in
a Macro.
The macro and the submacro can be the same macro so the resulting macro is recursive. See also The Possibility to Write Recursive Geometry Macros.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.7 Error Handling
During the execution of a geometry macro, an error handling system is active so that abortions of Tribon Drafting due to macro programming errors will be prevented.
The programmer has the possibility to list any data at the workstation during execution. This will make it easier to detect any errors in the macro programming.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.3.8 Execution in Batch
It is possible to execute a geometry macro in batch. All input to the macro must then be available in an ordinary text file and in exactly the same order as they are required by the macro.
The first parameter in the file must then be the activity and the second one the name of the macro.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4 Appendices
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.1 Syntax of Tribon Geometry Macro Language
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Conventions Used in this Document
```
In this document the following conventions are used (cf. "The Tribon Interpretative Language"):
```
[ ]optional
< >term
....preceding expression may be repeated
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Statement Types
The input language contains the following different statement types:
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
ARC The ARC statement defines a 2D arc. The arc can be used as input to the PRESENT and CONTOUR statements.
ASSIGN The ASSIGN statement assigns a previously defined variable to another variable which will get the same type as the first one. However, if a 2D or a 3D point has
been defined, one of these coordinates can be assigned to a variable with type decimal.
ATTRIBUTE The ATTRIBUTE statement is used to put attributes in the object. The attributes contain non-geometrical data and it is possible to store 100 integers, 50 reals and
12 strings. Both attribute numbers and the variables can be addressed with an alias name defined in an alias file assigned to the logical variable SBD_ALIAS.
CALL The CALL statement is used to call another macro. The parameter types must match and the parameters can be used for either input or output purposes. There is
no limit for the number of levels of submacros.
CHANGEDRAW The CHANGEDRAW statement is used to change the appearance of an object, a component or a subcomponent. This can be done either in one view or in all views.
CIRCLE The CIRCLE statement defines a 2D circle. The circle can be used as input to the PRESENT statement.
COLOUR The COLOUR statement sets the modal colour. Default colour is green. If the given colour is an empty string, the background colour will be used.
CONE The CONE statement defines a 3D cone. The cone can be used as input to the PRESENT statement.
CONNECTIONPOINT The CONNECTIONPOINT statement defines a 3D connection point. The connection point can be used as input to the PRESENT statement.
CONTOUR The CONTOUR statement defines a 2D contour. The contour can be used as input to the GENERALCYLINDER and PRESENT statements.
CURRENT The CURRENT statement makes it possible to structure a drawing or a volume.
CYLINDER The CYLINDER statement defines a 3D cylinder. The cylinder can be used as input to the PRESENT statement.
DECLARE The DECLARE statement allows the user to specify the type of any variable. The default type is DECIMAL. The DECLARE statements must be given directly after
the MACRO statement.
DELAY The DELAY statement makes it possible to introduce a delay in a macro. It has only an effect when geometry is presented at a workstation.
DISTANCE The DISTANCE statement assigns a value or a previously defined variable to another variable. The value is scaled with the current scale.
DRAWING_NAME The DRAWING_NAME statement assigns the name of the current drawing to it's parameter.
ELSE The ELSE statement must be used together with the IF statement. If the condition given in the IF statement is not fulfilled, then the statements after the ELSE
statement will be executed.
ENDIF The ENDIF statement terminates the IF statement.
ENDLOOP The ENDLOOP statement terminates the LOOP statement.
ENDMACRO The ENDMACRO statement terminates the MACRO statement.
ENDWHILE The ENDWHILE statement terminates the WHILE statement.
EXTRACTION The EXTRACTION statement makes it possible to use Data Extraction to get any data item of a stored Tribon object. This statement is optional.
GENERALCYLINDER The GENERALCYLINDER statement defines a 3D general cylinder. The general cylinder can be used as input to the PRESENT statement.
GET The GET statement enables the user to get a number of variables which will be used as parameters.
HATCH The HATCH statement defines a hatch pattern in a drawing. User defined patterns can be created. The hatch pattern may include islands. The hatch pattern is
used as input to the PRESENT statement.
IF The IF statement tests an expression and performs a specified action if the result of the test is true. All statements between the IF and ENDIF statements will be
executed. If the expression is false, no action will be taken unless the ELSE statement is given. In this case, all statements between the ELSE and ENDIF
statements will be executed. All statements except the MACRO and ENDMACRO statements can be given after the IF statement. The IF statements can be nested.
LAYER The LAYER statement sets the modal layer. The default layer is 0. The layer can be given either as a number or as an alias if an alias file exists. The aliases
should be defined in a file assigned to the logical variable SB_LAYER_ALIAS. In this case, geometry, text and symbols will get the same modal layer. To give
them different layer values, it is possible to use layer classes. The classes are defined in a file assigned to the logical variable SBD_LAYER_CLASS.
LINE The LINE statement defines a 2D line. The line can be used as input to the CONTOUR and PRESENT statements.
LINETYPE The LINETYPE statement sets the modal line type. Default line type is solid. The width can also be changed. Default line width is thin.
LOOP The LOOP statement makes it possible to execute the same statements a number of times. All statements except the MACRO and ENDMACRO statements can be
given after the LOOP statement. The LOOP statements can be nested.
MACRO The MACRO statement must be the first statement in the macro. Parameters may be given and, in that case, they will be given values before the execution of the
macro.
NAME The NAME statement is used to define a name on the drawing/ subpicture/volume to be created and stored on a data bank. If the statement is omitted, the macro
name will be used. It is also possible to give the form to be used, if any. If the form is omitted, a drawing will be created with no form. The scale can also be givenfor drawings and subpictures.
NOTE The NOTE statement defines a note in a drawing. The note is used as input to the PRESENT statement.
PARALLELEPIPED The PARALLELEPIPED statement defines a 3D parallelepiped. The parallelepiped can be used as input to the PRESENT statement.
POINT_2D The POINT_2D statement defines a 2D point. The point is used as input to several of the other 2D statements. It is also possible to use this statement when any
of the coordinates are to be changed.
POINT_3D The POINT_3D statement defines a 3D point. The point is used as input to several of the other 3D statements. It is also possible to use this statement when any
of the coordinates are to be changed.
POLYGON The POLYGON statement defines a 3D polygon. The polygon is used as input to the PRESENT statement.
PRESENT The PRESENT statement presents the geometry created by the macro.
PUT The PUT statement makes it possible to print any variable data.
RANGE The RANGE statement defines a range of variables. The range is used in the EXTRACTION and the LOOP statements.
ROTATIONAL The ROTATIONAL statement defines a 3D rotational primitive. The rotational primitive is used as input to the PRESENT statement.
SPHERESEG The SPHERESEG statement defines a 3D spherical segment. The segment is used as input to the PRESENT statement.
SPLINE The SPLINE statement defines a 2D spline. The spline is used as input to the CONTOUR and PRESENT statements.
SPLIT The SPLIT statement splits a model name into project, module and subsystems. These items can then be used in the EXTRACT statement.
SYMBOL The SYMBOL statement defines a symbol. The symbol is used as input to the PRESENT statement.
TABLE The TABLE statement makes it possible to present a number of variables with a format determined by the user. The table is used in the PRESENT statement.
TEXT The TEXT statement defines a text. The text is used as input to the PRESENT statement.
TEXTFILE The TEXTFILE statement defines a text file. The text file is used as input to the PRESENT statement.
TOROID The TOROID statement defines a 3D toroid. The toroid is used as input to the PRESENT statement.
VECTOR_2D The VECTOR_2D statement defines a 2D vector. The vector is used as input to other 2D statements. It is also possible to use this statement when any of the
coordinates shall be changed.
VECTOR_3D The VECTOR_3D statement defines a 3D vector. The vector is used as input to several of the other 3D statements. It is also possible to use this statement when
any of the coordinates are to be changed.
VMSJOB The VMSJOB statement is used to execute a job code or command VMS-file.
WHILE The WHILE statement makes it possible to execute the same statements a number of times. The WHILE statement tests an expression and performs a specified
action as long as the result of the test is true. All statements between the WHILE and ENDWHILE statements will be executed. If the expression is false, no action
will be taken. All statements except the MACRO and ENDMACRO statements can be given after the WHILE statement. The WHILE statements can be nested.
Copyright © 1993-2005 AVEVA AB
Statement Syntax
Below, the complete syntax of each statement type is described.
The ARC Statement
ARC,<arc_name>,<start_pnt>
```
[/ARCMIDPNT=(<mid_pnt>,<end_pnt>)]
```
```
[/ARCRADIUS=(<end_pnt>,<rad>)]
```
```
[/ARCAMPLITUDE=(<end_pnt>,<ampl>)];
```
<arc_name> is the name of the arc and will be assigned the type ARC_2D. The maximum length of <arc_name> is 32 characters.
<start_pnt> is the starting point of the arc with type POINT_2D.
```
ARCMIDPNT=(<mid_pnt>,<end_pnt>)
```
<mid_pnt> is the mid point of the arc when the arc is defined by giving three points. It has the type POINT_2D.
<end_pnt> is the ending point of the arc with type POINT_2D.
```
ARCRADIUS=(<end_pnt>,<rad>)
```
<end_pnt> is the ending point of the arc with type POINT_2D.
<rad> is the arc radius when the arc is defined by giving two points + radius. It has the type DECIMAL.
```
ARCAMPLITUDE=(<end_pnt>,<ampl>)
```
<end_pnt> is the ending point of the arc with type POINT_2D.
<ampl> is the arc amplitude when the arc is defined by giving two points + amplitude. It has the type DECIMAL.
```
Structure:
```
The ASSIGN Statement
ASSIGN,<variable_1>,<variable_2>
[/XCOORD]
[/YCOORD]
```
[/ZCOORD];
```
<variable_1> is assigned the same value as <variable_2> and will get the same type as the first one. The maximum length of <variable_1> and <variable_2> is 32
characters. <variable_2> can be an expression or have any of the following types:
INTEGER
DECIMAL
STRING
POINT_2D
LINE_2D
ARC_2D
CONTOUR_2D
CIRCLE_2D
VECTOR_2D
SPLINE_2D
TEXTFILE_2D
TEXT_2D
SYMBOL_2D
NOTE_2D
HATCH_2D
EXTRACT
RANGE
TABLE
POINT_3D
VECTOR_3D
CONNECTIONPOINT_3D
CONE_3D
CYLINDER_3D
GENERALCYLINDER_3D
PARALLELEPIPED_3D
POLYGON_3D
SPHERESEG_3D
TOROID_3D
ROTATIONAL_3D
XCOORD
If <variable2> is of type POINT_2D or POINT_3D, then <variable1> can be assigned the x coordinate of <variable2>. This variable will get type DECIMAL.
YCOORD
If <variable2> is of type POINT_2D or POINT_3D, then <variable1> can be assigned the y coordinate of <variable2>. This variable will get type DECIMAL.
ZCOORD
If <variable2> is of type POINT_3D, then <variable1> can be assigned the z coordinate of <variable2>. This variable will get type DECIMAL.
The ATTRIBUTE Statement
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(N,<arc_name>,'NSEG')
```
```
/STRUCTURE=(X,<arc_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<arc_name>,'AMPLITUDE',2,'Y');
```
ATTRIBUTE,<attr_no>
```
/ATTRDATA=(<variable>,<attribute>)....;
```
```
<attr_no> is the attribute number (> 0) and must be given within ' ' if it is addressed with an alias name. If <attr_no> is a true number or a variable, it shall not be given within ' '.
```
The maximum length of <attr_no> as an alias is 26 characters and as a variable 32 characters.
```
ATTRDATA=(<variable>,<attribute>)....
```
<variable> is the variable name given as an alias or using the default names. These are I1 - I100 for the integers, R1 - R50 for the reals and S1 - S12 for the strings.
<variable> shall always be given within ' '. The maximum length of <variable> as an alias is 26 characters and as a variable 32 characters.
```
<attribute> is the data to be stored in the attribute as an integer, real or string (max 26 characters). <attribute> must be given within ' ' if it is a string but not if it is a true
```
number or a variable. The maximum length of <attribute> as a variable is 32 characters.
The CALL Statement
CALL,<macro_name>
```
[,<arg_1>[,<arg_2>....[,<arg_25>]....]];
```
<macro_name> is the name of the submacro. The maximum length of <macro_name> is 32 characters. Only upper case letters and _ are allowed characters.
<arg_1>,<arg_2>, ....,<arg_25> are the arguments to the submacro. They cannot be expressions but must be variables. Any type is allowed. It is important to notice that if
a parameter in the submacro is changed, the corresponding argument in the calling macro will also be changed. Thus, it is of great advantage if an argument is used for either inputor output.
The CHANGEDRAW Statement
CHANGEDRAW,<obj_type>,<obj_name>
```
/COMPID=(<comp_id>)
```
```
/MARKINGCOLOUR=(<marking_colour>)
```
```
/SUBCOMPID=(<subcomp_id>)
```
```
/VIEW=(<view_id>);
```
<obj_type> is a keyword describing the type of the object. The following keywords exist:
PANEL plane and curved panel objects
CWAY cableway object
CABLE cable objects
EQUIP equipment objeACT
The object type must be a STRING constant.
<obj_name> is the name of the object to be changed, and has the type STRING.
<comp_id> is the id of a component of the type INTEGER, and is only used in the case of changing a single component.
<marking_colour> is the new colour of the object. It has the type STRING. The maximum length of <marking_colour> is 32 characters. If DEFAULT is assigned as
<marking_colour>, the geometry will be redrawn in the default colour. In a modelling view the default colour is determined by the model and in a diagram view the default colour
is determined by the General Diagram default file and, if applicable, pipe specification.
See Tribon M3 Drafting_Appendices for valid Tribon colours
<subcomp_id> is used in the same manner as <comp_id>, but for subcomponents. It has the type INTEGER.
<view_id> is the id of the view in which to change the object, and has the type INTEGER. If not given, the appearance of the object is changed in all views of the current drawing.
The CIRCLE Statement
```
CIRCLE,<circ_name>,<circ_cent>,<circ_rad>;
```
<circ_name> is the name of the arc and will be assigned the type CIRCLE_2D. The maximum length of <circ_name> is 32 characters.
<circ_cent> is the centre point of the circle with type POINT_2D.
<circ_rad> is the radius of the circle. It has the type DECIMAL.
```
Structure:
```
:
The COLOUR Statement
```
COLOUR,<col>;
```
<col> is the new modal colour. It has the type STRING. The maximum length of <col> is 32 characters.
See Tribon M3 Drafting_Appendices for valid Tribon colours.
Empty String means the background colour.
The CONE Statement
CONE,<cone_name>,<rad_1>,<rad_2>
```
/COORDCONE=(<cl_pnt_1>,<cl_pnt_2>);
```
<cone_name> is the name of the cone and will be assigned the type CONE_3D. The maximum length of <cone_name> is 32 characters.
<rad_1> and <rad_2> are the radii of the bottom and top circles respectively with type DECIMAL.
```
COORDCONE=(<cl_pnt_1>,<cl_pnt_2>)
```
<cl_pnt_1> and <cl_pnt_2> are the centre line starting and ending points, respectively. They have the type POINT_3D.
```
Structure:
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(N,<circ_name>,'NSEG')
```
```
/STRUCTURE=(X,<circ_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<circ_name>,'AMPLITUDE',2,'Y');
```
```
PNT(1:3) (POINT_3D)
```
```
VEC(1:3) (VECTOR_3D)
```
```
BASE (DECIMAL)
```
```
TOP (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<cone_name>,'PNT',1)
```
```
/STRUCTURE=(Z,<cone_name>,'VEC',3)
```
```
/STRUCTURE=(R1,<cone_name>,'BASE')
```
The CONNECTIONPOINT Statement
CONNECTIONPOINT,<conn_name>,<conn_type>,<conn_no>,
```
<conn_pnt>,<conn_vect>,<conn_desc>;
```
<conn_name> is the name of the connection point and will be assigned the type CONNECTIONPOINT_3D. The maximum length of <conn_name> is 32 characters.
<conn_type> is the connection type of type INTEGER. Only types between 1 and 9 are valid.
<conn_no> is the connection number of type INTEGER. Only numbers between 1 and 199 are valid.
<conn_pnt> is the connection point defining the position. It has the type POINT_3D.
<conn_vect> is the connection vector defining the direction. It has the type VECTOR_3D.
<conn_desc> is the connection description of type STRING. Maximum length of <conn_desc> is 100 characters.
```
Structure:
```
The CONTOUR Statement
CONTOUR,<cnt_name>[,<start_pnt>]
[/ARC=<arc_name>]
```
[/ARCMIDPNT=(<mid_pnt>,<end_pnt>)]
```
```
[/ARCRADIUS=(<end_pnt,<rad>)]
```
```
[/ARCAMPLITUDE=(<end_pnt,<ampl>)]
```
[/CONTOUR=<cnt_name>]
[/LINE=<line_name>]
[/LINEEND=<end_pnt>]
```
[/LINEANGLE=(<len>,<ang>)]
```
[/LINEOFFS=<offs>]
```
[/SPLINE=<spl_name>];
```
<cnt_name> is the name of the contour and will be assigned the type CONTOUR_2D. The maximum length of <cnt_name> is 32 characters.
<start_pnt> is the starting point of the contour with type POINT_2D. If /ARC, /CONTOUR, /LINE or /SPLINE is used for the first segment of the contour, then <start_pnt> shall
be omitted.
```
ARC=<arc_name>
```
<arc_name> is the name of the arc and has the type ARC_2D. If <arc_name> is not the first segment in the contour, the starting point of <arc_name> will be ignored. No check
is made whether this point coincides with the ending point of the previous segment or not.
```
ARCMIDPNT=(<mid_pnt>,<end_pnt>)
```
<mid_pnt> and <end_pnt> are the mid and ending points of the arc. They have the type POINT_2D. The starting point is defined by <start_pnt> or by the ending point of
the previous segment.
```
ARCRADIUS=(<end_pnt>,<rad>)
```
<end_pnt> is the ending point of the arc with the type POINT_2D. The starting point is defined by <start_pnt> or by the ending point of the previous segment.
<rad> is the arc radius when the arc is defined by giving two points + radius. It has the type DECIMAL.
```
ARCAMPLITUDE=(<end_pnt,<ampl>)
```
<end_pnt> is the ending point of the arc with the type POINT_2D. The starting point is defined by <start_pnt> or by the ending point of the previous segment.
<ampl> is the arc amplitude when the arc is defined by giving two points + amplitude. It has the type DECIMAL.
```
CONTOUR=<cnt_name>
```
<cnt_name> is the name of the contour and has the type CONTOUR_2D. If <cnt_name> is not the first segment in the contour, the starting point of <cnt_name> will be ignored.
No check is made whether this point coincides with the ending point of the previous segment.
```
LINE=<line_name>
```
<line_name> is the name of the line and has the type LINE_2D. If <line_name> is not the first segment in the contour the starting point of <line_name> will be ignored. No
check is made whether this point coincides with the ending point of the previous segment or not.
```
LINEEND=<end_pnt>
```
<end_pnt> is the ending point of the line with the type POINT_2D. The starting point is defined by <start_pnt> or by the ending point of the previous segment.
```
LINEANGLE=(<len>,<ang>)
```
<len> is the length of the line and <ang> is the angle of the line, both with type DECIMAL. The starting point is defined by <start_pnt> or by the ending point of the previous
segment.
```
LINEOFFS=<offs>
```
<offs> is the offset from the current point. It has the type STRING with at most 72 characters. The following formats are valid:
```
du, dv (e.g. 100,50) or
```
```
length, angle (e.g. 100,45D) or
```
```
length, verbal direction (e.g. 100,N).
```
```
Verbal directions can be North, South, West, East, Right, Left, Up or Down. Only the first letter is relevant. If the string ends with a 'U' or a 'V', the u axis or the v axis will belocked. Angles must be followed by D (degrees) or R (radians).
```
The strings must only contain digits, a '-' or a '.'. '-' is only valid in the first position. Between the strings, it is allowed to have a couple of ' ' and ',' but at least one, either a ' ' or a','. If one of the letters mentioned above is at a valid position, the rest of the string is ignored. Spaces in the beginning or the end of the string are removed.
```
SPLINE=<spl_name>
```
<spl_name> is the name of the spline and has the type SPLINE_2D. If <spl_name> is not the first segment in the contour, the starting point of <spl_name> will be ignored. No
check is made whether this point coincides with the ending point of the previous segment or not.
```
Structure:
```
```
/STRUCTURE=(R2,<cone_name>,'TOP');
```
```
CONTYPE (INTEGER)
```
```
CONNUMBER (INTEGER)
```
```
PNT(1:3) (DECIMAL)
```
```
VEC(1:3) (DECIMAL)
```
```
DESCR (STRING)
```
```
Example:
```
```
GET/STRUCTURE=(T,<conn_name>,'CONTYPE')
```
```
/STRUCTURE=(N,<conn_name>,'CONNUMBER')
```
```
/STRUCTURE=(X,<conn_name>,'PNT',1)
```
```
/STRUCTURE=(Y,<conn_name>,'VEC','Z')
```
```
/STRUCTURE=(D,<conn_name>,'DESCR');
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
The CURRENT Statement
```
CURRENT[/SUBPICTURE=(<view_name>,<subview_name>)
```
[/VIEWSCALE=<view_scl>]]
```
[/SUBVOLUME=<subvol_no>];
```
```
SUBPICTURE=(<view_name>,<subview_name>)
```
[/VIEWSCALE=<view_scl>]
<view_name> is the name of the view. It has the type STRING. The maximum length of <view_name> is 26 characters. If <view_name> does not exist a new view and a new
subview are created. The subview will get the name <subview_name>.
<subview_name> is the name of the subview. It has the type STRING. The maximum length of <subview_name> is 26 characters. If <subview_name> does not exist a new
subview is created.
<view_scl> is the scale to be used when a new view is created. It has the type DECIMAL. If this attribute is not given then the view scale will be the same as the drawing scale
```
(given in the NAME statement).
```
A new component is always created when a macro is run. This is the case even if the CURRENT statement is not present.
```
SUBVOLUME=<subvol_no>
```
<subvol_no> is the number of the subvolume. It has the type INTEGER. If <subvol_no> does not exist it is created.
The CYLINDER Statement
CYLINDER,<cyl_name>,<rad>
```
/COORDCYL=(<cl_pnt_1>,<cl_pnt_2>;
```
<cyl_name> is the name of the cylinder and will be assigned the type CYLINDER_3D. The maximum length of <cyl_name> is 32 characters.
<rad> is the radius of the cylinder with type DECIMAL.
```
COORDCYL=(<cl_pnt_1>,<cl_pnt_2>)
```
<cl_pnt_1> and <cl_pnt_2> are the centre line starting and ending points, respectively. They have the type POINT_3D.
```
Structure:
```
The DECLARE Statement
```
DECLARE,<variable>,<type>;
```
<variable> is the name of the variable whose type is to be declared. The maximum length of <variable> is 32 characters.
<type> is the type of <variable>. It has the type STRING and the whole type name must be given. The following types are available:
INTEGER
DECIMAL
STRING
POINT_2D
LINE_2D
ARC_2D
CONTOUR_2D
CIRCLE_2D
VECTOR_2D
SPLINE_2D
TEXTFILE_2D
TEXT_2D
SYMBOL_2D
NOTE_2D
HATCH_2D
EXTRACT
RANGE
TABLE
POINT_3D
VECTOR_3D
CONNECTIONPOINT_3D
CONE_3D
CYLINDER_3D
GENERALCYLINDER_3D
PARALLELEPIPED_3D
POLYGON_3D
SPHERESEG_3D
TOROID_3D
ROTATIONAL_3D
The default type is DECIMAL.
The DELAY Statement
```
DELAY,<del_time>;
```
<del_time> is the delay time in seconds. It has the type DECIMAL.
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(N,<cnt_name>,'NSEG')
```
```
/STRUCTURE=(X,<cnt_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<cnt_name>,'AMPLITUDE',2,'Y');
```
```
PNT(1:3) (DECIMAL)
```
```
VEC(1:3) (DECIMAL)
```
```
BASE (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<cyl_name>,'PNT',1)
```
```
/STRUCTURE=(Y,<cyl_name>,'VEC','Y')
```
```
/STRUCTURE=(R,<cyl_name>,'BASE');
```
The DISTANCE Statement
DISTANCE,<variable_1>,<variable_2>
<variable_1> is assigned the same value as <variable_2> and will get the same type as the first one. The maximum length of <variable_1> and <variable_2> is 32
characters. <variable_2> can be an expression, an integer constant or a decimal constant.
When the DISTANCE statement is used <variable_1> will be scaled with the current scale. This is not the case when the ASSIGN statement is used.
The DRAWING_NAME Statement
```
DRAWING_NAME, <name_drawing>;
```
This statement assigns the name of current drawing to <name_drawing> which is a string parameter. If there is no current drawing, the statement prompts the user to supply the
name as text either in input window or on terminal.
The ELSE Statement
```
ELSE;
```
This statement must be used together with the IF statement.
The ENDIF Statement
```
ENDIF;
```
The ENDIF statement terminates the IF statement.
The ENDLOOP Statement
```
ENDLOOP;
```
The ENDLOOP statement terminates the LOOP statement.
The ENDMACRO Statement
```
ENDMACRO;
```
The ENDMACRO statement terminates the MACRO statement.
The ENDWHILE Statement
```
ENDWHILE;
```
The ENDWHILE statement terminates the WHILE statement.
```
The EXTRACTION Statement (OPTIONAL)
```
```
EXTRACTION,<dex_name>,<dex_str>;
```
<dex_name> is the name of the data extraction variable and has the type EXTRACT. The maximum length of <dex_name> is 32 characters.
<dex_str> is the data extraction string and has the type STRING. For further information, see documentation in Tribon User's Guide Data Extraction.
The GENERALCYLINDER Statement
```
GENERALCYLINDER,<gencyl_name>,<cnt_name>,<thick>, <pnt_1>,<pnt_2>,<pnt_3>;
```
<gencyl_name> is the name of the general cylinder and will be assigned the type GENERALCYLINDER_3D. The maximum length of <gencyl_name> is 32 characters.
```
<cnt_name> is the name of a 2D contour (with type CONTOUR_2D) which has previously been defined.
```
<thick> is the thickness of the general cylinder and has the type DECIMAL.
<pnt_1> is the origin of the general cylinder.
<pnt_2> and <pnt_3> defines together with <pnt_1> the orientation in space. The u vector is given by <pnt_2> and <pnt_1> and the v vector by <pnt_3> and <pnt_1>.
<pnt_1>, <pnt_2> and <pnt_3> all have the type POINT_3D.
```
Structure:
```
The GET Statement
GET
```
[/INTEGER=(<prompt>,<int>)]
```
```
[/DECIMAL=(<prompt>,<dec>)]
```
```
[/STRING=(<prompt>,<str>)]
```
```
[/DISTANCE=(<prompt>,<dist>)]
```
```
[/POINT_2D=(<prompt>,<pnt>)]
```
```
[/POINT_3D=(<prompt>,<pnt>)]
```
```
[/EXTRACT=(<variable>,<status>,<dex_name>,<arg_1>
```
```
[,<arg_2]...[,<arg_10>]..]])]
```
```
[/RANGE=(<rng_name>,<status>,<dex_name>[,<arg_1>
```
```
[,<arg_2]...[,<arg_10>]..]])]
```
```
[/STRUCTURE=(<variable>,<struct_name>,<arg_1>
```
```
[,<arg_2]...[,<arg_10>]..]])];
```
```
[/MODEL_NAME=(<prompt>, <status>, <name_model>, <name_component>)];
```
```
[/VIEW_ID=(<prompt>, <get_viewid>)];
```
<prompt> is a text displayed at the workstation before entering any values. It has the type STRING and the maximum length is 100 characters. <prompt> has the same
meaning for the following attributes to the GET statement.
```
INTEGER=(<prompt>,<int>)
```
```
PNT(1:3) (DECIMAL)
```
```
UVEC(1:3) (DECIMAL)
```
```
VVEC(1:3) (DECIMAL)
```
```
THICK (DECIMAL)
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example: )
```
```
GET/STRUCTURE=(PX,<gencyl_name>,'PNT',1
```
```
/STRUCTURE=(N,<gencyl_name>,'NSEG')
```
```
/STRUCTURE=(X,<gencyl_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<gencyl_name>,'AMPLITUDE',2,'Y');
```
<int> is the integer value which has been given as input at the workstation.
```
DECIMAL=(<prompt>,<dec>)
```
<dec> is the decimal value which has been given as input at the workstation.
```
STRING=(<prompt>,<str>)
```
<str> is the string value which has been given as input at the workstation.
```
DISTANCE=(<prompt>,<dist>)
```
```
<dist> is a distance which has been given as input at the workstation. By default, the <dist> is given as the distance between two cursor positions (or any other point mode)
```
but it is possible to key in <dist> by answering REJECT at the first cursor position. <dist> has the type DECIMAL.
It is important to use DISTANCE and not DECIMAL when a distance is wanted, because the current scale is taken care of in DISTANCE but not in DECIMAL.
```
POINT_2D=(<prompt>,<pnt>)
```
<pnt> is a point which has been given as input at the workstation. The default point mode is cursor position but it is possible to use any of the other available modes. <pnt> has
the type POINT_2D.
```
POINT_3D=(<prompt>,<pnt>)
```
<pnt> is a point which has been given as input at the workstation. The default point mode is cursor position but it is possible to use any of the other available modes. <pnt> has
the type POINT_3D.
```
EXTRACT=(<variable>,<status>,<dex_name>,<arg_1>[,<arg_2>]... [,<arg_10>]..]]) Optional function.
```
<variable> is the name of the variable to be assigned. It can have the type INTEGER, DECIMAL or STRING. The maximum length of <variable> is 32 characters.
<status> is a variable giving the status of <variable>. It can have the following INTEGER values:
0<variable> not defined
1<variable> defined
Before using <variable>, there must always be a test on <status> to ensure that <variable> is defined. Otherwise the macro will be aborted.
<dex_name> is the name of the data extraction variable and has the type EXTRACT. The maximum length of <dex_name> is 32 characters.
<arg_1>[,<arg_2>]...[,<arg_10>]..]] are the arguments corresponding to the data extraction keywords, from the top level down to the bottom level. These arguments
can have the type INTEGER, DECIMAL or STRING.
```
RANGE=(<rng_name>,<status>,<dex_name>[,<arg_1>[,<arg_2>]... [,<arg_10>]..]]) Optional function.
```
<rng_name> is the name of the range which was the result of the extraction. It has the type RANGE. The maximum length of <rng_name> is 32 characters. The range can for
instance contain the resulting object names.
<status> is a variable giving the status of <rng_name>. It can have the following INTEGER values:
0<rng_name> not defined
1<rng_name> defined
Before using <rng_name>, there shall always be a test on <status> to ensure that <rng_name> is defined. Otherwise the macro will be aborted.
<dex_name> is the name of the data extraction variable and has the type EXTRACT. The maximum length of <dex_name> is 32 characters.
[,<arg_1>[,<arg_2>]...[,<arg_10>]..]] are the arguments corresponding to the data extraction keywords, from the top level down to the bottom level. These
arguments can have the type INTEGER, DECIMAL or STRING.
```
STRUCTURE=(<variable>,<struct_name>,<arg_1>
```
```
[,<arg_2]...[,<arg_10>]..]])
```
<variable> is the name of the variable to be assigned. It can have the type INTEGER, DECIMAL or STRING. The maximum length of <variable> is 32 characters.
<struct_name> is the name of the structure from which the data shall be taken. It has the type STRING. The following structure types are available:
POINT_2D
LINE_2D
ARC_2D
CONTOUR_2D
CIRCLE_2D
VECTOR_2D
SPLINE_2D
TEXTFILE_2D
TEXT_2D
SYMBOL_2D
NOTE_2D
HATCH_2D
POINT_3D
VECTOR_3D
CONNECTIONPOINT_3D
CONE_3D
CYLINDER_3D
GENERALCYLINDER_3D
PARALLELEPIPED_3D
POLYGON_3D
SPHERESEG_3D
TOROID_3D
ROTATIONAL_3D
[<arg_1>[,<arg_2>]...[,<arg_10>]..]] are the arguments in the structure. It is thus possible for instance to get the end coordinates for the n:th segment in a certain
contour or the total number of lines in the file used by the TEXTFILE statement.
The arguments are described at the respective structure statement.
```
MODEL_NAME=(<prompt>,<status>,<name_model>, <name_component>)
```
<status> is a variable giving the status of <variable>. It can have the following INTEGER values:
0<name_model> and <name_component> not defined
1<name_model> defined, <name_component> not defined
2<name_model> and <name_component> defined
Before using either of <name_model> and <name_component>, there must always be a test on <status> to ensure that the variable about to be used is defined. Otherwise
the macro will be aborted. Moreover, the variable must be declared by a DECLARE statement.
<name_model> is a string assigned to by the statement. It is only valid if <status> = 1. The parameter has the name of the model indicated by user when the statement was
executed.
<name_component> is a string assigned to by the statement. It is only valid if <status> = 1. The parameter has the name of the model object component indicated by user
when the statement was executed.
```
VIEW_ID=(<prompt>,<get_viewid>)
```
<get_viewid> is the ID of a view which has been given as input at the workstation. <get_viewid> has the type INTEGER.
The HATCH Statement
HATCH,<hatch_name>,<hatch_cnt>,<hatch_type>
[/HATCHANGLE=<hatch_angle>]
[/HATCHDISTANCE=<hatch_dist>]
```
[/USERDEFINED=(<hatch_page>,<hatch_number>]
```
```
[/ISLAND=<island_cnt>];
```
<hatch_name> is the name of the hatch pattern and has the type HATCH_2D. The maximum length of <hatch_name> is 32 characters.
<hatch_type> is the type of hatch pattern. It has the type INTEGER. The following types are available:
1 normal, positive angle
2 normal, negative angle
3 cross-hatching
4 user defined
```
HATCHANGLE=<hatch_angle>
```
<hatch_angle> is the angle of the hatch pattern lines. It has the type DECIMAL. The default angle is 60 degrees.
```
HATCHDISTANCE=<hatch_dist>
```
<hatch_dist> is the distance between the hatch pattern lines. It has the type DECIMAL. The default distance is 5 mm.
```
USERDEFINED=<hatch_page>,<hatch_number>
```
```
<hatch_page> is the page number (1-999) in the standard book for user defined hatch patterns. It has the type INTEGER.
```
```
<hatch_number> is the standard number (1-8) within the page <hatch_page> in the standard book for user defined hatch patterns. It has the type INTEGER.
```
/ISLAND=<island_cnt>
<island_cnt> is the island contour where the hatch pattern shall be removed. It is of the type CONTOUR_2D or TEXT_2D.
```
Structure:
```
The IF Statement
```
IF,<cond>;
```
<cond> is the condition to be tested. It has the type
BOOLEAN.
The LAYER Statement
```
LAYER,<lay_no>;
```
```
<lay_no> is the layer number (> 0) and must be given within ' ' if it is addressed with an alias name. If <lay_no> is a true number or a variable, it shall not be given within ' '. If
```
<lay_no> refers to a layer class, it must be preceded by # and directly followed by the class number or the class name. In this case, <lay_no> shall be given within ' '.
The maximum length of <lay_no> as an alias is 26 characters and as a variable 32 characters.
The LINE Statement
LINE,<line_name>,<stp_pnt>
[/LINEEND=<end_pnt>]
```
[/LINEANGLE=(<len>,<ang>)]
```
```
[/LINEOFFS=<offs>];
```
<line_name> is the name of the line and has the type LINE_2D. The maximum length of <line_name> is 32 characters.
<stp_pnt> is the starting point of the line with the type POINT_2D.
```
LINEEND=<end_pnt>
```
<end_pnt> is the ending point of the line with the type POINT_2D.
```
LINEANGLE=(<len>,<ang>)
```
<len> is the length of the line and <ang> is the angle of the line, both with type DECIMAL.
```
LINEOFFS=<offs>
```
<offs> is the offset from the current point. It has the type STRING with at most 72 characters. The following formats are valid:
```
du, dv (e.g. 100,50) or
```
```
length, angle (e.g. 100,45D) or
```
```
length, verbal direction (e.g. 100,N).
```
```
Verbal directions can be North, South, West, East, Right, Left, Up or Down. Only the first letter is relevant. If the string ends with a 'U' or a 'V', the u axis or the v axis will belocked. Angles must be followed by D (degrees) or R (radians).
```
The strings must only contain digits, a '-' or a '.'. '-' is only valid in the first position. Between the strings, it is allowed to have a couple of ' ' and ',' but at least one, either a ' ' or a','. If one of the letters mentioned above is at a valid position, the rest of the string is ignored. Spaces in the beginning or the end of the string are removed.
```
Structure:
```
```
TYPE (INTEGER)
```
```
ANGLE (DECIMAL)
```
```
DISTANCE (DECIMAL)
```
```
PAGE (INTEGER)
```
```
NUMBER (INTEGER)
```
```
NSEG (INTEGER)
```
```
ISLANDS (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(T,<hatch_name>,'TYPE'
```
```
/STRUCTURE=(A,<hatch_name>,'ANGLE')
```
```
/STRUCTURE=(D,<hatch_name>,'DISTANCE')
```
```
/STRUCTURE=(P,<hatch_name>,'PAGE')
```
```
/STRUCTURE=(M,<hatch_name>,'NUMBER')
```
```
/STRUCTURE=(N,<hatch_name>,'NSEG')
```
```
/STRUCTURE=(I,<hatch_name>,'ISLANDS')
```
```
/STRUCTURE=(X,<hatch_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<hatch_name>,'AMPLITUDE',2,'Y');
```
```
STARTPNT(1:2) (DECIMAL)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<line_name>,'STARTPNT',1)
```
```
/STRUCTURE=(Y,<line_name>,'ENDPNT','Y'
```
The LINETYPE Statement
LINETYPE,<lin_type>
```
[/LINEWIDTH=<lin_wid>];
```
```
<lin_type> is the modal line type to be used. It has the type INTEGER. Default line type is 1 (solid). The types 1 - 5 are available.
```
```
LINEWIDTH=<lin_wid>
```
```
<lin_wid> is the modal line width to be used. It has the type INTEGER. Default line width is 1 (thin). The types 1 - 3 are available.
```
The LOOP Statement
```
LOOP,<loop_var>,<range>;
```
<loop_var> is the loop variable and the type is dependent on how <range> is given.
<range> can be given in three ways:
<start_value> : <end_value>
or
<start_value> : <end_value> :: <step_value>
or
<range>
where <range> has the type RANGE.
In the to first cases <loop_var> can have the type INTEGER or DECIMAL. If <range> has the type RANGE then <loop_var> can also have type STRING.
When <step_value> is omitted, it is by default put to 1.
<start_value>, <end_value> and <step_value> have the type DECIMAL.
The MACRO Statement
MACRO,<macro_name>
```
[,<arg_1>[,<arg_2>....[,<arg_25>]....]];
```
<macro_name> is the name of the macro. The maximum length of <macro_name> is 32 characters. Only upper case letters, digits and _ are allowed characters.
<arg_1>,<arg_2>, ....,<arg_25> are the arguments to the macro. They cannot be expressions but must be variables. All types given in the ASSIGN statement are allowed.
The NAME Statement
NAME,<dwg_name>
[/DWG]
[/FORM=<form_name>]
[/PICT]
[/SCALE=<dwg_scale>]
```
[/VOLUME=(<xmax>,<ymax>)];
```
<dwg_name> is the name of the drawing/subpicture/ volume to be created and stored on a data bank. If the NAME statement is omitted, <macro_name> will be used. <dwg_name>
has the type STRING and the maximum length is 32 characters.
If the drawing/subpicture/volume given by <dwg_name> already exists on the data bank, the geometry created by the macro will be added to the existing object.
DWG
This attribute is used to specify that a drawing is to be created.
```
FORM=<form_name>
```
<form_name> is the name of the form to be used, if any. <form_name> has the type STRING and the maximum length is 32 characters.
PICT
This attribute is used to specify that a subpicture is to be created.
```
SCALE=<dwg_scale>
```
<dwg_scale> is the drawing/subpicture scale to be used. The default scale is 1:50. <dwg_scale> has the type DECIMAL.
```
VOLUME=(<xmax>,<ymax>)
```
<xmax> and <ymax> are the x and y extensions for the volume to be created. They have the type DECIMAL.
The NOTE Statement
NOTE,<note_name>,<start_pnt>,<ref_cnt>,<note_text>
[/NOTESYMBOL=<note_symb>]
```
[/REFSYMBOL=<ref_symb>];
```
<note_name> is the name of the note and has the type NOTE_2D. The maximum length of <note_name> is 32 characters.
<start_pnt> is the starting point of the reference lines of the note. It has the type POINT_2D.
<ref_cnt> is the reference lines of the note. It has the type CONTOUR_2D. This contour must have been defined previously.
```
<note_text> is the text in the note (with type TEXT_2D) which has previously been defined.
```
```
NOTESYMBOL=<note_symb>
```
<note_symb> is the number of the note symbol. It has the type INTEGER. The default note symbol is number 31.
```
REFSYMBOL=<ref_symb>
```
<ref_symb> is the number of the reference symbol. It has the type INTEGER. The default reference symbol is number 21.
```
Structure:
```
```
TEXT (STRING)
```
```
NOTESYMB (INTEGER)
```
```
REFSYMB (INTEGER)
```
```
PNT(1:2) (DECIMAL)
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(NS,<note_name>,'NOTESYMB')
```
```
/STRUCTURE=(RS,<note_name>,'REFSYMB')
```
```
/STRUCTURE=(SX,<note_name>,'PNT',1)
```
```
/STRUCTURE=(N,<note_name>,'NSEG')
```
```
/STRUCTURE=(X,<note_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<note_name>,'AMPLITUDE',2,'Y');
```
The PARALLELEPIPED Statement
PARALLELEPIPED,<para_name>
```
[/COORDPARA=(<corn_1>,<corn_2>,<corn_3>)]
```
```
[/CENLINPARA=(<cl_pnt_1>,<cl_pnt_2>,<corn>)];
```
<para_name> is the name of the parallelepiped and has the type PARALLELEPIPED_3D. The maximum length of <para_name> is 32 characters.
```
COORDPARA=(<corn_1>,<corn_2>,<corn_3>)
```
<corn_1> is the origin of the parallelepiped and the lower right corner when looking in the direction of the centre line. <corn_2> is the upper right corner at the end surface
when looking in the same direction. <corn_3> is then, in the same way, the upper left corner at the end surface.
<corn_1>, <corn_2> and <corn_3> all have the type POINT_3D.
```
COORDPARA=(<cl_pnt_1>,<cl_pnt_2>,<corn>)
```
<cl_pnt_1> is the starting point of the centre line and <cl_pnt_2> is the ending point of the centre line.
<corn> is the upper left corner at the end surface when looking in the direction of the centre line.
<cl_pnt_1>, <cl_pnt_2> and <corn> all have the type POINT_3D.
```
Structure:
```
The POINT_2D Statement
```
POINT_2D,<pnt_name>,<x>,<y>;
```
<pnt_name> is the name of the point and has the type POINT_2D. The maximum length of <pnt_name> is 32 characters.
<x> and <y> are the x and y coordinates of the point, both with type DECIMAL.
If only one of the coordinates of a previously defined point are to be changed, the other one is simply omitted.
```
Structure:
```
The POINT_3D Statement
```
POINT_3D,<pnt_name>,<x>,<y>,<z>;
```
<pnt_name> is the name of the point and has the type POINT_3D. The maximum length of <pnt_name> is 32 characters.
<x>, <y> and <z> are the x, y and z coordinates of the point, all with type DECIMAL.
If only one of the coordinates of a previously defined point shall be changed, the others are simply omitted.
```
Structure:
```
The POLYGON Statement
POLYGON,<pol_name>,<stp_pnt>
```
/LINEPOLYGON=<end_pnt>....;
```
<pol_name> is the name of the polygon and has the type POLYGON_3D. The maximum length of <pol_name> is 32 characters.
<stp_pnt> is the starting point of the polygon with the type POINT_3D.
```
LINEPOLYGON=<end_pnt>....
```
<end_pnt> is the ending point of the polygon segment with the type POINT_3D.
```
Structure:
```
The PRESENT Statement
```
PRESENT,<var_name>;
```
<var_name> is the name of the variable which is to be presented. It can have any of the following types:
POINT_2D
LINE_2D
ARC_2D
CIRCLE_2D
```
PNT(1:3) (DECIMAL)
```
```
UVEC(1:3) (DECIMAL)
```
```
VVEC(1:3) (DECIMAL)
```
```
LENGTH (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<para_name>,'PNT',1)
```
```
/STRUCTURE=(Y,<para_name>,'UVEC',2)
```
```
/STRUCTURE=(Z,<para_name>,'VVEC','Z')
```
```
/STRUCTURE=(L,<para_name>,'LENGTH');
```
```
PNT(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<pnt_name>,'PNT',1)
```
```
/STRUCTURE=(Y,<pnt_name>,'PNT','Y');
```
```
PNT(1:3) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<pnt_name>,'PNT','X')
```
```
/STRUCTURE=(Y,<pnt_name>,'PNT',2)
```
```
/STRUCTURE=(Z,<pnt_name>,'PNT','Z');
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:3) (DECIMAL)
```
```
AMPLITUDE(1:3) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(N,<pol_name>,'NSEG')
```
```
/STRUCTURE=(X,<pol_name>,'ENDPNT',N,1)
```
```
/STRUCTURE=(Y,<pol_name>,'AMPLITUDE',2,'Y');
```
CONTOUR_2D
SPLINE_2D
SYMBOL_2D
TEXT_2D
TEXTFILE_2D
NOTE_2D
TABLE
CONNECTIONPOINT_3D
CONE_3D
CYLINDER_3D
PARALLELEPIPED_3D
POLYGON_3D
ROTATIONAL_3D
TOROID_3D
SPHERESEG_3D
GENERALCYLINDER_3D
The maximum length of <var_name> is 32 characters.
The PUT Statement
```
PUT,<var_name>;
```
<var_name> is the name of the variable which contents is to be written. It can have any type. The maximum length of <var_name> is 32 characters.
The RANGE Statement
RANGE,<rng_name>
```
[/FILENAME=<file_name>];
```
<rng_name> is the name of the range and has the type RANGE. The maximum length of <rng_name> is 32 characters.
```
FILENAME=<file_name>
```
<file_name> is the file where the range is stored. It has the type STRING. The file contains a number of integer numbers OR decimal numbers OR strings, one on each line.
The ROTATIONAL Statement
```
ROTATIONAL,<rot_name>,<cnt_name>,<pnt>,<vec>;
```
<rot_name> is the name of the rotational primitive and will be assigned the type ROTATIONAL_3D. The maximum length of <rot_name> is 32 characters.
```
<cnt_name> is the name of a 2D contour (with type CONTOUR_2D) which has previously been defined.
```
<pnt> is the origin of the 2D contour in space. It has the type POINT_3D.
<vec> is the vector around which <cnt_name> is rotated. It has the type VECTOR_3D.
```
Structure:
```
The SPHERESEG Statement
SPHERESEG,<seg_name>,<rad>
```
/COORDSEG=(<cl_pnt_1>,cl_pnt_2>);
```
<seg_name> is the name of the spherical segment and has the type SPHERESEG_3D. The maximum length of <seg_name> is 32 characters.
<rad> is the radius of the spherical segment. It has the type DECIMAL.
```
COORDSEG=(<cl_pnt_1>,<cl_pnt_2>)
```
<cl_pnt_1> is the starting point and <cl_pnt_2> is the ending point of the centre line, both with the type POINT_3D.
```
Structure:
```
The SPLINE Statement
SPLINE,<spl_name>
[/SPLPNT=<spl_pnt>]
```
[/SPLTAN=(<spl_pnt>,<tang_ang>)];
```
<spl_name> is the name of the spline and has the type SPLINE_2D. The maximum length of <spl_name> is 32 characters.
It is possible to define the spline with or without tangent conditions in the points in the following way:
```
1)no tangent condition
```
```
2)tangent condition in the start point
```
```
3)tangent condition in the end point
```
```
4)tangent conditions in both start and end point
```
```
5)tangent conditions in all points
```
```
SPLPNT=<spl_pnt>
```
<spl_pnt> is the spline point with type POINT_2D. It is used when no tangent condition is wanted.
```
PNT(1:3) (DECIMAL)
```
```
VEC(1:3) (DECIMAL)
```
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
ENDPNT(1:2) (DECIMAL)
```
```
AMPLITUDE(1:2) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<rot_name>,'PNT',1)
```
```
/STRUCTURE=(N,<rot_name>,'NSEG')
```
```
/STRUCTURE=(Y,<rot_name>,'AMPLITUDE',N,'Y');
```
```
PNT(1:3) (DECIMAL)
```
```
UVEC(1:3) (DECIMAL)
```
```
RADIUS (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<seg_name>,'PNT',1)
```
```
/STRUCTURE=(Z,<seg_name>,'UVEC',3)
```
```
/STRUCTURE=(R,<seg_name>,'RADIUS');
```
```
SPLTAN=(<spl_pnt>,<tang_ang>)
```
<spl_pnt> is the spline point with type POINT_2D.
```
<tang_ang> is the tangent angle to be used in 2) - 5) above. It has the type DECIMAL.
```
```
Structure:
```
The SPLIT Statement
```
SPLIT,<model_name>,<delimiter>,<project>,<module>, <subsyst_1>,<subsyst_2>,<subsyst_3>;
```
<model_name> is the name of the model. It has the type STRING. The maximum length of <col> is 26 characters.
<delimiter> is the character which is used to separate the different parts of <model_name>. It has the type STRING.
<project> is the project of <model_name> and has the type STRING.
<module> is the module of <model_name> and has the type STRING.
<subsyst_1> is the first subsystem of <model_name> and has the type STRING.
<subsyst_2> is the second subsystem of <model_name> and has the type STRING.
<subsyst-3> is the third subsystem of <model_name> and has the type STRING.
All three subsystems need not be present in the model name. How many subsystems that exist depends on the application.
The SYMBOL Statement
SYMBOL,<symb_name>,<symb_no>,<symb_pnt>,<symb_ang>
[/MIRRORX]
[/MIRRORY]
[/SYMBFONT=<symb_fnt>]
[/SYMBHEIGHT=<symb_hgt>]
[/SYMBWIDTH=<symb_wid>]
```
[/AUTOOFF];
```
<symb_name> is the name of the symbol and has the type SYMBOL_2D. The maximum length of <symb_name> is 32 characters.
<symb_no> is the number of the symbol. It has the type INTEGER.
<symb_pnt> is the origin of the symbol and has the type POINT_2D.
<symb_ang> is the symbol angle which is of type DECIMAL.
MIRRORX
With this attribute, it is possible to reflect the symbol in the x axis. It cannot be used together with MIRRORY.
MIRRORY
With this attribute it is possible to reflect the symbol in the y axis. It cannot be used together with MIRRORX.
```
SYMBFONT=<symb_fnt>
```
<symb_fnt> is the symbol font and has the type INTEGER. The default font is the system font number 21.
```
SYMBHEIGHT=<symb_hgt>
```
<symb_hgt> is the symbol height and has the type DECIMAL. The symbol is given a default height value and the symbol height can be changed with this attribute.
```
SYMBWIDTH=<symb_wid>
```
<symb_wid> is the symbol width and has the type DECIMAL. The symbol is given a default width value but the symbol width can be changed with this attribute.
AUTOOFF
With this attribute it is possible to switch off the default automatic positioning of the symbol.
```
Structure:
```
The TABLE Statement
TABLE,<tab_name>
```
[/ARGUMENTS=([<arg_1>[,<arg_2>....[,<arg_15>]....]])]
```
```
[/FORMAT=([<width_1>,<ndec_1>[,<width_2>,ndec_2>....
```
```
[,<width_15>,<ndec_15>]....]])]
```
[/FILENAME=<file_name>]
[/QUOTES]
```
[/NOAPPEND];
```
<tab_name> is the name of the table and has the type TABLE. The maximum length of <tab_name> is 32 characters.
```
NSEG (INTEGER)
```
```
SEGPARTS(1:NSEG)
```
```
PNT(1:2) (DECIMAL)
```
```
VEC(1:2) (DECIMAL)
```
```
Example: )
```
```
GET/STRUCTURE=(N,<spl_name>,'NSEG'
```
```
/STRUCTURE=(X,<spl_name>,'PNT',N,1)
```
```
/STRUCTURE=(Y,<spl_name>,'VEC',N,2);
```
```
SYMBNO (INTEGER)
```
```
PNT(1:2) (DECIMAL)
```
```
ANGLE (DECIMAL)
```
```
FONTNO (INTEGER)
```
```
WIDTH (DECIMAL)
```
```
HEIGHT (DECIMAL)
```
```
MIRR (INTEGER)
```
```
AUTO (INTEGER)
```
```
Example:
```
```
GET/STRUCTURE=(S,<symb_name>,'SYMBNO')
```
```
/STRUCTURE=(X,<symb_name>,'PNT',1)
```
```
/STRUCTURE=(A,<symb_name>,'ANGLE')
```
```
/STRUCTURE=(F,<symb_name>,'FONTNO')
```
```
/STRUCTURE=(W,<symb_name>,'WIDTH')
```
```
/STRUCTURE=(H,<symb_name>,'HEIGHT')
```
```
/STRUCTURE=(M,<symb_name>,'MIRR')
```
```
/STRUCTURE=(A,<symb_name>,'AUTO');
```
```
ARGUMENTS=([<arg_1>[,<arg_2>.... [,<arg_15>]....]])
```
<arg_1>,<arg_2>, ....,<arg_25> are the arguments to be put in the table. They can have the type INTEGER, DECIMAL or STRING.
```
FORMAT=([<width_1>,<ndec_1>[,<width_2>,<ndec_2>.... [,<width_15>,<ndec_15>]....]])
```
This attribute describes the format of the table. <width_1>,<width_2>, ...,<width_15> is the width of the column for the i:th argument. It has the type integer. The default
```
width is 8 which will be the result if FORMAT is not given or if the width for a variable is omitted (i.e. given as ,,). If the width is negative the result will be positioned left-justified,otherwise right-justified.
```
<ndec_1>,<ndec_2>, ...,<ndec_15> is the number of decimals for the i:th argument. It has the type integer. The default number of decimals is 3 which will be the result if
```
FORMAT is not given. It is of course only necessary to give the number of decimals for arguments of type DECIMAL. In other cases it can be omitted (i.e. given as ,,) or given as0.
```
The attributes ARGUMENTS and FORMAT must be given together and with the same number of parameters.
```
FILENAME=<file_name>
```
<file_name> is the file where the table will be presented when the PRESENT statement is used. It has the type STRING.
QUOTES
When this attribute is given in the TABLE statement all terms will be surrounded by ' '. The resulting file can then directly be used as input to the Tribon Report Generator.
NOAPPEND
When this attribute is given in the TABLE statement the old contents in <tab_name> will be deleted and the <tab_name> can be used for another table. The attribute must also
be given the first time <tab_name> is used.
The TEXT Statement
TEXT,<txt_name>,<txt_pnt>
[/TEXTLINE=<txt_str>]
[/TEXTDECNO=<txt_dec>]
[/TEXTINTNO=<txt_int>]
[/TEXTANGLE=<txt_ang>]
[/TEXTHEIGHT=<txt_hgt>]
```
[/TEXTFONT=<txt_fnt>];
```
<txt_name> is the name of the text line and has the type TEXT_2D. The maximum length of <txt_name> is 32 characters.
<txt_pnt> is the text origin which is the lower left corner of the text. It has the type POINT_2D.
```
TEXTDECNO=<txt_dec>
```
<txt_dec> is a number which shall be presented as a text. It has the type DECIMAL.
```
TEXTINTNO=<txt_int>
```
<txt_int> is a number which will be presented as a text. It has the type INTEGER.
```
TEXTLINE=<txt_str>
```
<txt_str> is a string which will be presented as a text. It has the type STRING.
```
TEXTANGLE=<txt_ang>
```
<txt_ang> is the text angle and has the type DECIMAL. The default angle is 0.0 but the text angle can be changed with this attribute.
```
TEXTHEIGHT=<txt_hgt>
```
<txt_hgt> is the text height and has the type DECIMAL. The text is given a default height value but the text height can be changed with this attribute.
```
TEXTFONT=<txt_fnt>
```
<txt_fnt> is the text font and has the type INTEGER. Available font numbers are 0-99. The default font number is 0.
```
Structure:
```
The TEXTFILE Statement
TEXTFILE,<txf_name>,<file_name>
[/INTERLINESPACE=<intlin_space>]
```
[/POSLINES=(<start_pnt>,<first_line>,<last_line>)]
```
[/TEXTANGLE=<text_ang>]
[/TEXTHEIGHT=<text_hgt>]
```
[/TEXTFONT=<text_fnt>];
```
<txf_name> is the name of the text file variable and has the type TEXTFILE_2D. The maximum length of <txf_name> is 32 characters.
<file_name> is the name of the file from where the text is fetched. It has the type STRING.
```
INTERLINESPACE=<intlin_space>
```
<intlin_space> is the factor for the interline space. The interline space is defined as the factor * the text height. It has the type DECIMAL. The default factor is 1.5.
```
POSLINES=(<start_pnt>,<first_line>,<last_line>)
```
<start_pnt> is the origin of the first text line and the lower left corner of that line. It has the type POINT_2D.
<first_line> is the number of the first line to be presented. It has the type INTEGER.
<last_line> is the number of the last line to be presented. It has the type INTEGER.
```
TEXTANGLE=<text_ang>
```
<text_ang> is the text angle and has the type DECIMAL. The default angle is 0.0 but the text angle can be changed with this attribute.
```
TEXTHEIGHT=<text_hgt>
```
<text_hgt> is the next height and has the type DECIMAL. The text is given a default height value but the text height can be changed with this attribute.
```
TEXTFONT=<text_fnt>
```
<text_fnt> is the text font and has the type INTEGER. Available font numbers are 0-99. The default font number is 0.
It is possible to give both absolute and relative values of the lines to be presented. This is illustrated by the following examples:
```
/POSLINES=(P1,1,15) lines 1 to 15
```
```
/POSLINES=(P1,10,) next 10 lines (16 to 25)
```
```
/POSLINES=(P1,20,) next 20 lines (26 to 45)
```
```
/POSLINES=(P1,,10) previous 10 lines (16 to 25)
```
```
/POSLINES=(P1,,) the whole file
```
```
TEXT (STRING)
```
```
PNT(1:2) (DECIMAL)
```
```
ANGLE (DECIMAL)
```
```
HEIGHT (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(T,<txt_name>,'TEXT'
```
```
/STRUCTURE=(X,<txt_name>,'PNT',1)
```
```
/STRUCTURE=(A,<txt_name>,'ANGLE')
```
```
/STRUCTURE=(H,<txt_name>,'HEIGHT');
```
```
Structure:
```
The TOROID Statement
TOROID,<tor_name>,<rad>
```
/COORDTOR=(<cl_pnt_1>,cl_pnt_2>,<cl_pnt_3>);
```
<tor_name> is the name of the toroid and has the type TOROID_3D. The maximum length of <tor_name> is 32 characters.
<rad> is the radius of the toroid. It has the type DECIMAL.
```
/COORDTOR=(<cl_pnt_1>,cl_pnt_2>,<cl_pnt_3>);
```
<cl_pnt_1> is the starting point, <cl_pnt_2> is the mid point and <cl_pnt_3> is the ending point of the toroid centre line. All have the type POINT_3D.
```
Structure:
```
The VECTOR_2D Statement
```
VECTOR_2D,<vect_name>,<x>,<y>;
```
<vect_name> is the name of the vector and has the type VECTOR_2D. The maximum length of <vect_name> is 32 characters.
<x> and <y> are the x and y coordinates of the vector, both with type DECIMAL.
If only one of the coordinates of a previously defined point shall be changed, the other one is simply omitted.
```
Structure:
```
The VECTOR_3D Statement
```
VECTOR_3D,<vect_name>,<x>,<y>,<z>;
```
<vect_name> is the name of the vector and has the type VECTOR_3D. The maximum length of <vect_name> is 32 characters.
<x>, <y> and <z> are the x, y and z coordinates of the vector, all with type DECIMAL.
If only one of the coordinates of a previously defined point shall be changed, the others are simply omitted.
```
Structure:
```
The VMSJOB Statement
```
VMSJOB,<jobfilename>;
```
The parameter <jobfilename> is the name of the file to be executed. It has the type STRING. The maximum length of <jobfilename> is 100 characters.
The WHILE Statement
```
WHILE,<cond>;
```
<cond> is the condition to be tested. It has the type BOOLEAN.
```
FILENAME (STRING)
```
```
ANGLE (DECIMAL)
```
```
HEIGHT (DECIMAL)
```
```
ILSP (DECIMAL)
```
```
NDATA (INTEGER)
```
```
DATA(1:NDATA)
```
```
PNT(1:2) (DECIMAL)
```
```
FIRST (INTEGER)
```
```
LAST (INTEGER)
```
```
Example:
```
```
GET/STRUCTURE=(F,<txf_name>,'FILENAME'
```
```
/STRUCTURE=(A,<txf_name>,'ANGLE')
```
```
/STRUCTURE=(H,<txf_name>,'HEIGHT')
```
```
/STRUCTURE=(I,<txf_name>,'ILSP')
```
```
/STRUCTURE=(N,<txf_name>,'NDATA')
```
```
/STRUCTURE=(X,<txf_name>,'PNT',N,1)
```
```
/STRUCTURE=(S,<txf_name>,'FIRST',N)
```
```
/STRUCTURE=(E,<txf_name>,'LAST',N);
```
```
STARTPNT(1:3) (DECIMAL)
```
```
ENDPNT(1:3) (DECIMAL)
```
```
AMPLITUDE(1:3) (DECIMAL)
```
```
Example:
```
```
GET/STRUCTURE=(X,<tor_name>,'STARTPNT',1)
```
```
/STRUCTURE=(Y,<tor_name>,'ENDPNT',2)
```
```
/STRUCTURE=(Z,<tor_name>,'AMPLITUDE',3);
```
```
VEC(1:2) (DECIMAL)
```
```
Example: )
```
```
GET/STRUCTURE=(X,<vect_name>,'VEC',1
```
```
/STRUCTURE=(Y,<vect_name>,'VEC','Y');
```
```
VEC(1:3) (DECIMAL)
```
```
Example: )
```
```
GET/STRUCTURE=(X,<vect_name>,'VEC',1
```
```
/STRUCTURE=(Y,<vect_name>,'VEC','Y')
```
```
/STRUCTURE=(Z,<vect_name>,'VEC','Z');
```
Copyright © 1993-2005 AVEVA AB
17.4.2 Example of Macros Creating 2D Geometry
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 1
This example is a macro creating some simple geometry.
!
! All macros begin with the MACRO-stmt
!
```
MACRO,RECTANGLE;
```
```
GET/POINT_2D=('Give first corner',P1)
```
```
/POINT_2D=('Give second corner',P3);
```
```
ASSIGN,X1,P1/XCOORD;
```
```
ASSIGN,Y1,P1/YCOORD; ! The x- and y-coordinates
```
```
ASSIGN,X2,P3/XCOORD; ! of the 2 points are needed
```
```
ASSIGN,Y2,P3/YCOORD;
```
```
POINT_2D,P2,X1,Y2; ! Create the other
```
```
POINT_2D,P4,X2,Y1; ! two corners
```
CONTOUR,CNT,P1
/LINEEND = P2
/LINEEND = P3 ! Create a contour
/LINEEND = P4
```
/LINEEND = P1;
```
```
PRESENT,CNT; ! Display the contour
```
!
! All macros end with the ENDMACRO-stmt
!
```
ENDMACRO;
```
In the macro RECTANGLE, the contour was created using the four 2D points. In some cases, it might be more convenient to define a contour with lines instead. The macro above willthen look like this:
```
MACRO,RECTANGLE;
```
```
GET/POINT_2D=('Give first corner',P1)
```
```
/POINT_2D=('Give second corner',P3);
```
```
ASSIGN,X1,P1/XCOORD;
```
```
ASSIGN,Y1,P1/YCOORD;
```
```
ASSIGN,X2,P3/XCOORD;
```
```
ASSIGN,Y2,P3/YCOORD;
```
```
POINT_2D,P2,X1,Y2;
```
```
POINT_2D,P4,X2,Y1;
```
```
LINE,L1,P1/LINEEND=P2;
```
```
LINE,L2,P2/LINEEND=P3;
```
```
LINE,L3,P3/LINEEND=P4;
```
```
LINE,L4,P4/LINEEND=P1;
```
CONTOUR,CNT
/LINE = L1
/LINE = L2
/LINE = L3
```
/LINE = L4;
```
```
PRESENT,CNT;
```
```
ENDMACRO;
```
Note that the CONTOUR statement looks different now. In the first case, the start point must be given but in the second case this point is the start point of the first line.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 2
The macro SCREW below has 4 parameters. One of them, the drawing name, is given in the MACRO statement. This parameter tells where the result of the macro shall be stored whenexecuted by the stand alone program. A drawing will be created using the form A3 and the scale chosen is 1:1. The NAME statement has no effect when the macro is executed
interactively at a workstation. The result is then put into the current drawing.
The macro can be found by following this link:
macro_screw.txt
The figure below shows the result of the execution of the macro SCREW. The current drawing contained the rectangle and the length of the screw was given by using the different pointmodes, in this case the node mode. The start point was given with the close point mode.
Figure 17:1. The result of the execution of the macro SCREW.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.3 A Macro Generating a Volume
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 3
The macro PUMP is an example of a geometry macro creating a volume. It uses most of the volume primitives. Note that the general cylinder has a 2D parameter but the result is 3D. Ifthe macro is run stand alone, the NAME statement gives the name of the volume model on the data bank. The x- and y-extensions are also given.
The macro can be found by following this link:
macro_pump.txt
The figure below shows the result of the execution of the macro PUMP. The input angles were 180 degrees and 45 degrees respectively. The dimension was given as the distancebetween two cursor positions, both for the pump length and the pump height.
Figure 17:2. The result of the execution of the macro PUMP.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.4 The Possibility to Present a Text File on a Drawing
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 4
The macro LIST uses the TEXT and TEXTFILE statements to present a table on a drawing. The data are stored on a file. A heading is added and a frame is drawn.
The macro can be found by following this link:
macro_list.txt
The result of the macro is shown in the figure below.
Figure 17:3. The result from the execution of the macro LIST.
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.5 The Usage of Attributes in Geometry Macros
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 5
The macro ATTR shows the usage of the ATTRIBUTE statement. Note that it is possible to give the attribute number as an alias, a number or a variable.
```
MACRO,ATTR;
```
```
ASSIGN,LS,105.6;
```
```
ASSIGN,DS,0.2543;
```
```
ATTRIBUTE,'CHAIR'/ATTRDATA=(I2,4)
```
```
/ATTRDATA=(R1,LS)
```
```
/ATTRDATA=(R2,DS)
```
```
/ATTRDATA=(R3,35.45)
```
```
/ATTRDATA=(S2,'I2: chair no')
```
```
/ATTRDATA=(S3,'R1-R3: chair data');
```
```
ATTRIBUTE,55/ATTRDATA=(I,3)
```
```
/ATTRDATA=(R4,1.234);
```
```
ASSIGN,ATTNO,7777;
```
```
GET/STR=('Give a string: ',STR);
```
```
ATTRIBUTE,ATTNO/ATTRDATA=('S1',STR);
```
```
ENDMACRO;
```
The result of a stand alone execution of the macro ATTR is shown below.
RUN SB_SYSTEM:SZ006
Present Geometry Macro:
```
(0) Exit
```
```
(1) Print on terminal
```
```
(2) Create 2D geometry and store on DB
```
```
(3) Create 3D volume model and store on DB
```
```
(4) Create 3D volume model + picture and store on DB
```
Enter activity : 1
General Component Data Bank not assigned!
Give name of macro to be run: ATTR
```
ATTNO = 1111
```
I1 0
I2 4
R1 105.60000
R2 0.25430
R3 35.45000
S1
S2 I2: chair no
S3 R1-R3: chair data
```
ATTNO = 55
```
R1 0.00000
R2 0.00000
R3 0.00000
R4 1.23400
S1
S2
S3 3
Give a string:
> Just a test string !!!
```
ATTNO = 7777
```
S1 Just a test string !!!
Once more ? N
Give name of macro to be run:
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.6 Layer Handling
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 6
The macro LAYER shows the layer alias and layer class facilities. Note that a layer can be given as an alias or as a number. The layer class can be given either as the class name or theclass number, each preceded by '#'.
```
MACRO,LAYER;
```
```
GET/STRING=('Layer alias : ',LALIAS)
```
```
/STRING=('Layer class : ',LCLASS)
```
```
/INTEGER=('Layer number: ',LNUMBER);
```
```
LAYER,'NOLL';
```
```
LAYER,'FORM';
```
```
LAYER,1001;
```
```
LAYER,'#DRA';
```
```
LAYER,'#1';
```
```
LAYER,LALIAS;
```
```
LAYER,LCLASS;
```
```
LAYER,LNUMBER;
```
```
ENDMACRO;
```
The result of a stand alone execution of the macro LAYER is shown below.
Present Geometry Macro:
```
(0) Exit
```
```
(1) Print on terminal
```
```
(2) Create 2D geometry and store on DB
```
```
(3) Create 3D volume model and store on DB
```
```
(4) Create 3D volume model + picture and store on DB
```
Enter activity : 1
General Component Data Bank not assigned!
Give name of macro to be run: LAYER
Layer alias :
> FORM
Layer class :
> #AAA
Layer number:
> 12
LAYER & ALIAS: 0 ZERO
LAYER & ALIAS: 300 FORM
LAYER & ALIAS: 1001 VIEW1
LAYER CLASS: 10 DRA
LAYER CLASS: 1 PIPE
LAYER & ALIAS: 300 FORM
LAYER CLASS: 11 AAA
LAYER & ALIAS: 12 DOZEN
Once more ? Y
Layer alias :
> FROM
Layer class :
> #DRAW
Layer number:
> 100
LAYER & ALIAS: 0 ZERO
LAYER & ALIAS: 300 FORM
LAYER & ALIAS: 1001 VIEW1
LAYER CLASS: 10 DRA
LAYER CLASS: 1 PIPE
Layer alias FROM not defined. Layer ignored!
Layer class DRAW not found. Layer ignored!
```
LAYER: 100
```
Once more ? N
Give name of macro to be run:
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.7 The Facility of Using Conditional Statements in a Macro
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 7
This example illustrates the possibility of using the IF and WHILE statement to test the input data. Such a test can be useful to avoid runtime errors.
```
MACRO,INPUT;
```
```
ASSIGN,CONT,1;
```
```
WHILE,CONT == 1;
```
```
GET/STR=('Key in colour',COL);
```
IF,COL == 'GREEN' OR COL == 'CYAN'
OR COL == 'BLUE' OR COL == 'MAGENTA'
OR COL == 'RED' OR COL == 'YELLOW'
```
OR COL == 'WHITE';
```
```
ASSIGN,CONT,0;
```
```
ENDIF;
```
```
ENDWHILE;
```
!
! When desired colour has been given the rest
! of the macro is executed.
!
```
ENDMACRO;
```
It might be more convenient to have such a parameter check as a submacro which would look like follows.
```
MACRO,INPUT_COLOUR,COL;
```
```
DECLARE,COL,STRING;
```
```
ASSIGN,CONT,1;
```
```
WHILE,CONT == 1;
```
```
GET/STR=('Key in colour',COL);
```
IF,COL == 'GREEN' OR COL == 'CYAN'
OR COL == 'BLUE' OR COL == 'MAGENTA'
OR COL == 'RED' OR COL == 'YELLOW'
```
OR COL == 'WHITE';
```
```
ASSIGN,CONT,0;
```
```
ENDIF;
```
```
ENDWHILE;
```
```
ENDMACRO;
```
The usage of INPUT_COLOUR could be like this.
```
MACRO,MAIN;
```
```
DECLARE,C,STRING;
```
```
CALL,INPUT_COLOUR,C;
```
```
COLOUR,C;
```
!
```
ENDIF;
```
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.8 The Possibility to Write Recursive Geometry Macros
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 8
This example illustrates the possibility of writing a recursive macro, i.e. a macro which calls itself as a submacro. It uses a modified version of the macro RECTANGLE given in Appendix2.
```
MACRO,RECPNT,PNT1,PNT2;
```
```
DECLARE,PNT1,POINT_2D;
```
```
DECLARE,PNT2,POINT_2D;
```
```
CALL,RECTANGLE,PNT1,PNT2;
```
```
ASSIGN,X1,PNT1/XCOORD;
```
```
ASSIGN,Y1,PNT1/YCOORD;
```
!
! When the condition is not fulfilled
! no further calls to RECPNT are made
! and the execution is terminated
!
```
IF,X1 < 250;
```
```
ASSIGN,X2,PNT2/XCOORD;
```
```
ASSIGN,Y2,PNT2/YCOORD;
```
```
POINT_2D,PNT3,X2+X2-X1,Y2+Y2-Y1;
```
```
CALL,RECPNT,PNT2,PNT3;
```
```
ENDIF;
```
```
ENDMACRO;
```
```
MACRO,RECTANGLE,P1,P3;
```
```
DECLARE,P1,POINT_2D;
```
```
DECLARE,P3,POINT_2D;
```
```
ASSIGN,X1,P1/XCOORD;
```
```
ASSIGN,Y1,P1/YCOORD;
```
```
ASSIGN,X3,P3/XCOORD;
```
```
ASSIGN,Y3,P3/YCOORD;
```
```
POINT_2D,P2,X1,Y3;
```
```
POINT_2D,P4,X3,Y1;
```
CONTOUR,CNT,P1
/LINEEND = P2
/LINEEND = P3
/LINEEND = P4
```
/LINEEND = P1;
```
```
PRESENT,CNT;
```
```
ENDMACRO;
```
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
17.4.9 Change Colour in Drawing by Using Geometry Macro
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
Copyright © 1993-2005 AVEVA AB
Example 9
This macro is supposed to be started from the General Diagrams application.
All cables without interference class and component defined will be drawn red.
All cables with both interference class and component defined will be drawn green.
All cables with either interference class or component defined will be drawn blue.
The same function for Equipments with the data room and component.
```
MACRO, OUTF_DIAG_COLOUR;
```
! Declarations
```
DECLARE, A1, STRING;
```
```
DECLARE, COMPNAME, STRING;
```
```
DECLARE, DELIM, STRING;
```
```
DECLARE, DWG, STRING;
```
```
DECLARE, E1, EXTRACT;
```
```
DECLARE, INDEX, INTEGER;
```
```
DECLARE, INT_C, STRING;
```
```
DECLARE, LOOPMAX, INTEGER;
```
```
DECLARE, MODNAME, STRING;
```
```
DECLARE, PROJ, STRING;
```
```
DECLARE, ROOM, STRING;
```
```
DECLARE, STAT, INTEGER;
```
```
DECLARE, SUB1, STRING;
```
```
DECLARE, SUB2, STRING;
```
```
DECLARE, SUB3, STRING;
```
! Initiate
```
ASSIGN, DELIM,'-';
```
! Get the drawing name
```
DRAWING_NAME,DWG;
```
! Use data extraction to see which cables that are drawn in the diagram
```
ASSIGN,A1,'DRA(DWG).VIE(*).NCABLE';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(LOOPMAX,STAT,E1,DWG,,);
```
```
IF,STAT == 1;
```
```
LOOP,INDEX,1:LOOPMAX;
```
```
ASSIGN,A1,'DRA(DWG).VIE(*).CABLE(INDEX).NAME';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(MODNAME,STAT,E1,DWG,,INDEX,);
```
```
IF,STAT == 1;
```
! Get the cable data by using data extraction
```
SPLIT,MODNAME,DELIM,PROJ,CAB_SYS,CAB_NAM,SUB2,SUB3;
```
```
ASSIGN,CABLE_NAME,CAB_SYS&DELIM&CAB_NAM;
```
```
ASSIGN,A1,'CABLE(PROJ).CAB_M(CABLE_NAME). COMP_N';EXTRACT,E1,A1;
```
```
GET/EXTRACT=(COMPNAME,STAT,E1,PROJ,
```
```
CABLE_NAME,);
```
```
IF,STAT == 0;
```
```
ASSIGN,COMPNAME,'';
```
```
ENDIF;
```
ASSIGN,A1,
```
'CABLE(PROJ).CAB_M(CABLE_NAME).EL_PROP.INT_C';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(INT_C,STAT,E1,PROJ,CABLE_NAME,,);
```
```
IF,STAT == 0;
```
```
ASSIGN,INT_C,'';
```
```
ENDIF;
```
! Draw cables without any data red
```
IF,COMPNAME == '' AND INT_C == '';
```
CHANGEDRAW,'CABLE',MODNAME
```
/MARKINGCOLOUR='RED';
```
```
ELSE;
```
! Draw cables with all data green
```
IF,COMPNAME /= '' AND INT_C /= '';
```
CHANGEDRAW,'CABLE',MODNAME
```
/MARKINGCOLOUR='GREEN';
```
! Draw ca bles with some date blue
```
ELSE;
```
CHANGEDRAW,'CABLE',MODNAME
```
/MARKINGCOLOUR='BLUE';
```
```
ENDIF;
```
```
ENDIF;
```
```
ENDIF;
```
```
ENDLOOP;
```
ENDIF,
! Use data extraction to see which equipments that are drawn in the diagram
```
ASSIGN,A1,'DRA(DWG).VIE(*).NEQUIP';
```
User's Guide Vitesse
```
Chapter: The Tribon Geometry Macro Facility
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(LOOPMAX,STAT,E1,DWG,,);
```
```
IF,STAT == 1;
```
```
LOOP,INDEX,1:LOOPMAX;
```
```
ASSIGN,A1,'DRA(DWG).VIE(*).EQUIP(INDEX).NAME';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(MODNAME,STAT,E1,DWG,,INDEX,);
```
```
IF,STAT == 1;
```
! Get the equipment data by using data extraction
```
SPLIT,MODNAME,DELIM,PROJ,EQ_NAME,SUB1,SUB2,SUB3;
```
```
ASSIGN,A1,'EQUIP(PROJ).ITEM(EQ_NAME).COMP_N';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(COMPNAME,STAT,E1,PROJ,EQ_NAME,);
```
```
IF,STAT == 0;
```
```
ASSIGN,COMPNAME,'';
```
```
ENDIF;
```
```
ASSIGN,A1,'EQUIP(PROJ).ITEM(EQ_NAME).ROOM';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(ROOM,STAT,E1,PROJ,EQ_NAME,);
```
```
IF,STAT == 0;
```
```
ASSIGN,ROOM,'';
```
```
ENDIF;
```
! Draw equipment items without any data red
```
IF,COMPNAME == '' AND ROOM == '';
```
CHANGEDRAW,'EQUIP',MODNAME/
```
MARKINGCOLOUR='RED';
```
```
ELSE;
```
! Draw equipment items with all data green
```
IF,COMPNAME /= '' AND ROOM /= '';
```
CHANGEDRAW,'EQUIP',MODNAME
```
/MARKINGCOLOUR='GREEN';
```
! Draw equipment items with some date blue
```
ELSE;
```
CHANGEDRAW,'EQUIP',MODNAME
```
/MARKINGCOLOUR='BLUE';
```
```
ENDIF;
```
```
ENDIF;
```
```
ENDIF;
```
```
ENDLOOP;
```
ENDIF,
```
ENDMACRO;
```
The following macro would change the colours of the equipments and cables back to be the one defined by the default file.
```
MACRO, OUTF_DIAG_DEFAULT;
```
! Declarations
```
DECLARE, A1, STRING;
```
```
DECLARE, DWG, STRING;
```
```
DECLARE, E1, EXTRACT;
```
```
DECLARE, INDEX, INTEGER;
```
```
DECLARE, LOOPMAX, INTEGER;
```
```
DECLARE, MODNAME, STRING;
```
```
DECLARE, STAT, INTEGER;
```
! Get the drawing name
```
DRAWING_NAME,DWG;
```
! Use data extraction to see which cables that are drawn in the diagram
```
ASSIGN,A1,'DRA(DWG).VIE(*).NCABLE';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(LOOPMAX,STAT,E1,DWG,,);
```
```
IF,STAT == 1;
```
```
LOOP,INDEX,1:LOOPMAX;
```
```
ASSIGN,A1,'DRA(DWG).VIE(*).CABLE(INDEX).NAME';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(MODNAME,STAT,E1,DWG,,INDEX,);
```
```
IF,STAT == 1;
```
CHANGEDRAW,'CABLE',MODNAME
```
/MARKINGCOLOUR='DEFAULT';
```
```
ENDIF;
```
```
ENDLOOP;
```
```
ENDIF;
```
! Use data extraction to see which equipments that are drawn in the diagram
```
ASSIGN,A1,'DRA(DWG).VIE(*).NEQUIP';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(LOOPMAX,STAT,E1,DWG,,);
```
```
IF,STAT == 1;
```
```
LOOP,INDEX,1:LOOPMAX;
```
```
ASSIGN,A1,'DRA(DWG).VIE(*).EQUIP(INDEX).NAME';
```
```
EXTRACT,E1,A1;
```
```
GET/EXTRACT=(MODNAME,STAT,E1,DWG,,INDEX,);
```
```
IF,STAT == 1;
```
CHANGEDRAW,'EQUIP',MODNAME
```
/MARKINGCOLOUR='DEFAULT';
```
```
ENDIF;
```
```
ENDLOOP;
```
```
ENDIF;
```
```
ENDMACRO;
```
Copyright © 1993-2005 AVEVA AB
18 User Defined Simple Rules in Forms
When a drawing form is created it is possible to define a set of simple rules in the form for automatic addition of information to the drawing. E.g. when a burning sketch is added to thedrawing form this feature facilitates setting of texts with information extracted from the nesting.
```
The rules are defined by a number preceded by a $ sign ("$ values"). The text corresponding to the rule number will be positioned in the drawing form as indicated by the $ value.
```
```
A great number of rules with predefined meaning already exist already since long (e.g. rules used in Tribon Hull Plate Nesting forms- see User's Guide Plate Nesting, Nesting System -Application Functions SAVE FORM).
```
It is also possible for the customer to create new rules with the meaning as defined by him. The rule numbers of these $ values should be in the interval 10000 - 10999. The texts createdby the user-defined rules are all defined in a Vitesse script called _TBhook_Formula.py. When such a rule is recognised in the drawing form this Vitesse script will be called upon. Vitesse
commands corresponding to the user-defined rule will then be evaluated in order to create a text that will be put into the drawing form.
User defined rules are supported in for example the Tribon Nesting system. When a user-defined rule is evaluated the Vitesse script _TBhook_Formula.py is supplied with the modelcontext and the formula number. After the user defined Vitesse commands for the formula have been executed, a formula value will be returned as a text string.
Another form of rules is also supported by Vitesse script _TBhook_Formula.py. Those rules may be called user-implemented rules. They will all have a specific purpose defined in Tribondocumentation. However, the user is free to implement the rules by Vitesse commands in _TBhook_Formula.py. The rule numbers for those predefined rules are in the interval 5000 -
5999. User implemented rules may be supplied with extra input and may also return extra output beside the formula value text.
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
18.1 Vitesse Script Example
This script is an example of _TBhook_Formula.py. The script text contains a detailed guideline for implementation of new formulas together with some formula examples.
The example script can be found here:
TBhook_Formula_py.txt
User's Guide Vitesse
```
Chapter: User Defined Simple Rules in Forms
```
Copyright © 1993-2005 AVEVA AB
19 Project Copy COM Interfaces
```
Tribon Project Copy is implemented as a COM server, available for use in any automation-enabled language. This means that it can be used in Visual Basic, Visual Basic Scripting,JavaScript, C++ etc. It can also be used from Python (requires COM support for Python, win32com). Tribon Project Copy provides a number of COM interfaces that enables customers to
```
write custom applications and scripts that make use of the functionality of Tribon Project Copy. The methods of these COM interfaces are described in this section.
User's Guide Vitesse
Copyright © 1993-2005 AVEVA AB
19.1 Sisterships COM interface
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT SlaveImport()
```
Import the objects according to the effectivity specification into the current project. This requires an Oracle project and that the current project is a slave project.
```
HRESULT ResultFile(BSTR* filename)
```
Return the name of the result file.
Output parameters:
filename BSTR Result file name
Copyright © 1993-2005 AVEVA AB
19.2 Interface ITBTransferSet
This interface is the topmost interface in Tribon Project Copy. The ITBTransferSet interface is used as an entry point to obtain interfaces for object selection, archiving etc.
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT GetSelection(EAction mode, BSTR transferSetDir, VARIANT srcProjEnv, ITBSelection** pItf)
```
Get An ITBSelection interface.
Input parameters:
```
mode EAction Copy mode (kExport, kImport or kVerify)
```
transferSetDir BSTR Transfer set location
```
srcProjEnv VARIANT Source project info (optional). This is only valid if mode=kDirectImport. Must be VT_EMTPTY otherwise. If supplied, it should be an array with thefollowing information:
```
```
arr[0] = project server host (BSTR)
```
```
arr[1] = project group (BSTR)
```
```
arr[2] = project name (BSTR)
```
```
arr[3] = subjproject name BSTR)
```
```
arr[4] = project type (long). This is not used.
```
```
arr[5] = Oracle user name BSTR). Empty if soruce project is a native project.
```
```
arr[6] = Oracle password (BSTR) Empty if source project is a native project.
```
Output parameters:
pItf ITBSisterShip Interface pointer
```
HRESULT GetArchive(BSTR archiveDir, ITBArchive** pItf)
```
Get an ITBArchive interface.
Input parameters:
archiveDir BSTR Transfer set location
Output parameters:
pItf ITBSelection Interface pointer
```
HRESULT GetOptions(ITBOptions** pOptions)
```
Get an interface to the copy options.
Output parameters:
pOptions ITBOptions** ITBOptions interface.
```
HRESULT GetDrawingTypes(ITBDrawingTypes** pTypes)
```
Get an ITBDrawingTypes interface.
Output parameters:
PTypes ITBDrawingTypes** ITBDrawingTypes interface.
```
HRESULT Label(BSTR label)
```
Set transfer set label..
Input parameters:
label BSTR Transfer set label.
```
HRESULT Comment(BSTR comment)
```
Set transfer set comment.
Input parameters:
comment BSTR Transfer set comment.
Copyright © 1993-2005 AVEVA AB
19.3 Interface ITBTransferSet2
This interface extends ITBTransferSet with the methods below:
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT OpenProject (BSTR user, BSTR password)
```
Call this method supply login credentials to perform an Oracle login without user interaction. This requires an Oracle project.
Input parameters:
mode BSTR Oracle user name
password BSTR Oracle password
```
HRESULT SisterShipMode (VARIANT_BOOL bMode)
```
Call this method to make Project Copy run in Sistership mode. This requires an Oracle project.
Input parameters:
bMode VARIANT_BOOL Sisterhship mode
```
HRESULT GetSisterShip (BSTR logDir, VARIANT srcProjEnv, ITBSisterShip** pltf)
```
Get an ITBSisterShip interface. This requires an Oracle project.
Input parameters:
logDir BSTR Log file location
srcProjEnv VARIANT Source project info. See
```
ITBTransferSet::GetSelection()
```
Output parameters:
pltf ITBSisterShip Interface pointer
Copyright © 1993-2005 AVEVA AB
19.4 Interface ITBSearch Criteria
This interface can be used to specify search criteria during the object selection process. The ObjectType property is mandatory and the possible values are listed below. If ObjectType iskDrawing, then the DrawingType property also has to be given.
The possible values of the DrawingType property can be found in Tribon Toolkit Preferences, on the Drawing Types page in the Code column.
```
The ObjectName, Module, System and Block properties may be given with wildcards (using an asterisk character '*') and no value means '*'. Setting zero, one or both of the FromDateand ToDate properties can specify a date interval.
```
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
Selectable objects types
kAssembly kAssemblyStd kBasicStd
kCable kCableway kCompartment
kComponent kComponentVolume kCoordTable
kCurve kCurvedPanel kDiagram
kDiagramStencil kDiagramTemplate kDrawing
kDwgStdDetail kDwgStdHatchPattern kEquipment
kHullReferencePlane kHullStd kOutfitStd
kPinJig kPipe kPipeSpec
kPipeline kPlacedVolume kPlane
kPlanePanel kPlateNesting kPoint
kProfileNesting kRSO kRawPlate
kSeam kShellPlate kShellStiffener
kStdStructure kStructure kSurface
kTPOCunused kUnkplacedVolume kVentilation
```
HRESULT ObjectType(EObjectType* pVal)
```
Get-property of object type.
Output parameters:
pVal EObjectType* Object type
```
HRESULT ObjectType(EObjectType newVal)
```
Put-property of object type.
Input parameters:
newVal EObjectType Object type
```
HRESULT ObjectName(BSTR* pVal)
```
Get-Property of object name.
Output parameters:
pVal BSTR* Object name
```
HRESULT ObjectName(BSTR newVal)
```
Put-Property of object name.
Input parameters:
newVal BSTR Object name
```
HRESULT Module(BSTR* pVal)
```
Get-Property of module name.
Output parameters:
pVal BSTR* Module name
```
HRESULT Module(BSTR newVal)
```
Put-property of module name.
Input parameters:
NewVal BSTR Module name
```
HRESULT System(BSTR* pVal)
```
Get-property of system name.
Output parameters:
pVal BSTR* System name
```
HRESULT System(BSTR newVal)
```
Put-property of system name.
Input parameters:
newVal BSTR System name
```
HRESULT Block(BSTR* pVal)
```
Get-property of block name.
Output parameters:
pVal BSTR* Block name
```
HRESULT Block(BSTR newVal)
```
Put-property of block name.
Input parameters:
newVal BSTR Block name
```
HRESULT FromDate(DATE* pVal)
```
Get-property of beginning of date interval.
Output parameters:
pVal DATE* Date
```
HRESULT FromDate(DATE newVal)
```
Put-property of beginning of date interval.
Input parameters:
newVal DATE Date
```
HRESULT ToDate(DATE* pVal)
```
Get-property of end of date interval.
Output parameters:
pVal DATE* Date
```
HRESULT ToDate(DATE newVal)
```
Put-property of end of date interval.
Input parameters:
newVal DATE Date
```
HRESULT DrawingType(long* pVal)
```
Get-property of drawing type.
Output parameters:
pVal long* Drawing type
```
HRESULT DrawingType(DATE newVal)
```
Put-property of drawing type.
Input parameters:
newVal long Drawing type
```
HRESULT GetBox(ITBBox* pBox)
```
Get the current box.
Input parameters:
pBox ITBBox* ITBBox interface.
```
HRESULT SetBox(ITBBox* pBox)
```
Set the current box.
Input parameters:
pBox ITBBox* ITBBox interface
```
HRESUTL Clear()
```
Clear this search criteria.
Copyright © 1993-2005 AVEVA AB
19.5 Interface ITBSelection
The ITBSelection interface can be used to export objects from current project to a transfer set, import objects into current project from a transfer set and verify references within currentproject. It has methods to build a collection of Tribon objects and to extend the collection with referred objects.
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT ResultFile(BSTR* filename)
```
Return the name of the result file.
Output parameters:
filename BSTR Result file name.
```
HRESULT GetSearchCriteria(ITBSearchCriteria** pCrit)
```
Get an ITBSearchCriteria interface.
Output parameters:
pCrit ITBSearchCriteria** ITBSearchCriteria interface
```
HRESULT GetFilter(ITBFilter** pFilter)
```
Get an ITBFiler interface.
Output parameters:
pFilter ITBFiler** ITBFilter interface. For Oracle projects only.
```
HRESULT Load(BSTR filename)
```
```
Loads a (previously saved) object selection from disk.
```
Input parameters:
filename BSTR file name
```
HRESULT Save(BSTR filename)
```
Saves current object selection to disk.
Input parameters:
filename BSTR file name
```
HRESULT Export()
```
Export objects in current selection.
```
HRESULT Import()
```
Import objects in current selection.
```
HRESULT Verify(BOOL bRemoveBrokenRefs)
```
Verify objects in current selection.
Input parameters:
bRemoveBrokenRefs BOOL FALSE: log broken references
```
TRUE: remove broken references
```
```
HRESULT VerifyProject(BOOL bRemoveBrokenRefs)
```
Verify all objects in current project.
Input parameters:
bRemoveBrokenRefs BOOL FALSE: log broken references
```
TRUE: remove broken references
```
```
HRESULT CollectAll()
```
Adds all objects to the selction.
```
HRESULT AddObjects(ITBSearchCriteria* pCrit)
```
Add objects to current object selection.
Input parameters:
pCrit ITBSearchCriteria Search criteria
```
HRESULT GetObjects(ITBSearchCriteria* pCrit, BSTR* pXML)
```
Search for objects.
Input parameters:
pCrit ITBSearchCriteria Search criteria
Output parameters:
pXML BSTR* XML document with object names
```
HRESULT AddObjectsByTBQuery(ITBFilter* pFilter)
```
Add objects to current object selection using TBQuerySrv. This requires an Oracle project.
Input parameters:
pFilter ITBFilter*
```
HRESULT GetObjectsByTBQuery(ITBFilter* pFilter, BSTR* pXML)
```
Search for standard objects.
Input parameters:
pFilter ITBFilter* Add objects to curren object selection using TBQuerySrv. This requires an Oracle project.
Output parameters:
pXML BSTR* XML document with obejct names
```
HRESULT RemoveObjects(ITBSearchCriteria* pCrit)
```
Remove objects from current object selection.
Input parameters:
pCrit ITBSearchCriteria Search criteria
```
HRESULT AddDeletedObjects(ITBSearchCriteria* pCrit)
```
Add delete-marked object to current object selection. This requires an Oracle project.
Input parameters:
pCrit ITBSearchCriteria Search criteria
```
HRESULT GetDeletedObjects(ITBSearchCriteria* pCrit, BSTR* pXML)
```
Search for delete-marked objects. This requires an Oracle project.
Input parameters:
pCrit ITBSearchCriteria Search criteria
Output parameters:
pXML BSTR XML document with object names
```
HRESULT RemoveDeletedObjects(ITBSearchCriteria* pCrit)
```
Remove delete-marked objects from current object selection. This requires an Oracle project.
Input parameters:
pCrit ITBSearchCriteria Search criteria
```
HRESULT RemoveObjectsByTBQuery(ITBFilter* pFilter)
```
Remove objects from current object selection using TBQuerySrv. This requires an Oracle project.
Input parameters:
pFilter ITBFilter Pointer to an ITBFilter interface that contains search criteria.
```
HRESULT ExtendAll()
```
Extend selection with referred objects from all objects in current collection.
```
HRESULT ExtendSelection(BSTR objectName, EObjectType objectType, long subType)
```
Extend selection with references from a single obejct. The object is required to be part of the current selection prior calling this method.
Input parameters:
objectName BSTR object name
objectType EObjectType obejct type
```
subType long Drawing type (used for drawings only).
```
```
HRESULT GetReferredObjects(BSTR objectName, EObjectType objectType, long subType, BSTR* pXML)
```
Get referred objects from a single object. The object is required to be part of the current selection prior calling this method.
Input parameters:
objectName BSTRA object name
objectType EObjectType object type
```
subType long Drawing type (used for drawings only).
```
Output parameters:
pXML BSTR* XML document with object names
```
HRESULT GetSelection(BSTR* pxmlSelection)
```
Return the current selection as an XML document.
Output parameters:
pxmlSelection BSTR* current selection
```
HRESULT SetSelection(BSTR xmlSelection)
```
Replace the current selection.
Input parameters:
xmlSelection BSTR new object selection
```
HRESULT AppendSelection(BSTR xmlSelection)
```
Append objects to the current selection.
Input parameters:
xmlSelection BSTR object selection to append
Copyright © 1993-2005 AVEVA AB
19.6 Interface ITBOptions
This interface can be used to modify the copy options. The copy options are defined by the EExpOptions enum below. For more information about copy options, please refer todocumentation of Project Copy User's Guide.
All options can have a value of either EO_NO or EO_YES, except the options listed below:
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
typedef enum EExpOptions
```
{
```
//
```
// General options (both import & export)
```
//
```
tbVerifyRefs = 1,
```
tbRemoveAssemblyRefs tbIncludeAssemblyDrawings
tbIncludeAssemblyWelds
= 2,
= 3,
= 4,
tbIncludePPanelProdObjects tbIncludeCPanelProdObjects = 6,
= 7,
```
tbIncludeShPlateProdObjects = 8,
```
tbExpAutoIncludePipeSpools tbExpAutoIncludePipeSketche = 10,
= 11,
tbPlateNestData tbProfNestData = 12,
= 13,
```
tbSameSurface = 14,
```
```
tbIncludeStructProdObjects = 15,
```
tbResultFileLevel
tbWriteTraceFile
= 998,
= 999,
//
// Export Options
//
//
// Import Options
//
tbImpIncludePenetrations
= 2101,
tbImpRemoveAssemblySubassemblies tbImpRemoveAssemblyParts = 2301,
= 2302,
```
tbImpSimpleShStiffCopy = 2305,
```
```
} EExpOptions;
```
Option name Possible values
tbVerifyRefs EO_OFF
EO_LOG_BROKEN
EO_REMOVE_BROKEN
tbWriteTraceFile EO_LEVEL_NONE
EO_LEVEL_ALL
tbResultFileLevel EO_LEVEL_NONE
EO_LEVEL_ALL
EO_LEVEL_ERRORS_ONLY
```
HRESULT Option(EExpOptions propName, long *pVal)
```
Get-property of a copy option.
Input parameters:
propName EExpOption copy option id
Output parameters:
pVal long* copy option value
```
HRESULT Option(EExpOptions propName, long newVal)
```
Put-property of a copy option
Input parameters:
propName EExpOption coopy option id
newVal long new copy option value
```
HRESULT Options(BSTR* pXML)
```
Get-property of all copy options.
Output parameters:
pXML BSTR* copy options as XML
```
HRESULT Options(BSTR xml)
```
Put-property of all copy options.
Input parameters:
xml BSTR copy options as XML
Copyright © 1993-2005 AVEVA AB
19.7 Interface ITBFilter
The ITBFilter interface can be used to define a search filter, which uses TBQuery as search engine. The AddFilter method uses the same argument types as the corresponding AddFiltermethod in TBQuery. Please refer to the documentation of TBQuery for a description of available search fields, operators and possible values.
```
Note: This search mechanism is only available for Oracle projects.
```
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT AddFilter(TrdFieldNameEnum Field, TrdOperEnum Operator, VARIANT Value, VARIANT Value2)
```
Add a search critera to this filter.
Input parameters:
Field TrdFieldName Enum
Operator TrdOpoerEnum
Value VARIANT
Value2 VARIANT optional
```
HRESULT ClearFilters()
```
Clear all search fields.
Copyright © 1993-2005 AVEVA AB
19.8 Interface ITBArchive
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT ArchiveProject()
```
Archive the current project.
```
HRESULT ResultFile(BSTR* filename)
```
Return the name of the result file.
Output parameters:
filename BSTR Result file name
Copyright © 1993-2005 AVEVA AB
19.9 Interface ITBSisterShip
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
HRESULT SlaveImport()
```
Import the objects according to the effectivity specification into the current project. This requires an Oracle project and that the current project is a slave project.
```
HRESULT ResultFile(BSTR* filename)
```
Return the name of the result file.
Output parameters:
filename BSTR Result file name
Copyright © 1993-2005 AVEVA AB
19.10 Project Copy Example Scripts
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
Copyright © 1993-2005 AVEVA AB
19.10.1 How to Select Project from a Script
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
Example 1:
Select a native project called M3SP, defined in a project group called 'M3 Projects' on the default project server machine.
```
Set ps = CreateObject("Tbprojectselect.TBProjSelect")
```
ps.SelectProjectBatch "M3 Projects", "M3SP", ""
Example 2:
Select an Oracle project called M3SP, defined in a project group called 'M3 TDM' on machine 'PServer'.
```
Set ps = CreateObject("Tbprojectselect.TBProjSelect")
```
ps.ProjectServerHost = "PServer"
ps.User = "TBUSER"
ps.Password = "TBUSER"
ps.SelectProjectBatch "M3 TDM", "M3SP", ""
Copyright © 1993-2005 AVEVA AB
19.10.2 How to Use Tribon Project Copy from a Script
```
Before any objects are exported or imported, a copy session must be initialized with an action parameter and the transfer set location. This is done with a call to BeginSelect(EAction
```
```
mode, BSTR transferSetDir), where mode is set to kExport, kImport or kVerify.
```
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
Example 1:
Export drawings named '*DWG*' and all cableways in module 'MA' from current project.
<job>
<reference object="Tbtransfer.TBTransferSet"/>
<script language="VBScript">
'
' Create a TBTransferSet object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
ts.Label = "export label"
ts.Comment = "export comment"
```
set sel = ts.GetSelection(kExport, "c:\temp\xfer")
```
set crit = sel.GetSearchCriteria
crit.ObjectType = kDrawing
crit.DrawingType = 1
crit.ObjectName = "*DWG*"
sel.AddObjects crit
crit.ObjectType = kCableway
crit.ObjectName = "*"
crit.Module = "MA"
sel.AddObjects crit
sel.Export
```
MsgBox ("Export finished")
```
</script>
</job>
Example 2:
Import a complete transfer set into current project.
<job>
<reference object="Tbtransfer.TBTransferSet"/>
<script language="VBScript">
'
' Create a TBSelection object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
```
set sel = ts.GetSelection(kImport, "c:\temp\xfer")
```
sel.CollectAll
sel.Import
```
MsgBox ("Import finished")
```
</script>
</job>
Example 3:
Export from a specified project and import into another project.
<job>
<reference object="Tbtransfer.TBTransferSet"/>
<script language="VBScript">
'
' Select source project
'
```
Set ps = CreateObject("Tbprojectselect.TBProjSelect")
```
ps.SelectProjectBatch "Local projects", "sp", ""
'
' Create a TBSelection object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
```
set sel = ts.GetSelection(kExport, "c:\temp\xfer")
```
set crit = sel.GetSearchCriteria
crit.ObjectType = kCableway
crit.ObjectName = "*"
crit.Module = "MA"
sel.AddObjects crit
sel.Export
```
MsgBox ("Export finished")
```
'
' Select destination project
'
ps.SelectProjectBatch "Local projects", "empty", ""
'
' Create a new TBSelection object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
```
set sel = ts.GetSelection(kImport, "c:\temp\xfer")
```
sel.CollectAll
sel.Import
```
MsgBox ("Import finished")
```
</script>
</job>
Example 4:
Modify copy options from a script.
<job>
<reference object="Tbtransfer.TBTransferSet"/>
<script language="VBScript">
'
' Create a TBSelection object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
'
' Get an ITBOptions interface and change some copy options
'
set options = ts.GetOptions
```
options.Option(tbIncludeAssemblyWelds) = EO_NO
```
```
options.Option(tbIncludeAssemblyDrawings) = EO_YES
```
...
</script>
</job>
Example 5:
Export all objects that are modified by a certain user from a TDM project using ITBFilter as search criteria.
<job>
<reference object="Tbtransfer.TBTransferSet"/>
<script language="VBScript">
'
' Create a TBSelection object
'
```
set ts = CreateObject("tbtransfer.TBTransferSet")
```
```
set sel = ts.GetSelection(kExport, "c:\temp\xfer")
```
'
' Add objects via ITBFilter
'
set tbfilter = sel.GetFilter
tbfilter.AddFilter trdModifiedBy, trdOperEQ, "TBUSER"
sel.AddObjectsByTBQuery tbfilter
sel.Export
```
MsgBox ("Export finished")
```
</script>
</job>
Copyright © 1993-2005 AVEVA AB
19.10.3 Python Example
```
To make use of COM in Python, COM support for Python (win32com) must be installed. A Python wrapper class for the Project Copy type library has been created with the COM Makepyutility (called tbtransfer.py).
```
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
```
Example:
```
import tbtransfer
```
ts = tbtransfer.TBTransferSet()
```
```
sel = ts.GetSelection(tbtransfer.constants.kExport, "c:\\temp\\xfer")
```
```
crit = ts. GetSearchCriteria
```
crit.ObjectType = kCableway
crit.ObjectName = "*"
crit.Module = "MA"
sel.AddObjects crit
```
sel.Export()
```
Copyright © 1993-2005 AVEVA AB
19.10.4 Example Files
The above example scripts can be found as files in the ...Tribon\M3\bin\wsf directory.
 export_and_change_options.wsf
 export_and_import.wsf
 export_and_import_oracle.wsf
 export_cway.wsf
 export_via_filter.wsf
 import_all.wsf
 archive.wsf
User's Guide Vitesse
```
Chapter: Project Copy COM Interfaces
```
Copyright © 1993-2005 AVEVA AB
20 Vitesse Interface Quick Reference Index
User's Guide Vitesse
```
Assembly (kcs_assembly) Creation and manipulation of Assembly Structure and Part References
```
```
Cable Modelling (kcs_cable) Creation and manipulation of Cables, Cableways and Penetrations
```
```
Customisable User Interface (kcs_gui) Customisable User Interface
```
```
Customer Defined Attributes (kcs_att) Creation and manipulation Customer Defined Attributes
```
```
Database Listing (kcs_db) Listing of database objects
```
```
Data Extraction (kcs_dex) Extraction of model data
```
```
Drafting (kcs_draft) Creation and manipulation of Drawings
```
```
Hull Plane Panel Modelling (kcs_hullpan) Creation and manipulation of Planar Hull Panels
```
```
User Interface (kcs_ui) Simple user interface
```
```
Utility (kcs_util) Miscellaneous Utilities
```
```
Equipment (kcs_equip) Creation and manipulation of Equipment Items
```
```
Structure Modelling (kcs_struct) Creation and manipulation of Structure Items
```
```
Pipe Modelling (kcs_pipe) Creation and manipulation of Pipes and Parts
```
```
Placed Volume (kcs_placvol) Placing of volumes
```
```
Common Model Functions (kcs_model) Common model functions
```
```
Model Structures (kcs_modelstruct) Creation and manipulation of Model Structures
```
```
Hull Curved Modelling (kcs_chm) Curved Hulll modelling
```
```
Specifications (kcs_spec) Specifications
```
```
Weld Planning (kcs_weld) Weld Planning
```
```
Placed Volume (kcs_placvol) Creation and manipulation of volumes
```
Copyright © 1993-2005 AVEVA AB
21 Function Quick Reference Index
User's Guide Vitesse
```
Assembly (kcs_assembly)
```
```
assembly_activate(name) Acivates the given assembly. No assembly must be active
```
```
assembly_cancel() Cancel assembly
```
```
assembly_delete (name) Delete assembly
```
```
assembly_exist(name) Check if assembly exists
```
```
assembly_internal_name_get(pathName) Get internal name of assembly
```
```
assembly_keyin_ref_get (name) Get key in references
```
```
assembly_model_ref_get (name) Get model part references
```
```
assembly_move (newParentName) Move assembly
```
```
assembly_new (parentName, name) Create new assembly
```
```
assembly_parent_get (name) Get parent of assembly
```
```
assembly_path_name_create(parentName, name) Create path name of assembly
```
```
assembly_path_name_get(internalName) Get path name of assembly
```
```
assembly_properties_get(<name>) Get properties of assembly
```
```
assembly_properties_set (assembly) Set properties of assembly
```
```
assembly_save() Save assembly
```
```
assembly_sub_get(name) Get subordinates of assembly
```
```
assembly_wcog_calc() Calculate Weight & Centre of Gravity
```
```
document_reference_add(docRef) Add document reference for assembly
```
```
document_reference_get() Get document reference for assembly
```
```
document_reference_remove(docRef) Remove document reference from assembly
```
```
model_collect(keyin) Collect key in parts to assembly
```
```
model_collect(model) Collect model parts to assembly
```
```
model_decollect(keyin) Decollect key in parts from assembly
```
```
model_decollect(model) Decollect model parts from assembly
```
```
Customer Defined Attributes (kcs_att)
```
```
attribute_copy(Target, Attribute) Copy an attribute
```
```
attribute_create(Target, Category, Template) Create an attribute
```
```
attribute_detach(Target, Attribute) Detach an attribute from a drawing
```
```
attribute_edit(Target, Readonly) Edit attributes for a drawing
```
```
attribute_first_get(Target, Readonly, Iterator) Get the first attribute for model object
```
```
attribute_is(Attribute, Uuid) Check the type of an attribute
```
```
attribute_match(Target, Attribute, Convert) Check if an attribute matches the template
```
```
attribute_next_get(Iterator) Get the next attribute
```
```
attribute_title_get(Attribute) Get title of attribute
```
```
date_count_get(Attribute) Get the number of dates in attribute
```
```
date_get(Attribute, Index) Get date in attribute
```
```
date_set(Target, Attribute, Index, Seconds, Milliseconds) Set date in attribute
```
```
date_title_get(Attribute, Index) Get title of date
```
```
integer_count_get(Attribute) Get number of integers in attribute
```
```
integer_get(Attribute, Index) Get integer in attribute
```
```
integer_set(Target, Attribute, Index, Value) Set integer in attribute
```
```
integer_title_get(Attribute, Index) Get title of integer
```
```
model_save(Target) Save Target and releases the lock
```
```
real_count_get(Attribute) Get the number of reals in attribute
```
```
real_get(Attribute, Index) Get real in attribute
```
```
real_set(Target, Attribute, Index, Value) Set real in attribute
```
```
real_title_get(Attribute, Index) Get title of real
```
```
reference_count_get(Attribute) Get the number of references in attribute
```
```
reference_get(Attribute, Index) Get reference in attribute
```
```
reference_set(Target, Attribute, Index, Value) Set reference in attribute
```
```
reference_title_get(Attribute, Index) Get title of reference
```
```
string_count_get(Attribute) Get the number of strings in attribute
```
```
string_get(Attribute, Index) Get string in attribute
```
```
string_set(Target, Attribute, Index, Value) Set string in attribute
```
```
string_title_get(Attribute, Index) Get title of string
```
```
Cable Modelling (kcs_cable)
```
```
cable_activate (system, name) Activate a cable
```
```
cable_cancel() Cancel an active cable
```
```
cable_component_set (component name) Get component of current cable
```
```
cable_delete(system, name) Delete a cable
```
```
cable_document_reference_add (docRef) Adds a document reference to the active cable object
```
```
cable_document_reference_get () Returns a list of document references associated with the active cable
```
```
cable_document_reference_remove (docRef) Removes document reference from active cable object
```
```
cable_equipment_connect(equipment name, connection) Connect a cable to an equipment
```
```
cable_equipment_disconnect(connection) Disconnect a cable from an equipment
```
```
cable_exist (system, name) Check if a cable exists
```
```
cable_markpoint_set (mark point name) Set mark point information to current cable
```
```
cable_name_get() Get name of current cable
```
```
cable_new (system, name) Create new cable
```
```
cable_ready() Save with Ready checks
```
```
cable_save() Save an active cable
```
```
cable_system_get() Get system of current cable
```
```
Cableway Modelling (kcs_cway)
```
```
cpen_delete (name) Delete a cable penetration
```
```
cpen_document_reference_add (docRef, name) Add a document reference to the penetration object
```
```
cpen_document_reference_get (name) Returns a list of document references associated with thepenetration
```
```
cpen_document_reference_remove (docRef,name) Removes document reference from active cable object
```
```
cpen_imag_new (name, cableway name, point) Create a new imaginary cable penetration
```
```
cpen_real_new(name, cableway name, point, <component name>,<height>, <width>) Create a new real cable penetration
```
```
cpen_real_transform (name, T) Transform a real cable penetration
```
```
cway_activate (name) Activate an existing cableway
```
```
cway_cancel() Cancel modifications to a cableway
```
```
cway_check_cables() returns the number of cables on the cableway
```
```
cway_cwenv_clear () Reset list of cableways to connect to
```
```
cway_cwenv_connect ( ) Connect current cableway to other
```
```
cway_cwenv_incl (name) Add a cableway to list of allowed to connect to
```
```
cway_delete(name) Delete a cableway
```
```
cable_document_reference_add (docRef) Add a document feference to the active cableway object
```
```
cable_document_reference_get () Returns a list of document references associated with the activecableway
```
```
cable_document_reference_remove (docRef) Removes document reference srom active cableway object
```
```
cway_duplicate (from cableway) Duplicate cableway
```
```
cway_exist (name) Check if a cableway exists
```
```
cway_interference_exclude (class) Exclude interference class
```
```
cway_interference_permit (<class>) Permit interference class
```
```
cway_material_remove (start_id, end_id,) Material is removed on current cableway
```
```
cway_material_rotate ( part_id, angle ) cway_material_rotate ( part_id, vector ) Rotate material of cableway
```
```
cway_material_rotate_branch ( part_id, angle ) cway_material_rotate_branch ( part_id, vector ) Rotate branch of material on cableway
```
```
cway_material_set ( start_id, end_id, straight_material, <bend_material>,<start_distance>, <intermediate_distance>,<end_distance> )Set material of cableway
```
```
cway_name_get() Returns name of current cableway
```
```
cway_new (name, module, colour) Create a new cableway
```
```
cway_part_posno_set (posno, <id>) Set position number for part
```
```
cway_planning_unit_set (plu) Set planning unit of cableway
```
```
cway_ready() Make current cableway ready
```
```
cway_remove_cable(<cable system>, <cable name>) Remove cable from the cableway
```
```
cway_route_delete ( start_id, end_id ) Delete part of route
```
```
cway_route_point ( point ) Add intermediate point to route
```
```
cway_route_end_point ( <point> ) Set end point of route
```
```
cway_route_start_point ( <point> ) Set start point of route
```
```
cway_save() Save current cableway
```
```
cway_transform ( T ) Transform current cableway
```
```
default_value_get (statement) Get a default value
```
```
default_value_set (statement) Set a default value
```
```
Database Listing (kcs_db)
```
```
object_list_get(objectCriteria, databankName, resultList) Get list of objects from db
```
```
Data Extraction (kcs_dex)
```
```
extract(dexstring) Perform data extraction
```
```
get_box() Get box
```
```
get_commandstring() Get Data Extraction command string
```
```
get_indexedreal(index) Get value from real vector
```
```
get_int() Get integer value
```
```
get_real() Get real value
```
```
get_reavec2d() Get 2D real vector
```
```
get_reavec3d() Get 3D real vector
```
```
get_string() Get string
```
```
next_result() Get next result
```
```
Drafting (kcs_draft)
```
```
arc_highlight(Object) Highlight an arc
```
```
arc_new(Arc) Create a new arc
```
```
circle_highlight(Object) Highlight a circle
```
```
circle_new(Circle) Create a new circle
```
```
cloud_new(Parent, Shape) Create a new cloud primitive
```
```
colour_get(ModalColour) Get modal colour
```
```
colour_set(ModalColour) Set modal colour
```
```
component_capture(region) Return a list of handles to components captured by given region
```
```
component_identify(name) Get component handle by name
```
```
component_identify(point) Get component handle by point
```
```
component_new (<name>) Create a new component subpicture
```
```
conic_highlight(Object) Highlight a conic segment
```
```
conic_new(Conic) Create a new conic segment
```
```
contour_capture(region) Get contour handles by region
```
```
contour_highlight(Object) Highlight a contour
```
```
contour_identify(point) Get contour handle by point
```
```
contour_new(Contour) Create a new contour
```
```
contour_properties_get(handle, contour) Get properties of contour
```
```
cross_new(Parent, String, Line1, Line2) Create a new cross primitive
```
```
default_value_get(DefKeyword) Get drafting default value
```
```
default_value_set(DefStatement) Set drafting default value
```
```
delete_by_area (handles, act, contour) Delete everything inside or outside specified area
```
```
dim_capture(region) Get dimension handles by region
```
```
dim_angle_new(Line1, Line2, ArcPos, TextPos) Create a new 2D angular dimension
```
```
dim_diameter_new(CircleOrArc, Pos1, Pos2) Create a new 2D diameter dimension
```
```
dim_identify(point) Get dimension handle by point
```
```
dim_linear_new(Measpnts, Type, Dir, Pos) Create a new 2D dimension
```
```
dim_linear_new(polygon3D, type, projDir, locPoint2D, witnDir, <modelsubview>,<basepoint>)Create a new 3D dimension
```
```
dim_point_3d(point3D, locPoint, height, rotation, annotation, <modelsubview>) Create a new 3D point dimension
```
```
dim_radius_new(CircleOrArc, Pos1, Pos2) Create a new 2D radius dimension
```
```
dim_shell_new(Viewhandle,From, Along, To, <Type>, <Colour>) Add dimensioning from one model object to another along a third in a given view
```
```
document_reference_add (docRef) Add a document reference to the active drawing object
```
```
document_reference_get () Returns a list of document references associated with the active drawing
```
```
document_reference_remove (docRef) Removes document reference from ative drawing object
```
```
dwg_close() Close current drawing
```
```
dwg_current() Check if a drawing is current
```
```
dwg_delete(DwgName, <DwgType>) Delete a drawing
```
```
dwg_dxf_export(FileName, <ACVersion>, <Mode>, <nElemVisibility>, <nLayerVisibility>) Export current drawing in DXF format
```
```
dwg_dxf_import(FileName, DrawingName , <MapFileName>) Exports the current drawing to a 2D DXF file
```
```
dwg_dxf_3d_export(FileName, ViewSubviewsList, <DetailLevel>, <ACVersion>, <Mode>) Export all models in the given views and subviews to a 3D DXF Facet format
```
```
dwg_exist(DwgName, <DwgType>) Check if drawing exists
```
```
dwg_layers_is_hidden() Tests if application display mode is hide layer
```
```
dwg_layers_hidden_get () Returns list of layer that are hidden when application mode is hide layers
```
```
dwg_layers_is_shown () Tests if application display mode is show layer
```
```
dwg_layers_shown_get () Returns list of layer that are displayed when application mode is show layers
```
```
dwg_name_get() Get current drawing name
```
```
dwg_new(DwgName, <FormName>, <DwgType>) Create a new drawing and make it current
```
```
dwg_open(DwgName, <DwgType>, <OpenMode>, <DwgRevision>), <EnvelopeMode>) Open an existing drawing and make it current
```
```
dwg_pack() Pack the current drawing
```
```
dwg_print(options) Print current drawing
```
```
dwg_properties_set (PropRef) Removes document reference from active drawing object. More than one documentreference, the first found will be deleated.
```
```
dwg_purge() Purges the current drawing
```
```
dwg_repaint() Repaint drawing
```
```
dwg_reference_show (show, <views>) Show or collapse drawing reference
```
```
dwg_revision_freeze() Freeze latest revision of currnt drawing.
```
```
dwg_revision_new() Create new revision for current drawing. Previous 'current* revision is frozen.
```
```
dwg_revision_unfreeze() Unfreeze lates revision of current drawing.
```
```
dwg_save() Save current drawing
```
```
dwg_save_as('NewDwgName', <Databank>) Save current drawing with new name
```
```
dwg_status_set (StatusType, StatusValue) Changes status for current drawing
```
```
dwg_type_list_get() Returns all drawing types registered in the Tribon system as a Python dictionary
```
```
dwg_validate(OutOfDate, NotFound) Validate the current drawing and returns two lists of KCSModel
```
```
dwg_wmf_export(FileName) If no path is given, the file is created in current directory. If no extension is given, the defultextension .wmf will be used.
```
```
dwg_zoom() Zoom display of drawing
```
```
element_child_first_get(<subpictureHandle>) Get handle of first subordinate element
```
```
element_colour_get(handle, colour) Get colour of element
```
```
element_colour_set(Handle, Colour) Change colour of arbitrary element
```
```
element_copy(elementHandle, <targetSubpictureHandle>) Copy an element in drawing
```
```
element_delete(Handle) Delete element
```
```
element_extent_get(<ElementHandle>) Get extents of element
```
```
element_highlight(Handle) or element_highlight([Handles]) Highlight an arbitrary element
```
```
element_transformation_redefine (Handle, Transf2d) Redefines transformation for given element
```
```
view_capture(region) Get element handle by name
```
```
element_identify(Name) Return a handle to the entity in the current drawing
```
```
element_is_bodyplan_view (ViewPtr) Check whether the current picture is a BodyplanView
```
```
element_is_burning_sketch(elementHandle) Check if element is burning sketch subview
```
```
element_is_component(elementHandle) Check if element is component
```
```
element_is_contour(elementHandle) Check if element is contour
```
```
element_is_curpanel_view (ViewPtr) Check whether the current picture is a CurpanelView
```
```
element_is_detail_sketch (elementHandle) Check if element is detail sketch subview
```
```
element_is_detail_view (ViewPtr) Check whether the current picture is a Detail View
```
```
element_is_devpla_view (ViewPtr) Check whether the current picture is DevplaView
```
```
element_is_devsti_view (ViewPtr) Check whether the current picture is a DevstiView
```
```
element_is_dimension(elementHandle) Check if element is dimension
```
```
element_is_general_view (ViewPtr) Check Whether the current picture is a General View
```
```
element_is_hatch(elementHandle) Check if element is hatch
```
```
element_is_nesting(elementHandle) Check if element is nesting subview
```
```
element_is_note(elementHandle) Check if element is note
```
```
element_is_posno(elementHandle) Check if element is posno
```
```
element_is_shellx_view (ViewPtr) Check whether the current picture is a ShelxView
```
```
element_is_subpicture(elementHandle) Check if element is subpicture
```
```
element_is_subview(elementHandle) Check if element is subview
```
```
element_is_symbol(elementHandle) Check if element is symbol
```
```
element_is_symbolic_view (ViewPtr) Check whether the current picture is a Symbolic View
```
```
element_is_templ_view (ViewPtr) Check whether the current picture is a TemplView
```
```
element_is_text(elementHandle) Check if an element is a text
```
```
element_is_view(elementHandle) Check if element is view
```
```
element_layer_get(handle, layer) Get layer of element
```
```
element_layer_set(handle, layer) Set layer of element
```
```
element_linetype_get(handle, linetype) Get linetype of element
```
```
element_linetype_set(handle, linetype) Set linetype of element
```
```
element_parent_get(elementHandle) Get handle of parent element
```
```
element_sibling_next_get(elementHandle) Get handle of next sibling element
```
```
element_transform(elementHandle, <transf2d>) Transform an element in drawing
```
```
element_transformation_get (ElemHandle, Transf2D) Get the transformation of element in drawing
```
```
element_visibility_get (elementHandle) Set visibility of element specified by handle.
```
```
element_visibility_set (elementHandle, Visibility) Set visibility of element specified by handle.
```
```
ellipse_highlight(Object) Highlight an ellipse
```
```
ellipse_new(Ellipse) Create a new ellipse
```
```
form_name_get() Get the name of currently used drawing form
```
```
general_restr_symbol_new(Parent, StartPt, EndPt, Soft ) Create a new general restriction symbol primitive
```
```
geometry_capture(region) Get geometry handles by region
```
```
geometry_identify(point) Get geometry handle by point
```
```
hatch_capture(region) Get hatch handles by region
```
```
hatch_identify(point) Get hatch handle by point
```
```
hatch_island_new(HatchHandle, Island) Create a new hatch pattern island by contour
```
```
hatch_island_new(HatchHandle, IslandHandle) Create a new hatch pattern island by handle
```
```
hatch_new(ContHandle) Create a new hatch pattern component by contour handle
```
```
hatch_new(Contour) Create a new hatch pattern component by contour
```
```
hatch_pattern_set(Angle, Distance) Set modal hatch pattern
```
```
highlight_off(Handle) Turn off highlight
```
```
kcs_draft.model_handle_get(model) Get a handle to a model subview
```
```
layer_get() Get modal layer
```
```
layer_hide(layer) Hide a layer in drawing
```
```
layer_hide(layersList) Hide a list of layers in drawing
```
```
layer_set(Layer) Set modal layer
```
```
layer_show(layer) Show a layer in drawing
```
```
layer_show(layersList) Show a list of layers in drawing
```
```
layer_show_all() Show all layers in drawing
```
```
line_highlight(Object) Highlight a line
```
```
line_new(Line) Create a new line
```
```
linetype_display_settings_get() Return the line type display settings.
```
```
linetype_display_settings_set (modelLTDSettings) Set the line type display setting.
```
```
linetype_get(ModalLinetype) Get modal line type
```
```
linetype_set(ModalLinetype) Set modal line type
```
```
model_capture(region) Get model handles by region
```
```
model_colour_set(Model, Colour, <ViewHandle>) Set colour of model object in drawing
```
```
model_delete(Model, <ViewHandle>) Delete a model in drawing
```
```
model_draw(AssemblyCriteria, <viewhandle>) Draw an assembly
```
```
model_draw(model, <viewhandle>) Draw a model object
```
```
model_identify(IdPnt, Model) Get model handle by point
```
```
model_layer_set(model, layer) Set layer of model subview
```
```
model_layer_set(Model, Layer, <ViewHandle>) Set the layer of a model subview
```
```
model_object_revision_save(model, revision, view_handle, save_spools) Save a model object revision
```
```
model_object_revision_get(model, view_handle, list) List model object revision
```
```
model_object_revision_set(model, revision, view_handle) Displays model object revision
```
```
model_properties_get(handle, model) Get the properties of a model subview
```
```
note_capture(region) Get note handles by region
```
```
note_identify(point) Get note handle by point
```
```
note_new(Text, RefLine) Create a new note
```
```
note_symbol_get() Get modal note symbol
```
```
note_symbol_set(Symbol) Set modal note symbol
```
```
pipe_restr_symbol_new(Parent, StartPt, EndPt ) Create a new pipe restriction symbol primitive
```
```
point_capture(region) Get point handles by region
```
```
point_highlight(Object,<Type>) Highlight a point
```
```
point_identify(point) Get point handle by point
```
```
point_new(Point) Create a new point
```
```
point_transform(ViewHandle, ModelPnt, DwgPnt) Transform 3D point to 2D point in view
```
```
position_ruler_new (Act, View, StartPt, EndPt) Create different kinds of rulers
```
```
posno_capture(region) Get posno handles by region
```
```
posno_height_get() Get modal position number symbol height
```
```
posno_height_set(Height) Set modal position number symbol height
```
```
posno_identify(point) Get posno handle by point
```
```
posno_new(Text, RefLine) Create a new position number
```
```
posno_symbol_get() Get modal position number symbol
```
```
posno_symbol_set(Symbol) Set modal position number symbol
```
```
rectangle_highlight(Object) Highlight a rectangle
```
```
rectangle_new(rectangle, <radius>) Create a new rectangle
```
```
reference_move () Move reference symbol together with associated text to a new location
```
```
ruler_new(Parent, StartPt, TickLen, FirstTick, LastTick, LabelTick, TextProp) Create a new ruler primitive
```
```
rule_text_new(Text, RuleNo) Create a new text according to drawing rule
```
```
shd_autoscale() Auto scales a shaded view
```
```
shd_new(ViewHandle) Create a shaded view given a handle to a view
```
```
shd_projection_set(TransformationMatrix) Set the projection for a shaded view given a tranformation matrix
```
```
shd_zoom_box(BoxMinPoint, BoxMaxPoint) Zoom a shaded view given the min and max points of a 3D box
```
```
spline_highlight(Object) Highlight a spline
```
```
spline_new(Spline) Create a new spline
```
```
std_hatch_pattern_set(Type) Set modal standard hatch pattern
```
```
subpicture_current_get () Get current subpicture
```
```
subpicture_current_set (subpictureHandle) Set a subicture to be current for the creation of new geometry
```
```
subpicture_name_set(subpictureHandle, name) Set current subpicture
```
```
subpicture_insert(subpName, <parentHandle>), <databank='SBD_PICT'>) Insert a subpicture from databank
```
```
subpicture_name_get(subpictureHandle) Get the name of subpicture
```
```
subpicture_name_set(subpictureHandle, name) Set the name of subpicture
```
```
subpicture_save(subpHandle) Save a subpicture on databank
```
```
subview_capture(region) Return a list of handles to subviews captured by given region
```
```
subview_identify(name) Get subview handle by name
```
```
subview_identify(point) Get subview handle by point
```
```
subview_new (<name>) Create a new subview subpicture
```
```
symbol_capture(region) Get symbol handles by region
```
```
symbol_height_get() Get modal symbol height
```
```
symbol_height_set(Height) Set modal symbol height
```
```
symbol_identify(point) Get symbol handle by point
```
```
symbol_new(Font, SymbNo, Pos) Create a new symbol
```
```
symbol_new(Symbol) Create a new symbol
```
Get properties of symbol
```
symbol_rotation_get() Get modal symbol rotation
```
```
symbol_rotation_set(Rot) Set modal symbol rotation
```
```
text_capture(region) Get text handles by region
```
```
text_ascii_font_get() Get modal ASCII text font
```
```
text_ascii_font_set(Font) Set modal ASCII text font
```
```
text_aspect_get() Get modal text aspect
```
```
text_aspect_set(Aspect) Set modal text aspect
```
```
text_height_get() Get modal text height
```
```
text_height_set(Height) Set modal text height
```
```
text_identify(point) Get text handle by point
```
```
text_ilsp_get() Get modal text interline space factor
```
```
text_ilsp_set(Ilsp) Set modal text interline space factor
```
```
text_length(Text) Calculate the text length in specified font format
```
```
text_new(String, Pos) Create a new text
```
```
text_new(Text) Create a new text
```
```
text_properties_get(handle, text) Get properties of text
```
```
text_rotation_get() Get modal text rotation angle
```
```
text_rotation_set(Rot) Set modal text rotation angle
```
```
text_slant_get() Get modal text slant
```
```
text_slant_set(Slant) Set modal text slant
```
```
text_vector_font_get() Get modal vector font
```
```
text_vector_font_set(Vfont) Set modal vector font
```
```
userdef_hatch_pattern_set(Page, Detail) Set modal user defined hatch pattern
```
```
view_hl_remove(ViewHandle) Remove hidden lines in view
```
```
view_identify(IdPnt, <PictWinExt>) Get view handle by point
```
```
view_identify(ViewName, <PictWinExt>) Get view handle by name
```
```
view_move(ViewHandle, DeltaVec) Move a view
```
```
view_new(ViewName, <Uvect>, <Vvect>) Create a new view
```
```
view_projection_get (ViewHandle, Transf3D) Get the projection of a view
```
```
view_projection_set(ViewHandle, uVector, vVector, <DefaultDrawCode>) Set the projection of a view
```
```
view_reflect(ViewHandle, Reflect, Centre) Reflect a view
```
```
view_restriction_area_get(ViewHandle) Get the restriction area of a view
```
```
view_rotate(ViewHandle, RotAngle, Centre) Rotate a view
```
```
view_scale(ViewHandle, ScaleFac, Centre) Scale a view
```
```
view_slice_planes_get(handle) Return slice planes for symbolic view
```
```
view_slicedepth_get (ViewHandle) Get the slice depth of a sliced view
```
```
view_symbolic_model_tra(ViewHandle,Transf3D) Retrieve the model tranformation matrix for a given symbolic view
```
```
view_symbolic_new(ViewName, LocPoint, Uvect, Vvect, Forward, Backward, box)view_symbolic_new(SymbolicView)Create a symbolic view
```
```
zoom_extent_get() Get extent of current displayed area
```
```
Equipment (kcs_equip)
```
```
equip_activate(name) Activate equipment item
```
```
equip_alias_set(alias) Set the alias for equipment item
```
```
equip_cancel() Cancel current equipment item
```
```
equip_component_set(compname) Set the component for equipment item
```
```
equip_delete(name) Delete equipment item
```
```
equip_description_set(description) Set the description for equipment item
```
```
equip_exist(name) Check if equipment item exists
```
```
equip_module_get() Get the module of current equipment item
```
```
equip_name_get() Get the name of current equipment item
```
```
equip_new(module, name) Create new equipment item
```
```
equip_place(point, uvector, vvector) Place equipment item in model
```
```
equip_ready() Make equipment item ready for installation
```
```
document_reference_add (docRef) Add a document reference to the active equipment object
```
```
document_reference_get () Return a list of document references associated with the active equipment
```
```
document_reference_remove (docRef) Remove document reference from active equipment object
```
```
equip_room_set(room) Set the room for equipment item
```
```
equip_save() Save current equipment item
```
```
equip_transform(transformation) Transform equipment item
```
```
Customisable User Interface (kcs_gui)
```
```
accelerator_add(Key, SystemKeys, Function) Set Key as an accelerator key for Function
```
```
frame_title_set(Application, Format)
```
```
menu_add(Menu, Position, Caption)
```
```
menu_get(Menu, Position)
```
```
menu_item_get(Menu, Position)
```
```
menu_item_set(Menu, Position, Caption, Function)
```
```
menu_item_std_add(Menu, Position, Caption, Function)
```
```
menu_item_usr_add(Menu, Position, Caption, Script, Message)
```
```
menu_remove(Menu, Position)
```
```
toolbar_add(Caption)
```
```
toolbar_button_remove(Toolbar, Position)
```
```
toolbar_button_std_add(Toolbar, Position, Function, ImageFile, Tooltip, Message)
```
```
toolbar_button_usr_add(Toolbar, Position, Script, ImageFile, Tooltip, Message)
```
```
toolbar_get(Id)
```
```
Hull Curved Modelling (kcs_chm)
```
```
cpan_hole_create(PanelName, HoleOptions) Creates a new hole in a curved panel object
```
```
curve_principal_create(CurveName, Plane, MinPt, MaxPt, SurfName) Creates a shell curve or a shell seam
```
```
delete(Model) Delete a curved hull object
```
```
plate_prop_get(Obj) Get properties of a shell plate
```
```
plate_prop_set(Obj, Prop) Set properties of a shell plate
```
```
recreate(Model) Recreate a curved hull object
```
```
remarking_length(ObjectFrom, ObjectAlong, ObjectTo) Returns length between two objects along a third
```
```
remarking_length_ext(Activity, PanelName, ObjectFrom, ObjectAlong, ObjectTo) Returns length between two objects along a third with adjustments according to set flags
```
```
run_XML(XmlFileName, LogFileName) Generates a number of curved hull object described in the XML document
```
```
output_XML(ModelList, OutputFileName) Get the XML description of existing curved hull model objects
```
```
skip(Model) Skips a curved hull object, i.e. removes any locks set on the object and related objects
```
```
stiffener_combine(Stiff1, Stiff2) Combines two shell stiffeners into one
```
```
stiffener_prop_get(Obj) This is the shell stiffener to get data for.
```
```
stiffener_prop_set(Obj, Prop) This function will lock the shell stiffener.
```
```
stiffener_split(ObjToSplit, SplittingObj) Split a shell profile or a shell stiffener at a given postion
```
```
store(Model) Store a curved hull object
```
```
view_bodyplan_new(ViewOptions) Create a body plan view
```
```
view_curvedpanel_new(Panel, ViewOptions) Create a curved panel view
```
```
view_devpla_new(Plate) Create a shell profile view
```
```
view_modify(ViewHandle) Get the view options data for a given view
```
```
view_recreate(ViewHandle) Recreate a given view
```
```
view_shprof_new(Stiffener) Create a shell profile view
```
```
Hull Plane Panel Modelling (kcs_hullpan)
```
```
document_reference_add (docRef) =>document_reference_add (docRef, PanelName) Add a document refereence to the panel object
```
```
document_reference_get () =>document_reference_get (PanelName) Return a list of document references associated with the panel
```
```
document_reference_remove (docRef) =>document_reference_remove (docRef, PanelName) Removes document reference from panel object
```
```
group_get(panel,part_id) Get group number for given component
```
```
group_next(panel,act,group) Get next group number
```
```
pan_activate(ListOfPanels) Activate a number of panels
```
```
pan_copy(ListOfPanels, CopyPanOptions) Copy some of the currently activated panels
```
```
pan_curve_create( ) Return a curve statement to add in the current panel
```
```
pan_curve_store( ) Make curve object out of the contour and save it on the Tribon databank
```
```
pan_delete(ListOfPanels) Delete the panels indicated by "ListOfPanels"
```
```
pan_group_delete(panel_name,group) Delete a group of components from a panel
```
```
pan_group_divide(panel_name, group, ListOfModels) Move some components from a group into a new group
```
```
pan_init(scheme,ident) Initialize a new panel
```
```
pan_list_active( ) Get a list of all currently activated panels
```
```
pan_modify(panel,mode) Activate an existing panel
```
```
pan_move(ListOfPanels, MovePanOptions) Move all currently selected panels
```
```
pan_recreate(<ListOfPanels>) Recreate current panel
```
```
pan_remove_seam(panel_name, component) Remove a seam from a panel
```
```
pan_scheme_runmode_get( ) Get the current run mode options
```
```
pan_scheme_runmode_set(RunModeOptions) Set the current run mode options
```
```
pan_skip(ListOfPanels) Skip the current panel
```
```
pan_split(ListOfPanels, SplitPanOptions) Split all the currently activated panels
```
```
pan_sti_split_by_model(group, component_id) Split a group of stiffeners where they intersect another model
```
```
pan_sti_split_by_plane(group, plane) Split a group of stiffeners where they intersect a plane
```
```
pan_store(ListOfPanels) Store the current panel
```
```
pan_topology(Model, Act) Calculate the dependencies to/from a given model object
```
```
stmt_exec(group,statement) Add statement to current scheme and execute
```
```
stmt_get(panel,group) Get statement text for group
```
```
view_detail_new(act, component_handle) When a handle to a component is given, and create a detail view
```
```
view_symbolic_modify(ViewHandle, SymbolicViewOptions) View all options from an existing symbolic view
```
```
view_symbolic_recreate(ViewHandle) Recreate a symbolic view
```
```
Common Model Functions (kcs_model)
```
```
model_hull_contact (Model) Extract hull panels touched by structure or equipment
```
```
model_hull_interference_check (Model, Type, Range ) Return list of touched outfitting models of given type
```
```
model_properties_set (model, properties) Sets parameters of a model object
```
```
model_status_set(Model, StatusType, StatusValue) Changes status for given model
```
```
status_values_get(StatusType) Returns possible status values for given status type
```
```
tdm_strings_get (StatusType) Returns either the Planning Units or Cost Codes as specified by the user
```
```
Model Structures (kcs_modelstruct)
```
```
block_delete(name) Delete a hull block
```
```
block_new(name, MinPt3d, MaxPt3d) Create a new hull block
```
```
module_delete(name) Delete an outfitting module
```
```
module_new(name) Create a new outfitting module
```
```
system_delete(name) Delete an outfitting system
```
```
system_new(name, description, <SurfPrepCode>) Create a new outfitting system
```
```
Pipe Modelling (kcs_pipe)
```
```
default_bendobj_id_get() Get ID of default bending machine
```
```
default_bendobj_id_set(bendObjId) Set ID of default bending machine
```
```
default_value_get (Keyword) Get default value
```
```
default_value_set (Statement) Set default value
```
```
joint_add (PartId, Conn, Criteria) Add joint to part connection
```
```
joint_insert (PartId, Conn, Criteria) Insert joint in part
```
```
kcs_pipe.document_reference_add(docRef) Add document reference for pipe
```
```
kcs_pipe.document_reference_get() Get document reference for pipe
```
```
kcs_pipe.document_reference_remove(docRef) Remove document reference from pipe
```
```
part_add (PartId, Conn, Criteria, <SpecSearch>) Add part to pipe
```
```
part_add (PartId, Criteria, <SpecSearch>) Add part to pipe
```
```
part_boss_conn_type_set (PartId, Conn, Code) Set boss connection type for part
```
```
part_branch_get (PartId) Get branch for part
```
```
part_conn_coord_get(PartId, Conn, Point) Get connection coordinate for part
```
```
part_conn_find (PartId, Point) Get closest connection to given point
```
```
part_conn_part_get (PartId, Conn) Get part id connected to given connection of part
```
```
part_connect (PartId1, Conn1, Name, PartId2, Conn2) Connect a part to another part
```
```
part_connect (PartId1, Conn1, PartId2, Conn2) Connect a part to another part
```
```
part_delete (PartId) Delete a part
```
```
part_disconnect (PartId, Conn) Disconnect a part
```
```
part_end_excess_set (PartId, Conn, Excess, <Enable>) Set end excess for part
```
```
part_ext_structure_connect (PartId, Point, Structure) Connect a pipe part to a structure at a specific point on the structure part
```
```
part_ext_structure_disconnect (PartId, Structure) Disconnect the part from structure
```
```
part_ext_structure_disconnect (PartId) Disconnect the part from structure
```
```
part_feed_excess_set (PartId, <Enable>) Set feed excess for part
```
```
part_feed_min_set (PartId, Length, <Enable>) Set minimum feed excess for part
```
```
part_flip(PartId) Flip a part
```
```
part_incline(PartId, Vect) Inclines an existing part. Part flange type 2601.
```
```
part_insert (PartId, Conn, Criteria, <SpecSearch>) Insert a part
```
```
part_material_remove (PartId) Remove material from part
```
```
part_material_set (PartId1, <PartId2>, Prop, <SpecSearch>) Set material for part
```
```
part_properties_set (PartId, Prop) Set properties of a part
```
```
part_resize (Option, PartId, NomDia, [NomDia2]) Resize a part
```
```
part_respec (Option, PartId, SpecName, [NomDia2]) Respec a part
```
```
part_rotate (PartId, Conn, Angle) Rotate part
```
```
part_spool_get (Spoold) Get spool ID for part
```
```
part_spool_limit_set (PartId, Conn, <Enable>) Set spool limit for part
```
```
part_structure_connect (PartId, Structure, Alias) Connect pipe part to structure
```
```
part_structure_disconnect (PartId, Structure) Disconnect pipe part from structure
```
```
part_structure_get (PartId) Get name of structure connected to part
```
```
part_turn (PartId, Conn, Angle) Turn part
```
```
part_weldgap_delete (PartId) Delete weld gap for part
```
```
part_weldgap_edit (PartId, GapSize) Modify weld gap for part
```
```
part_weldgap_set (PartId, Conn, GapSize) Set weld gap for part
```
```
pipe_activate(Name) Activate a pipe
```
```
pipe_auto_spool_name_delete() Delete automatic spool names
```
```
pipe_auto_spool_name_set() Set automatic spool names
```
```
pipe_cancel() Cancel changes to current pipe
```
```
pipe_check (Check) Perform production checks
```
```
pipe_check_settings (Settings) Activate or deactivate pipe check functions
```
```
pipe_check_settings (Settings, PartId) Activate or deactivate pipe check functions
```
```
pipe_delete (Name) Delete a pipe
```
```
pipe_duplicate(Name, NewName) Create a copy of a pipe and stores it in the databank.
```
```
pipe_exist (Name) Check if a pipe exists
```
```
pipe_list () List a pipe
```
```
part_material_remove (PartId) Remove material from the current pipe
```
```
pipe_material_set (<BranchId>, Prop, <SpecSearch>) Set material for a pipe branch
```
```
pipe_mode_activate() Activate Pipe Mode
```
```
pipe_name_get () Get name of current pipe
```
```
pipe_new(Name, Colour, <UserId>, <Maincomp>, <SpecSearch>) Create a new pipe
```
```
pipe_part_find (Act, <PartId>) Get ID of first/next/previous part
```
```
pipe_properties_set (Prop) Set properties of pipe
```
```
pipe_ready () Mark pipe as ready for production
```
```
pipe_regenerate () Regenerate modelling information
```
```
pipe_route_end (Prop) End a pipe route
```
```
pipe_route_point (Prop) Add an intermediate point to a pipe route
```
```
pipe_route_start (Prop) Start a pipe route
```
```
pipe_save() Save current pipe
```
```
pipe_split(Name) Split pipe into spools for production
```
```
pipe_spool_find (Act, <SpoolId>) Get ID of first/next/previous spool
```
```
pipe_spool_part_find (Act, <PartId>) Get f first/next/previous part within spool
```
```
pipe_transform(T) Transform part
```
```
pipe_weldgap_set (GapSize) Set weld gap of pipe
```
```
spool_properties_set (SpoolId, Prop) Set properties of spool
```
```
spool_weldgap_delete (PartId) Delete weld gap for spool
```
```
spool_weldgap_edit (PartId, GapSize) Edit weld gap for spool
```
```
spool_weldgap_set (PartI, GapSize) Set weld gap for spool
```
```
vent_mode_activate() Activate Ventilation Mode
```
```
Specifications (kcs_spec)
```
```
Spec_search(SpecSearch) The function performs a search in the specifications.
```
```
Placed Volume (kcs_placvol)
```
```
conn_add (KcsVolConnection) Add connection in current volume
```
```
conn_delete (KcsVolConnection) Delete connection in current volume
```
```
conn_list () Return connection properties in current volume
```
```
conn_properties_get (KcsVolConnection) Return connection properties in current volume
```
```
conn_properties_set (KcsVolConnection) Set connection properties in current volume
```
```
placvol_exist (VolName) Checks if a volume exists
```
```
placvol_new(unplacedName, point, uVector, vVector, <placedName>) Place a volume in model
```
```
Primitive_add(nSubVolNumber, PyObject) Get primitive properties
```
```
Primitive_list(nSubVolNumber) Get primitive properties
```
```
Primitive_properties_get (nSubVolNumber, nPrimNumber ) Get primiitive properties
```
```
Primitive_properties_set (nSubVolNumber, nPrimNumber, PyKcsPrimVolProp) Get primitive properties
```
```
subvol_add () Create new subvolume on current volume
```
```
subvol_delete (nSubVolNumber) Delete subvolume in current volume
```
```
subvol_list () Return list of subvolumes for current volume
```
```
vol_cancel() Cancel the current volume
```
```
vol_close() Cancel the current volume
```
```
vol_delete(VolName, <VolType>) Delete a volume from the data bank
```
```
vol_exist (VolName, <VolType>) Ceck if a volume exists in the data bank
```
```
vol_new (VolName, <MaxExt>) Initialise a new volume
```
```
vol_open (VolName, <MaxExt>) Initialise a new volume
```
```
vol_save () Save a volume
```
```
vol_save_as (Vol_Name, <VolType>) Save current volume with given name
```
```
Structure Modelling (kcs_struct)
```
```
document_reference_add (docRef) Add a document reference to the active structureobject
```
```
document_reference_get () Return a list of document references associated withthe active structure
```
```
document_reference_remove (docRef) Removes document reference from active structureobject
```
get_standard_desc Get description about standard structure
get_standard_origin Get standard-origin for structure
```
hole_new (comp_name, id, point, vector) hole_new (contour2D, id, point, vector) hole_new (comp_name, id, point, vector, side)hole_new (contour2D, id, point, vector, side)Add standard hole to plate part
```
```
misc_comp_new (Name, Point, Route, Rotation) Add miscellaneous component part to currentstructure
```
```
part_assembly (Id, Assembly) Collect the structure part to an assembly
```
```
part_delete (ID) Delete a part or hole in current structure
```
```
part_duplicate (Structure, Id) Duplicate a part from given structure into current
```
```
part_posno (Id, Posno) Set position number for specific part
```
```
part_transform (id, T) Transform a part in current structure
```
```
plate_bent_new(id1, point1, id2, point2, radii) Add bent plate to current structure
```
```
plate_new_contour2D (Name, Origo, Material,Rotation,Contour) Add plate part to current structure
```
```
profile_check_restrict (id) Check profile endcuts against hull profile restriction file
```
```
profile_endcut (Id, Point, Type, Param1, Param2,Param3,Param4, Param5, Param6) Add endcut to profile
```
```
profile_new_2 point3D (Name, Start point, End point, Material vector) Add profile part to current structure
```
```
profile_new_contour2D(compName, contour, origo, normal, rotation) Add bent profile to current structure
```
```
pseudoname_hole (h,w,r) Create pseudo component name for hole
```
```
pseudoname_plate (t) Create pseudo component name for a plate
```
```
pseudoname_profile (Type, a, b, s, t, c, u) Create pseudo component name for a profile
```
set_standard_desc Set description about standard structure
set_standard_origin Set standard-origin point for structure
```
standard_input (StdName, NewMod, NewName, PlacePoint) Input a standard structure
```
```
standard_output (name, stdname) Save a standard structure
```
```
standard_replace (name, stdname) Replace a standard structure
```
```
struct_activate (Structure) Activate a structure object
```
```
struct_assembly (Assembly) Collect the structure object to an assembly
```
struct_cancel Cancel current structure object
```
struct_check_posno () Check if position number is defined twice
```
```
struct_check_restrict () Check profile endcuts against hull profile restriction file
```
```
struct_cway_connect (cway name, part_id, point, struct name) Create reference to cableway
```
```
struct_cway_data (node, route, rotation, length, width, height) Update cableway connection
```
```
Struct_cway_disconnect (cway name, structure name) Disconnect from cableway
```
```
struct_delete (Structure) Delete a structure object
```
```
struct_duplicate (Structure) Duplicate given structure into current
```
```
struct_marking_lines_off () Set marking line off for current structure object
```
```
struct_marking_lines_on () Set marking line on for current structure object
```
```
struct_name_get () Get name of current structure object
```
```
struct_new (Structure, Module, Colour) Create a new structure object
```
struct_save Save current structure object
```
struct_split () Split and transfer structure to production
```
```
struct_transform (T) Transform current structure object
```
```
Weld Planning (kcs_weld)
```
```
weld_calculation(assembly_name,recursive) Starts the weld detection
```
```
weld_properties_get(assembly_name, weld_table) Returns the result of the weld detection
```
```
weld_properties_set(assembly_name, weld_table) Updates an existing weld table
```
```
weld_delete(assembly_name) Deletes the weld table object on data bank
```
```
User Interface (kcs_ui)
```
```
answer_req(Title, Question) Display question message box
```
```
app_window_maximize () Maximize main window
```
```
app_window_minimize () Minimize main window
```
```
app_window_refresh() Refresh main window
```
```
app_window_restore () Restore main window
```
```
choice_select(Title, Header, Actions) Display multiple choice dialog
```
```
colour_select(Title, Colour) Display colour selection dialog
```
```
int_req(Message, InitValue) Input dialog for integer
```
```
message_confirm(Message) Display message box
```
```
message_debug (Message, <Color>,<Bold>,<Underline>) Display message in Vitesse Log window
```
```
message_noconfirm(Message) Display message in message window
```
```
model_info() Display model info interactively
```
```
point2D_req(Message, Point <Status>, <Buttons>)) Input of 2D point in drawing
```
```
point3D_req(Message, InitStatus, Point) Input of 3D point in drawing
```
```
real_req(Message, InitValue) Input dialog for real
```
```
string_req(Message, InitValue) Input dialog for string
```
```
string_select(Title, Header, Prompt, Alternatives) Display string list selection dialog
```
```
symbol_select(Prompt, Font) Display symbol selection dialog for entire symbol font
```
```
symbol_select(Prompt, SymbList) Display symbol selection dialog for selected symbols
```
```
Utility (kcs_util)
```
```
all() Function return value checking: All
```
```
app_basic_design() Check if Basic Design application is running
```
```
app_cable() Check if Cable application is running
```
```
app_curved_hull() Check if Curved Hull application is running
```
```
app_diagram() Check if Diagram application is running
```
```
app_drafting() Check if Drafting application is running
```
```
app_nesting() Check if Nesting application is running
```
```
app_pipe() Check if Pipe application is running
```
```
app_planar_hull() Check if Planar Hull application is running
```
```
app_structure() Check if Structure application is running
```
```
app_ventilation() Check if Ventilation application is running
```
```
cancel() Function return value checking: Cancel
```
```
clean_workspace() Cleans the workspace of all objects not reserved by the current application
```
```
coord_to_pos(Axis, Coord) Translate coordinate to FR or LP position
```
```
exit_function() Function return value checking: Exit function
```
```
exit_program() Exit the running program
```
```
no() Function return value checking: No
```
```
ok() Function return value checking: OK
```
```
operation_complete() Function return value checking: Operation complete
```
```
options() Function return value checking: Options
```
```
pos_to_coord(Axis, No) Translate FR or LP position to coordinate
```
```
quit() Function return value checking: Quit
```
```
reject() Function return value checking: Reject
```
```
TB_environment_get(Env) Get value of Tribon Environment Variable
```
```
TB_environment_set(Env, Value) Set value of Tribon Environment Variable
```
```
tra_coord_pan (Ucoord, Vcoord, Name) Get coordinate in panel coordinate system
```
```
tra_coord_ship (Ucoord, Vcoord, Name) Get coordinate in ship coordinate system
```
```
trigger_abort() Return a code to abort trigger execution
```
```
trigger_ok() Return an OK code for trigger execution
```
```
trigger_override() Return an override code for trigger execution
```
```
undo() Function return value checking: Undo
```
```
yes() Function return value checking: Yes
```
Copyright © 1993-2005 AVEVA AB
22 Python Class Quick Reference Index
User's Guide Vitesse
Assembly
Class KcsAssembly.Assembly Assembly properties
Class KcsAssemblyKeyInItem.AssemblyKeyInItem Assembly Key In Item properties
Date and Time
Class KcsDate.Date Date
Class KcsDateTime.DateTime Date and Time
Class KcsTime.Time Time
Geometry
Class KcsArc2D.Arc2D 2D arc segment
Class KcsCircle2D.Circle2D 2D circle
Class KcsConic2D.Conic2D 2D conic segment
Class KcsContour2D.Contour2D 2D contour
Class KcsContourOperations. BooleanOperations: Information about two 2D dimensional# contours
```
Class KcsEllipse2D.Ellipse2D(Corner1,Corner2) 2D ellipse circumscribed by a rectangle
```
```
Class KcsLine3D.Line3D(Point,Direction) Unlimited 3D line
```
```
Class KcsPlane3D.Plane3D) Unlimited plane
```
Class KcsCircle3D.Circle3D 3D circle
Class KcsBox.Box 3D box
Class KcsCap.Cap Holds information about a cap
Class KcsCone.Cone Holds information about a cone
Class KcsConnection.Connection Holds information about a connection
Class KcsPoint2D.Point2D 2D point
Class KcsPoint3D.Point3D 3D point
Class KcsPolygon2D.Polygon2D 2D polygon
```
Class KcsPolygon3D.Polygon3D(Start) 3D polygon
```
```
ClassPolygon3D.GetNoOfPoints() Returns number of points in polygon
```
```
ClassPolygon3D.GetPoint() Returns Point3D instance of polygon point selected by index
```
```
Class KcsRectangle2D.Rectangle2D(Corner1,Corner2) 2D axis-parallel rectangle
```
```
Class KcsRline2D.Rline2D(Start,End) Restricted 2D line
```
```
Class KcsVector2D.Vector2D(X,Y) 2D vector
```
Class KcsVector3D.Vector3D 3D vector
Hull
Class KcsBodyPlanViewOptions.BodyPlanViewOptions Body Plans View Options
Class KcsCopyPanOptions Copy Panel Options : Inherits from KCSMovePanOptions
Class KcsMovePanOptions Move Panel Options
Class KcsPanelSchema Contains functions operating on panel schema
Class KcsPanHoleOptions PanHole Options
Class KcsRunModeOptions Planar hull scheme run mode options
Class KcsShPlateProp.ShPlateProp The class holds information about a shell plate.
ClassKcsShStiffProp.ShStiffProp The class holds information about a shell stiffener.
Class KcsShellXViewOptions Shell Expansion View Options
Class KcsSplitPanOptions.SplitPanOptions Split Panel Options
Miscellaneous
```
Class KcsCaptureRegion2D.CaptureRegion2D() 2D Capture region
```
```
Class KcsColour.Colour) Colour
```
```
Class KcsDocumentReference. DocumentReference () Document reference
```
Class KcsInterpretationObject.SymbolicView Symbolic view
Class KcsInterpretationObject.CurvedPanelView Curved panel view
```
Class KcsLayer.Layer(layerid) Layer in drawing
```
```
Class KcsLinetype.Linetype(LinetypeString) Line type
```
```
Class KcsModel.Model(Type,Name) Model item
```
Class KcsModelDrawAssyCriteria. ModelDrawAssyCriteria Criteria for drawing assemblies
```
Class KcsModelObjectRevision.ModelObjectRevision() Model object revision properties
```
Class KcsObject.Object Database Object
Class KcsObjectCriteria.ObjectCriteria Database Object selection criteria
```
Class KcsPrintOptions.PrintOptions(printername) Printing Options
```
```
Class KcsProjectCopyArg. ProjectCopyArg () 3D transformation matrix
```
```
Class KcsStat_point3D_req. Stat_point3D_req() Initial status when defining a 3D point
```
```
Class KcsStringlist.Stringlist(Initstring) List of strings
```
```
Class KcsSymbol.Symbol(fontid, symbolid) Symbol element
```
```
Class KcsSymbollist.Symbollist(FontId,SymbNo) List of symbols
```
```
Class KcsText.Text(text) Text element
```
```
Class KcsTransformation2D.Transformation2D() 2D transformation matrix
```
```
Class KcsTransformation3D.Transformation3D() 3D transformation matrix
```
Model
Class KcsCommonProperties. CommonProperties Model object
Pipe
Class KcsPipeCheck.PipeCheck Production checks for a pipe
Class KcsPipeCheck.Settings.PipeCheckSettings Settings for Pipe Production Checks
Class KcsPipeJointAddCriteria.PipeJointAddCriteria Criteria for Joint Insertion into Pipe
Class KcsPipeMaterial.PipeMaterial Pipe Material Components
Class KcsPipeName.PipeName Name of a Pipe
Class KcsPipePartAddCriteria.PipePartAddCriteria Criteria of Part Insertion into Pipe
Class KcsPipePartProp.PipePartProp Pipe Part properties
Class KcsPipeProp.PipeProp Pipe properties
Class KcsPipeSpoolProp.PipeSpoolProp Pipe Spool properties
Class KcsResultPipeCheck.ResultPipeCheck Pipe Check result
Class KcsResultPipeStructConn.ResultPipeStructConn Structure Item connected to Pipe Part
Class KcsSpecSearch.SpecSearch Specification information
Class PipeRoute.PipeRoute Pipe Route
User Interface
Class KcsButtonState.ButtonState State of Lock Buttons during interactive operations
Class KcsCursorType.CursorType Cursor type used for point request functions
Class KcsHighlightSet.HighlightSet Holds information defining drag cursor
Class KcsStat_point2D_req.Stat_point2D_req 2D point selection method
```
Class KcsStat_point3D_req. Stat_point3D_req() 3D point selection method
```
Weld
Class KcsWeldTable.WeldTable Information about a weld table
Class KcsWeldedJoint.WeldedJoint Information about a welded joint
Class KcsWeld.Weld Information about a weld
Volume
Class KcsVolPrimitiveBase. VolPrimitiveBase Information about properties of primitive
Class KcsVolPrimitiveBlock. VolPrimitiveBlock Information about Block Primitive
Class KcsVolPrimitiveGeneralCylinder. VolPrimitiveGeneralCylinder Information about General Cylinder Primitive
Class KcsVolPrimitiveRevolution. VolPrimtiveRevolution Information about Revolution Primtive
Class KcsVolPrimitiveTorusSegment. VolPrimtiveTorusSegment Information about Torus segment Primitive
Class KcsArc3D.Arc3D Information about a 3D arc segment
Class KcsVolPrimitiveTruncatedCone. VolPrimitiveTruncatedCone Information about Truncated Cone Primitive
Class KcsVolPrimitiveSphericalCap. VolPrimitiveSphericalCap Information about Spherical Cap Primitive
Copyright © 1993-2005 AVEVA AB
23 Vitesse Trigger Quick Reference Index
User's Guide Vitesse
Drafting Equipment move pre-trigger
Drafting Equipment move post-trigger
Drafting Init Drafting Pre-Trigger
Drafting Init Drafting Post-Trigger
Drafting New drawing pre-trigger
Drafting New drawing post-trigger
Drafting Open drawing pre-trigger
Drafting Open drawing post-trigger
Drafting Close drawing pre-trigger
Drafting Close drawing post-trigger
Drafting Save drawing pre-trigger
Drafting Save drawing post-trigger
Drafting Save As drawing pre-trigger
Drafting Print drawing pre-trigger
Drafting Print drawing post-trigger
Drafting Insert Model pre-trigger
Drafting Insert Model post-trigger
Drafting Model Info pre-trigger
Drafting Model Info post-trigger
Drafting Model Info property edit pre-trigger
Drafting Verify drawing pre-trigger
Drafting Verify drawing post-trigger
Drafting Insert Model Filter Pre-Trigger
Drafting Popup menu pre-trigger
Equipment Equipment place pre-trigger
Equipment Equipment place post-trigger
Equipment Equipment delete pre-trigger
Equipment Equipment delete post-trigger
Equipment Equipment ready pre-trigger
Equipment Equipment ready post-trigger
Pipe Modelling Pipe PipeGroup Rename Pre-trigger
Pipe Modelling Pipe PipeGroup Rename Post-trigger
Pipe Modelling Pipe PipeGroup Duplicate Pre-trigger
Pipe Modelling Pipe PipeGroup Duplicate Post-trigger
Pipe Modelling PipeProduction PipeInfo Update Pre-trigger
Pipe Modelling PipeProduction PipeInfo Update Post-trigger
Pipe Modelling PipeProduction SpoolInfo Update Pre-trigger
Pipe Modelling PipeProduction SpoolInfo Update Post-trigger
Pipe Modelling PipeProduction SpoolInfo Delete Pre-trigger
Pipe Modelling PipeProduction SpoolInfo Delete Post-trigger
Pipe Modelling PipeProduction PartInfo Update Pre-trigger
Pipe Modelling PipeProduction PartInfo Update Post-trigger
Pipe Modelling PipeModel Material FrameToPipe Pre-trigger
Pipe Modelling PipeModel Material FrameToPipe Post-trigger
Pipe Modelling PipeModel Material SubstituteBend Pre-trigger
Pipe Modelling PipeModel Material SubstituteBend Post-trigger
Pipe Modelling Pipe New Pre-trigger
Pipe Modelling Pipe New Post-trigger
Pipe Modelling Pipe ready post-trigger
Pipe Modelling Pipe ready pre-trigger
Cable Modelling CableWay Group Rename Pre-trigger
Cable Modelling CableWay Group Rename Post-trigger
Cable Modelling CableWay Group Duplicate Pre-trigger
Cable Modelling CableWay Group Duplicate Post-trigger
Cable Modelling Cable Route Pre-trigger
Cable Modelling Cable Route Post-trigger
Cable Modelling Cableway New Pre-trigger
Cable Modelling Cableway New Post-trigger
Cable Modelling Cableway Rename Pre-trigger
Cable Modelling Cableway Rename Post-trigger
Cable Modelling Cableway Material Straight Pre-trigger
Cable Modelling Cableway Material Straight Post-trigger
Cable Modelling Cableway Material Bent Pre-trigger
Cable Modelling Cableway Material Bent Post-trigger
Cable Modelling Cableway Material Intermediate Pre-trigger
Cable Modelling Cableway Material Intermediate Post-trigger
Structure Modelling Structure Group Duplicate Pre-trigger
Structure Modelling Structure Group Duplicate Post-trigger
Pipe Support PipeSupport Save for New Pre-trigger
Pipe Support Structure Group Duplicate Post-trigger
Pipe Support PipeSupport Save for Add Pre-trigger
Pipe Support PipeSupport Save for Add Post-trigger
Pipe Support PipeSupport Delete for Model Pre-trigger
Pipe Support PipeSupport Delete for Model Post-trigger
Pipe Support PipeSupport Delete for Part Pre-trigger
Pipe Support PipeSupport Delete for Part Post-trigger
Pipe Support PipeSupport Rename for Model Pre-trigger
Pipe Support PipeSupport Rename for Model Post-trigger
Pipe Support PipeSupport Rename for Part Pre-trigger
Pipe Support PipeSupport Rename for Part Post-trigger
Data Management Change status Pre-trigger
Data Management Change status Post-trigger
Data Management Create Vitesse reference Pre-trigger
Data Management Open Vitesse reference Pre-trigger
Design Manager Filter Active Pre-trigger
Design Manager Drag & drop filter Pre-trigger
Design Manager Drag & drop filter Post-Trigger
Planar Modelling Panel store pre-trigger
Planar Modelling Panel store post-trigger
```
Registering trigger register_trigger(name, type, function)
```
```
Registering trigger unregister_trigger(name, type, function)
```
```
Registering trigger get_registered_triggers ()
```
Project Copy Project copy export pre-trigger
Project Copy Project copy export post-trigger
Project Copy Project copy import pre-trigger
Project Copy Project copy import post-trigger
Assembly Planning Part List Create Post-Trigger
Sistership Management Sistership Management import pre-trigger
Sistership Management Sistership Management import post-trigger
Copyright © 1993-2005 AVEVA AB
User's Guide
Data Extraction
Tribon M3
Copyright © 1993-2005 AVEVA AB
1 Basic Data Extraction
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
1.1 General
Data in the Tribon data banks are accessible via the Data Extraction facilities. It is possible to retrieve specific information from one or several Tribon objects by specifying the type andname of the model object and the wanted item within the object.
There are three ways to utilize the Data Extraction functions. With a specific query program, SX700, it is possible to ask for specific terms and get the answer at the terminal. The DataExtraction commands are also available within the Geometry Macro language and Vitesse. A COM-object with Data Extraction procedures is available for development of customized
programs.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.2 Syntax
To describe the wanted item, a specific Data Extraction syntax is used. With this syntax the type of object is specified as well as the name of the object and a description of the wanteditem within the object.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.2.1 Keywords
The hierarchical data extraction syntax is a combination of keywords that reflects how the user has built up the model.
The first keyword level is normally the Tribon application e.g. Pipe, Hull, Cable, etc. The second keyword level is a specific object within the Tribon application. The following keywordlevels determine a specific term within the object. The levels and keywords are of course different for the different kinds of object.
```
The levels are separated by the character '.'. Each keyword can normally be abbreviated to the number of characters where the keyword is still unique. The complete lists of keywords(and abbreviations allowed) are documented in the following documents:
```
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
DRAWING see Drafting Keywords.
VOLUME see Drafting Keywords.
EQUIP see Equipment Keywords.
STRUCTURE see Structure Keywords.
HULL see Hull Keywords.
CABLE see Cable Keywords.
COMP see Component Keywords.
PIPE see Pipe Keywords.
VENT see Ventilation Keywords.
Copyright © 1993-2005 AVEVA AB
The Help Keyword
The HELP keyword, valid in all system parts, can replace any valid keyword. The result of a command ended with the HELP keyword is a list of keywords that can replace HELP at itscurrent position.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
Example
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Command string: CABLE.HELP
The following keywords are valid:
CAB_MOD
CWAY
PNTR
```
Command string: CABLE.PNTR(*).HELP
```
The following keywords are valid:
POINT
TYPE
TOTAL_AREA
USED_AREA
COMP_NAME
NCWAY
CWAY_LOC
NAME
Copyright © 1993-2005 AVEVA AB
1.2.2 Arguments
```
Each keyword can be combined with an argument or a list of arguments. An argument is always surrounded by brackets. Three different types of argument exist: string, integer number orreal number. A string is surrounded by apostrophes. The kind of argument depends on the keyword (see the keyword documentation).
```
```
The following operators can occur in an argument (or argument list):
```
Combinations of these operators are allowed in one argument.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
- wildcard character where * replaces one or several characters. It is valid only for string arguments.
```
Example: ('PUMP'*)
```
: defines an interval. Valid for all argument types.
```
Examples: (1:5), ('A':'C'*)
```
, repetition operator. Valid for all argument types.
```
Example: (1,5)
```
Copyright © 1993-2005 AVEVA AB
1.2.3 Examples
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
```
EQUIP('TB').ITEM('EQUIP1').PIPE.NCONNECTION
```
string arg string arg
```
EQUIP('TB').ITEM('EQUIP'*).PIPE.NCONNECTION
```
string arg string arg
with wildcard
```
EQUIP('TB').ITEM('EQUIP'*).DRAWING(1,3,5:10).NAME
```
string arg string arg integer arg with
with wildcard interval and repetition
```
PIPE('TB').PIPMODEL('230X-TB').CONNECTION(1:5).PART
```
string arg string arg integer arg
with interval
```
COMP('COMP1':'COMP2'*).MAN_PROPERTY.CREATION_DATE
```
string arg with wildcards
```
(range) and interval
```
Copyright © 1993-2005 AVEVA AB
1.2.4 Multiple Lines
When writing a command on the screen that includes more than 80 characters then use the hyphen as a continuation character.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
For example, the following command:
```
EQUIP('TB').ITEM(A).PIPE.-
```
NCONNECTION
means exactly the same as
```
EQUIP('TB').ITEM(*).PIPE.NCONNECTION
```
Copyright © 1993-2005 AVEVA AB
1.2.5 Resulting Data Types
The result of a Data Extraction command is returned as one or several values, which can be of different data types. Below follows a list of the most common data types.
A complete list of the data types may be found in the chapter PROGRAMMING WITH DATA EXTRACTION.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
```
String (s) A character varying string
```
```
Integer (i) An integer value (double integer)
```
```
Real (r) A real value (double precision)
```
```
Real vector(3r) A vector with three real double precision values.
```
Copyright © 1993-2005 AVEVA AB
1.3 Environment
To be able to use the Data Extraction facilities, some files and logical names must be defined.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.3.1 Tribon Data Banks
Only the data banks needed for the specific data extraction command have to be assigned.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
General Design
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SB_PDB Drawing Data Bank
SBD_VOLUME Volume Data Bank
SBE_GENCMPDB General Component Data Bank
SBE_GENEQPDB General Equipment Data Bank
Copyright © 1993-2005 AVEVA AB
Hull
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SB_OGDB Hull Data Bank
SB_PLDB Hull Plate Data Bank
Copyright © 1993-2005 AVEVA AB
Pipe
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SB_PSDB Pipe Structure Data Bank
SB_PPDB Pipe Production Data Bank
SB_SURT Surface Treatment file
Copyright © 1993-2005 AVEVA AB
Structure
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SBF_DB_FSTRU Structure model data bank
Copyright © 1993-2005 AVEVA AB
Cable
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SBC_CABSTRDB Cable model DB
SBC_CAWSTRDB Cableway model DB
Copyright © 1993-2005 AVEVA AB
1.3.2 Tribon Environment Variables
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
SB_PROJECT Default Project Name.
If default project is not defined, then the project must be given in the extraction command.
SB_CUSTOMER Default Customer
SB_LANGUAGE Default Language.
The language parameter is used only for components and equipment. If not defined, then the parameter = 1.
SBD_ALIAS Alias file.
Used only for drawings.
SB_SREF Hull Structure Reference Object.
Used only for hull extraction.
Copyright © 1993-2005 AVEVA AB
1.3.3 Miscellaneous Files
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
D0300069.SBM Message file
D0300093.SBM Message file
Copyright © 1993-2005 AVEVA AB
1.4 Data Extraction COM-object
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.4.1 General
```
This COM-object includes the Data Extraction program but extends the use to handle over more of the integration and implementation of the Data Extraction program to the user. It allowsintegration in own developed programs using the programming language that best suits the application, include it in VBA (Visual Basic for Applications)-scripts for Microsoft products such
```
as Word, Excel etc. All connections between the COM-object and the application are done through an interface.
COM is short for Component Object Model.
For further information on using data extraction COM-object, see the customised examples in your Tribon installation.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.4.2 Using the COM-object
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
DoDataExtraction Method
The DoDataExtraction method takes a string as parameter and the string to input is the string that the Data Extraction program would take to extract the desired data.
```
Example of how to call (VBA), there the object name is defined as dextr.
```
```
dextr.DoDataExtraction "HULL.PANEL('ES123'*).NBRA"
```
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
GetValue Method
The GetValue method gets the next value in the Data extraction result structure and is implemented as a function, which means that it will return the value. This method starts by movingthe pointer to the next result value in the result structure and ends by returning the value found. If the last value in the structure is current when calling GetValue the result will be a
Boolean variable set to the value FALSE.
Example of the GetValue method
```
Value = dextr.GetValue
```
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
GetResTree Method
The GetResTree method returns the result string of the current value in the result structure and is implemented as a function. The string is returned as an array ordered in pairs withstatements in even positions and arguments in odd positions. In the example of 1.2.1 the 0 element would hold the string 'HULL' the 1 element would hold an empty string, the 2 element
would hold 'PANEL' and the 3 element would hold the panel name of the currently extracted object etc.
```
Note: As this method does not move the result structure pointer it can only be used together with GetValue method.
```
```
Example of use (VBA):
```
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
```
Example:
```
```
ResultTree = dextr.GetResTree
```
Resulting array of data extraction input string from 1.2.1 could look like this example.
```
ResultTree(0) = "HULL"
```
```
ResultTree(1) = ""
```
```
ResultTree(2) = "PANEL"
```
```
ResultTree(3) = "ES123-621"
```
```
ResultTree(4) = "NBRACKET"
```
```
ResultTree(5) = ""
```
Copyright © 1993-2005 AVEVA AB
ConvertToImperial Method
```
The ConvertToImperial method makes it possible to display result values in Imperial Units. Conversion to imperial units will be made if the Tribon environment variable for the unit is set toIMP (see chapter 5 in the Basic Users Guide).
```
```
ConvertToImperial(
```
VARIANT value,
short quantity,
short nDecimals,
short notation,
short syntax,
```
VARIANT *pVal);
```
Parameter description:
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
value - VARIANT containing the value to convert
quantity - The quantity type:
```
1 (XD969_LIN_MEAS) Linear
```
```
2 (XD969_WEIGHT) Weight
```
```
3 (XD969_DENSITY) Density
```
```
4 (XD969_AREA) Area
```
```
5 (XD969_VOLUME) Volume
```
```
6 (XD969_VELOCITY) Velocity
```
```
7 (XD969_FLOW) Flow
```
```
8 (XD969_PRE_DROP) Pressure drop
```
```
9 (XD969_TEMP) Temperature
```
```
10 (XD969_IMPEDANCE) Impedance
```
```
11 (XD969_LUMINANCE) Luminance
```
```
12 (XD969_INDUCTANCE) Inductance
```
```
13 (XD969_COORD) Coordinate
```
nDecimals - Maximum number of decimals to use
notation - The wanted notation:
```
1 (WY268_FIXED) Syntax with fixed point notation
```
```
2 (WY268_SCIENT) Syntax with scientific notation
```
syntax The wanted presentation syntax:
```
1 (WY268_OUTPUT) Output syntax
```
```
2 (WY268_INPUT) Input syntax
```
Only relevant for imperial coordinates and linear measures, where:'OUTPUT' means delimiters ' and ", and 'INPUT' means delimiters F and I.
pVal - return value
Copyright © 1993-2005 AVEVA AB
VBA Example
An example file can be found here:
basic_vba_example.txt
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
C++ Example
An example file can be found here:
basic_cplus_example.txt
A sample MFC application that illustrates the usage of the Data Extraction component from C++ can be downloaded:
Sx711.zip
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
.
Copyright © 1993-2005 AVEVA AB
1.5 Data Extraction in Geometry Macro Language
In the Geometry Macro language it is possible to retrieve data with the Data Extraction syntax.
With the EXTRACTION statement the wanted data is retrieved from the Tribon data base and put in the Data Extraction result structure.
With the statement GET/EXTRACT or possibly GET/RANGE the extracted information is obtained and assigned to ordinary variables in the Geometry Macro language.
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.5.1 Example files:
 Example 1:
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
basic_macro_dex.txt
 Example 2:
basic_macro_dexj.txt
Copyright © 1993-2005 AVEVA AB
1.5.2 Example in Data Extraction
```
The macro in the example file below will extract and list the endcut parameters for all panels beginning with 'TB172-'. Note that the endcut parameters will be stored in an n-dimensionalarray of real elements (cf. Section I, Chapter 4, paragraph 5 of this binder). This is the case even if only one parameter exists. Therefore it is not possible to print the result directly.
```
First the number of parameters must be extracted with GET/STRUCTURE. The following loop over the N parameters adds them 3 and 3 in the output list.
The example file:
basic_macro_stif.txt
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.6 Data Extraction from Vitesse
Data extraction can be used from Vitesse to extract model information, which can be further processed in the Python language and by using Tribon Vitesse API calls. See the documentTribon M3 Vitesse, "Functions in Vitesse Data Extraction Interface".
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
1.7 Data Extraction in Query Program
The program SX700 is an interactive data extraction program run from a command prompt.
Input to the program is a Data Extraction command given from a command prompt. The resulting values will be presented on the screen
User's Guide Data Extraction
```
Chapter: Basic Data Extraction
```
Copyright © 1993-2005 AVEVA AB
2 Drafting Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
2.1 General
This section contains a description of the currently available keywords that can be used in the data extraction of Drawing & Volume information. A description of general principles, andespecially of the syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Drafting.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column OUTPUT specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Drafting Keywords
```
Copyright © 1993-2005 AVEVA AB
2.2 Information from a Volume
The following is an overview of keywords available for all volume objects:
Datext_Volume.xls
```
Note: It is possible to specify the source data bank for the VOLUME keyword. This is done by suffixing the volume name with the '@' sign followed by the "volume type". If no optionaldata bank is given, the default data bank is "Project Volume" ( SBD_VOLUME.).
```
At present, there are two different volume types, namely:
```
 the project dependant volume DB (SBD_VOLUME)
```
```
 the component volume DB (SBE_GENVOLDB)
```
The volume type can be given as
```
 the logical name of the data bank (SBD_VOLUME or SBE_GENVOLDB)
```
```
 the description of the data bank ("Project volume" or "Component volume"
```
```
 an integer corresponding to the type ( 1 for SBD_VOLUME and 2 for SBE_GENVOLDB)
```
Equivalent ways to extract the names of all volumes starting with XYZ in the SBD_VOLUME data bank
Equivalent ways to extract the names of all volumes starting with XYZ in the SBE_GENVOLDB data bank.
Equivalent ways to extract the names of all volumes starting with XYZ in the SBD_VOLUME data bank and all volumes starting with ABC in the SBE_GENVOLDB.
Equivalent ways to extract the names of all volumes in the interval XYZ90 to XYZ99 in the SBD_VOLUME data bank and three equivalent ways to extract the names of all volumes in theinterval XYZ90 to XYZ99 in the SBE_GENVOLDB data bank.
```
Note: Note that when giving intervals, the optional volume type is given in the lower (first) limit. A volume type in the upper (second) limit will be ignored.
```
Example
```
 VOLUME( 'XYZ90@SBE_GENVOLDB' : 'XYZ99@SBD_VOLUME').NAME
```
is the same as
```
VOLUME( 'XYZ90@SBE_GENVOLDB' : 'XYZ99').NAME
```
and
```
 VOLUME( 'XYZ90' : 'XYZ99@SBE_GENVOLDB').NAME
```
is the same as
```
VOLUME( 'XYZ90@SBD_VOLUME' : 'XYZ99').NAME
```
User's Guide Data Extraction
```
Chapter: Drafting Keywords
```
Example 1
```
VOLUME( 'XYZ'*).NAME
```
```
VOLUME( 'XYZ@SBD_VOLUME'*).NAME
```
```
VOLUME( 'XYZ@Project Volume'*).NAME
```
```
VOLUME( 'XYZ@1'*).NAME
```
Example 2
```
VOLUME( 'XYZ@SBE_GENVOLDB'*).NAME
```
```
VOLUME( 'XYZ@Component Volume'*).NAME
```
```
VOLUME( 'XYZ@2'*).NAME
```
Example 3
```
VOLUME( 'XYZ@SBD_VOLUME'*, 'ABC@SBE_GENVOLDB'*).NAME
```
```
VOLUME( 'XYZ@SBD_VOLUME'*, 'ABC@2'*).NAME
```
```
VOLUME( 'XYZ'*, 'ABC@2'*).NAME
```
```
VOLUME( 'XYZ@SBD_VOLUME'*, 'ABC@Component Volume'*).NAME
```
```
VOLUME( 'XYZ@Project Volume'*, 'ABC@Component Volume'*).NAME
```
```
VOLUME( 'XYZ@1'*, 'ABC@Component Volume'*).NAME
```
Example 4
```
VOLUME( 'XYZ90' : 'XYZ99').NAME
```
```
VOLUME( 'XYZ90@SBD_VOLUME' : 'XYZ99').NAME
```
```
VOLUME( 'XYZ90@Project Volume' : 'XYZ999').NAME
```
```
VOLUME( 'XYZ90@1' : 'XYZ999').NAME
```
```
VOLUME( 'XYZ90@SBE_GENVOLDB' : 'XYZ99').NAME
```
```
VOLUME( 'XYZ90@Component Volume' : 'XYZ99').NAME
```
```
VOLUME( 'XYZ90@2' : 'XYZ99').NAME
```
Copyright © 1993-2005 AVEVA AB
2.3 Information from a Drawing
For every drawing it is possible to extract detailed information about all objects, shown on the drawing. The following is an overview of all relevant keywords:
Datext_Drawing.xls
```
Note: It is possible to specify the source data bank for the DRAWING keyword. This is done by suffixing the drawing name with the '@' sign followed by the "drawing type". If nooptional data bank is given, the default data bank is "General Drawing" (SB_PDB).
```
The drawing type can be given as:
```
 the logical name of the data bank ( e.g. SB_PDB)
```
```
 the description of the data bank (e.g. "General Drawing")
```
```
 an integer corresponding to the type ( 1 for SB_PDB, 2 for SBD_BACKUP etc)
```
Equivalent ways to extract the names of all drawings starting with XYZ in the SB_PDB data bank.
Equivalent ways to extract the names of all drawings starting with XYZ in the SBD_PICT data bank.
Equivalent ways to extract the names of all drawings starting with XYZ in the SB_PDB data bank and all drawings starting with ABC in the SBD_PICT data bank.
Equivalent ways to extract the names of all drawings in the interval XYZ90 to XYZ99 in the SB_PDB data bank and three equivalent ways to extract the names of all drawings in theinterval XYZ90 to XYZ99 in the SBD_PICT data bank.
```
Note: Note that when giving intervals, the optional drawing type is given in the lower (first) limit. A drawing type in the upper (second) limit will be ignored.
```
Example
```
 DRAWING( 'XYZ90@SBD_PICT' : 'XYZ99@SB_PDB').NAME
```
is the same as
```
DRAWING( 'XYZ90@SBD_PICT' : 'XYZ99').NAME
```
and
```
 DRAWING( 'XYZ90' : 'XYZ99@SBD_PICT').NAME
```
is the same as
```
DRAWING( 'XYZ90@SB_PDB' : 'XYZ99').NAME
```
User's Guide Data Extraction
```
Chapter: Drafting Keywords
```
Example 1
```
DRAWING( 'XYZ'*).NAME
```
```
DRAWING( 'XYZ@SB_PDB'*).NAME
```
```
DRAWING( 'XYZ@General Drawing'*).NAME
```
```
DRAWING( 'XYZ@1'*).NAME
```
Example 2
```
DRAWING( 'XYZ@SBD_PICT'*).NAME
```
```
DRAWING( 'XYZ@General Subpicture'*).NAME
```
```
DRAWING( 'XYZ@3'*).NAME
```
Example 3
```
DRAWING( 'XYZ@SB_PDB'*, 'ABC@SBD_PICT'*).NAME
```
```
DRAWING( 'XYZ@SB_PDB'*, 'ABC@3*).NAME
```
```
DRAWING( 'XYZ'*, 'ABC@3'*).NAME
```
```
DRAWING( 'XYZ@SB_PDB'*, 'ABC@General Subpicture'*).NAME
```
```
DRAWING( 'XYZ@General Drawing'*, 'ABC@General Subpicture'*).NAME
```
```
DRAWING( 'XYZ@1'*, 'ABC@General Subpicture'*).NAME
```
Example 4
```
DRAWING( 'XYZ90' : 'XYZ99').NAME
```
```
DRAWING( 'XYZ90@SB_PDB' : 'XYZ99').NAME
```
```
DRAWING( 'XYZ90@General Drawing' : 'XYZ999').NAME
```
```
DRAWING( 'XYZ90@1' : 'XYZ999').NAME
```
```
DRAWING( 'XYZ90@SBD_PICT' : 'XYZ99').NAME
```
```
DRAWING( 'XYZ90@General Subpicture' : 'XYZ99').NAME
```
```
DRAWING( 'XYZ90@3' : 'XYZ99').NAME
```
Copyright © 1993-2005 AVEVA AB
```
3 TDM (Tribon Data Management) Keywords
```
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
3.1 General
This section contains a description of the currently available keywords that can be used in the data extraction of TDM information. A description of general principles, and especially of thesyntax of the data extraction commands, can be found in Basic Data Extraction.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column OUTPUT specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: TDM (Tribon Data Management) Keywords
```
Copyright © 1993-2005 AVEVA AB
```
3.2 Information from TDM (Tribon Data Management)
```
General TDM information can be extracted from different objects in the Tribon databanks The following is an overview:
Datext_TDM.xls
```
Note: The TDM keywords may also be valid for other objects. Refer to each separate Data Extraction chapter.
```
User's Guide Data Extraction
```
Chapter: TDM (Tribon Data Management) Keywords
```
Copyright © 1993-2005 AVEVA AB
4 Equipment Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
4.1 Overview
This document contains a description of the currently available keywords that can be used in data extraction of equipment information. A description of general principles and especially ofthe syntax of the data extraction commands can be found in Basic Data Extraction.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column Output specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Equipment Keywords
```
Copyright © 1993-2005 AVEVA AB
4.2 Information from Equipment
The following is an overview of keywords available for all equipment objects:
DatExt_Equipment.xls
User's Guide Data Extraction
```
Chapter: Equipment Keywords
```
Copyright © 1993-2005 AVEVA AB
5 Structure Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
5.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of structure information. A description of general principles, and especiallyof the syntax of the data extraction commands can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Structure.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column OUTPUT specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values are specified as a factor.
User's Guide Data Extraction
```
Chapter: Structure Keywords
```
Copyright © 1993-2005 AVEVA AB
5.2 Information from a Structure Object
User's Guide Data Extraction
```
Chapter: Structure Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
STR[UCTURE][(s)], s=<project> Application structure -
```
```
.MOD[ULE](s), s=<name> Module object by name -
```
.NAM[E] Module object name s
.BOX Module circumscribed box 6*r
.NITE[M] Number of objects in module object i
```
.ITE[M](i), i=1,NITE Object reference by index -
```
.NAM[E] Object name s
.BOX Circumscribed object box 6*r
```
.ITE[M](s), s=<name> Structure object by name -
```
.NAM[E] Structure object name s
.MOD[ULE]
.NAM[E] Module object name s
.BOX Circumscribed box 6*r
.WEI[GHT] Weight r
.COG Centre Of Gravity 3*r
.STA[NDARD_REF] Standard reference name s
.ASS[EMBLY] Assembly reference name s
.HULL_M[ARKING] Indicator for Hull Marking creation s
.REA[DY] Indicator if structure is split i
0 = No, 1=Yes.
.PDI_T[RANSFERED] Indicator if structure is trans- ferred to PDI. 0=No, 1=Yes. i
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
```
.NCW_CON(NECTION) Number of cableway connections i
```
```
.CW_CON(NECTION)(i) i=1,NCW_CON Cableway connection -
```
```
.NAM(E) Name of cableway s
```
```
.PRO(J) Project of cableway s
```
```
.NPIPE_CON(NECTION) Number of pipe connections i
```
```
.PIPE_CON(NECTION)(i) i=1,NPIPE_CON Pipe connection -
```
```
.NAM(E) Name of pipe (- as delimiter) s
```
```
.PRO(J) Project of pipe s
```
```
.NVENT_CON(NECTION) Number of ventilation connections i
```
```
.VENT_CON(NECTION)(i) i=1,NVENT_CON Ventilation connection (- as delimiter) -
```
```
.NAM(E) Name of ventilation s
```
```
.PRO(J) Project of ventilation s
```
```
.CW_COM(P) Cableway component -
```
```
.NOD(E) Cableway component data 3*r
```
```
.DIR(ECTION) Cableway component data 3*r
```
```
.ROT(ATION) Cableway component data 3*r
```
```
.HEI(GHT) Cableway component data r
```
```
WID(TH) Cableway component data r
```
```
.LEN(GTH) Cableway component data r
```
.NGRO[UP] Number of groups i
```
.GRO[UP](i), i=1,NGRO Group reference by index -
```
.WEI[GHT] Weight r
.COG Centre Of Gravity 3*r
.TDM_I[NFORMATION] Data management -
.ALIAS1 Alias information s
.ALIAS2 Alias information s
.ALIAS3 Alias information s
.ALIAS4 Alias information s
.DESC[RIPTION] Description s
.REM[ARKS] Remarks s
.TYPE1 Type s
.TYPE2 Type s
.TYPE3 Type s
.TYPE4 Type s
.PLA[NINGUNIT] Planning unit s
.COST[CODE] Cost code s
.STATUS_D[ESIGN] Status design s
.STATUS_MAT[ERIAL] Status material s
.STATUS_MAN[UFACT] Status manufact s
.STATUS_A[SSEMBLY] Status material s
.TDM_R[EFERENCES] Drawing references -
.NREF[ERENCE] Number of references i
.REF[ERENCE] Drawing references s
Copyright © 1993-2005 AVEVA AB5.2.1 Reference to Parts Via Running Number
User's Guide Data Extraction
```
Chapter: Structure Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
.TYP[E] Group type
0 = Default
1 = Bent Plate
i
.THI[CKNESS] Thickness for a bent plate group. Zero for the default group. r
.NPAR[T] Number of parts i
```
.PAR[T](i) i=1,NPART Part reference by index -
```
Copyright © 1993-2005 AVEVA AB
5.2.2 General Part Data
User's Guide Data Extraction
```
Chapter: Structure Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
.POS[ITION_NUMBER] Part position number s
.TYP[E] Structure component type s
.COMP_N[AME] Component name s
.AREA For plates and holes area r
.WEI[GHT] Part weight r
.COG Centre Of Gravity 3*r
.ASS[EMBLY] Assembly reference name s
.POI[NT] Node point 3*r
.ROU[TE_VECTOR] Route vector 3*r
.ROT[ATION_VECTOR] Rotation vector 3*r
.PART[_ID] Part id i
.BAR Bar data -
.DES[IGNATION] Type of bar s
.LEN[GTH] Bar length r
.A Cross-section dimension r
.B Cross-section dimension r
.S Cross-section dimension r
.T Cross-section dimension r
.C Cross-section dimension r
.U Cross-section dimension r
.MTRL[_LENGTH] Bar material length r
.MAT[ERIAL_VECTOR Material vector 3*r
```
.END(i), i=1,2 Bar end -
```
.END.POI End point 3*r
.END.CUT End cut data -
.END.CUT.TYP[E_CODE ] Type code i
.END.CUT.NPA[RAMETER] Number of parameters i
.END.CUT.PAR[AMETER] Parameters npar*r
.STA[RT_POINT] Start point of contour for bent profile 2*r
.NSEG[MENT] Number of segments i
```
.SEG[MENT](i), i=1,NSEG
```
Segment reference by index
.AMP[LITUDE] Amplitude r
.END_[POINT] Segment end point r
.PLA[TE] Plate data -
.THI[CKNESS] Plate thickness r
.LE[NGTH] Length of material r
.WI[DTH] Width of material r
.POI[NT] Reference point for geometry 3*r
.MAT[ERIAL_VECTOR] Material vector, perpendicular 3*r
.ROT[ATION_VECTOR] Rotation of plate contour 3*r
.STA[RT_POINT] Plate contour start point 2*r
.NSEG[MENT] Number of segments i
```
.SEG[MENT](i), i=1,NSEG
```
Segment reference by index
.AMP[LITUDE] Amplitude r
.END_[POINT] Segment end point r
.RAD[II] Bending radii for a bent plate r
.HOLE_S[TANDARD] Standard hole data -
.DES[IGNATION] Hole type s
.A Hole length r
.B Hole width r
.R Hole corner radius r
.POI[NT] Ref. point for geometry 3*r
.MAT[ERIAL_VECTOR] Material vector, perpendicular 3*r
.ROT[ATION_VECTOR] Rotation of hole 3*r
.HOLE_G[ENERAL] General hole. -
.POI[NT] Ref. point for geometry 3r
.MAT[ERIAL_VECTOR] Material vector, perpendicular 3r
.ROT[ATION_VECTOR] Rotation of hole 3r
.NSEG[MENT] Number of segments i
```
.SEG[MENT](i),i=1,NSEG
```
Segment reference by index. -
.AMP[LITUDE] Amplitude r
.END_[POINT] Segment end point 2r
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
Copyright © 1993-2005 AVEVA AB
5.2.3 Reference to belonging Parts via Running Number
Hole part data can be used under belonging parts
User's Guide Data Extraction
```
Chapter: Structure Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
.NPART_B[ELONGING] Number of belonging parts i
```
.PART_B[ELONGING](i), I=1,NPART_B
```
Belonging part reference by index -
Copyright © 1993-2005 AVEVA AB
6 Hull Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
6.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of hull information. A description of general principles, and especially ofthe syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Hull.
The currently available keywords do not cover all data items within all types of hull objects.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
All keywords are presented on Excel Sheets. In these sheets, all hierarchies of keywords can be found, together with explanations.
The column OUTPUT specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Hull Keywords
```
Copyright © 1993-2005 AVEVA AB
6.2 Information from a Hull Object
User's Guide Data Extraction
```
Chapter: Hull Keywords
```
Hull, Overview The various objects in Tribon Hull are all accessed via the Hull keyword. The following is an overview of the top level keywords, includingaccess to surfaces.
DatExt_Hull.xls
Surface Surfaces can be used to access shell profiles.
DatExt_Surface.xls
Blocks For each block it is possible to get information about all the panels which are referred to from that block. For each panel the information canbe extracted that is stored together with the reference i.e. on block level. For information stored in the panel itself, see Panel below.
DatExt_Blocks.xls
Curved Panels For curved panels, much of the information stored in the panel is available, especially regarding.
DatExt_Curved_Panels.xls
Shell Profiles For shell profiles, that information is primarily available which is interesting for the profile as a part.
In selecting a certain profile part within a given longitudinal/transversal two main options are available:
```
 the profile part is selected via its name (PART)
```
 the part is selected via a principal plane perpendicular to any of the main axes at a given coordinate.
```
In the latter case an x-coordinate can be selected via a frame term, built up in the same way as in the panel generation, etc., e.g. FRA('FR107+100')
```
DatExt_Shell_Profiles.xls
Panels For plane panels, much of the information is available that is stored in the panel, especially regarding
 plates
 brackets
 doubling
 stiffeners
 flanges
 pillar
 boundaries
```
i.e. mainly about those items that will result in parts (except the boundaries). Coordinates are expressed in the local coordinate system ofpanel.
```
For brackets, information is available about its profiles in the same way as for profiles on the panel itself. Coordinates are then in thecoordinate system of the bracket.
DatExt_Panels.xls
Boundary DatExt_Boundary.xls
Plate DatExt_Plate.xls
Bracket DatExt_Bracket.xls
Doubling DatExt_Doubling.xls
Stiffener DatExt_Stiffener.xls
Flanges DatExt_Flange.xls
Pillar DatExt_Pillar.xls
Bead DatExt_Bead.xls
Hole DatExt_Hole.xls
Notch DatExt_Notch.xls
Cutout DatExt_Cutout.xls
Seams DatExt_Seams.xls
TAP DatExt_Tap.xls
Plates Objects stored as plates are selected via its name. Its coordinates are represented in a local uv-system. By using the transformation matrix,it is possible to transform to the ship's xyz-system.
DatExt_Plates.xls
Curves Objects stored as curves are selected via its name. Its coordinates are represented in a local uv-system. By using the transformationmatrix, it is possible to transform to the ship's xyz-system.
DatExt_Curves.xls
Nested Profiles For each nested profile it is possible to extract the following information
DatExt_Nested_Profiles.xls
Nested Plates For each nested plate following information is available
DatExt_Nested_Plates.xls
Raw Plates For parent plates only names and quantity used are available information.
DatExt_Raw_Plates.xls
Assembly Plates DatExt_Assembly_Plates.xls
Copyright © 1993-2005 AVEVA AB
7 Cable Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
7.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of cable information. A description of general principles, and especially ofthe syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Structure.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column OUTPUT specifies the type of the resulting output value,
 I -for integer
 r -for real
 s -for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Copyright © 1993-2005 AVEVA AB
7.2 Information from a Cable Object
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
CAB[LE][(s)], s=<Project> Cable application. -
```
```
.CAB_M[OD](s), s=<System-Name> Cable name. -
```
.NAME Cable. s
.CABLE_A[LIAS] Cable alias. See the documentation for the CAB_ALIAS and CAB_ALIAS_REPLACEkeywords in the cable default file.s
.COMP_N[AME] Name of cable component. s
.COMP_T[YPE] Component type. I
.ASS[EMBLY] Assembly reference. s
.DES_STA[TUS] Design status
0 = not ready
1 = not ready
2 and 3 = route ready and confirmed
4 and 5 = route ready but not confirmed
I
.PRD_STA[TUS] Production status. I
```
(see appendix).
```
.REA[DY] User defined ready
1 = YES
0 = NO
I
.PDI_T[RANSFERED] Object transferred to PDI
1 = YES
0 = NO
I
.PDI_N[EEDS_RETRANSFER] Object updated after transfer
1 = YES
0 = NO
I
```
.LENGTH_N[ORM] Length excluding excess (mm). r
```
```
.LENGTH_T[OT] Length including excess (mm). r
```
.LENGTH_EXC1 Excess length 1. r
.LENGTH_EXC2 Excess length 2. r
.LENGTH_EXTRA_EXC1 Extra excess length 1. r
.LENGTH_EXTRA_EXC2 Extra excess length 2. r
.WEI[GHT] Returns the weight in kilograms r
```
.COG(Type) Returns the centre of gravity as a coordinate.
```
Type can have the following values:
0 = An approximative calculation is made as midpoint of the route end points.
1 = An exact calculation is made. Zone lengths are not considered. Excess lengths areplaced at the connection points or at route end points if not connected.
3r
.NMARKP[OINT] Number of markpoints. I
```
.MARKP[OINT](I), I=1,NMARKP Markpoint number. -
```
.NAM[E] Penetration name. s
```
.LENGTH_B[EF] Length from startpoint to markpoint (mm). r
```
```
.LENGTH_A[FT] Length from markpoint to end point (mm). r
```
.POI[NT] Coordinates for markpoint. 3r
.EL_PROP[ERTIES] Electrical property data. -
.INT_C[LASS] Interference class. s
.MAN_PROP[ERTIES] Management property data. -
.WORKO[RDER] Workorder name. s
.PLAN_U[NIT] Planning unit. s
```
.CON[NECTION](I), I=1,2 Connections. -
```
```
.STAT[US] Status (see appendix).
```
.POI[NT] Coordinates for connection. 3r
.PRO[JECT] Equipment project name. s
.EQUIP[MENT] Equipment name. s
.PREL_ELC_NAME Name of main connection, if preliminary. s
.PREL_ELC_ALIAS Name of alias for connection. if prel. s
.ALL_ELC_NAME Name of main connection, regardless of preliminary. s
.ALL_ELC_ALIAS Name of alias for connection, regardless of preliminary. s
.NCOR[E] Number of cores. I
```
.CORE(j), j=1,NCOR Core number. -
```
.ELC_N[AME] Main connection name. s
.CORE_N[AME] Core connection name. s
.ELC_R[EFNO] Main connection number. I
.CORE.R[EFNO] Core connection number. I
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
.NROUTE_N[ODE] Number of route nodes. I
```
.ROUTE_N[ODE](I), I=1, NROUTE_NODE Route node number -
```
```
.NAM[E] Name of route node (penetration) s
```
.NLENGT_Z[ONE] Number of length zones I
```
.LENGTH_Z[ONE](I), I=NLENGTH_ZONE Length zone number -
```
.NAM[E] Name of length zone s
.LEN[GTH] Length of length zone r
```
CAB[LE][(s)], s=<Project> Cable application. -
```
```
.CAB_M[OD](s), s=<System-Name> Cable name. -
```
.NBRAN[CH] Number of route branches. I
```
.BRAN[CH](I), I=1,NBRAN Branch number. -
```
.NPAR[T] Number of parts in branch. I
```
.PART(j), j=1,NPAR Part number in branch. -
```
.TYPE Type of part.
1 = cableway reference
2 = single route
I
.PRO[JECT] Cableway project name. s
if TYPE = 1
.CWAY Cable way name s
if TYPE=1
.NPNTR_R[EAL] Number of real penetrations I
```
.PNTR_R[EAL](I), I=1,NPNTR_R Real penetration number -
```
.NAM[E] Penetration name s
.POI[NT] Coordinates for penetration 3r
.NPNTR_I[MAG] Number of imaginary penetrations i
```
.PNTR_I[MAG](I), I=1,NPNTR_I Imaginary penetration number -
```
.NAM[E] Penetration name s
.POI[NT] Coordinates for penetration 3r
.NPNTR_A[LL] Number of all penetrations I
```
.PNTR_A[LL](I), I=1,NPNTR_A Penetration number -
```
.NAM[E] Penetration name s
.POI[NT] Coordinates for penetration 3r
.TDM_I[NFORMATION] Data management -
.ALIAS1 Alias information s
.ALIAS2 Alias information s
.ALIAS3 Alias information s
.ALIAS4 Alias information s
.DESC[RIPTION] Description s
.REM[ARKS] Remarks s
.TYPE1 Type s
.TYPE2 Type s
.TYPE3 Type s
.TYPE4 Type s
.PLA[NINGUNIT] Planning unit s
.COST[CODE] Cost code s
.STATUS_D[ESIGN] Status design s
.STATUS_MAT[ERIAL] Status material s
.STATUS_MAN[UFACT] Status manufact s
.STATUS_A[SSEMBLY] Status material s
.TDM_R[EFERENCES] Drawing references -
.NREF[ERENCE] Number of references i
.REF[ERENCE] Drawing references s
.X_PLACE[MENT] Placement string
.Y_PLACE[MENT] Placement string
.Z_PLACE[MENT] Placement string
Copyright © 1993-2005 AVEVA AB
7.3 Information from Cableway Object
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
CAB[LE][(s)], s=<Project> Cable application. -
```
```
.CWAY(s), s=<Name> Cableway name. -
```
.NAME Cableway name. s
.MODUL[ENAME] Module name. s
.BOX Box. 2x 3r
```
.WEI[GHT](Type) Returns the weight in kilograms.
```
Type can have the following values:
0 = Only those cableway parts dressed with components, that cannot have standardstructures as reference, are added.
1 = The weight of the cables placed on this cableway are added.
10= Adds the weight of structure objects used as cableway parts, for those components notincluded when type is 0.
11= Total weight including both cables and structure objects.
r
```
.COG(Type) Returns the centre of gravity as a coordinate.
```
Type can have the same values as for weight.
3r
.REA[DY] User defined ready
1 = YES
0 = NO
I
.PDI_T[RANSFERED] Object transferred to PDI
1 = YES
0 = NO
I
.PDI_N[EEDS_RETRANSFER] Object updated after transfer
1 = YES
0 = NO
i
.NCON[NECTION] Number of connections. I
```
.CON[NECTION] (I), I=1,NCON Connection number. -
```
.BRAN[CH] Connection branch ID. I
.PART Connection part ID. I
.ID[ENTITY] Connection point ID. I
```
.TYP(E) 1=Cableway, 2=Structure I
```
.REF[ERENCE] References to connected cableway. -
.CONN_PR[OJECT] Cableway project name, only valid if TYPE=1 s
.CONN_C[WAY] Cableway name, only valid if TYPE=1 s
.CONN_B[RANCH] Cableway branch ID, only valid if TYPE=1 I
.CONN_PA[RT] Cableway part ID, only valid if TYPE=1 I
.CONN_I[DENTITY] Cableway point ID, only valid if TYPE=1 I
```
.CONN_S(TRUCT) Name of structure, only valid if TYPE=2 s
```
```
.EVEN[T] (ID) Event point. -
```
.BRAN[CH] Branch ID. I
.PART Part ID. I
.NREF[ERENCE] Number of connected cableway references. I
```
.REF[ERENCE] (I), I=1,NREF Reference number. -
```
.CONN_PR[OJECT] Cableway project name. s
.CONN_C[WAY] Cableway name. s
.CONN_B[RANCH] Cableway branch ID. I
.CONN_PA[RT] Cableway part ID. I
.CONN_I[DENTITY] Cableway point ID. I
.NCAB[LE] Number of cables. I
```
.CAB[LENO](I), I=1,NCAB Cable number.
```
.PRO[JECT] Cable project name. s
```
.NAM[E] Cable name (System-Name). s
```
.GRO[UP] Group name. s
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
```
CAB[LE][(s)], s=<Project> Cable application. -
```
```
.CWAY(s), s=<Name> Cableway name. -
```
```
.PNTR(ID) Penetration identity. I
```
.TYPE Type of penetration
1 = real
2 = imaginary
I
.NAM[E] Penetration name.
.POI[NT] Coordinates of penetration. 3r
```
.USED_A[REA] Used area (if real)(mm2). r
```
```
.TOTAL_A[REA] Total area (if real)(mm2). r
```
```
.COMP_N[AME] Component name (if real). s
```
```
.NCAB[LE] Number of cables passing (if real). I
```
```
.CAB[LENO](I),I=1,NCAB Cable number (if real). -
```
.PRO[JECT] Cable project name. s
.NAM[E] Cable name. s
.GLA[ND_COMPONENT] Gland component name. s
.NGLA[ND] No. of glands in penetration
```
(if real). I
```
```
.GLA[ND](I), I=1,NGLAN Gland number (if real). -
```
.GLA[ND_COMPONENT] Gland component name. s
.CABLE_PRO[JECT] Cable project name. s
.CABLE_NAM[E] Cable name. s
```
.BRAN[CH](ID) Branch. -
```
.NCON[NECTION] Number of connections. I
```
.CON[NECTION](I), I=1,NCON Connection number. -
```
.PART Part number. I
.ID[ENTITY] Identity. I
.REF[ERENCE] Connected cableway reference. -
.CONN_PR[OJECT] Cableway project name. s
.CONN_C[WAY] Cableway name. s
.CONN_B[RANCH] Cableway branch ID. I
.CONN_P[ART] Cableway part ID. I
.CONN_I[DENTITY] Cableway point ID. I
.NINT[ERFERENCE] Number of interference classes. I
```
.INT[ERFERNECE](I), I=1,NINT Interference number. -
```
.C[LASS] Class. s
.START[_POINT] Coordinate of start point in first branch. 3r
.END[_POINT] Coordinate of end point in last branch. 3r
.CABLE[_EXCESS] Excess length added to cable routed on branch. r
```
CAB[LE][(s)], s=<Project> Cable application. -
```
```
.CWAY(s), s=<Name> Cableway name. -
```
```
.PART(ID Part identity. -
```
.MAN_PROP[ERTIES] Management properties. -
.POS[ITION_NUMBER] Position number. s
.COMP_T[YPE] Component type. I
.COMP_N[AME] Component name s
```
(if COMP_T > 0)
```
.CUT_ST[ATUS] Cut status
0 = material not cut.
1 = material cut.
I
.FORM Form
1 = straight
2 = bend
I
```
.TOTAL_A[REA] Total area (mm2). r
```
```
.MATERIAL_L[ENGTH] Material length (mm). r
```
```
.ROUTE_L[ENGTH] Route length (mm). r
```
.NCON[NECTION] Number of connections. I
```
.CON[NECTION](I) I=1,NCONN Connection number. -
```
.POI[NT] Coordinates for connection. 3r
.ID[ENTITY] Identity. I
.MAN_PROP[ERTIES] Management property data. -
.PLAN_U[NIT] Planning unit. s
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
.NGRO[UP] Number of groups. -
```
.GRO[UP](I) I=1, NGROUP Group number. -
```
.NAME Group name. s
.ASS[EMBLY] Assembly reference name s
.TDM_I[NFORMATION] Data management -
.ALIAS1 Alias information s
.ALIAS2 Alias information s
.ALIAS3 Alias information s
.ALIAS4 Alias information s
.DESC[RIPTION] Description s
.REM[ARKS] Remarks s
.TYPE1 Type s
.TYPE2 Type s
.TYPE3 Type s
.TYPE4 Type s
.PLA[NINGUNIT] Planning unit s
.COST[CODE] Cost code s
.STATUS_D[ESIGN] Status design s
.STATUS_MAT[ERIAL] Status material s
.STATUS_MAN[UFACT] Status manufact s
.STATUS_A[SSEMBLY] Status material s
.TDM_R[EFERENCES] Drawing references -
.NREF[ERENCE] Number of references i
.REF[ERENCE] Drawing references s
Copyright © 1993-2005 AVEVA AB
7.4 Information from Penetration Object
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
CAB[LE][(s)] s=<Project> Cable application. -
```
```
.PNTR(s) s=<Name> Penetration name. -
```
.NAME Penetration name. s
.POI[NT] Coordinates of penetration. 3r
.TYPE Type of penetration
1 = real
2 = imaginary
I
```
.TOTAL_A[REA] Total area (if real) (mm2). r
```
```
.USED_A[REA] Used area (if real) (mm2). r
```
```
.COMP_N[AME] Component name (if real). s
```
.ASS[EMBLY] Assembly reference. s
.NCWAY Number of cableways. I
```
.CWAY_L[OC](I), I=1,NCWAY Cableway location number. -
```
.REF[ERENCE] Reference to cableway. -
.PRO[JECT] Cableway project name. s
.CWAY Cableway name. s
.BRAN[CH] Cableway branch ID. I
.PART Cableway part ID. I
.ID[ENTITY] Cableway point ID. I
.NCAB[LE] Number of cables passing. I
```
.CAB[LENO](I), I=1,NCAB Cable number. -
```
.PRO[JECT] Cable project. s
.NAM[E] Cable name. s
.GLA[ND_COMPONENT] Gland component name. s
.NGLA[ND] Number of glands in penetration. I
```
.GLA[ND](I), I=1,NGLAND Gland number. -
```
.GLA[ND_COMPONENT] Gland component name. s
.CABLE_PRO[JECT] Cable project name. s
.CABLE_NAM[E] Cable name. s
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
Copyright © 1993-2005 AVEVA AB
7.5 Cable Production Status
The matrix below describes the CABLE.CAB_MODEL.PRD_STATUS output.
```
A=Defined in workorder
```
```
B=Precut
```
```
C=Cable run
```
```
D=Connected to equipment in end 1
```
```
E=Connected to equipment in end 2
```
Click picture to enlarge
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Copyright © 1993-2005 AVEVA AB
7.6 Cable Connection Status
The matrix below describes the CABLE.CAB_MODEL.CONNECTION. STATUS output.
```
A = Equipment name defined
```
```
B = Equipment location defined (room name)
```
```
C = Equipment placed
```
```
D = Cable end point defined by coordinates, not by equipment
```
values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Cable Keywords
```
Copyright © 1993-2005 AVEVA AB
8 Component Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
8.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of component information. A description of general principles, andespecially of the syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in the Tribon structure system.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights an kg's.
the column OUTPUT specifies the type of the resulting output value.
 i -for integer
 r -for real
 s -for character string
If more than one value is delivered, the number of values is specified as a factor.
User's Guide Data Extraction
```
Chapter: Component Keywords
```
Copyright © 1993-2005 AVEVA AB
8.2 Information from a Component
The following is an overview of keywords available for all component objects:
DatExt_Component.xls
User's Guide Data Extraction
```
Chapter: Component Keywords
```
Copyright © 1993-2005 AVEVA AB
9 Pipe Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
9.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of pipe information. A description of general principles, and especially ofthe syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Pipe.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
The column OUTPUT specifies the type of the resulting output value.
 i -for integer
 r -for real
 s -for character string
```
If more than one value is delivered, the number of values are specified as a factor, e.g. 5s, 2*3r, xi (x means varying).
```
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Copyright © 1993-2005 AVEVA AB
9.2 Information from Pipe Model Object
The following is an overview of keywords available for all model objects:
DatExt_Pipe_Model_Object.xls
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Copyright © 1993-2005 AVEVA AB
9.3 Information from Pipe Line Object
The following is an overview of keywords available for pipe line objects:
DatExt_Pipe_Line.xls
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Copyright © 1993-2005 AVEVA AB
9.4 Information from Pipe Spool Object
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
PIP[E][(s)] s=<project> Pipe application single -
```
```
(only single values in arg.)
```
```
.PIPS[POOL](s,
```
```
s=<module>-<subsystem>-<sketch name>
```
Pipe spool -
.NAM[E] Name of pipe sketch object s
.PROJ[ECT] Name of project
.MAX[IMUM_ID] Maximum identification i
.MOD[IFICATION_STRING] Modification string s
.SYS_N[OTE] System notation s
.ASS[EMBLY] Assembly name s
.GEN_P[ROPERTY] General property block -
.SUBP[ROJECT] Subproject s
```
.NOT[E](i), i=1,3 Note s
```
.NOTE_C[ODE] Note code i
.MTRL_C[ODE] Material code i
.JOI[NT_PREPARATION_CODE]
Joint preparation code i
.WELDC[ODE] Weld code i
.HEATC[ODE] Heat treatment code i
.SUR[FACE_TREATMENT_CODE] -
.ARE[A] Area to be treated i
.NPRET[REATMENT] No. of pretreatment lines i
```
.PRET[REATMENT](i), i=1,NPRETREATMENT
```
Pretreatment s
.NOUTS[IDE_TREATMENT] No. of outside treatment files i
```
.OUTS[IDE_TREATMENT](i), i=1,NOUTSIDE_TREATMENT
```
Outside treatment s
.NINS[IDE_TREATMENT] No. of inside treatment files i
```
.INS[IDE_TREATMENT](i), i=1,NINSIDE_TREATMENT
```
Inside treatment s
```
.SHO[RT_CODE](i), i=1,2 Short code used in pipe shop i
```
```
.SUR[FACE_TREATMENT_CODE](i), i=1,2
```
Surface treatment code i
.BEN[DING_RADIUS] Bending radius r
.TESTPRES[SURE] Test pressure r
.MIN_T[EMPERATURE] Minimum temperature r
.MAX_T[EMPERATURE] Maximum temperature r
```
.WEI[GHT] Weight (kg) r
```
.INS[ULATION_CODE] Insulation code i
.MAN_P[ROPERTY] Management property block -
.COMP_A[LIAS] Component alias s
.ACQ[UISITION_CODE] Acquisition code s
.CRE[ATION_DATE] Date of creation s
.MOD[IFICATION_DATE] Modification date s
.APPL_D[ATE] Application dependent date s
.STAND_I[D] Standard id s
.APPL_N[AME] Application dependent name s
.APPL_A[LIAS] Application dependent alias s
.PLA[NNING_UNIT] Planning unit s
.PROD[UCTION_CODE Production code i
.US[ER_IDENTIFICATION_CODE] User identification string s
.DRA[WING_NAME] Name of drawing s
.DESCR[IPTION] Description string s
```
.BRA[NCH](i), i=id 0, 999 Branch, by id -
```
.PSDB_N[AME] Name of the pipe object on PSDB s
.PSDB_P[ROJECT] Project name of the pipe object on PSDB s
.PSDB_I[D] Id of the corresponding branch on PSDB. i
.SPART PART LIST on Branch with order. i
```
.PART(i), i=id -1000, -32000 Part, by id. -
```
.COMP_N[AME] Name of component. s
.COMP_T[YPE] Type of component. i
.PSDB_I[D] Id of the corresponding part on PSDB. i
.MTRL_REF[ERENCE] Id of the corresponding material element. i
.REF_P[OINT] Reference point number. i
.MTRL_US[AGE] Portion of used material. r
.ROT[ATION] Rotation angle. r
.NNOD[E] Number of node points. i
```
.NODP[OINT](i), i=0,NNODE
```
Node point, by index. 3r
.NCON[NECTION] Number of connections. i
```
.CON[NECTION](i), i=1,NCONNECTION
```
Connection, by index. -
.VEC[TOR] Vector. r
.NOD[E] Node. i
.LEN[GTH] Length. r
.TYP[E] Type. i
.GEN_P[ROPERTY] General property block See:PIPE.PIPSPOOL.GEN _PROPERTY. -
.MAN_P[ROPERTY] Management property block See:PIPE.PIPSPOOL.MA_PROPERTY. -
.DESCR[IPTION] Description string. s
```
.MTRL(i), i=<mtrl.ref.> Material information. -
```
.COMP_N[AME] Name of component. s
.COMP_T[YPE] Type of component. I
.BRA[NCH_ID] Id of branch. i
.NPART Number of parts. i
```
.PART_I[D](i) i=1,NPART Part, by index. i
```
.UN[IT_CODE] Unit code. i
.QU[ANTITY] Quantity.
.BUILDING_L[ENGTH] Building length. r
.GEN_P[ROPERTY] General property block See: PIPE.PIPSPOOL.GEN _PROPERTY
.MAN_P[ROPERTY] Management property block See: PIPE.PIPSPOOL.MAN _PROPERTY -
.DESCR[IPTION] Description string s
.BEND[ING] Bending information -
.MAC[HINE] Machine number i
.DIR[ECTION] Operation direction i
.NAC[TIVITY] Number of activities i
```
.ACT[IVITY_CODE](i), i=1,NACTIVITY
```
Activity code, by index
=1 feed, unit mm
=2 turn, unit rad
=3 bend, unit rad
i
```
.OPE[RATING_VALUE](i), i=1,NACTIVITY
```
Operating value, by index r
E.g. bending and turning angle
.RAD[IUS] Bending radius r
.CHE[CKSUM] Check sum for machine i
.AUT[OWELDING] Automatic welding info -
```
.COD[E](i), i=<conn> 1,2
```
Welding code
i
=0 no auto welding
=1 auto welding
```
.ID(i), i=<flange>1,2 Material id
```
= -1 not auto welded
> 0 will be auto welded
i
.ANG[LE] Rotation angle between two flanges r
.REF_NO Reference of pipe end going to machine
> 0 mtrl.number of connected part
< 0 reference point number
i
.NJOI[NT] Number of joints i
```
.JOI[NT](i), i=1,NJOINT Joint, by index -
```
.INT_C[ODE] Internal connection code
How to treat this connection:
0 none
1-99 boss joint
1=USER_EXTRUDE
2=USER_INSERT
3=USER_SADDLE
4=USER_SURFACE
90=EXTRUDE_MANUAL
91=EXTRUDE
92=SURFACE
93=SADDLE
94=DRILL
95=WELD
96=SOLDER
97=SADDLE_NS
98=BURN
99=CENTRAL
101-104 joint excess
i
101=insert
201=mitre
300=thread
401=form
.INT_E[XCESS] Internal excess r
.EXT_C[ODE] External connection code
When to cut external excess:
0 = no excess
1 = in work shop
2 = on board
i
.EXT_E[XCESS] External excess r
.CONN_REF[ERENCE] Connection reference
< 0 reference point number
= 0 no reference
> 0 mtrl.id
i
.ROT[ATION] Rotation info -
.VEC[TOR] Vector 3r
.ANG[LE] Rotation angle r
.REF[ERENCE] Reference -
.PLANE_C[ODE] Plane type code
= -1 undefined
=10 pipe bend, with no comp
=11 pipe bend, with comp.
=20 eccentric comp.
=25 mitre
=30 boss conn., with comp.
=40 boss conn., with no comp.
=45 comp. has more than two connections
```
=50 flange (with rot. def.)
```
i
.PLANE_V[ECTOR] Vector 3r
```
.PLANE_P[ART](i), i=1,2
```
Part id i
.INC[LINATION] Inclination info -
.VEC[TOR] Vector 3r
.ANG[LE] Turning angle r
.REF[ERENCE] Reference -
.PLANE_V[ECTOR] Vector 3r
.TURN[ING] Turning info -
.VEC[TOR] Vector 3r
.ANG[LE] Turning angle r
.REF[ERENCE] Reference -
.PLANE_C[ODE] Plane type code i
See ROTATION.REFERENCE .PLANE_CODE
.PLANE_V[ECTOR] Vector 3r
```
.PLANE_P[ART](i), i=1,2
```
Part id i
```
.MIT[RE](i), i=<conn>1,2 Mitre info -
```
.VEC[TOR] Vector 3r
.TURN[ING_ANGLE] Turning angle r
.INC[LINATION_ANGLE] Inclination angle r
.REF[ERENCE] Reference -
.PLANE_C[ODE] Plane type code i
See ROTATION.REFERENCE .PLANE_CODE
.PLANE_V[ECTOR] Vector 3r
```
.PLANE_P[ART](i), i=1,2
```
Part id i
```
.INCL_A[NGLE](i), i=1,3
```
Inclination angle r
.MIT[RE_END] Reference to mitre end
<0 reference point number
=0 no reference
>0 material id
i
.POI[NT_NO] Point number if pipe bend is ref. plane i
.REF[ERENCE] Used reference
<0 reference point number
=0 no reference
>0 material id
i
.NFE[ED] Number of feed excess points i
```
.FE[ED](i), i=1,NFEED Feed excess, by index -
```
.PART Part with the feed excess i
.POI[NT] Point with the feed excess 3r
.EXC[ESS] Feed excess r
.REF_NO Reference point number i
.NBRA[NCH] Number of branches i
```
.BRA_NO(i), i=0,NBRANCH -1 Branch, by index -
```
.BRA_ID Branch id i
.NCLPART Number of centre line parts i
```
.CLPART_NO(i), i=1,NCLPART
```
Centre line part, by index -
.CLPART_ID Centre line id i
.NPERPART Number of peripheral parts i
```
.PERPART_NO(i), i=1,NPERPART
```
Peripheral part, by index -
.PERPART_ID Peripheral part id i
.NUSER_ATT[RIBUTE] Number of user attributes i
```
.USER_ATT[RIBUTE](i), See Information from a Drawing in Chapter Drafting Keywords
```
.TDM_I[NFORMATION] Data management -
.ALIAS1 Alias information s
.ALIAS2 Alias information s
.ALIAS3 Alias information s
.ALIAS4 Alias information s
.DESC[RIPTION] Description s
.REM[ARKS] Remarks s
.TYPE1 Type s
.TYPE2 Type s
.TYPE3 Type s
.TYPE4 Type s
.PLA[NINGUNIT] Planning unit s
.COST[CODE] Cost code s
.STATUS_D[ESIGN] Status design s
.STATUS_MAT[ERIAL] Status material s
.STATUS_MAN[UFACT] Status manufact s
.STATUS_A[SSEMBLY] Status material s
.TDM_R[EFERENCES] Drawing references -
.NREF[ERENCE] Number of references i
.REF[ERENCE] Drawing references s
Copyright © 1993-2005 AVEVA AB
9.5 Information from Pipe Component in Pipe Object
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Keyword Explanation Output
1 2 3 4 5 6
```
PIP[E][(s)], s=<project> Pipe application -
```
```
.PIPO[BJECT](s), s=<module>-<subsystem> Pipe spool -
```
```
.PIPC[OMP](s), s=<'sketch name'> Pipe component element -
```
.NAM[E] Name of pipe component s
.COMP_N[AME] Name of component s
.COMP_T[YPE] Type of component i
.PSDB_I[D] Id of the corresponding part on PSDB i
.MAT[ERIAL] Material used r
.ROT[ATION] Rotation angle r
.SYS_N[OTE] System notation s
.ASS[EMBLY] Assembly name s
.NNOD[E] Number of node points i
```
.NODP[OINT](i), i=0,NNODE Node point, by index 3r
```
.NCON[NECTION] Number of connections i
```
.CON[NECTION](i), i=1,NCONNECTION
```
Connection, by index -
.VEC[TOR] Vector r
.NOD[E] Node i
.LEN[GTH] Length r
.TYP[E] Type i
.NCONN_D[ESCRIPTION] Number of connection descriptions i
```
.CONN_D[ESCRIPTION](I), i=1,NCONN_DESCRIPTION
```
Connection description, by index -
.TOT[AL_LENGTH] Total length r
.OUT[ER_DIAMETER] Outer diameter r
.PIPD[IAMETER] Pipe diameter r
.NBHOLE Number of bolt holes i
.BHOLE_L[ENGTH] Bolt hole length r
.BHOLE_C[IRCLE_DIAMETER] Bolt hole circle diameter r
.BHOLE_D[IAMETER] Bolt hole diameter r
.WALLT[HICKNESS] Wall thickness r
.GAS[KET_DIAMETER] Gasket diameter r
.FLA[NGECODE] Flange code i
.THR[EADCODE] Thread code i
.NOM[INALDIAMETER] Nominal diameter i
.PRES[SURE] Pressure i
.SYM_F[ONT] Symbol font number i
.SYM_N[UMBER] Symbol number i
.SYM_S[CALE] Scale factor r
.NSYM_P[ARAMETER] Number of symbol parameters i
```
.SYM_P[ARAMETER](i), i=1,NSYM_PARAMETER
```
Symbol parameter, by index i
.GEN_P[ROPERTY] General property block -
.SUBP[ROJECT] Subproject s
```
.NOT[E](i), i=1,3 Note i
```
.NOTE_C[ODE] Note code i
.JOI[NT_PREPARATION_CODE]
Joint preparation code i
.WELDC[ODE] Weld code i
.HEATC[ODE] Heat treatment code i
.TESTPRES[SURE] Test pressure r
.MIN_T[EMPERATURE] Minimum temperature r
.MAX_T[EMPERATURE] Maximum temperature r
```
.WEI[GHT] Weight (kg) r
```
.INS[ULATION_CODE] Insulation code i
.MAN_P[ROPERTY] Management property block -
.COMP_A[LIAS] Component alias s
.ACQ[UISITION_CODE] Acquisition code s
.CRE[ATION_DATE] Date of creation s
.MOD[IFICATION_DATE] Modification date s
.APPL_N[AME] Application dependent name s
.APPL_A[LIAS] Application dependent alias s
.PLA[NNING_UNIT] Planning unit s
.PROD[UCTION_CODE] Production code i
.US[ER_IDENTIFICATION_CODE]
User identification string s
.DRA[WING_NAME] Name of drawing s
.DESCR[IPTION] Description string
.TDM_I[NFORMATION] Data management -
.ALIAS1 Alias information s
.ALIAS2 Alias information s
.ALIAS3 Alias information s
.ALIAS4 Alias information s
.DESC[RIPTION] Description s
.REM[ARKS] Remarks s
.TYPE1 Type s
.TYPE2 Type s
.TYPE3 Type s
.TYPE4 Type s
.PLA[NINGUNIT] Planning unit s
.COST[CODE] Cost code s
.STATUS_D[ESIGN] Status design s
.STATUS_MAT[ERIAL] Status material s
.STATUS_MAN[UFACT] Status manufact s
.STATUS_A[SSEMBLY] Status material s
.TDM_R[EFERENCES] Drawing references -
.NREF[ERENCE] Number of references i
.REF[ERENCE] Drawing references s
Copyright © 1993-2005 AVEVA AB
9.6 Information from Specification
Keywords available for specification objects are shown in the following overview:
DatExt_Pipe_Specification.xls
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Copyright © 1993-2005 AVEVA AB
9.7 Information from Surface Treatment
The following is an overview of keywords available for surface treatment objects:
DatExt_Pipe_Surface_Treatment.xls
User's Guide Data Extraction
```
Chapter: Pipe Keywords
```
Copyright © 1993-2005 AVEVA AB
10 Ventilation Keywords
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
10.1 General
This document contains a description of the currently available keywords that can be used in the data extraction of ventilation information. A description of general principles, andespecially of the syntax of the data extraction commands, can be found in Basic Data Extraction.
The hierarchical structure of the keywords reflects how the user has built up the model in Tribon Ventilation.
Unless otherwise stated measures are given in mm's, areas in square mm's and weights in kg's.
the column OUTPUT specifies the type of the resulting output value.
 i for integer
 r for real
 s for character string
If more than one value is delivered, the number of values are specified as a factor.
User's Guide Data Extraction
```
Chapter: Ventilation Keywords
```
Copyright © 1993-2005 AVEVA AB
10.2 Information from Ventilation Model Object
The following is an overview of keywords available for all ventilation model objects:
DatExt_Ventilation.xls
User's Guide Data Extraction
```
Chapter: Ventilation Keywords
```
Copyright © 1993-2005 AVEVA AB
11 Assembly Keywords
There is no implementation of Data Extraction for assemblies in Tribon M3. Instead the Vitesse Assembly Functions should be used. Reference: Vitesse / Assembly / Functions.
User's Guide Data Extraction
Copyright © 1993-2005 AVEVA AB
User's Guide
Production Data Interface
Tribon M3
Copyright © 1993-2005 AVEVA AB
Section I
Installation of PDI
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 Installation of PDI using Oracle
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1.1 General
```
This chapter describes the steps needed to install a Production Data Interface (PDI) database with Oracle.
```
```
The reader is expected to have a working knowledge of Oracle database administration and to have the privileges needed to act as DBA (creating users etc.).
```
Also check any readme files or special information documents that may be included in the Tribon distribution.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.2 Oracle requirements
The requirements on Oracle for installing and running the Production Data Interface are:
 Oracle server 8.1.8 or 9
 Oracle client 8.1.7 or 9
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.3 Decide on Schema Configuration
A PDI database contains production information, stored in tables with prefix TPR, and components, stored in tables with prefix TCM.
```
You can choose to have a single PDI database schema for everything, or to have separate schemes for TPR and TCM. You can also have several TPR and/or TCM schemes (e.g. oneTPR schema per project) but note that Tribon application programs can not connect to more than one TPR and one TCM schema during a session.
```
If you plan to integrate PDI with Tribon Materials via the ERP-TBM option in Tribon M3, please also note that a TBM installation can not be connected to more than one TPR schema andone TCM schema.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.4 Create Table-space
You will probably want to create one or more new table-spaces dedicated to PDI.
Due to the many different ways PDI can be used and the very large variation of data volumes among customers, general disk space estimates cannot be given. However, since there isno large initial load, you can start with modest space and expand it later.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.5 Create Schemes and Roles
```
Create user-names for the PDI scheme(s) and distribute the user-names, passwords and database names to persons responsible for setting up Tribon environment variables. Tribonprograms need them to run as owners of the PDI scheme(s).
```
A PDI database is read-only for customer applications. To avoid unintentional changes of the database it is strongly recommended that all end-users and customer applications accessthe database via user-names granted only the necessary read privileges.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.6 Run Installation Scripts
```
To initially create all PDI tables, constraints, indexes and other database objects in a PDI schema, log on as owner and run one or both (depending on your chosen configuration) of thesql scripts
```
pdi_install.sql
cmp_install.sql
```
These scripts call subscripts which create all basic database objects (named TPRB_ or TCMB_) as well as views and synonyms for use in customer applications (TPRE_, TCME_) orwithin Tribon (TPRT_, TCMT_).
```
```
All scripts are initially installed in the /usr subdirectory in SB_SYSTEM. They are ordinary Oracle text file sql scripts and can thus be copied and run from any node with access to theserver and some tool (SQL*Plus etc.) to run Oracle sql scripts. The install scripts assume that subscripts are stored in the same directory.
```
Some dictionary tables are preloaded by the installation scripts, but otherwise all tables are initially empty.
```
If the scripts are rerun they may complain about objects already installed but will not delete them, just add those that are missing. If you need to remove tables or other objects alreadyinstalled, you must do so 'manually' (or construct your own drop scripts).
```
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.7 Performance Tuning
```
The installation scripts delivered with Tribon are purely 'logical', i.e. they contain no physical storage parameters (PCTFREE, STORAGE, ALLOCATE EXTENT etc.). These parametersare dependent on installation specific data volumes and access patterns and can be adjusted after installation if the defaults are not appropriate.
```
```
Also the need for secondary indexes may be installation specific. Some indexes are created by the installation scripts, but more can be added by the DBA if needed. To avoid nameconflicts, don't start your index names (or any other non-Tribon names) in the PDI schema with T.
```
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.8 Notes on Database Copying
If the contents of a PDI schema is copied to another schema which will be used in parallel with the old one, then special consideration must be taken to the field DB_IKEY in the single-row table TPRE_DB_DESCR.
This field must not have the same values in different schemes. If copied it must be set to NULL before starting to use the schema. Otherwise there is an increased risk that the keys thatare generated as record identifiers will not be unique between the different schemes and thus may cause problems if data is to be moved between them.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.9 Upgrades
To upgrade an existing PDI schema from a previous version to the current version, run scripts named
pdi_upgrade_<vvv>.sql
cmp_upgrade_<vvv>.sql
where '<vvv>' is the number of the version you are upgrading from. This number can be found in field DB_VERSION in TPRE_DB_DESCR.
Compatibility issues concerning program versions vs database versions are treated in release notes.
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
1.10 Maintenance
There are two special maintenance tasks that should be handled by the PDI database administrator:
The database contains a table, TPRE_EVENT, in which insertions, updates and deletions of PDI items are logged. Tribon programs add rows to this table but never removes any so thereshould be some installation routine for this. Rows can be deleted from this table in any order at any time by means of ordinary sql DELETE command.
```
The other special case is deletion of all TPR items for a specific project. To do this, run (as owner) the sql script
```
pdi_delete_project.sql
```
It will prompt for a project name and then deletes all records in all TPR tables related to this project. There is also a choice between commit per item or just one commit for the wholeproject. In either case; make sure you have a good backup before running this script!
```
User's Guide Production Data Interface
```
Chapter: Installation of PDI using Oracle
```
Copyright © 1993-2005 AVEVA AB
Section II
Basic
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 PDI Basic
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1.1 General
Tribon Production Interface, PDI, makes it possible to extract production oriented information from Tribon and store it in an open relational database where it can easily be accessed viastandard tools and interfaces for use in customer applications.
Figure 1:1. PDI Data flow.
PDI uses Oracle as database platform. The customer is assumed to provide the necessary infrastructure including server, network and client installations and to have resources fordatabase administration and user support.
This guide is written for developers who need information to build PDI-based customer applications and for users of PDI-enabled Tribon programs who may want some backgroundinformation on data transfer to PDI.
The guide describes
 Overall contents and structure of the database
 General principles for transfer from Tribon applications
 Some guidelines for database access from customer applications
User's Guide Production Data Interface
```
Chapter: PDI Basic
```
Copyright © 1993-2005 AVEVA AB
2 Database Structure
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 General
A PDI database contains production items and components.
Production items can be of different types: assemblies, plates, profiles, cable-ways, pipe spools and so on, and are organized in hierarchical assembly, module, block and system trees.For each item, data of interest for production is stored in one or more tables.
The database contains data for components used by the items. Components can be common or project specific.
This chapter contains general database documentation. For details on tables, fields and codes, see Appendices.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
2.1.1 Naming Conventions
All Tribon-defined tables and other database objects are named with a prefix TPR for production data or TCM for component data. Other prefixes may be used in the future but to avoidconflicts with user-defined objects they will always begin with a T and have at least three characters.
Tables are named TPRB_ or TCMB_, views and synonyms on these tables published for customer use are prefixed TPRE_ or TCME_ while objects named TPRT_ or TCMT_ areintended for internal Tribon use only. The purpose of this arrangement is to allow future enhancements to the database definition while keeping a stable platform for customer
applications.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
2.1.2 Production Item Data
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Item Identification
```
An item is uniquely identified by its item type, project and item name (= Tribon object name) and the main table TPRE_ITEM which is common for all items, has a unique key defined onthe fields ITEM_TYPE, PROJECT, ITEM_NAME.
```
```
However, in order to save space, gain performance and make it easier to write SQL queries, an artificial key is used as primary key instead of the explicit item type, project, item namekey. The artificial key, IKEY, is a randomly generated CHAR(16) string without internal meaning.
```
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Item Types
The item types that can be transferred from Tribon are:
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Project 1
Assembly 2
Module 3
Block 4
System 5
Key-in assembly part 11
Assembly component part 21
Plate 1001
Profile 1002
Fabricated bracket 1003
Pipe spool 2001
Pipe part 2002
Pipe component 2003
Ventilation spool 2051
Ventilation part 2052
Ventilation comp. 2053
Equipment 2101
Cableway 2201
Cableway part 2202
Cable penetration 2203
Cable 2204
Structure component 2303
Structure 2304
Copyright © 1993-2005 AVEVA AB
Tree Structures
```
Items can belong to up to four tree structures (depending on item type):
```
 Assembly tree
 Module tree
 Block tree
 System tree
There are four types of tree nodes:
1. A 'project' node which is the common top node for all trees within a project.
2. Assembly, module, block or system nodes for the four trees
3. Application specific sub assemblies, e.g. pipe spools, cable-ways, etc.
4. Application specific parts, e.g. pipe parts, cable-way parts, etc.
The hierarchies are represented by the 'parent' attributes, ASSY_PARENT-_IKEY, MODULE_PARENT_IKEY, BLOCK_PARENT_IKEY and SYSTEM-_PARENT_-IKEY respectively, inthe TPRE_ITEM table. Each of the these attributes refers to the applicable parent item, using the IKEY of the parent item as identification. The parent item is also an item in the
TPRE_ITEM table which can have its own parent reference.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Geometry and Joints
The geometry of a part is stored in the TPRE_PART_GEO table as a set of points and curves which can be of different types. A pipe part, for instance, can have bend points, endconnection points or branch points, cables have points making up the cable route and so on.
Items that are physically connected share a joint in the TPRE_JOINT table where joint properties, e.g. welding parameters, are stored. The TPRE_ITEM_JOINT table has one row foreach item-joint combination. For the most common case where two items are connected, there will thus be two rows in the TPRE_ITEM_JOINT table pointing at two different items in the
TPRE_ITEM table and pointing to the same joint in the TPRE_JOINT table.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Database Diagram for Items
Figure 2:1. PDI Item Tables.
See Appendices for more information.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
2.1.3 Component Data
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Component Identification
```
Project specific components are identified by project and component name stored in fields named PROJECT and CMP_NAME respectively. These fields are used in all tables (no artificialkeys as for item tables). Components that are independent of project have PROJECT = '*'.
```
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Database Diagram for Components
Figure 2:2. PDI Component Tables.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
Documentation of TCM Schema
The tables and fields in the TCM schema are documented in
<tcmTableDescr.xls>
<tcmColumnDescr.xls>
The Tribon defined codes used in the TCM tables are documented in
<tcmCode.xls>
See Appendices for more information.
User's Guide Production Data Interface
```
Chapter: Database Structure
```
Copyright © 1993-2005 AVEVA AB
3 Data Transfer from Tribon Applications
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Update Principles
Each Tribon PDI interface program can write one or several types of items to the PDI database. An item can be any node in the complete assembly tree e.g. a plate part, an assembly ora pipe spool. All data for an item is inserted, updated or deleted as a unit, i.e. all tables containing data for a certain item is handled within the same transaction.
```
When an item is updated, it will replace any previous data and its UPDATE_NO (in TPRE_ITEM) will be increased by one. A row indicating that an update has occurred will be written tothe TPRE_EVENT table.
```
Components used by PDI items are automatically copied to TCM tables when items are inserted or updated.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
3.1.1 Transfer Combinations
The Tribon interface programs can be run independently of each other.
```
When an item is transferred to PDI, it appears in the module, block or system, all depending on the item type. When the assembly, referring to the item, is transferred, the item will appearalso in the assembly tree. If the assembly, referring to a certain item, is transferred before the actual item, a 'shell item' (preliminary item) will be created. When the actual item transfer is
```
run at a later stage, the shell data will be replaced by real production data.
An application reading the PDI database can distinguish the preliminary data from the real production data by the value of the ITEM_STATUS column of the TPRE_ITEM table.
The creation of shell data is a common occurrence where one application creates items belonging to another application. For example when an equipment item is transferred which isconnected to a cable item the equipment application will create a shell cable item. Later when the cable item is transferred the ITEM_STATUS will be changed to indicate that a cable
item with real production data exists.
The creation of the shell items enables any browsing tool to view items in a tree structure even before all real data have been transferred to the PDI database.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
3.1.2 Project Name
For each item in PDI, the project name is included in the identification, in the item key. Thus, to be able to access PDI data by project, all items, independent of the applications, musthave the same project identification. PDI transfer routines handle project name in the following way:
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Pipe, equip, cable: Project name is fetched from the object name.
```
Structure: Project name is fetched from the project attribute stored in the structure object at creation
```
```
Hull: Project name is fetched at run-time from
```
1. SB_PROJ_HULL if set, otherwise
2. SB_PROJ if set, otherwise
3. project name as defined in the hull structure object
```
Assembly: Project name is fetched at run-time from SB_PROJ.
```
Copyright © 1993-2005 AVEVA AB
3.1.3 How Transfers are Controlled
The transfer of data from a Tribon interface program is controlled by environment variables. The variables listed below are common to all programs. Their values are given by the PDIdatabase administrator. There is also a number of application specific variables and default file values which are described in the documentation for each application.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
```
SB_PDI_DBNAME Database name for PDI item data (TPR-tables). The name identifies a specific server database within a network.
```
SB_PDI_DBUSER User name for connect operation.
SB_PDI_DBPASSWORD Password for SB_PDI_USER. Defined by database administrator.
SB_PDI_DBSCHEMA Name of database schema for item data. Must be given if not equal to SB_PDI_DBUSER.
```
SB_CMP_DBNAME Database name for PDI component data (TCM-tables).
```
SB_CMP_DBUSER User name used by Tribon programs when accessing PDI components.
SB_CMP_DBPASSWORD Password for SB_CMP_DBUSER.
SB_CMP_DBSCHEMA Name of database schema for component data. Must be given if not equal to SB_CMP_DBUSER.
SB_CMP_SOURCE Specification of the source for the Component catalogue. The values can be RDB or NATIVE. See Tribon M3 Components User's Guide for further information.
```
Note: CMP variables must be set also when they are identical to the corresponding PDI names
```
For troubleshooting purposes there are two more variables. They may generate large listings and performance impairments and should not be used in normal operation.
SB_PDI_SQL_LOG Value "YES" turns on logging messages of calls to the PDI database. Default value is "NO".
SB_PDI_XRA_LOG Value "YES" turns on a still more detailed logging of database calls. Default value is "NO".
Copyright © 1993-2005 AVEVA AB
3.1.4 How Programs connect to Oracle
```
PDI interface programs connect to the Oracle database server via Oracle Call Interface (OCI) libraries which belong to the Oracle client installation and must be found in the library pathsearched by Tribon programs at run-time. The PDI database administrator should provide the necessary routines for setting up this environment.
```
Some PDI interface programs are dedicated transfer programs but others have PDI transfer as an option and must be possible to use also on installations where there is no Oracleinstallation. The mechanisms to provide this flexibility is platform dependent.
On Tribon M3 running on Windows nothing special is needed. Programs connect to OCI on the fly if necessary, but will run anyway, without PDI transfers, if OCI is not found.
On TRIBON 5 on UNIX or Open VMS, scripts that run the programs look at SB_PDI_-DBNAME. If this variable is set and is not empty, the script connects the program to a Tribon Oracleinterface module which in turn requires OCI. Otherwise the program is connected to a dummy module that makes it possible to run the program without Oracle connection. Both the
```
dummy module and the Oracle interface module are installed in SB_SYSTEM (or its subdirectories).
```
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
3.1.5 Compatibility with PDI in Tribon M3
PDI in Tribon 5 version 2 and in Tribon M3 are fully compatible. The PDI database can be updated either from Tribon 5 version 2 or from Tribon M3 independently of each other.
In Tribon M3 there is an option to use Oracle for the storage of Components. If this option is active, the complete Tribon Component catalogue is initially stored in Oracle, in the TCMschema, instead of in a Tribon native database. Consequently Components are not transferred to PDI by the application PDI transfer programs in this case. This option is controlled by
the environment variable SB_CMP_SOURCE. For further information see Tribon M3 Components User's Guide.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
3.1.6 PDI Release Control Mechanism
There is a feature in the Tribon PDI transfer programs, which can be invoked to control or prevent the updating of PDI. This could be useful e.g. to prevent updating of a certain item inPDI in the case that the production of this item has already started.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
Update
Before the Tribon application really updates the PDI database, a check is performed if the updating is allowed or not. This means that even if the PDI transfer is ordered, it could happenthat the transfer is not performed due to the Release control mechanism.
This update check is done via an Oracle procedure. It is called by the Tribon application before the actual update/transfer is made. In this way the checking procedure is completelyconfigurable by the customer.
Please see the chapter Oracle functions for a detailed function specification.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
Delete
A delete command in Tribon is handled as usual i.e. the item is deleted from the Tribon database as long as Tribon allows it. The deletion in the PDI database is initiated from Tribonwhenever the item is deleted in Tribon.
Before the Tribon application may really delete an item from the PDI database, a check is performed if deletion is allowed or not. This check is done via an Oracle procedure. It is calledby the Tribon application before the actual deletion is made. In this way the checking procedure is completely configurable by the customer.
Please see the chapter "Oracle functions" for a detailed function specification.
The following situations can occur:
```
 Deletion allowed (YES):
```
 Tribon will perform the delete without restrictions. The item is completely removed from the PDI tables.
 Restricted Deletion:
 The item is not removed from PDI, instead it is marked for deletion.
 Assembly reference is removed.
 Delete all detailed item data in connected tables
 Item status is set to Cancelled
 Manufacturing status is set to the specified value
 Note that is this case the item is anyhow removed from the Tribon database, while it remains in the PDI database, marked as "cancelled".
```
 Deletion not allowed (NO):
```
 No action.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
Copyright © 1993-2005 AVEVA AB
Oracle Functions
Function Interfaces
A template SQL script for a release control package is included in the Tribon distribution. But the function bodies of the functions specified below have to be written by the customer.
where itemtype, project, itemname identifies the item for which Tribon asks permission to update/delete.
The manufactstatus is returned by the function, and used by the Tribon application to update the Manufacturing status in the Oracle database.
The message parameter can be used to return an optional error message or an explanation why a permission is denied. The message is written to a log file and may, depending on theapplication, be shown interactively. The maximum message length is 256 characters. The parameter is initially empty.
The return code is interpreted by Tribon as follows:
```
Other values (0 or > 3) must not be used and are regarded as "Unknown error" by Tribon.
```
Function Package
The release control functions must be bundled together in a PL/SQL package created by the customer. The package name can be freely chosen by the customer although it isrecommended to avoid names beginning with T. The name is to be set in the Tribon logical variable
SB_PDI_TPR_RELCTRL
If, for instance, this variable is set to XYZ, Tribon tries to call the function XYZ.TPR_UPDATE_ALLOWED before update.
If the variable is not present, not set or set to NO, Tribon assumes that unrestricted update/delete is allowed.
User's Guide Production Data Interface
```
Chapter: Data Transfer from Tribon Applications
```
```
FUNCTION TPR_UPDATE_ALLOWED(
```
itemtype IN NUMBER,
project IN VARCHAR2,
itemname IN VARCHAR2,
manufactstatus IN OUT NUMBER,
```
message IN OUT VARCHAR2 )
```
RETURN NUMBER
```
FUNCTION TPR_DELETE_ALLOWED(
```
itemtype IN NUMBER,
project IN VARCHAR2,
itemname IN VARCHAR2,
manufactstatus IN OUT NUMBER,
```
message IN OUT VARCHAR2 )
```
RETURN NUMBER IN NUMBER,
1 = YES, unrestricted update/delete allowed
2 = NO, update/delete not allowed
```
3 = RESTRICTED, Restricted delete (not applicable for update)
```
< 0 = An error is detected, permission is denied
Copyright © 1993-2005 AVEVA AB
4 Accessing a PDI Database
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
4.1 Accessing Tools
A PDI database is an open relational database, using only basic relational constructs and data-types and implemented on the well-known Oracle database platform.
This means that the database can be accessed from virtually any computer environment via a host of different tools provided by Oracle, Microsoft or several other vendors.
```
Database applications can be built from low level API:s (OCI, ODBC) or more or less generated by higher level tools like Oracle Forms or application wizards in Microsoft Visual studiousing OLEDB/ADO.
```
Data can easily be imported to end-user tools, for instance to Microsoft Excel via MS Query, or the database can be queried ad hoc through SQL command tools like Oracle SQL*Plus.
User's Guide Production Data Interface
```
Chapter: Accessing a PDI Database
```
Copyright © 1993-2005 AVEVA AB
4.1.1 Access Restrictions
PDI data are read-only for customer applications or end-users. Updates must be done via Tribon. An exception is TPRE_USER_CODE where some user specific codes may be entereddirectly by the customer.
To avoid update 'accidents', the PDI database administrator should provide user-names with suitable privileges. Do not use the names intended for Tribon programs.
User's Guide Production Data Interface
```
Chapter: Accessing a PDI Database
```
Copyright © 1993-2005 AVEVA AB
4.1.2 Guidelines for Stable Interfaces
The published database tables and views have synonyms or views with name prefix TPRE_ or TCME_. Customer applications should always use these names when accessing thedatabase. They form a stable interface that will be kept independent of changes to underlying tables and views.
 Additions of new tables
 Additions of new fields in existing tables and views
```
Customer applications should be prepared for such changes of the database definitions. For instance they should avoid 'SELECT *' in SQL statements if the application is not ready toaccept that new fields may turn up (or that the order of fields is changed).
```
To avoid future naming conflicts, customer defined views or other database objects stored within a PDI schema should not begin with a T and must not be 'perceived' by Tribon, forinstance by foreign keys referring to PDI tables.
```
The artificial keys (IKEY, JOINT_IKEY, NEST_IKEY) used as record identifiers should not be used in customer applications, except temporarily within a run-unit. They are not guaranteedto be unchanged when items are updated.
```
User's Guide Production Data Interface
```
Chapter: Accessing a PDI Database
```
Copyright © 1993-2005 AVEVA AB
A1 Appendices
User's Guide Production Data Interface
Link to Excel file
1. Description of the TPRE tables (printout of TPRE_TABLE_DESCR) tprTableDescr.xls
2. Description of the TPRE columns (printout of TPRE_COLUMN_DESCR) tprColumnDescr.xls
3. Description of which tables are used for which item types (printout of TPRE_TABLE_USE) tprTableUse.xls
4. Documentation / Translation of the Code values for numeric or alphanumeric codes in the TPRE tables (printout of TPRE_CODE) tprCode.xls
5. Description of the TCM tables (printout of TCME_TABLE_DESCR) tcmTableDescr.xls
6. Description of the TCM columns (printout of TCME_COLUMN_DESCR) tcmColumnDescr.xls
7. Documentation / Translation of the Code values for numeric and alphanumeric codes in the TCM tables (printout of TCME_CODE) tcmCode.xls
Copyright © 1993-2005 AVEVA AB
Section III
Cable Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Cable Interface
This chapter describes the concept and functionality of the Tribon Cable production interface to PDI. This interface transfers Cableway, Penetration and Cable production data such ashierarchy, size, component reference and route description. The assembly references are not handled by the Cable interface to PDI.
For more information:
 Tribon PDI in general, see section Basic.
 Documentation table delivered in section Installation of PDI.
 Equipment handling, see section Equipment Interface.
 Assembly structure, see section Assembly Planning Interface.
 Cable ready functions and default values, see Tribon Cable User's Guide.
 Data extraction keywords, see Tribon Data Extraction User's Guide.
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2 Transfer Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 User Routine
The PDI transfer takes place automatically when a Cable or Cableway, respectively, is made Ready. The ready functions check the model before storing. Cable Ready starts the transferof Cable data. Cableway Ready starts the transfer of Cableway and Penetration data. The user may define which data to check by setting the appropriate default values. It is also
possible to define which kind of model objects shall be transferred.
Cableways may be set ready, and transferred to PDI in the Cable Interactive Modelling program. Cables may be set ready in both Cable Interactive and Non Interactive Modelling. TheReady functions are described in the Cable User's Guide.
There are two possibilities in Tribon to see the 'transfer to PDI' status: The Model Info function and Data Extraction show if models in the cable system are ready, transferred to PDI and ifthey need to be transferred to PDI again.
The Tribon modelling delete function in the cable modelling and cable maintenance programs removes data from PDI.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2 Controlling Data Transfer
```
The PDI transfer is controlled by keywords in the Cable default files (SBC_DEF, SBC_DEF1 and SBC_DEF5). The following keywords are valid:
```
See also the general PDI environment variables, described in section Basic.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
PDI_TRANS_CABLEWAY YES or NO
PDI_TRANS_PENETRATION YES or NO
PDI_TRANS_CABLE YES or NO
Copyright © 1993-2005 AVEVA AB
3 Storage Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Cableway
The hierarchical structure, project, module, cableway and cableway part are transferred to PDI. Parts without component and position number are not transferred to PDI.
The naming convention for a cableway part is <cableway name>-<position number>. The structure name is, as default, used as position number if the component is of the kind that
has a standards structure reference and the user not has given a specific position number to the part. The weight for 'structure parts' is 0, since the part may be modified from standardconstruction by the structure application.
For more information about the data stored for cableway and cableway part items see Appendices in section Basic.
A cableway part is given a quantity which is defined differently depending on the type of component specified. The length is used for straight parts. Either pieces or an angle is used forbent parts depending on if it is possible to cut.
Each cableway part has geometrical data connected to it. For straight parts there are two elements, number 1 is start point and number 2 is end point. For bend parts there are threepoints, number 1 is start point, number 2 is node point and number 3 is end point.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
3.2 Penetration
It is possible to transfer real penetrations to PDI along with the cableway. The hierarchical structure, project, cableway module and penetration are transferred.
For more information about the data stored for a penetration item see Appendices in section Basic.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
3.3 Cable
The hierarchical structure, project, system and name are transferred. The route is stored in a specific table.
```
The storage of equipment references are described in document Equipment. Referred items such as equipments, cableways and penetrations will be created if they have not beentransferred already. They will be transferred without their full production data and with design status set to 'not ready for production' (See TPRE_CODE Table).
```
The route is described in TPRE_CABLE_ROUTE - the cable route table. Each item in this table refers to a geometrical point which is found in the TPRE_PART_GEO table. Thegeometrical point may belong to a cableway, penetration or the cable itself, in the case of a free route. Note that many cables may have a reference to the same geometrical point. In the
```
cable route table each entry has a sequence number which defines the order of the route. A group name is given which is defined by the group function in cable modelling. In the partgeometry table a geo name is given to describe the name of a passed imaginary penetration. The geo type is the type of geometrical point (documented in the TPRE_CODE table).
```
Possible types are:
 point on cableway
 imaginary penetration
 real penetration
 point on cable
A joint will also be created if the cable is passing a real penetration. Insert blocks are transferred as component references in the joint.
For more information about the data stored for cable items see Appendices.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Section IV
Equipment Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Equipment Interface
This chapter describes the concept and functionality of the Tribon Equipment Production Interface to PDI. This interface transfers Equipment production data such as hierarchy, size,component reference and transformation matrix. The assembly references are not handled by the Equipment interface to PDI.
For more information:
 Tribon PDI in general, see Section PDI Basic.
 Documentation table delivered in Section Installation of PDI using Oracle.
 Assembly structure, see Section Assembly Planning Interface.
 Data extraction keywords, see Tribon Data Extraction User's Guide.
 Default data, see Tribon Equipment User's Guide.
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2 Transfer Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 User Routine
The PDI-transfer for an equipment object is done when the equipment is marked as ready. The ready functions check the model before it is transferred. The user may define which datato check by setting the appropriate default values.
Equipment objects can be set to ready and subsequently transferred to PDI in all modelling programs where the handle equipment menu is active.
The status of the PDI transfer can be seen from two places within Tribon: The Model Info function and Data Extraction program show if the equipment is ready, transferred to PDI and if itneeds to be transferred to PDI again.
The Tribon modelling delete function in the handle equipment menu removes data from PDI.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2 Controlling Data Transfer
```
The PDI transfer is controlled by a keyword in the Equipment default file (SBE_EQDEF).
```
See also the general PDI environment variables, described in section Basic.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
PDI_TRANS_EQUIPMENT YES or NO
Copyright © 1993-2005 AVEVA AB
3 Storage Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Equipment Properties
The hierarchical structure of the equipment consisting of the project, module and equipment are transferred to PDI.
For more information about the data stored for an equipment item see Appendices in section Basic.
The equipment component properties are stored in the component tables where they are identified by the component name. The equipment table contains a component name thatreferences these tables.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
3.1.1 Geometry
The connection points to cables and pipe parts are stored in the part geometry table TPRE_PART_GEO. This table describes the physical position of the connection. The geo types "pipeconnection" and "cable connection" are valid. This is documented in TPRE_CODE. The segment number is always 1.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
3.1.2 Connections
Information about the physical connections between equipment and pipe parts and between equipment and cables are stored in the joint and item joint tables. Further information aboutthese tables and the concept of a PDI joint can be found in the Tribon PDI Basic section.
```
When an equipment is attached to a cable or pipe part that does not already exist in the database, a shell item will be created. The shell pipe or cable will contain minimal information.This includes the name, project, type and a link to the respective parents (module and system for pipe parts and system for cables). The item status of the shell item is "not ready for
```
production".
A shell equipment is created in the same way when a pipe or cable is transferred from their respective applications to PDI.
Where an equipment connects to a pipe part or a cable the connection number is the connection point on the component where the connection is made. The element number refers to thegeometrical point found in the part geometry table. For the case of core connections the sub-connection number is used to reference each connection with the main connection number
referencing the end of the cable that the equipment is attached to. The segment number currently always has a value of one. For specific information about pipe and cable connectionssee the respective chapters.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Section V
Pipe Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Pipe Interface
This chapter describes the concept and functionality of the Tribon Pipe Production Interface to PDI. This interface transfers pipe production data such as pipe and ventilation spoolprefabrication information as well as parts list data to the PDI database.
For more information:
 Tribon PDI in general, see section Basic.
 Section Equipment Interface.
 Section Assembly Planning Interface.
 Tribon Pipe User's Guide.
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2 Transfer Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 User Routine
```
The transfer of pipe spool data to the PDI database is done from the Tribon Pipe production (splitting) program. The details of running this program are documented in the Tribon PipeUser's Guide. This document only covers the specifics of the built-in PDI interface.
```
All references to pipe spools, pipe parts and single pipe components in this document also apply to the corresponding ventilation items.
The pipe production program will always produce pipe spool data on the PPDB databank as well as pipe sketches on the PDB data bank, while the creation of data in PDI database isoptional. To perform the transfer of pipe production data to the PDI database, perform the following steps:
1. Set up the environment variables that control the PDI transfer operation. These include database name, user name, password and other options. Some of these variables are pipespecific and are described further down in this document. Some other variables are general to all Tribon application programs that use the PDI database. They are described in detail
in Basic chapter.
2. Perform the normal steps involved to run the pipe production program, including the setting up of an input file with SPLIT or DELETE statements. SPLIT statements will result in thewriting of pipe spool data to the PDI database, and DELETE statements will delete data from the PDI database. It is also possible to run the splitting program automatically which is
described under the next heading.
3. Examine the pipe splitting logs which will include messages whether the pipe spools were successfully transferred to or deleted from the PDI database or not. If any error messagesare present, please refer to the troubleshooting part in Basic chapter.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2 Automatic Execution
The interactive pipe modelling program supports the transfer of spool data to PDI by automatically activating the splitting program as a background job when the 'Ready' command isgiven. The current pipe will then be split and stored in the PPDB data bank, and if the controlling environment variable is set, it will also be transferred to the PDI database.
Automatic splitting is not supported for the Batch Pipe Modelling program. Any pipes created using this program must be ordered for splitting manually. When running the splittingprogram, these pipes can also be transferred to the PDI database. The only difference lies in that the batch modelling program does not automatically start the splitting process.
Any pipes deleted in Tribon either by using interactive or batch modelling will also automatically be deleted in the PDI database if the environment variables are correctly set up atprogram execution.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.3 Controlling Data Transfer for Pipe Spools to PDI Database
The following environment variables are used for controlling the transfer of data to the PDI database. See also the general PDI environment variables described in Basic section.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
SB_PDI_TRANS_PIPE A value of 'YES' will activate the transfer of pipe spools to the PDI database. Otherwise pipe spools will be processed in the normal way by the pipe productionprogram, but not written to the PDI database.
Copyright © 1993-2005 AVEVA AB
2.4 Updating Principles
When a pipe spool is written to PDI, it will result in one spool item and a number of subordinate part items. If the pipeline currently consists of fewer spools than previously, or the spoolsconsist of fewer parts, the obsolete items will be removed from PDI. Each time a pipe is split, the resulting spools and parts will have a new version number in the PDI database. A single
pipe component is stored as one pipe spool item and one subordinate pipe component part. The most common example of such a 'pipe component' is a valve. Any referred componentswill automatically be updated in the PDI component tables. For more information, see 'principles of data transfer' in Basic section.
Figure 2:1. Pipe Spool "item" Structure in the PDI Database.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
3 Storage Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 PDI Items Handled by PDI Pipe
The pipe spools, their corresponding parts and other related data are stored in a number of tables in the PDI database. The table names and detailed definitions of the data can be foundin the PDI database itself. For more information, see Tables in Section Appendices in the PDI Basic. Item types created by the pipe spool interface program are listed below:
 pipe spool
 pipe part
 single pipe component
 ventilation spool
 ventilation part
 single ventilation component
 module
 system
 project
```
 components (not an 'item', stored in separate tables)
```
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
3.2 Pipe Properties
The different properties of pipe spools and their parts are stored in general and pipe specific tables in the PDI database. The table structure used for these properties is described below.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Pipe Spool and Pipe Part Properties
The general properties for both pipe spools and pipe parts are stored in the item table. The pipe spool specific properties are stored in the pipe spool table. The pipe part specificproperties are stored in the pipe part table.
For more information about the data stored for pipe and ventilation, spool and part items see Appendices in Section Basic.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Hierarchical Structure
Pipe spools can belong to assemblies if assembly information has been transferred. This is represented by the assembly reference. Pipe spools also belong to modules and systemswhich are represented by the module and system references. Pipe parts belong to pipe spools in both hierarchical structures.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Component Specifics
The pipe component properties are stored in the component tables prefixed by TCM where they are identified by the component name. The column CMP_NAME in TPRE_ITEM containsthe component name that reference these tables.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Geometry
The connection points, bend points etc. for each pipe part are stored in the part geometry table. In the pipe part properties table, there is information on which branch of the spool the partbelongs to and its sequence number within that branch. By using this information it is possible to obtain a complete geometrical description of a pipe spool.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Connections
Information on the physical connections between pipe parts is stored in the joint and item-joint tables. This also includes connections between pipe parts that are members of differentspools. The joints refer to geometry points for the parts, so it is possible to see which point on one part connects to which point on the other part. For a mitre connection, a direction vector
and an angle is stored in the geometry and joint tables respectively. These describe the layout of the mitre joint.
Joints to equipment are stored in the same tables. See Tribon Equipment User's Guide for more information.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Excess
Excess is stored in the pipe excess table. Each excess instance refers to a geometry point in the geometry table that describes the location of the excess to be cut.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Bending
The bending operations for a pipe material part are described in the pipe bending table.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Automatic Welding
If automatic welding of flanges on pipe material should be performed, information on this is stored in the joint table. A code indicates that automatic welding should be performed, and anangle defining the rotation of the flange is also present.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Section VI
Structure Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Structure Interface
This chapter describes the concept and functionality of the Tribon Structure Production Interface to PDI. This interface transfers Structure data such as hierarchy, size and componentreference. The assembly references are not handled by the Structure interface to PDI.
For more information:
 Tribon PDI in general, see section Basic.
 Documentation table delivered in section Installation of PDI.
 Assembly structure, see section Assembly Planning Interface.
 Nesting, see section Hull Interface.
 Structure split function and default values, see Tribon Structure User's Guide.
 Data extraction keywords, see Tribon Data Extraction User's Guide.
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2 Transfer Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 User Routine
The transfer of data from the structure system is done when the objects are split and transferred to the hull production environment. When nesting a plate or profile, references are alsoupdated for parts from the structure system.
There are two possibilities in Tribon to see the 'transfer to PDI' status: The Model Info function and Data Extraction show if models in the structure are ready, transferred to PDI and if theyneed to be transferred to PDI again.
The delete function in the structure modelling removes data from PDI.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2 Controlling Data Transfer
```
The PDI transfer is controlled by a keyword in the Drafting default file (SBD_DEF1):
```
See also the general PDI environment variables, described in section Basic.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
PDI_TRANS_STRUCTURE YES or NO
Copyright © 1993-2005 AVEVA AB
3 Storage Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Structure Properties
The hierarchical structure, project, module, structure and structure part are transferred to PDI. Parts without component are not transferred to PDI.
The naming convention for the part items follows strictly the naming convention for structure parts in the hull production environment:
 Plate parts are named :
<structure name> - <part name>
 Profile parts are named :
<structure name> \\ <part name>
 Component parts are named :
<structure name> - <part name>
The part name is the parts position number with a C appended if a numeric position number is defined for the part. Otherwise an internal number is used and CI is appended.
Structure plate type is always defined as PLANE PLATE.
Structure profile type is always defined as PLANE PROFILE.
For more information about the data stored for structure and structure part items see Appendices in Section Basic.
```
Nesting data for Structure parts (profiles and plates) are handled in the same way as for Hull parts. See Section Hull Interface.
```
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Section VII
Hull Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Hull Interface
The Tribon Hull Production Data Interface to PDI Database can be used to connect Tribon Hull production data with external systems such as planning systems, material systems, etc.The transferred data is however not sufficient for post processors and other geometry based applications. For this task, the products Tribon Plate Interface and Tribon Profile Interface are
needed.
Transfer of hull production data can be made either manually on command, automatically by setting a logical variable or a combination of these.
For more information:
 Tribon PDI in general, see section Basic.
 see section Pipe Interface.
 see section Assembly Planning Interface.
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2 Transfer Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 Control of Transfer
A number of basic environment variables control the transfer of production data to the PDI database. These variables are of type 'database name', 'password', etc. and are common to allother possible transfers of Tribon data. Details about this can be found in section Basic.
Apart from those, there are some Hull specific environment variables to control how hull data is transferred to PDI.
See also the general PDI environment variables, described in section Basic.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
TB_PDI_HULL Should be set to 'YES' if the PDI transfer should take place.
SBH_EXTRA_INFO To be set to any value. The names of all transferred hull parts are displayed in the log file.
Copyright © 1993-2005 AVEVA AB
2.2 Manual Transfer
The Hull production data can be transferred manually for many reasons. The user can decide that transfers up to a certain point shall be manually controlled and after this point set-up thesystem to make transfers automatically. This will reduce the number of transfers in the period of time when a lot of changes take place.
An other reason for a manual transfer may be that the automatic transfer has failed for some reason and re-running the Hull application is not applicable.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2.1 Input
Input to the program is based on the general selection tool of Tribon and this input is normally generated automatically when activating this function through any of the interactive hullapplications via a production program interface. This interface and the selection possibilities are described in Tribon Manufacturing, General About the Production Program Interface.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
Language
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Statements/attributes Usage
BLOCK All plate and profile parts within the given block are selected.
ASSEMBLY This statement selects all plate and profile parts belonging to the given assembly.
PANEL This statement select all plate and profile parts on the given panel.
PLATE Use this statement to select individual plate parts.
PROFILE Use this statement to select individual profile parts.
NESTED_PLATE Use this statement to select individual plate nesting.
NESTED_PROFILE Use this statement to select individual profile nesting.
DATE Attribute to the statements above. Only parts with dates after given date will be selected.
Copyright © 1993-2005 AVEVA AB
2.2.2 Example
The following input will select all plate and profile parts within the given block.
```
BLOCK, 'ES123';
```
The following input will select all plate and profile parts within the given panel.
```
PANEL, 'ES133-2SP';
```
The following input will select all plate and profile parts within the given plate nesting.
```
NESTED_PLATE, 'MJ01';
```
The following input will select all plate and profile parts within the given panel.
```
NESTED_PROFILE, 'ES123_STIFF-1*' /DATE= '1996-10-01';
```
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2.3 Project Environment
The manual transfer program requires that a project is made active with all general environment variables set, such as data banks, file path for list files and data files, etc.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.2.4 Invoking the Program
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
Via Tribon Job Launcher
```
The name of the executable of this program is sf860d. It communicates via an input file and resulting files. The program is normally activated through the Tribon Job Launcher (TJL)where the following set-up is required:
```
Name recognised by TJL:
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Tribon logical TJL set-up and explanation
SB_INPUT1 Input file to be set-up with extension '.dat' in TJL.
SB_OUTPUT1 Output file with run-time information. To be set-up in TJL as first output file with extension '.log'.
SB_OUTPUT2 Output file to be used only when a direct transfer to an open relational database is not wanted. Instead a text file containing names of terms and corresponding valueswill be created.
To be set-up in TJL with extension '.out'.
Copyright © 1993-2005 AVEVA AB
Via the Command Prompt
The program is started from the command prompt with the command: >sf860d
The program will ask the user for names of input and output files.
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.3 Automatic Transfer
The automatic transfer is activated by setting the environment variable TB_PDI_HULL. By doing this, the programs listed below will automatically transfer their results to the PDIdatabase. PDI will be updated in all situations where parts are created, updated or deleted. In other cases, when parts are not stored on hull data banks, then no update of the PDI
database is made. A manual transfer is then needed if the part shall be available on the PDI database. Any errors or other problems in the automatic transfer will be notified in the log ofeach program.
```
If a curved panel is not created (e.g. a plate is developed by using platedev with T51 input data), then is assumed that the plate is named according to conventions.
```
Hull production data is transferred to PDI automatically from the following applications:
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
Copyright © 1993-2005 AVEVA AB
2.3.1 Curved Hull Generation
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
```
Interactive Curved Hull Modelling (tbchm sh700)
```
```
Longitudinals and Transversals (profgen sf404d)
```
Profile parts are added to PDI
```
Curved Panel Generation (cpangen sf412d)
```
Plate and profile parts are deleted from PDI when panels are deleted.
```
Add Marking to Developed Plate (platemark sf831d)
```
Plate parts are added to PDI.
Copyright © 1993-2005 AVEVA AB
2.3.2 Plane Hull Modelling
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
```
Interactive Hull Modelling (sbhm sj001)
```
```
Batch Hull Modelling (sbhmgen sj011)
```
Plate and profile parts are deleted from PDI when panels are deleted.
```
Auto Parts Generation (ppanparts sf416d)
```
Plate and profile parts are added to PDI.
Copyright © 1993-2005 AVEVA AB
2.3.3 Plate Nesting
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
```
Interactive Nesting (nesting se001)
```
```
Panel Line Control Module (assnest se002)
```
```
External Automatic Nesting (autonesting se003)
```
```
Res-sketch (resketch se010)
```
Plate nestings are added to PDI.
Copyright © 1993-2005 AVEVA AB
2.3.4 Profile Nesting
User's Guide Production Data Interface
```
Chapter: Transfer Principles
```
```
Profile Nesting (profnest sf605d)
```
Profile nestings are added to PDI.
Copyright © 1993-2005 AVEVA AB
3 Storage Principles
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Hull Production Data
The data transferred is stored in the PDI database using relational database technique. The set-up of views on this database, the relations between data, etc. are described in detail inSection I, Basic. This section will describe the hull data that can be transferred. The Appendices in Section I, Basic describe which data is used by PDI and the names and descriptions of
the relevant relational database fields.
The transferred hull production data follows the same format as other PDI applications. Both plates and profiles are regarded as being items in the traditional PDI sense with datacommon to both of them being stored in TPRE_STEEL_PART and data specific to each being stored in TPRE_PLATE_PART and TPRE_PROFILE_PART respectively. For more
information about PDI items see section Basic.
Since nestings are not found on an assembly tree they are treated differently from plate and profile parts. A nesting is identified by the NEST_IKEY, which is the primary key of all thenesting tables. General nesting data is stored in TPRE_NEST and data specific to plates and profiles is stored in TPRE_NEST_PLATE and TPRE_NEST_PROFILE respectively. Each
```
instance of a nesting is recorded in TPRE_NEST_INSTANCE with the instance number and position (starboard or portside) given. Rest material data is recorded in TPRE_NEST_RESTwith SEQ_NO giving an index to each rest plate.
```
To link a plate or profile PDI item to a nesting, the IKEY of the item and the NEST_IKEY of the nesting is recorded in TPRE_ITEM_NEST. If there is more than one identical plate orprofile on the nesting then its instance is also recorded here. For a diagrammatic view of the above relations see Figure 2:1.: PDI Item Tables. in section Basic.
For more information about the hull data which is transferred to PDI see Appendices in section Basic.
User's Guide Production Data Interface
```
Chapter: Storage Principles
```
Copyright © 1993-2005 AVEVA AB
Section VIII
Assembly Planning Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1 General about Assembly Planning Interface
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
1.1 Purpose
```
This User's Guide describes the concept and functionality of the program, which transfers data from Tribon Assembly Planning (AP) to the Tribon Production Data Interface (PDI).
```
The transfer of assembly data to the PDI database is done using an interface program, wop2pdi.
```
The wop2pdi program is a part of the Tribon Production Data Interface (PDI) and follows the general guidelines for PDI.
```
For more information
 PDI in general, see section Basic.
The operation of the program is controlled via some environment variables, specifying whether the data should be transferred to PDI or not, log options etc.
The data transfer can be controlled by selecting a transfer criterion which is based on the assembly work status.
Please note that this program is available only as a Tribon product, and is delivered only on Windows. It is compatible with Tribon 5 and works together with Tribon 5 programs anddatabase.
User's Guide Production Data Interface
```
Chapter: General about Assembly Planning Interface
```
Copyright © 1993-2005 AVEVA AB
1.2 Document Structure
This guide provides a detailed description how to run the wop2pdi utility in Transfer of Assembly Data.
Information on how the program works and which data are transferred is given in Storage of Assembly Data.
User's Guide Production Data Interface
```
Chapter: General about Assembly Planning Interface
```
Copyright © 1993-2005 AVEVA AB
1.3 Conventions
In the following chapters will be found frequent references to programs and filenames incl. various examples describing how to execute a certain function. In these cases the followingconventions apply:
In some chapters you might find descriptions of syntax elements like program commands or file structures. For syntax definitions, the following notational elements are used:
User's Guide Production Data Interface
```
Chapter: General about Assembly Planning Interface
```
mono-spaced used for filenames, program names, computer generated output and similar software related items
mono-spaced bold user input to programs
sans serif software functions, application menu titles, product names
italic definition of a term, highlighting
[ ] optional element
```
{ } alternative choice (one must be chosen from the vertically listed choices or at least one from the repeated expressions, see below)
```
< > term
.... preceding expression may be repeated
Copyright © 1993-2005 AVEVA AB
2 Transfer of Assembly Data
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
2.1 Transfer Using wop2pdi.
The wop2pdi program is started from the command prompt with the following syntax:
```
Where;
```
User's Guide Production Data Interface
```
Chapter: Transfer of Assembly Data
```
-noparts the assembly tree is transferred without the references to the parts.
-all the complete assembly tree is transferred.
```
<assembly> only the specified assembly is transferred (including everything below).
```
-calc recalculation of the value for Bounding box, Weight and Centre of Gravity.
Copyright © 1993-2005 AVEVA AB
2.1.1 Checking Data Transfer
See also the general PDI environment variables, described in section Basic.r
User's Guide Production Data Interface
```
Chapter: Transfer of Assembly Data
```
SB_PDI_WOP_LOG The value can be set to any valid file name. This file will be installed in SB_SHIPPRINT directory, if there are errors in reading the Tribon databases. In this casethe file will contain the error messages.
If no value is to be set, possible messages are displayed on screen.
Copyright © 1993-2005 AVEVA AB
2.2 PDI Updating Principles
```
When wop2pdi is executed, the specified assembly will be transferred to PDI subject to the transfer parameters. At each new transfer the assemblies will get a new version number in thePDI database. If there are any changes in the tree structure (e.g. some assemblies have been removed), it is reflected in the event table. The code will indicate that it has been
```
'DELETED' instead of 'INSERTED' or 'UPDATED'.
User's Guide Production Data Interface
```
Chapter: Transfer of Assembly Data
```
Copyright © 1993-2005 AVEVA AB
3 Storage of Assembly Data
User's Guide Production Data Interface
Copyright © 1993-2005 AVEVA AB
3.1 Assembly
Each assembly is an item in the TPRE_ITEM table. The ITEM_NAME column contains the Tribon internal assembly name, which has to be unique. The user defined assembly name isstored as an alias in the ALIAS_NAME1 column. The complete user defined path of an assembly is con catenated from the names along the whole tree down to the assembly itself.
The detailed assembly properties are stored in the tables TPRE_ITEM and TPRE_WOP_ASSEMBLY.
User's Guide Production Data Interface
```
Chapter: Storage of Assembly Data
```
Copyright © 1993-2005 AVEVA AB
3.2 Assembly Tree
```
An assembly stored in PDI refers to its sub-assemblies via the Assembly Parent column (ASSY_PARENT_IKEY in the TPRE_ITEM table) of the sub-assemblies or referenced parts.
```
User's Guide Production Data Interface
```
Chapter: Storage of Assembly Data
```
Copyright © 1993-2005 AVEVA AB
3.3 Parts Referenced by an Assembly
```
If an assembly refers parts to hull parts, pipe parts, equipment, etc. these references are also stored in the PDI database (see the paragraph Assembly Tree).
```
If the referenced item already exists in PDI, the assembly refers to the real item. If the item is not stored in PDI, wop2pdi will create a "preliminary item". This is later replaced by the realitem, when this is transferred by the appropriate Tribon application.
A "preliminary item" is indicated by the value "preliminary" in the field ITEM_STATUS for the specific item.
User's Guide Production Data Interface
```
Chapter: Storage of Assembly Data
```
Copyright © 1993-2005 AVEVA AB
3.4 Items Handled by the PDI Assembly Module
Assemblies, all sub-assemblies, referenced parts and other related data are stored in a number of tables in the PDI database. The table containing detailed Assembly properties in theassembly table.
The table names and detailed definitions of the table columns and the data can be found in PDI itself. See section Basic for more information. Item types created and referenced bywop2pdi can be all kinds of model objects, referenced or generated by Tribon Assembly Planning, such as:
 Assemblies
 Equipment
 Pipe spools and pipe parts
 Ventilation spools and ventilation parts
 Structure parts
 Cableway parts
 Hull parts
 Assembly key-in parts *
 Components *
 Placed volumes *
Note that wop2pdi only will handle the references to parts. The program will not transfer any detailed part attributes to PDI. The detailed part data are transferred by each applicationspecific PDI transfer routine.
User's Guide Production Data Interface
```
Chapter: Storage of Assembly Data
```
- These parameters are handled as shell parts only. There are no transfer routines for detailed part attributes for these.
Copyright © 1993-2005 AVEVA AB
Python Documentation
Tribon M3
Copyright © 1993-2005 AVEVA AB
Documentation for Python
Python's standard documentation can be downloaded or viewed on-line at Python's official Website:
www.python.org/doc/
Earlier versions of documentation can be found here:
www.python.org/doc/versions.html
Python Documentation
Copyright © 1993-2005 AVEVA AB
User's Guide
Toolkit Preference Program
Tribon M3
Copyright © 1993-2005 AVEVA AB
1 Toolkit Preference
User's Guide Toolkit Preference Program
Copyright © 1993-2005 AVEVA AB
1.1 General
The property-sheet based application called Tribon Toolkit Preference is used to customize the behaviour of Tribon functions.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2 Attribute Templates
The Attribute Templates page is used to create and maintain attribute templates. An attribute template is a description of what kind of data a user-defined attribute consists of. Theattribute template is used when the user-defined attribute is created. For more information on user-defined attributes, please see the Vitesse documentation.
All attribute templates are stored in a Tribon database. The Tribon variable SB_SETTINGS_DB must point to this database.
Figure 1:1. Tribon Toolkit Preferences, Attribute Templates property page.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2.1 Categories
```
To make it easier to find a certain attribute template it is possible to create different attribute template categories (e. g. hull, pipe, or general). The names of the categories can onlycontain English letters, numbers, and '_'. The reason is that they are used to define a Python function.
```
Right-clicking the Categories node brings up a menu with all functions available for this node. These functions are described below.
New Category...
A new category is created by selecting the New Category... function. This will bring up a dialogue in which the category name can be entered.
Edit Obsolete templates...
```
This function will bring up a dialogue in which all obsolete templates (see below for a full description) are visible. The obsolete templates can be deleted within this dialogue. Please notethat after an obsolete template has been deleted, there is no way to check if an attribute is of the deleted attribute template type using the Vitesse user-defined Attributes function
```
attribute_is.
Recreate template database
This function must be used when attribute template objects have been copied from another project.
To copy all attribute templates from one project into another use a Tribon Database Utility and copy all objects named TEMPLATE-nnnnn from the settings database in the other projectinto the SB_SETTINGS_DB database. After the copy, recreate the template database using this function.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2.2 Category
Right-clicking a category node brings up a menu with all functions available for a category. These functions are described below.
New Template...
This function will bring up a dialogue where the name of the template should be entered. The name has the same restriction as category names.
Paste
```
This function will place the attribute template in the clipboard (placed there with the Copy function in the template menu) into the selected category.
```
Delete
This function will delete the selected category and all attribute templates within. Please note that all deleted attribute templates will be copied to the invisible obsolete category.
In an ORACLE based project, it is not possible to delete an attribute template if attributes based on this attribute template exist on any object.
Rename
This function makes it possible to rename the selected category.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2.3 Template
When a user-defined attribute is created, an attribute template must be specified. The attribute template is located in the SB_SETTINGS_DB database to get the information on what datathe user-defined attribute should contain.
Right-clicking a template node will bring up a menu with all functions available for a template. These functions are described below.
New Data...
This function will create a new data description within the selected template.
If attributes based on the attribute template exist on any object, adding data could create problems. This problem is avoided differently in an ORACLE based project and in a nativeproject.
```
In an ORACLE based project, all existing attribute based on the attribute template will be updated (the new data will be added to all attributes). However, the default value for the newdata will not be applied.
```
In a native project nothing will happen automatically to existing attributes. A Vitesse function called kcs_att.attribute_match exists to help in migrating attributes to the new attributetemplate.
Copy
This function will copy the selected attribute template into the clipboard.
Delete
This function will delete the attribute template.
In an ORACLE based project, it is not possible to delete an attribute template if attributes based on this attribute template exist on any object.
Rename
This function will make it possible to rename the selected data description.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2.4 Data
A user-defined attribute without any data is of limited use.
Data elements can be any of the following five types:
```
 Integer number (long).
```
```
 Real number (double precision).
```
```
 String (any length).
```
```
 Date (two long integers, the first indicates the number of seconds since midnight 1st January 1970 and the second indicates the number of milliseconds since the last second).
```
 File reference.
```
Each data description will have an index (the last column in the list to the right). This index should be used in the Vitesse API when referring to the data element within an attribute.
```
```
Each data description (except date) will have a default value that will be used when creating an attribute using this attribute template.
```
Right-clicking a data description will bring up a menu with all functions available for a data description. These functions are described below.
Edit
This function will bring up a dialogue in which the title and the default value of a data description can be edited.
Delete
This function deletes the selected data description from the attribute template. This is not recommended if the template is in use.
In an ORACLE based project, it is not possible to delete data from an attribute template if attributes based on this attribute template exist on any object.
Rename
This function makes it possible to rename a data description.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.2.5 Vitesse Alias Functions
When writing Vitesse scripts that handles user-defined attributes it is necessary to be able to check whether a user-defined attribute is based on a certain attribute template. In the VitesseAPI for user-defined attributes there is a method that performs this operation. It has two parameters, the attribute and the identity of an attribute template. Since the attribute template
identity is hard to remember, some Vitesse alias scripts are created in the directory pointed to by SB_PYTHON. The scripts are called kcs_att_<category>.py. There will be one
script created for each category in the database.
In an alias file there is one Vitesse function for each template in the category. The function is called <customer>_<category>_<template> where <customer> is taken fromSB_CUSTOMER. The only thing an alias function does is to return the identity of the template.
Obsolete Templates
A potential problem is the following scenario:
 Create an attribute template in category 'hull' and call it 'block'.
 Create an attribute based on this template.
 Delete the attribute template.
In this case there is no longer any information on this attribute. To solve this problem, all attribute templates that are deleted are saved in a special category called "obsolete". Thiscategory is never shown, but it is used when the Vitesse alias files are created to make it possible to refer to attributes of this type.
The Vitesse alias script for obsolete templates is called kcs_att_obsolete.py.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.3 Object Properties
On the Object Properties page different property schemes can be created. A property scheme determines which properties of an object a user see when they use the function Tools /Inquiry / Model in Drafting-based programs or the Properties function in the Design Manager. With a property scheme it is also possible to create customer specific properties that are
displayed together with the other properties. In Drafting-based programs there is a possibility to choose a property scheme within the Tools / Preferences dialogue.
Figure 1:2. Example of a Property Sheet from within Tribon.
Figure 1:3. Tribon Toolkit Preferences, Object Properties property page.
All property schemes are stored in a Tribon database. The Tribon variable SB_SETTINGS_DB must point to this database.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.3.1 Property Scheme
The top rectangle in the dialogue handles the schemes. The box shows the active scheme. The New button creates a new scheme and the Delete button deletes the active scheme.
Between releases of Tribon it often happens that new properties are added. However, this is not reflected in old schemes so these new properties will not be visible. This has been solvedby checking whether a scheme needs to be upgraded when the scheme is selected in Tribon Toolkit Preferences.
```
If the upgrade dialogue appears, you have to make a decision if the scheme should be upgraded to reflect the new properties or not. The recommended choice is to upgrade, but in somecircumstances (e. g. when the new release is only tested and most users still use the older version of Tribon) it could be better not to upgrade. All user-defined properties will be copied to
```
the upgraded scheme.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.3.2 Objects
The left box named Objects lists all known Tribon objects that can have properties.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.3.3 Properties
The Properties list contains all properties belonging to the selected object. The check box on each line indicates whether the property is visible or not. The title is a short description ofthe property. The tab indicates on which property page the property will be displayed. See Figure 1:2.: Example of a Property Sheet from within Tribon. for an example of a property sheet
```
with more than one tab (General and Advanced). The script is used for customer created properties and is a Tribon Vitesse script that will be executed before the properties are shown.
```
The New button creates a customer property. The Delete button deletes the selected user property. The Edit button edits the selected property.
For a user created property the title, tab, and script can be changed but for the ordinary Tribon properties only the tab can be changed.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.3.4 Script
Please observe that the script must be located in the directory SB_PYTHON.
For each user created property a function called get in the associated script is executed. The get function must return one string that will be presented as a property value along with allthe other values in the property sheet. This get function must be declared as below
```
Note: The argument list has been changed in relation to the previous release of Tribon.
```
The "get" function receives one parameter, a Vitesse Model class containing information on the object to display properties for.
```
If user-defined column headers is used (see below), the get script must return a list of strings, one for every column except for the first. The first column is always the property Title. If thenumber of strings is less than the number of column headers minus one, empty strings are used. If the number of strings is more than or equal to the number of column headers, the last
```
strings will be ignored.
Using user-defined headers, the get function must be declared as below
User-defined column headers
```
It is also possible to define the column headers in the different tabs. If a Vitesse script called <name-of-tab>_tab_<type-of-object>.py (without spaces, e. g. user_tab_pipe.py) is
```
found in SB_PYTHON, a get function in this script is called to define new column headers. The get function must return a list of strings defining the new column headers.
This get function must be declared as below
The get function receives one parameter, a Vitesse Model class containing information on the object to display properties for.
Figure 1:4. Example of a Property Sheet with user-defined columns from within Tribon.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
```
def get(*args):res = 'Some value'
```
return res
```
def get(*args):list = []
```
```
list.append("A stiffener")]list.append("Important")
```
return list
```
def get(*args):list = []
```
```
list.append("Property")list.append("Value")]
```
```
list.append("Additional value")return list
```
Copyright © 1993-2005 AVEVA AB
1.3.5 Editing user-defined properties.
When the user right-clicks a user-defined property and selects Edit, a pre-trigger called trig_draft_property_edit will be fired. Please see trigger documentation for more information.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.4 Drawing Types
On the Drawing Types page it is possible to create user-defined drawing types. All user-defined drawing data banks are named SB_PDBnnn, where nnn is any number from 001 to 999.Create a new drawing type by clicking the Create button.
Figure 1:5. Tribon Toolkit Preferences, Drawing Types property page.
```
Note: Please note that the Tribon environment variable SB_PDBnnn must be created manually.
```
The Import button can be used to import user-defined drawing types from a text file into the current project. The user will be asked to specify the location of the file containing drawingtypes.
The Export button can be used to export user-defined drawing types from the current project to a text file. The user will be asked to specify the file name.
To change the attributes of a user-defined data bank, double-click the corresponding line in the list. This will bring up a dialog making it possible to change the attributes.
There are three different types of drawing types:
 Standard
A standard drawing type is a pre-created drawing type
 User-defined
A user-defined drawing type is a drawing type created by the user.
 Obsolete.
```
An obsolete drawing type is a user-defined drawing type that is no longer valid. Obsolete drawing types are not shown in applications (e.g. the Open Drawing dialog). A drawingtype is made obsolete by checking the Obsolete check box in the Attribute dialog.
```
By default the user-defined drawing types will be listed in the order they are created. If a different order is needed then it is possible to change order by editing the text file assigned toSB_TDM_DRAWINGTYPE_LIST.
In a non-ORACLE projects, it is possible to create a data bank used for drawing previews. For more information see Tribon Drafting documentation.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.5 Object Subtypes
On the Object Subtypes page, object subtypes codes can be defined.
Figure 1:6. Tribon Toolkit Preferences, Object Subtypes property page.
Each object subtype code belongs to a Tribon object type. To define a new code, click on the Create button. To modify a code, double-click on the code value in the list.
The Import button can be used to import object subtype definitions from a text file into the current project. The user will be asked to specify the location of the file containing objectsubtype definitions.
The Export button can be used to export object subtype definitions from the current project to a text file. The user will be asked to specify the file name.
See also Tribon M3 User's Guide / Data Management / Concepts.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
1.6 Status Levels
On the Status Levels page, status level codes can be defined.
Figure 1:7. Tribon Toolkit Preferences, Status Levels property page.
To define a new code, select the appropriate status type and click on the Create button. To modify a code, double-click on the code value in the list.
```
For status level codes (Design, Manufacture, Assembly and Material Control status), there is a possibility to change the promote/demote sequence order by selecting a status value andclicking on the Move up and Move down buttons.
```
The Import button can be used to import status level definitions from a text file into the current project. The user will be asked to specify the location of the file containing status leveldefinitions.
The Export button can be used to export status level definitions from the current project to a text file. The user will be asked to specify the file name.
See also Tribon M3 User's Guide / Data Management / Concepts.
User's Guide Toolkit Preference Program
```
Chapter: Toolkit Preference
```
Copyright © 1993-2005 AVEVA AB
User's Guide
TDM Views
Tribon M3
Copyright © 1993-2005 AVEVA AB
1 Views
User's Guide TDM Views
Copyright © 1993-2005 AVEVA AB
1.1 General
This document defines the Oracle views available to end-users of TDM.
```
Important: It is important to realize that these views are the interface to Tribon using SQL. Don't ever access the tables or other Oracle objects directly since these are eligible tochange over time.
```
User's Guide TDM Views
```
Chapter: Views
```
Copyright © 1993-2005 AVEVA AB
1.2 View definitions
There are a number of views defined for end-user purpose. In general they contain data that you may combine with data from other views using a so-called join. The main join field to usefor Tribon objects are the OBJECT_ID field. The OBJECT_ID field represents the unique instance of a Tribon Object. Each version and/or revision of a named object has its unique
identifier. For examples on joins, see section Usage.
User's Guide TDM Views
```
Chapter: Views
```
Copyright © 1993-2005 AVEVA AB
1.2.1 TDM$ views
The TDM$ views are views describing non-persistent data. The views only contain information during an active session with a project selected.
User's Guide TDM Views
```
Chapter: Views
```
TDM$SESSION
Holds context information for current setting
Only available after a project is selected
Name Type Comment
```
USERNAME VARCHAR2(30) Name of currently logged on user
```
```
CURRENT_SCHEMA VARCHAR2(30) Name of the Oracle schema where the project exists
```
```
PROJECT_NAME VARCHAR2(30) Name of active project
```
```
SESSION_VERSION_ID NUMBER(5) Version identifier of version active in session
```
```
TDM_ENABLED VARCHAR2(3) Yes/No
```
```
DEFAULT_ACCESS VARCHAR2(10) Default access level to objects in project
```
Copyright © 1993-2005 AVEVA AB
1.2.2 TBS_ views
The TBS_ views contain "static" system level and settings data. Data in these tables may or may not be project dependent.
User's Guide TDM Views
```
Chapter: Views
```
TBS_SETTINGS
Holds the project settings for the project
Only available after a project is selected
Name Type Comment
```
PROJECT_NAME VARCHAR2(30) Name of project
```
```
PROPERTY VARCHAR2(64) Name of property
```
```
VALUE VARCHAR2(256) Value of property
```
TBS_OBJECT_TYPES
Holds the object types as defined by access control system
Only available after a project is selected
Name Type Comment
```
DATABANK VARCHAR2(30) Name of databank
```
```
OBJECT_CODE1 NUMBER(5) Object code 1
```
```
OBJECT_CODE2 NUMBER(5) Object code 2
```
```
OBJECT_TYPE VARCHAR2(200) Type/Class of object
```
Copyright © 1993-2005 AVEVA AB
1.2.3 TDM_ views
TDM_ views contain all exposed information about Tribon -projects and -objects.
User's Guide TDM Views
```
Chapter: Views
```
TDM_PROJECT
Information of all projects defined in the database
Always available
Name Type Comment
```
PROJECT_NAME VARCHAR2(30) Name of project
```
```
ACTIVE_VERSION_ID NUMBER(5) Active version identifier for object
```
```
DESCRIPTION VARCHAR2(200) Description of project
```
```
SCHEMA_NAME VARCHAR2(30) Name of the Oracle schema where the project exists
```
```
STD_PROJECT_NAME VARCHAR2(30) Name of active standard project
```
```
TDM_ENABLED VARCHAR2(3) Yes/No
```
```
DEFAULT_ACCESS VARCHAR2(10) Default access level to objects in project
```
```
CREATED_BY VARCHAR2(30) User that created the project
```
CREATED_DATE DATE Creation date
TDM_VERSION
Information of all project versions defined in the database
Always available
Name Type Comment
```
PROJECT_NAME VARCHAR2(30) Name of project
```
```
VERSION_ID NUMBER(5) Version identifier
```
```
VERSION_NAME VARCHAR2(30) Name of version
```
```
DESCRIPTION VARCHAR2(200) Description of project
```
```
PARENT_VERSION_ID NUMBER(5) Parent version
```
```
PURGED VARCHAR2(3) Version purged? (YES/NO)
```
ACTIVATE_DATE DATE Date of activation
```
CREATED_BY VARCHAR2(30) User that created the project
```
CREATED_DATE DATE Creation date
TDM_OBJECT
All objects in the project with respect to selected project and version
Only available after a project is selected
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
OBJECT_NAME VARCHAR2(26) Object name
```
```
VERSION_ID NUMBER(5) Version identifier for object
```
```
DATABANK VARCHAR2(30) Name of databank
```
```
OBJECT_CODE1 NUMBER(5) Object code 1
```
```
OBJECT_CODE2 NUMBER(5) Object code 2
```
```
ACCESS_LEVEL VARCHAR2(10) Access level to object
```
```
OBJECT_STATE VARCHAR2(10) State of the object
```
```
REVISION_NAME VARCHAR2(30) Revision name
```
```
REVISION_REMARK VARCHAR2(200) Revision remark
```
```
CREATED_BY VARCHAR2(30) User that created the object
```
CREATED_DATE DATE Creation date
```
MODIFIED_BY VARCHAR2(30) User that modified the object
```
MODIFIED_DATE DATE Modification date
TDM_STATUS
Holds the TDM status for all objects
Only available after a project is selected
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
DESIGN_STATUS VARCHAR2(200) Current design status
```
```
MANUFACTURE_STATUS VARCHAR2(200) Current manufacture status
```
```
ASSEMBLY_STATUS VARCHAR2(200) Current assembly status
```
```
MATERIAL_STATUS VARCHAR2(200) Current material control status
```
TDM_TDM_ ATTRIBUTE
Holds the TDM attributes for all objects
Only available after a project is selected
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
TYPECODE1 NUMBER(5) TDM Typecode1
```
```
TYPECODE2 NUMBER(5) TDM Typecode2
```
```
TYPECODE3 NUMBER(5) TDM Typecode3
```
```
TYPECODE4 NUMBER(5) TDM Typecode4
```
```
ALIAS1 VARCHAR2(2000) TDM Alias1
```
```
ALIAS2 VARCHAR2(2000) TDM Alias2
```
```
ALIAS3 VARCHAR2(2000) TDM Alias3
```
```
ALIAS4 VARCHAR2(2000) TDM Alias4
```
```
DESCRIPTION VARCHAR2(2000) TDM Description
```
```
REMARK VARCHAR2(2000) TDM Remark
```
TDM_COSTCODE
Holds Cost Code for all objects
Only available after a project is selected
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
COST_CODE VARCHAR2(2000) Costcode
```
TDM_PLANNING_UNIT
Holds Planning unit for all objects
Only available after a project is selected
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
PLANNING_UNIT VARCHAR2(2000) Planning unit
```
TDM_EXPORT_ATT
All export attributes in the project with respect to selected project and version.
Only available after a project is selected.
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
SEQ NUMBER(10) Sequence number
```
```
LABEL VARCHAR2(4000) Transfer set label
```
```
REMARK VARCHAR2(4000) Transfer set comment
```
TRANSFERDATE DATE Transfer date
```
USERNAME VARCHAR2(4000) User that performed export
```
TDM_IMPORT ATT
All export attributes in the project with respect to selected project and version.
Only available after a project is selected.
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
```
SEQ NUMBER(10) Sequence number
```
```
ORIGINAL_PROJECT VARCHAR2(4000) Name of original project
```
```
LABEL VARCHAR2(4000) Transfer set label
```
```
REMARK VARCHAR2(4000) Transfer set comment
```
TRANSFERDATE DATE Transfer date
```
USERNAME VARCHAR2(4000) User that performed import
```
Copyright © 1993-2005 AVEVA AB
1.2.4 TBU views
There are two categories of the TBU views. The TBU$ that contains an overview of user defined attributes available, and the TBU_ - the actual views of the user defined attributes.
Example of TBU views
Table 1: 1. The example view.
Click picture to enlarge
Figure 1:1. The example attribute template
User's Guide TDM Views
```
Chapter: Views
```
TBU$ATTRIBUTE
Holds all user defined attributes
Only available after a project is selected
Name Type Comment
```
CATEGORY VARCHAR2(100) Template category
```
```
NAME VARCHAR2(100) Template name
```
```
USER_VIEW VARCHAR2(30) View where the attribute data is held
```
```
CREATED_BY VARCHAR2(30) User that created the template
```
CREATED_DATE DATE Creation date
TBU_cccc_nnnn
Holds user defined attribute data for all objects
Only available after a project is selected
The view name is dependent on the User defined attribute name
Fields, their names and data types are dependent on the attribute defined
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
ELEMENT_ID NUMBER Internal usage
SEQ NUMBER Internal usage
Fields as defined by user
TBU_GENERAL_MYATTR
Example of a User defined attribute
Name Type Comment
```
OBJECT_ID RAW(16) Unique object identifier
```
ELEMENT_ID NUMBER Internal usage
SEQ NUMBER Internal usage
```
NAME VARCHAR2(1000) Field corresponding to NAME in the template
```
```
DESC VARCHAR2(1000) Field corresponding to DESC in the template
```
```
CODE NUMBER(10) Field corresponding to CODE in the template
```
WHEN DATE Field corresponding to WHEN in the template
Copyright © 1993-2005 AVEVA AB
1.3 Usage
User's Guide TDM Views
```
Chapter: Views
```
Copyright © 1993-2005 AVEVA AB
1.3.1 Availability
The views are available using any tool of your choice. The examples are using SQLPlus.
User's Guide TDM Views
```
Chapter: Views
```
Copyright © 1993-2005 AVEVA AB
1.3.2 Connecting
Depends on the tool you are using, but you connect using the same userid, password and service name as you use with Tribon M3.
```
C:>sqlplus /nolog
```
SQL>connect myname/mypassword@myservice
Connected.
User's Guide TDM Views
```
Chapter: Views
```
Copyright © 1993-2005 AVEVA AB
1.3.3 Project select
You select project by using the stored procedure SET_PROJECT with project and version of your preference.
User's Guide TDM Views
```
Chapter: Views
```
```
Examples:
```
1. Select a project using active version.
```
SQL>call set_project('myproj');
```
2. Select a project using older version.
```
SQL>call set_project('myproj', 2);
```
Copyright © 1993-2005 AVEVA AB
1.3.4 Data access
```
You select data from the views using Oracle SQL or the SQL defined by your tool (ODBC are for instance using another way of joins).
```
User's Guide TDM Views
```
Chapter: Views
```
```
Examples:
```
1. Select projects information for project myproj:
```
SQL>select * from tdm_projectswhere project_name = 'myproj';
```
2. Select object name and design status for objects beginning with myname:
SQL>select obj.object_name, stat.design_statusfrom tdm_object obj, tdm_status stat
```
where obj.object_id = stat.object_isand obj.object_name like 'myname%';
```
Copyright © 1993-2005 AVEVA AB
User's Guide
Tribon Print Server
Tribon M3
Copyright © 1993-2005 AVEVA AB
```
1 Tribon Print Server (TBPrintSrv)
```
Tribon Print Server is a piece of software that enables batch oriented processing of Tribon Drawings.
The Tribon Print Server is implemented as a COM server, available for use in any automation-enabled language. This means that you can use it in Visual Basic and Visual BasicScripting, JavaScript. But it may also be used from C++ or Python.
```
Note: Tribon Print Server (TBPrintSrv) will replace TBBatchPrint in Tribon M3.
```
User's Guide Tribon Print Server
Copyright © 1993-2005 AVEVA AB
1.1 Reference
The Server is made up of a number of objects.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Drawing Represents a Tribon drawing
Drawings A collection of Drawings
DrawingType Represents a Tribon drawing type
DrawingTypes A collection of DrawingType
Filter Filter object that may be used in conjunction with FindDrawings
FindDrawings Search for drawings
Printer Represents a printer
PrintJob The object that performs the output work
PrintOptions Output options drawings
TBApplication For initialization and termination of Tribon
Copyright © 1993-2005 AVEVA AB
1.2 Objects
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Copyright © 1993-2005 AVEVA AB
1.2.1 Drawing
This object represents on drawing that may be eligible for output.
DrawingType property
Sets or returns the type of drawing this object represents. See DrawingTypes object for more information.
Name property
Sets or returns the name of the Drawing object.
PrintOptions property
Sets or returns the output options associated with this Drawing object. See PrintOptions object for more information.
Revision property
Sets or returns the revision of the Drawing object.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
DrawingType property Defines the type of drawing this is, see DrawingTypes object
Name property The drawing name
PrintOptions property Print options specific for this drawing, see PrintOptions object
Revision property The drawing revision
Object.DrawingType [= Value]
Object A Drawing object
Value A DrawingType object that represents the type of the drawing
Object.Name [= String]
Object A Drawing object
String A string that represents the name of the drawing
Object.PrintOptions [= Value]
Object A Drawing object
Value A PrintOptions object, with specific output options for this particular drawing object.
Object.Name [= String]
Object A Drawing object
String A string that represents the revision of the drawing
Copyright © 1993-2005 AVEVA AB
1.2.2 Drawings
A collection of Drawing objects. This may be found our associated with a number of objects.
Add method
Adds a Drawing object to the Drawings collection. See Drawing for more information.
AddDrawings method
Adds a collection of Drawings to the Drawings collection.
Clear method
Clears a collection of all Drawings.
Count property [read only]
Returns the number of drawings in a collection.
Item property [default property]
Sets or returns a drawing at a specific position in a collection.
Remove method
Removes a Drawing from the collection.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Add method Add a drawing to this collection
AddDrawings method Add the drawings from one collection to another
Clear method Clear the collection
Count property [read only] Number of drawings in the collection
Filter <Not used>
Item property [default property] A drawing in the collection
Remove method Remove a drawing form the collection
Object.Add Value
Object A Drawings collection object.
Value The Drawing object to add to the collection.
Object.AddDrawings Value
Object A Drawings collection object.
Value The Drawings collection to add to the collection.
Object.Clear
Object A Drawings collection object.
Object.Count
Object A Drawings collection object.
```
Object.Item(Index) [= Value]
```
Object A Drawings collection object.
Index The index of the Drawing object in the collection
Value A Drawing object
```
Object.Remove(Index)
```
Object A Drawings collection object.
Index The index of the Drawing object in the collection
Copyright © 1993-2005 AVEVA AB
1.2.3 DrawingType
Description property [read only]
Returns the description of a DrawingType.
Name property
Sets or returns the name of a DrawingType.
Type property [read only]
Returns the type of a DrawingType.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Description property [read only] Description of the drawing type
Name property Drawing type name
Type property [read only] Tells us how the drawing type is defined
[String =] Object.Description
String An arbitrary string
Object A DrawingType object.
Object.Description [= String]
Object A DrawingType object.
String A string describing drawing databanks in Tribon. E.g. a Databank logical name or a file path.
[Value =] Object.Description
Value A TbpDrawingTypeEnum variable.
Object A DrawingType object.
Copyright © 1993-2005 AVEVA AB
1.2.4 DrawingTypes
Count property [read only]
Returns the number of DrawingTypes in the collection.
Item property [read only / default property]
Sets or returns a drawing at a specific position in a collection.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Count property [read only] Number of drawing types in the collection
Item property [read only / default property] A drawing type in the collection
Object.Count
Object A DrawingTypes collection object.
```
Object.Item(Index)
```
Object A DrawingTypes collection object.
Index The index of the DrawingType object in the collection
Copyright © 1993-2005 AVEVA AB
1.2.5 Filter
Name property
Sets or returns the name filter string of the filter object.
Revision property
Sets or returns the revision filter string of the filter object.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Name property Drawing name filter string
Revision property Drawing revision filter string
Object.Name [= String]
Object A Filter object
String A string to use as filter on name for drawings, wildcards may be used.
Object.Revision [= String]
Object A Filter object
String A string to use as filter on revision for drawings, wildcards may be used.
Copyright © 1993-2005 AVEVA AB
1.2.6 FindDrawings
Drawings property [read only]
Returns a collection of all Drawings matching the filtering criteria.
DrawingType property
Sets or returns the DrawingTypes used to filter for drawings.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Drawings property [read only] The drawings collection that meets the drawingtype/filter criteria
DrawingType property Type of drawings to search for
Filter The filter to use in the search, see Filter object
Object.Drawings [Filter], [DrawingType]
Object A FindDrawings object.
Filter A string or a Filter object. If you use a string, that will be used to filter on drawing name.
DrawingType A string or DrawingType object. If you use a string, is should be a logical databank name, or a path to a drawing databank.
Object.DrawingType [= Value]
Object A Drawings collection object.
Value A DrawingType object
Copyright © 1993-2005 AVEVA AB
1.2.7 Printer
DeviceName property [read only]
Returns the device name of the selected printer.
Orientation property
Sets or returns the paper orientation of the printer.
PaperLength property
Sets or returns the length of the paper. If set, it overrides any PaperSize settings
PaperSize property
Sets or returns the length of the paper. If set, it overrides any PaperSize settings
PaperWidth property
Sets or returns the width of the paper. If set, it overrides any PaperSize settings
SelectPrinter method
Selects the Windows defined printer to use with this Printer object
ShowPageSetupDlg method
Shows the default page setup dialog for the selected printer. May have changed printer and settings on return.
ShowPrintSetupDlg method
Shows the default print setup dialog for the selected printer. May have changed printer and settings on return.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
DeviceName property [read only] The device name of the printer
Orientation property Paper orientation
PaperLength property Length of paper
PaperSize property Size of paper as defined by various standards, e.g. ISO
PaperWidth property Width of paper
SelectPrinter method Select the windows printer to use
ShowPageSetupDlg method Show the page setup dialog
ShowPrintSetupDlg method Show the printer setup dialog
Object.DeviceName
Object A Printer object.
Object.Orientation [= Value]
Object A Printer object.
Value A TbpOrientationEnum variable.
Object.PaperLength [= Value]
Object A Printer object.
Value The length of the paper in mm.
Object.PaperSize [= Value]
Object A Printer object.
Value The size of the paper according to the DMPAPER constants. See appendix for more info.
Object.PaperWidth [= Value]
Object A Printer object.
Value The width of the paper in mm.
Object.SelectPrinter Name [, Server]
Object A Printer object.
Name A string that is the name of the printer.
Server For network printers the name of the printer server
Object.ShowPageSetupDlg
Object A Printer object.
Object.ShowPrintSetupDlg
Object A Printer object.
Copyright © 1993-2005 AVEVA AB
1.2.8 PrintJob
Drawings property
Sets or returns the collection of Drawings to process in this PrintJob.
OnPrintEnd event
Gets called when a PrintJob has finished processing a Drawing.
OnPrintStart event
Gets called before a PrintJob starts processing a Drawing.
Printer property
Sets or returns the Printer to be used for processing the Drawings collection.
PrintOptions property
Sets or returns the default PrintOptions to be used for processing the Drawings collection.
StartPrint method
Starts processing the drawings associated with this PrintJob using the Printer and PrintOptions assigned.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Drawings property The collection of drawings to output
OnPrintEnd event Notification of the end of a print operation for a drawing
OnPrintStart event Notification of the start of a print operation for a drawing
Printer property The printer to use for output, see Printer object
PrintOptions property The default options to use for output
StartPrint method Start the output process
Object.Drawings [= Drawings]
Object A FindDrawings object.
Drawings A collection of drawings to assign to the printjob.
```
Object_OnPrintEnd(Name, State)
```
Object A PrintJob object.
Name The name of the drawing that was processed.
State The finishing status of the processing.
```
Object_OnPrintStart(Name)
```
Object A PrintJob object.
Name The name of the drawing that was processed.
Object.Printer [= Value]
Object A PrintJob object.
Value A Printer object.
Object.PrintOptions [= Value]
Object A PrintJob object.
Value A PrinterOptions object.
Object.StartPrint
Object A PrintJob object.
Copyright © 1993-2005 AVEVA AB
1.2.9 PrintOptions
AutoScale property
Sets or returns the AutoScale option.
CenterOnPage property
Sets or returns the AutoScale option.
Copies property
Sets or returns the Copies option.
EffectivePrintArea property
Sets or returns the EffectivePrintArea option.
NameMask property
Sets or returns the NameMask string.
Orientation property
Sets or returns the Orientation option.
OutputDirectory property
Sets or returns the OutputDirectory path.
PrintToFile property
Sets or returns the PrintToFile option.
Rotation property
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
AutoScale property Auto scale the drawing to fit the page size
CenterOnPage property Centre the drawing on the page
Copies property Number of copies to print
EffectivePrintArea property The output print area to use
HideDrawingForm <Not used>
NameMask property Mask to use for file names when printing to file.
Orientation property Page orientation
OutputDirectory property Directory to use when printing to file.
OverwriteExisting <Not used>
PrintToFile property Print drawing to file
Rotation property Rotate drawing on paper
Scale property Scale drawing
Object.AutoScale [= Boolean]
Object A PrintJob object.
Boolean Auto scale, true or false.
Object.CenterOnPage [= Boolean]
Object A PrintJob object.
Boolean Centre drawing on page, true or false.
Object.Copies [= Number]
Object A PrintJob object.
Number Number of copies to produce.
Object.EffectivePrintArea [= Value]
Object A PrintJob object.
Value The print area as a TbpPrintAreaEnum variable.
Object.NameMask [= String]
Object A PrintJob object.
```
String The mask to use to produce output names when using the PrintToFile option. Use an asterisk (*) to mark the position of the drawing name.
```
Object.Orientation [= Value]
Object A PrintJob object.
Value The orientation as a TbpOrientationEnum variable.
Object.OutputDirectory [= String]
Object A PrintJob object.
String The directory to write output to. Used in conjunction with the PrintToFile option.
Object.PrintToFile [= Boolean]
Object A PrintJob object.
Boolean Print output to file, true or false.
Sets or returns the Rotation option.
Scale property
Sets or returns the Scale value.
Object.Rotation [= Value]
Object A PrintJob object.
Value The rotation as a TbpRotationEnum variable.
Object.Orientation [= Value]
Object A PrintJob object.
Value The scale to use for printing.
Copyright © 1993-2005 AVEVA AB
1.2.10 TBApplication
TBApplication is the Tribon application object. Should be created, initialized and retained until all work with the server is done.
Initialize method
Initializes Tribon. Should be called before any other functionality is used in this server.
Terminate method
Terminates Tribon. No new operations should be performed after this have been called.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Initialize method Initialize Tribon
Terminate method Terminate Tribon
Object.Initialize
Object A PrintJob object.
Object.Terminate
Object A PrintJob object.
Copyright © 1993-2005 AVEVA AB
1.2.11 Enumerations
TbpDrawingTypeEnum
TbpOrientationEnum
TbpPrintAreaEnum
TbpPrintStatusEnum
TbpRotationEnum
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
tptPath 2 Drawing type specified as a string - path or logical name.
tptStandard 0 The drawing type is a Tribon system defined.
tptUser 1 The drawing type is user defined.
tpoLandscape 0 Landscape.
tpaPortrait 1 Portrait.
tpaDrawingExtension 1 Output everything that's on the drawing.
tpaDrawingForm 0 Output within the form boundary.
tpsDrawingNotFound 2 The drawing was not found.
tpsEnded 1 Output operation ended normally.
tpsError 4 Output operation ended abnormally.
tpsPrinterError 3 The printer signalled an error.
tpsStarted 0 Print started
tpr0 1 Zero degrees rotation of drawing.
tpr90 2 90 degrees rotation of drawing.
tpr180 3 180 degrees rotation of drawing.
tpr270 4 270 degrees rotation of drawing.
tprAuto 0 Auto rotate the drawing.
Copyright © 1993-2005 AVEVA AB
1.3 Examples
The examples shown are available in the samples directory of the Tribon installation.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Copyright © 1993-2005 AVEVA AB
```
1.3.1 A Visual Basic scripting example: (tbp.vbs)
```
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
```
Example:
```
''''''''''''''''''''''''''''''''''''
'
' TBP.VBS
'
' AVEVA
' Date: 2003-02-10
'
''''''''''''''''''''''''''''''''''''
Option Explicit
'On Error Resume Next
''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Event handler
''''''''''''''''''''''''''''''''''''''''''''''''''''''
```
Sub IPrintJob_OnPrintEnd(DrawingsName, Code)
```
Wscript.echo "Printed: " & DrawingsName & ", status: " &Code
End Sub
''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Main Script Code
''''''''''''''''''''''''''''''''''''''''''''''''''''''
dim app, fnd, job, prt
Define a event handler for the OnPrintEnd event
```
set app = wscript.createobject("TBPrintSrv.TBApplication")
```
app.Initialize
```
set fnd = wscript.createobject("TBPrintSrv.FindDrawings")
```
```
set job = wscript.createobject("TBPrintSrv.PrintJob", "IPrintJob_")
```
```
set prt = wscript.createobject("TBPrintSrv.Printer")
```
```
wscript.echo("Start")
```
Create and initialize the TBApplication object
```
set job.Drawings = fnd.Drawings("MW*", "SB_PDB")
```
set job.Printer = prt
job.Printer.SelectPrinter "P015", "NTSRV7"
job.PrintOptions.PrintToFile = True
Search for objects matching "MW*" on databank "SB_PDB and associate this collectionwith the PrintJob Drawings collection.
job.PrintOptions.NameMask = "VBS*.PS"
job.StartPrint
app.Terminate
```
wscript.echo("End")
```
Select a printer, and set some basic options - Start print.
Copyright © 1993-2005 AVEVA AB
```
1.3.2 A Python example: (tbp.py)
```
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
```
Example:
```
"""Example on how to use TBPrintSrv from Python.
This example needs win32com for Python to run.
""" Note: You need win32com for Python installed.
import TBPrintSrv
```
app = TBPrintSrv.TBApplication()
```
```
fnd = TBPrintSrv.FindDrawings()
```
```
job = TBPrintSrv.PrintJob()
```
```
prt = TBPrintSrv.Printer()
```
print "Start"
```
job.Drawings.AddDrawings(fnd.GetDrawings("MW*","SB_PDB"))
```
job.Printer = prt
# Remember to "escape" backslash
```
job.Printer.SelectPrinter("\\\\NTSRV7\\P015")
```
job.PrintOptions.PrintToFile = 1
job.PrintOptions.NameMask = "VBS*.PS"
if job.Drawings.Count:
```
print "Printing " + str(job.Drawings.Count) +" drawings."
```
```
job.StartPrint()
```
```
else:
```
print "No drawings found"
print "End"
Copyright © 1993-2005 AVEVA AB
```
1.3.3 A Visual Basic example: (TBPrintSrv.vbp)
```
This is an example on TBPrintSrv usage with a GUI. Accidentally this is also the Gui replacement for TBBatchPrint. The code is free to use and modify to suit your needs.
The Visual Basic source for the main dialog
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
```
Example:
```
Option ExplicitPrivate fTribon As TBApplication
Private fTypes As DrawingTypesPrivate fDrws As Drawings
Private fPrinter As TBPrintSrv.PrinterPrivate WithEvents fJob As PrintJob
Attribute fJob.VB_VarHelpID = -1Private fJobOpts As PrintOptions
Private fCpos As Integer
```
Private Sub cmdAddToJob_Click()MoveDrawings lvDrawList, lvDrawJob, False
```
lvDrawJob.SetFocusEnd Sub
Move drawings from selection list to print job list
```
Private Sub cmdAddAllToJob_Click()MoveDrawings lvDrawList, lvDrawJob, True
```
lvDrawJob.SetFocusEnd Sub
Move all drawings from selection list to print job list
```
Private Sub cmdOptions_Click()If fJobOpts Is Nothing Then
```
Set fJobOpts = New PrintOptionsEnd If
Set frmOptions.fOpt = fJobOptsfrmOptions.Caption = "Options for the print job"
frmOptions.Show vbModal, Me
If frmOptions.fOptSet ThenchJobOptions.Enabled = True
chJobOptions.Value = 1End If
End Sub
Show print options for the entire job
```
Private Sub cmdPrint_Click()Dim mDrw As Drawing
```
Dim mLi As ListItemFor Each mLi In lvDrawJob.ListItems
Start printing
fJob.Drawings.Add mLi.Tag The Drawing object is stored in the Tag attribute
Next
fPrinter.SelectPrinter cbPrinters.Text Select the printer
Set fJob.Printer = fPrinterIf chJobOptions.Value = 1 Then
Set fJob.PrintOptions = fJobOptsElse
Set fJob.PrintOptions = NothingEnd If
```
fCpos = 1fJob.StartPrint
```
fJob.Drawings.ClearEnd Sub Clear the drawings collection upon completion
```
Private Sub cmdPrintSetup_Click()
```
```
fPrinter.SelectPrinter (cbPrinters.Text)fPrinter.ShowPrintSetupDlg
```
cbPrinters.Text = fPrinter.DeviceName
End Sub
Show print setup dialog
```
Private Sub cmdRefresh_Click()On Error GoTo Error
```
Dim mFind As New FindDrawingsDim drw As Drawing
Dim li As ListItem
UpdateFilterCB cbFilter.Text
If cbDrawType.ListIndex >= 0 ThenmFind.DrawingType =
Search the Drawing databank for drawings accordingto the name filter and present it in the list view.
```
fTypes(cbDrawType.ItemData(cbDrawType.ListIndex))Else
```
mFind.DrawingType.Name = cbDrawType.TextEnd If
Set drawing type to search for
```
Set fDrws = mFind.Drawings(cbFilter.Text)lvDrawList.ListItems.Clear
```
For Each drw In fDrwsAddListItem lvDrawList, drw
Next
lvDrawList.SetFocusExit Sub
```
Error:MsgBox Err.Description, vbExclamation, "Error"
```
End Sub
Find drawings using the string in the filter text box
```
Private Sub fJob_OnPrintEnd(DrawingName As String, Status As TBPrintSrv.TbpPrintStatusEnum)sbStatus.SimpleText = ""
```
```
lvDrawJob.ListItems(fCpos).SubItems(3) = "Printed"
```
```
fCpos = fCpos + 1End Sub
```
```
Private Sub fJob_OnPrintStart(DrawingName As String)sbStatus.SimpleText = "Printing " & DrawingName
```
End Sub
Event handler for print end and start
```
Private Sub Form_Load()
```
Set fTribon = New TBApplicationSet fTypes = New DrawingTypes
Set fJob = New PrintJobDim mType As DrawingType
Dim mPrt As PrinterDim i As Long
```
'center the formMe.Move (Screen.Width - Me.Width) / 2, (Screen.Height - Me.Height) / 2
```
cbDrawType.Clear
```
For i = 0 To fTypes.Count - 1cbDrawType.AddItem (fTypes(i).Description)
```
```
cbDrawType.ItemData(cbDrawType.NewIndex) = iNext
```
cbDrawType.ListIndex = 1
Initialize drawing types combo box
Set fPrinter = New TBPrintSrv.PrinterFor Each mPrt In Printers
cbPrinters.AddItem mPrt.DeviceNameIf mPrt.DeviceName = fPrinter.DeviceName Then
cbPrinters.ListIndex = cbPrinters.ListCount - 1End If
NextEnd Sub
```
Private Sub UpdateFilterCB(fltStr As String)Dim i As Long
```
```
If Len(fltStr) > 0 Theni = 0
```
```
While i < cbFilter.ListCount And cbFilter.List(i) <> fltStri = i + 1
```
Wend
If i = cbFilter.ListCount ThencbFilter.AddItem fltStr
End IfEnd If
End Sub
```
Private Sub MoveDrawings(Source As ListView, target As ListView, All As Boolean)Dim i As Integer
```
```
i = 1While i <= Source.ListItems.Count
```
```
If All Or Source.ListItems(i).Selected Then
```
```
If target Is Nothing ThenSource.ListItems.Remove (i)
```
```
i = i - 1Else
```
```
AddListItem target, Source.ListItems(i).TagEnd If
```
End Ifi = i + 1
WendEnd Sub
Move drawings between two listviews
```
Private Sub AddListItem(lv As ListView, drw As Drawing)
```
```
Dim li As ListItemSet li = lv.ListItems.Add(, , drw.Name)
```
Set li.Tag = drwli.ListSubItems.Add , , drw.Revision
li.ListSubItems.Add , , drw.DrawingType.Descriptionli.ListSubItems.Add , , ""
End Sub
Add an item to a listview, store Drawing object in Tagattribute of ListItem
```
Private Sub lvDrawJob_DragDrop(Source As Control, x As Single, y As Single)If TypeOf Source Is ListView Then
```
MoveDrawings Source, lvDrawJob, FalselvDrawJob.SetFocus
End IfEnd Sub
Drop drawings to the Job listview
```
Private Sub lvDrawJob_KeyDown(KeyCode As Integer, Shift As Integer)Dim lLeft As Integer
```
Dim lTop As Integer
If KeyCode = 93 ThenlTop = lvDrawJob.Top + lvDrawJob.SelectedItem.Top + 300
```
lLeft = lvDrawJob.Left + lvDrawJob.SelectedItem.Left + 100PopupMenu pmList, , lLeft, lTop, miOptions
```
End IfEnd Sub
```
Private Sub lvDrawJob_MouseDown(Button As Integer, Shift As Integer, x As Single, y As Single)If Button = vbRightButton Then
```
PopupMenu pmList, , , , miOptionsEnd If
End Sub
Show the popup menu
```
Private Sub lvDrawJob_DblClick()miOptions_Click
```
End Sub
```
Private Sub lvDrawList_MouseMove(Button As Integer, Shift As Integer, x As Single, y As Single)If Button = vbLeftButton Then
```
lvDrawList.Drag vbBeginDragEnd If
End Sub
Begin the drag operation
```
Private Sub miCancel_Click()Dim mLi As ListItem
```
For Each mLi In lvDrawJob.ListItemsIf mLi.Selected Then
```
Set mLi.Tag.PrintOptions = NothingmLi.SubItems(3) = ""
```
End IfNext
End Sub
Clear options set on drawings
```
Private Sub miDelete_Click()MoveDrawings ActiveControl, Nothing, False
```
End Sub
Remove drawings
```
Private Sub miOptions_Click()If TypeOf ActiveControl Is ListView Then
```
ShowOptions ActiveControlEnd If
End Sub
```
Private Sub ShowOptions(Source As ListView)Dim mLi As ListItem
```
If Not Source.SelectedItem Is Nothing ThenSet frmOptions.fOpt = Source.SelectedItem.Tag.PrintOptions
frmOptions.Caption = "Options for specific drawings"frmOptions.Show vbModal, Me
Open options form for one or more drawings
If frmOptions.fOptSet ThenFor Each mLi In lvDrawJob.ListItems
If mLi.Selected ThenmLi.Tag.PrintOptions = frmOptions.fOpt
```
mLi.SubItems(3) = "Modified"End If
```
NextEnd If
End IfEnd Sub
Set a copy of PrintOptions for each selected drawing
Copyright © 1993-2005 AVEVA AB
1.3.4 Options Dialog
The Visual Basic source for the Options dialog
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Option ExplicitPublic fOpt As TBPrintSrv.PrintOptions
Public fOptSet As Boolean
```
Private Sub cmdBrowse_Click()
```
Dim mDir As StringmDir = Helpers.get_Folder
If mDir <> "" ThentbOutDir.Text = mDir
End IfEnd Sub
Use the Helper module to use the ShellBrowser
```
Private Sub chAutoScale_Click()tbScale.Enabled = chAutoScale.Value <> vbChecked
```
' udScale.Enabled = tbScale.EnabledEnd Sub
```
Private Sub chToFile_Click()tbOutDir.Enabled = chToFile.Value = vbChecked
```
tbNameMask.Enabled = tbOutDir.EnabledcmdBrowse.Enabled = tbOutDir.Enabled
End Sub
Enable/disable controls associated with PrintToFile
```
Private Sub cmdApply_Click()SetOptions
```
End Sub
```
Private Sub cmdCancel_Click()Unload Me
```
End Sub
```
Private Sub cmdOK_Click()SetOptions
```
Unload MeEnd Sub
```
Private Sub SetOptions()With fOpt
```
.AutoScale = chAutoScale.Value.CenterOnPage = chCenter.Value
```
.Copies = tbCopies.Text.EffectivePrintArea = cbPrintArea.ItemData(cbPrintArea.ListIndex)
```
```
.NameMask = tbNameMask.Text.Orientation = cbOrientation.ItemData(cbOrientation.ListIndex)
```
.OutputDirectory = tbOutDir.Text
```
.PrintToFile = chToFile.Value.Rotation = cbRotation.ItemData(cbRotation.ListIndex)
```
```
.Scale = CDbl(tbScale.Text)End With
```
```
fOptSet = True
```
End Sub
Set values to the PrintOptions object passed according to the settings made
```
Private Sub GetOptions()With fOpt
```
```
chAutoScale.Value = Abs(CInt(.AutoScale))chCenter.Value = Abs(CInt(.CenterOnPage))
```
```
tbCopies.Text = .CopiescbPrintArea.ListIndex = FindEntry(cbPrintArea, .EffectivePrintArea)
```
```
tbNameMask.Text = .NameMaskcbOrientation.ListIndex = FindEntry(cbOrientation, .Orientation)
```
```
tbOutDir.Text = .OutputDirectorychToFile.Value = Abs(CInt(.PrintToFile))
```
```
cbRotation.ListIndex = FindEntry(cbRotation, .Rotation)tbScale.Text = Format(.Scale, "#####0.000")
```
End WithchAutoScale_Click
chToFile_Click
End Sub
Set values from the PrintOptions object passed
```
Private Sub Form_Load()Dim str As String
```
```
'center the formMe.Move (Screen.Width - Me.Width) / 2, (Screen.Height - Me.Height) / 2
```
GetOptions
If cbPrintArea.ListIndex < 0 Then cbPrintArea.ListIndex = 0
If cbOrientation.ListIndex < 0 Then cbOrientation.ListIndex = 0If cbRotation.ListIndex < 0 Then cbRotation.ListIndex = 0
```
fOptSet = FalseEnd Sub
```
```
Private Function FindEntry(pList As Control, pval As Integer) As Integer
```
Dim i As IntegerFindEntry = -1
If TypeOf pList Is ComboBox Or TypeOf pList Is ListBox ThenFor i = 0 To pList.ListCount - 1
```
If pList.ItemData(i) = pval ThenFindEntry = i
```
End IfNext
End IfEnd Function
Get the enum type from a listbox using ItemData to hold the value
Copyright © 1993-2005 AVEVA AB
1.4 Appendix
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Copyright © 1993-2005 AVEVA AB
1.4.1 PaperSize table
This is defined in windows library and may be used to specify paper sizes to a Printer. Please note that you must be running Windows 2000 or higher for paper sizes >=DMPAPER_DBL_JAPANESE_POSTCARD.
User's Guide Tribon Print Server
```
Chapter: Tribon Print Server (TBPrintSrv)
```
Windows constant name # Description
DMPAPER_LETTER 1 Letter 8 1/2 x 11 in
DMPAPER_LETTERSMALL 2 Letter Small 8 1/2 x 11 in
DMPAPER_TABLOID 3 Tabloid 11 x 17 in
DMPAPER_LEDGER 4 Ledger 17 x 11 in
DMPAPER_LEGAL 5 Legal 8 1/2 x 14 in
DMPAPER_STATEMENT 6 Statement 5 1/2 x 8 1/2 in
DMPAPER_EXECUTIVE 7 Executive 7 1/4 x 10 1/2 in
DMPAPER_A3 8 A3 297 x 420 mm
DMPAPER_A4 9 A4 210 x 297 mm
DMPAPER_A4SMALL 10 A4 Small 210 x 297 mm
DMPAPER_A5 11 A5 148 x 210 mm
```
DMPAPER_B4 12 B4 (JIS) 250 x 354
```
```
DMPAPER_B5 13 B5 (JIS) 182 x 257 mm
```
DMPAPER_FOLIO 14 Folio 8 1/2 x 13 in
DMPAPER_QUARTO 15 Quarto 215 x 275 mm
DMPAPER_10X14 16 10x14 in
DMPAPER_11X17 17 11x17 in
DMPAPER_NOTE 18 Note 8 1/2 x 11 in
DMPAPER_ENV_9 19 Envelope #9 3 7/8 x 8 7/8
DMPAPER_ENV_10 20 Envelope #10 4 1/8 x 9 1/2
DMPAPER_ENV_11 21 Envelope #11 4 1/2 x 10 3/8
DMPAPER_ENV_12 22 Envelope #12 4 \276 x 11
DMPAPER_ENV_14 23 Envelope #14 5 x 11 1/2
DMPAPER_CSHEET 24 C size sheet
DMPAPER_DSHEET 25 D size sheet
DMPAPER_ESHEET 26 E size sheet
DMPAPER_ENV_DL 27 Envelope DL 110 x 220mm
DMPAPER_ENV_C5 28 Envelope C5 162 x 229 mm
DMPAPER_ENV_C3 29 Envelope C3 324 x 458 mm
DMPAPER_ENV_C4 30 Envelope C4 229 x 324 mm
DMPAPER_ENV_C6 31 Envelope C6 114 x 162 mm
DMPAPER_ENV_C65 32 Envelope C65 114 x 229 mm
DMPAPER_ENV_B4 33 Envelope B4 250 x 353 mm
DMPAPER_ENV_B5 34 Envelope B5 176 x 250 mm
DMPAPER_ENV_B6 35 Envelope B6 176 x 125 mm
DMPAPER_ENV_ITALY 36 Envelope 110 x 230 mm
DMPAPER_ENV_MONARCH 37 Envelope Monarch 3.875 x 7.5 in
DMPAPER_ENV_PERSONAL 38 6 3/4 Envelope 3 5/8 x 6 1/2 in
DMPAPER_FANFOLD_US 39 US Std Fanfold 14 7/8 x 11 in
DMPAPER_FANFOLD_STD_GERMAN 40 German Std Fanfold 8 1/2 x 12 in
DMPAPER_FANFOLD_LGL_GERMAN 41 German Legal Fanfold 8 1/2 x 13 in
```
DMPAPER_ISO_B4 42 B4 (ISO) 250 x 353 mm
```
DMPAPER_JAPANESE_POSTCARD 43 Japanese Postcard 100 x 148 mm
DMPAPER_9X11 44 9 x 11 in
DMPAPER_10X11 45 10 x 11 in
DMPAPER_15X11 46 15 x 11 in
DMPAPER_ENV_INVITE 47 Envelope Invite 220 x 220 mm
DMPAPER_RESERVED_48 48 RESERVED--DO NOT USE
DMPAPER_RESERVED_49 49 RESERVED--DO NOT USE
DMPAPER_LETTER_EXTRA 50 Letter Extra 9 \275 x 12 in
DMPAPER_LEGAL_EXTRA 51 Legal Extra 9 \275 x 15 in
DMPAPER_TABLOID_EXTRA 52 Tabloid Extra 11.69 x 18 in
DMPAPER_A4_EXTRA 53 A4 Extra 9.27 x 12.69 in
DMPAPER_LETTER_TRANSVERSE 54 Letter Transverse 8 \275 x 11 in
DMPAPER_A4_TRANSVERSE 55 A4 Transverse 210 x 297 mm
DMPAPER_LETTER_EXTRA_TRANSVERSE 56 Letter Extra Transverse 9\275 x 12 in
DMPAPER_A_PLUS 57 SuperA/SuperA/A4 227 x 356 mm
DMPAPER_B_PLUS 58 SuperB/SuperB/A3 305 x 487 mm
DMPAPER_LETTER_PLUS 59 Letter Plus 8.5 x 12.69 in
DMPAPER_A4_PLUS 60 A4 Plus 210 x 330 mm
DMPAPER_A5_TRANSVERSE 61 A5 Transverse 148 x 210 mm
```
DMPAPER_B5_TRANSVERSE 62 B5 (JIS) Transverse 182 x 257 mm
```
DMPAPER_A3_EXTRA 63 A3 Extra 322 x 445 mm
DMPAPER_A5_EXTRA 64 A5 Extra 174 x 235 mm
```
DMPAPER_B5_EXTRA 65 B5 (ISO) Extra 201 x 276 mm
```
DMPAPER_A2 66 A2 420 x 594 mm
DMPAPER_A3_TRANSVERSE 67 A3 Transverse 297 x 420 mm
DMPAPER_A3_EXTRA_TRANSVERSE 68 A3 Extra Transverse 322 x 445 mm
DMPAPER_DBL_JAPANESE_POSTCARD 69 Japanese Double Postcard 200 x 148 mm
DMPAPER_A6 70 A6 105 x 148 m
DMPAPER_JENV_KAKU2 71 Japanese Envelope Kaku #2
DMPAPER_JENV_KAKU3 72 Japanese Envelope Kaku #3
DMPAPER_JENV_CHOU3 73 Japanese Envelope Chou #3
DMPAPER_JENV_CHOU4 74 Japanese Envelope Chou #4
DMPAPER_LETTER_ROTATED 75 Letter Rotated 11 x 8 1/2 11 in
DMPAPER_A3_ROTATED 76 A3 Rotated 420 x 297 mm
DMPAPER_A4_ROTATED 77 A4 Rotated 297 x 210 mm
DMPAPER_A5_ROTATED 78 A5 Rotated 210 x 148 mm
```
DMPAPER_B4_JIS_ROTATED 79 B4 (JIS) Rotated 364 x 257 mm
```
```
DMPAPER_B5_JIS_ROTATED 80 B5 (JIS) Rotated 257 x 182 mm
```
DMPAPER_JAPANESE_POSTCARD_ROTATED 81 Japanese Postcard Rotated 148 x 100 mm
DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED 82 Double Japanese Postcard Rotated 148 x 200 mm
DMPAPER_A6_ROTATED 83 A6 Rotated 148 x 105 mm
DMPAPER_JENV_KAKU2_ROTATED 84 Japanese Envelope Kaku #2 Rotated
DMPAPER_JENV_KAKU3_ROTATED 85 Japanese Envelope Kaku #3 Rotated
DMPAPER_JENV_CHOU3_ROTATED 86 Japanese Envelope Chou #3 Rotated
DMPAPER_JENV_CHOU4_ROTATED 87 Japanese Envelope Chou #4 Rotated
```
DMPAPER_B6_JIS 88 B6 (JIS) 128 x 182 mm
```
```
DMPAPER_B6_JIS_ROTATED 89 B6 (JIS) Rotated 182 x 128 mm
```
DMPAPER_12X11 90 12 x 11 in
DMPAPER_JENV_YOU4 91 Japanese Envelope You #4
DMPAPER_JENV_YOU4_ROTATED 92 Japanese Envelope You #4 Rotated
DMPAPER_P16K 93 PRC 16K 146 x 215 mm
DMPAPER_P32K 94 PRC 32K 97 x 151 mm
```
DMPAPER_P32KBIG 95 PRC 32K(Big) 97 x 151 mm
```
DMPAPER_PENV_1 96 PRC Envelope #1 102 x 165 mm
DMPAPER_PENV_2 97 PRC Envelope #2 102 x 176 mm
DMPAPER_PENV_3 98 PRC Envelope #3 125 x 176 mm
DMPAPER_PENV_4 99 PRC Envelope #4 110 x 208 mm
DMPAPER_PENV_5 100 PRC Envelope #5 110 x 220 mm
DMPAPER_PENV_6 101 PRC Envelope #6 120 x 230 mm
DMPAPER_PENV_7 102 PRC Envelope #7 160 x 230 mm
DMPAPER_PENV_8 103 PRC Envelope #8 120 x 309 mm
DMPAPER_PENV_9 104 PRC Envelope #9 229 x 324 mm
DMPAPER_PENV_10 105 PRC Envelope #10 324 x 458 mm
DMPAPER_P16K_ROTATED 106 PRC 16K Rotated
DMPAPER_P32K_ROTATED 107 PRC 32K Rotated
```
DMPAPER_P32KBIG_ROTATED 108 PRC 32K(Big) Rotated
```
DMPAPER_PENV_1_ROTATED 109 PRC Envelope #1 Rotated 165 x 102 mm
DMPAPER_PENV_2_ROTATED 110 PRC Envelope #2 Rotated 176 x 102 mm
DMPAPER_PENV_3_ROTATED 111 PRC Envelope #3 Rotated 176 x 125 mm
DMPAPER_PENV_4_ROTATED 112 PRC Envelope #4 Rotated 208 x 110 mm
DMPAPER_PENV_5_ROTATED 113 PRC Envelope #5 Rotated 220 x 110 mm
DMPAPER_PENV_6_ROTATED 114 PRC Envelope #6 Rotated 230 x 120 mm
DMPAPER_PENV_7_ROTATED 115 PRC Envelope #7 Rotated 230 x 160 mm
DMPAPER_PENV_8_ROTATED 116 PRC Envelope #8 Rotated 309 x 120 mm
DMPAPER_PENV_9_ROTATED 117 PRC Envelope #9 Rotated 324 x 229 mm
DMPAPER_PENV_10_ROTATED 118 PRC Envelope #10 Rotated 458 x 324 mm
Copyright © 1993-2005 AVEVA AB