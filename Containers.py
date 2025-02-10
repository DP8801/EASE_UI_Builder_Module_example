'''
Created on Feb 05, 2025

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

createView("Components")
# Example Composite
# setColumnCount(2)
#
# c = createComposite()
# pushComposite(c)
# createLabel("Label (left align)", "<") # default (left)
# createLabel("Label (center align)", "x") # center
# createLabel("Label (right align)", ">") # right
# createButton("Button", "print('Button pressed')", "<") # left
# createButton("Button", "print('Button pressed')", "x") # center
# createButton("Button", "print('Button pressed')", ">") # right
# createButton("Button", "print('Button pressed')", "o") # fill
# createCheckBox("Checkbox", False, "callback0()", "<") #left
# createCheckBox("Checkbox", False, "callback0()", "x") #center
# createCheckBox("Checkbox", False, "callback0()", ">") #right
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "<") # left
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "x") # center
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', ">") # right
# popComposite()
#
# # creating a empty space
# c2 = createComposite()
# pushComposite(c2)
# popComposite()
# # creating a empty space
# pushComposite(createComposite())     
# popComposite()   
#
# c1 = createComposite()
# pushComposite(c1)
# createLabel("Label (left align)", "<") # default (left)
# createLabel("Label (center align)", "x") # center
# createLabel("Label (right align)", ">") # right
# createButton("Button", "print('Button pressed')", "<") # left
# createButton("Button", "print('Button pressed')", "x") # center
# createButton("Button", "print('Button pressed')", ">") # right
# createButton("Button", "print('Button pressed')", "o") # fill
# createCheckBox("Checkbox", False, "callback0()", "<") #left
# createCheckBox("Checkbox", False, "callback0()", "x") #center
# createCheckBox("Checkbox", False, "callback0()", ">") #right
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "<") # left
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "x") # center
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', ">") # right
# popComposite()
# showGrid()

# pushcomposite example
# setColumnCount(2)
#
# def layout(name):
#     createLabel(f"Composite {name}")
#     createButton("Button", "print('Button pressed')", "<") # left
#     createButton("Button", "print('Button pressed')", "x") # center
#     createButton("Button", "print('Button pressed')", ">") # right
#
# c1 = createComposite()
# c2 = createComposite()
# c3 = createComposite()
# c4 = createComposite()
#
# pushComposite(c2)
# layout("c2")
# popComposite()
#
# pushComposite(c1)
# layout("c1")
# popComposite()
#
# pushComposite(c3)
# layout("c3")
# popComposite()

# pop composite example
# c1 = createComposite()
# pushComposite(c1) # composite c1 is active
# createLabel("Composite 1") 
# c2 = createComposite()
# pushComposite(c2) # composite c2 is active inside c1
# createLabel("Composite 2 ")
# composite = getComposite()
# showGrid()
# popComposite() # remove c2 composite and bring back c1 from the stack
# createLabel("Composite 1") 
# showGrid()
# popComposite()
# showGrid()

# get Composite example
# TBD

# Example ScrolledComposite
# setColumnCount(2)
#
# c = createScrolledComposite() # Scrolled Composite
# pushComposite(c)
# createLabel("Label (left align)", "<") # default (left)
# createLabel("Label (center align)", "x") # center
# createLabel("Label (right align)", ">") # right
# createButton("Button", "print('Button pressed')", "<") # left
# createButton("Button", "print('Button pressed')", "x") # center
# createButton("Button", "print('Button pressed')", ">") # right
# createButton("Button", "print('Button pressed')", "o") # fill
# createCheckBox("Checkbox", False, "callback0()", "<") #left
# createCheckBox("Checkbox", False, "callback0()", "x") #center
# createCheckBox("Checkbox", False, "callback0()", ">") #right
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "<") # left
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "x") # center
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', ">") # right
# popComposite()
#
# # creating a empty space
# c2 = createComposite()
# pushComposite(c2)
# popComposite()
# # creating a empty space
# pushComposite(createComposite())     
# popComposite()   
#
# c1 = createScrolledComposite() # Scrolled Composite
# pushComposite(c1)
# createLabel("Label (left align)", "<") # default (left)
# createLabel("Label (center align)", "x") # center
# createLabel("Label (right align)", ">") # right
# createButton("Button", "print('Button pressed')", "<") # left
# createButton("Button", "print('Button pressed')", "x") # center
# createButton("Button", "print('Button pressed')", ">") # right
# createButton("Button", "print('Button pressed')", "o") # fill
# createCheckBox("Checkbox", False, "callback0()", "<") #left
# createCheckBox("Checkbox", False, "callback0()", "x") #center
# createCheckBox("Checkbox", False, "callback0()", ">") #right
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "<") # left
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', "x") # center
# createComboViewer(['A', 'B', 'C'], True, 'print("ComboViewer")', ">") # right
# popComposite()
# showGrid()


# Create Group example
createGroup("Gender", "o! o")
createRadioButton("Male", False)
createRadioButton("Female", False)
createRadioButton("Other", False)
createLabel("Want to go out of the group")

popComposite()

createLabel("Finally out of the group")