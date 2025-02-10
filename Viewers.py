'''
Created on Feb 05, 2025

@author: Dev Pandya
'''

# Import necessary modules for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
    
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
    
def executeUI(): pass
        
#import the system modules to use
loadModule('/System/UI Builder')
loadModule('/System/UI')
#imported system modules to use...


# # Create View Example
# createView("Dummy", "C:\\temp\\SMWWorkspace\\BA_Civil\\prd\\Python4Capella\\EASE\\WI2025\\Documentation_EASE_UI_Builder\\icon.png", "PyDevFilecreation", "<")


# createView("Viewers")

# Create List Viewer example
# def callback(ListViewerInstance):
#     print(ListViewerInstance.getSelection())
#
# ListViewerInstance = createListViewer(['apple', 'banana', 'cherry', 'date', 'elderberry'])
#
# createButton("Submit", "callback(ListViewerInstance)")

# Create Table Viewer example
# def callback(table_viewer_instance1): 
#     print(table_viewer_instance1.getSelection())
#
# def callback1():
#     return getProviderElement()
#
# table_viewer_instance1 = createTableViewer(['apple', 'banana', 'cherry', 'date','elderberry'])
#
# createButton("Submit", "callback(table_viewer_instance1)")

# Create Table Viewer example
# def callback(tree_viewer_instance1): 
#     print(tree_viewer_instance1.getSelection())
#
# tree_viewer_instance1 = createTreeViewer(['apple', 'banana', 'cherry', 'date','elderberry'])
#
# createButton("Submit", "callback(table_viewer_instance1)")

# CreateViewerColumn example
#
# def callback(table_viewer_instance1): 
#     print(table_viewer_instance1.getSelection())
#
# def callback1():
#     return getProviderElement()
#
# table_viewer_instance1 = createTableViewer(['apple', 'banana', 'cherry', 'date','elderberry'])
#
# createViewerColumn(table_viewer_instance1, "Fruits", createLabelProvider('callback1()'), 4)
# createViewerColumn(table_viewer_instance1, "Labels", createLabelProvider('callback1()'), 1)
#
# createButton("Submit", "callback(table_viewer_instance1)")

name = ""

# Create Dialog example
def build_layout():
    createLabel("Name", "<")
    global name
    name = createText()

dialog = createDialog("build_layout()", "Dialog Example", "An example to demonstrate dialog")

result = executeUI("dialog.open()")


if result == 0:
    name = dialog.getData(name)
    print(f"User enter \'{name}\' in text.")