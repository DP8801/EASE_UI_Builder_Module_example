'''
Created on Jan 15, 2025

@author: Dev
'''
def closeFile(): pass
def copyFile(): pass
def createFile(): pass
def createFolder(): pass
def createProblemMarker(): pass
def createProject(): pass
def deleteFile(): pass
def deleteFolder(): pass
def deleteProject(): pass
def fileExists(): pass
def findFiles(): pass
def getChecksum(): pass
def getFile(): pass
def getProject(): pass
def getWorkspace(): pass
def importProject(): pass
def linkProject(): pass
def openFile(): pass
def readFile(): pass
def readLine(): pass
def readStream(): pass
def refreshResource(): pass
def showFileSelectionDialog(): pass
def showFolderSelectionDialog(): pass
def unzip(): pass
def writeFile(): pass
def writeLine(): pass
def zip(): pass

def addControl(): pass
def createButton(): pass
def createCheckBox(): pass
def createComboViewer(): pass
def createComparator(): pass
def createComposite(): pass
def createDialog(): pass
def createGroup(): pass
def createImage(): pass
def createLabel(): pass
def createLabelProvider(): pass
def createListViewer(): pass
def createProgressBar(): pass
def createRadioButton(): pass
def createScrolledComposite(): pass
def createSeparator(): pass
def createTableViewer(): pass
def createText(): pass
def createTextBox(): pass
def createTreeViewer(): pass
def createView(): pass
def createViewerColumn(): pass
def getComposite(): pass
def getProviderElement(): pass
def getUiEvent(): pass
def popComposite(): pass
def pushComposite(): pass
def removeControl(): pass
def setColumnCount(): pass
def showGrid(): pass

def clearConsole(): pass
def closeView(): pass
def convertSelection(): pass
def createColor(red, green, blue): pass
def executeUI(): pass
def exitApplication(): pass
def getActiveEditor(): pass
def getActiveView(): pass
def getClipboard(): pass
def getConsole(): pass
def getSelection(): pass
def getShell(): pass
def isHeadless(): pass
def isUIThread(): pass
def maximizeView(): pass
def minimizeView(): pass
def moveView(): pass
def openDialog(): pass
def openEditor(): pass
def openView(): pass
def renameScriptShell(): pass
def setClipboard(): pass
def showConfirmDialog(): pass
def showEditor(): pass
def showErrorDialog(): pass
def showInfoDialog(): pass
def showInputDialog(): pass
def showMessageDialog(): pass
def showQuestionDialog(): pass
def showSelectionDialog(): pass
def showView(): pass
def showWarningDialog(): pass
def shutdown(): pass


loadModule('/System/Resources')
loadModule('/System/UI Builder')
loadModule('/System/UI')
from datetime import datetime 

# Text for the module methods
MODULE_METHODS_TEXT = {
        'UI Builder': '''
def addControl(): pass
def createButton(): pass
def createCheckBox(): pass
def createComboViewer(): pass
def createComparator(): pass
def createComposite(): pass
def createDialog(): pass
def createGroup(): pass
def createImage(): pass
def createLabel(): pass
def createLabelProvider(): pass
def createListViewer(): pass
def createProgressBar(): pass
def createRadioButton(): pass
def createScrolledComposite(): pass
def createSeparator(): pass
def createTableViewer(): pass
def createText(): pass
def createTextBox(): pass
def createTreeViewer(): pass
def createView(): pass
def createViewerColumn(): pass
def getComposite(): pass
def getProviderElement(): pass
def getUiEvent(): pass
def popComposite(): pass
def pushComposite(): pass
def removeControl(): pass
def setColumnCount(): pass
def showGrid(): pass
    
        ''',
        'UI': '''
def clearConsole(): pass
def closeView(): pass
def convertSelection(): pass
def createColor(red, green, blue): pass
def executeUI(): pass
def exitApplication(): pass
def getActiveEditor(): pass
def getActiveView(): pass
def getClipboard(): pass
def getConsole(): pass
def getSelection(): pass
def getShell(): pass
def isHeadless(): pass
def isUIThread(): pass
def maximizeView(): pass
def minimizeView(): pass
def moveView(): pass
def openDialog(): pass
def openEditor(): pass
def openView(): pass
def renameScriptShell(): pass
def setClipboard(): pass
def showConfirmDialog(): pass
def showEditor(): pass
def showErrorDialog(): pass
def showInfoDialog(): pass
def showInputDialog(): pass
def showMessageDialog(): pass
def showQuestionDialog(): pass
def showSelectionDialog(): pass
def showView(): pass
def showWarningDialog(): pass
def shutdown(): pass

        ''',
        'Scripting': '''
def createScriptEngine(): pass
def executeSync(): pass
def fork(): pass
def getSharedObject(): pass
def join(): pass
def listScriptEngines(): pass
def notify(): pass
def notifyAll(): pass
def setSharedObject(): pass
def wait(): pass

        ''',
        'Resources': '''
def closeFile(): pass
def copyFile(): pass
def createFile(): pass
def createFolder(): pass
def createProblemMarker(): pass
def createProject(): pass
def deleteFile(): pass
def deleteFolder(): pass
def deleteProject(): pass
def fileExists(): pass
def findFiles(): pass
def getChecksum(): pass
def getFile(): pass
def getProject(): pass
def getWorkspace(): pass
def importProject(): pass
def linkProject(): pass
def openFile(): pass
def readFile(): pass
def readLine(): pass
def readStream(): pass
def refreshResource(): pass
def showFileSelectionDialog(): pass
def showFolderSelectionDialog(): pass
def unzip(): pass
def writeFile(): pass
def writeLine(): pass
def zip(): pass
        
        ''',
        'Platform':'''
def adapt(): pass
def executeCommand(): pass
def getService(): pass
def getSystemProperty(): pass
def postEvent(): pass
def readPreferences(): pass
def runProcess(): pass
def waitForEvent(): pass
def writePreferences(): pass

        ''',
        'P2':'''
def checkForUpdates(): pass
def install(): pass
def registerUpdateSite(): pass
            
        ''',
        'OSGI':'''
def getBundle(): pass
def installBundle(): pass
        
        ''',
        'Launch': '''
def getLaunchConfiguration(): pass
def getLaunchConfigurationNames(): pass
def getLaunchConfigurations(): pass
def getLaunchManager(): pass
def launch(): pass
def launchUI(): pass

        ''',
        'JVM': '''
def compile(): pass
def createInstance(): pass
def invokeStatic(): pass

        ''',
        'Environment': '''
def execute(): pass
def exit(): pass
def getModule(): pass
def getScriptEngine(): pass
def help(): pass
def include(): pass
def loadJar(): pass
def loadModule(): pass
def print(): pass
def printError(): pass
def readInput(): pass
def wrap(): pass

        ''',
        'Build': '''
def build(): pass
        '''
    }

LOAD_MODULE_TEXT = {
    "Build": "loadModule('/System/Build')",
    "Environment": "loadModule('/System/Environment')",
    "JVM": "loadModule('/System/JVM')",
    "Launch": "loadModule('/System/Launch')",
    "OSGI": "loadModule('/System/OSGI')",
    "P2": "loadModule('/System/P2')",
    "Platform": "loadModule('/System/Platform')",
    "Resources": "loadModule('/System/Resources')",
    "Scripting": "loadModule('/System/Scripting')",
    "UI": "loadModule('/System/UI')",
    "UI Builder": "loadModule('/System/UI Builder')"
}

# Initialize global variables
PATH = ""
SYS_MODULE_NAME = ['Build', 'Environment', 'JVM', 'Launch', 'OSGI', 'P2', 'Platform', 'Resources', 'Scripting', 'UI', 'UI Builder']
MODULES_CHECKBOXS = []

FILENAME = "" #name of the file
AUTHOR = "" # name of author
FILETYPE = "" #file type Default py

def selectFile():
    """Open a file selection dialog and return the selected URL."""
    url = showFileSelectionDialog()
    return url

def teardown():
    """Clear filename and author text fields"""
    global FILENAME, AUTHOR
    #Teardown start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    # Clear the filename text field
    FILENAME.setText("")
    
    # Clear the author text field
    AUTHOR.setText("")
    
    # Uncheck all selected checkboxes
    for chkbox in MODULES_CHECKBOXS:
        if chkbox.getSelection():
            chkbox.setSelection(False)
    #Teardown end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def createheader(flag):
    global FILENAME, AUTHOR, PATH, FILETYPE
    
    # Create file path
    filepath = PATH + FILENAME.getText() + "." + FILETYPE.getSelection().getFirstElement()
    
    # Get the current date and format it
    formatted_time = datetime.now().strftime("%b %d, %Y")
    data = f'\'\'\'\nCreated on {formatted_time}\n\n'
    
    # Add author information if provided
    if AUTHOR:
        data += f"@author: {AUTHOR.getText()}\n"
    
    data+="\'\'\'\n"
    
    # Get the selected modules
    selected_modules = [i.getText() for i in MODULES_CHECKBOXS if i.getSelection()]
    
    if flag: # Flag to identify Creation or Updation
        showInfoDialog(f"Creating file at: {filepath} and selected modules are {str(selected_modules)}")
    else:
        showInfoDialog(f"Updating file at: {filepath} and selected modules are {str(selected_modules)}")
        
    # Add module methods to the data
    for i in selected_modules:
        data += MODULE_METHODS_TEXT[i]
    
    data += "\n#import the system modules to use\n"
    
    # Add loadModule statements to the data
    for i in selected_modules:
        data += LOAD_MODULE_TEXT[i] + "\n"
    
    data += "#imported system modules to use...\n"
    
    return data

def createPyFile(): 
    """Callback function to create a Python script file with selected modules and methods."""
    
    global FILENAME, FILETYPE, AUTHOR
    
    # Check is user input the filename
    if FILENAME.getText() == "": # file name not provided
        showErrorDialog("Please Enter File name!!")
        teardown()
    else: # file name provided
        
        # Create file path
        filepath = PATH + FILENAME.getText() + "." + FILETYPE.getSelection().getFirstElement()
        
        if fileExists(filepath): #Update existing file
            data = createheader(False)

            # Read present File 
            data_after = readFile(filepath)
            
            # Find the provided line in the  
            index = data_after.find("#imported system modules to use...\n")
            
            if index == -1:
                data += data_after
            else:    
                data += data_after[index+35:]
            
            writeFile(PATH + FILENAME.getText() + "." + FILETYPE.getSelection().getFirstElement(), data).close()
        else: 
            if FILETYPE.getSelection().getFirstElement() != 'py':
                showInfoDialog(f"Creating file at: {filepath}")
                writeFile(filepath, "").close()
            else:
                data = createheader(True)
            
                # Write the data to the specified file
                writeFile(filepath, data).close()
        
        teardown()

def createLayout():
    """Create the layout for the file creation interface."""
    global PATH, FILENAME, FILETYPE, AUTHOR
    # Select the PATH to save the file
    PATH = selectFile() + "/"
    
    # Create the view for file creation
    createView("PyDevFilecreation")
    createLabel(f"{'*'*25}Path selected: {PATH} {'*'*25}", "1-5/1 x!")
    
    # Create label and text field for the file name
    pushComposite(createComposite("1/2 >x"))
    createLabel("Filename (abc, xyz, pqr):")
    popComposite()
    
    pushComposite(createComposite("2-5/2 o!"))
    setColumnCount(2)
    FILENAME = createText()
    filext = ['py', 'txt']
    FILETYPE = createComboViewer(filext)
    # showGrid()
    popComposite()
    
    # Create label and text field for the author name
    pushComposite(createComposite("1/3 >x"))
    createLabel("Author:")
    popComposite()
    
    pushComposite(createComposite("2-5/3 o!"))
    AUTHOR = createText()
    popComposite()
    
    # Create checkboxes for module selection
    pushComposite(createScrolledComposite("1-5/4 o! o!"))
    createLabel("Choose the modules")
    for i in SYS_MODULE_NAME:
        chkbox = createCheckBox(i, False)
        MODULES_CHECKBOXS.append(chkbox)
    popComposite()
    
    # Create button to trigger the callback function
    createButton("Create File", "createPyFile()", "1-5/5 o!")
    
    # showGrid()

if __name__ == "__main__":
    createLayout()
    

    