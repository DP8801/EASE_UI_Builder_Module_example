'''
Created on Jan 29, 2025

@author: Dev Pandya
'''

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
    
        
#import the system modules to use
loadModule('/System/UI Builder')
#imported system modules to use...

# creating view 
createView("layout Example")

createLabel("________Reference Label___________", "o") #fill
createLabel("Label (left align)", "<") # left (defaul)
createLabel("Label (center align)", "x") # center
createLabel("Label (right align)", ">") # right

setColumnCount(5) # Set the column count to 5 
createLabel("Label1", "4-5/1 >")
createLabel("Label2", "3-5/2-3 x x") 
createLabel("Label3", "2/1-3 o o!") 
createLabel("Label4") 
createLabel("Label5","3-5/4 o!") # Updated Line

showGrid()