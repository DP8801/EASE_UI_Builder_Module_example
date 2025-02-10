'''
Created on Jan 31, 2025

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

# Create View
createView("Components")



# Callback function
def greet(name):
    print(f"Hi {name}, Good Morning et Bonjour !")

name = "Dev"

# Button examples
# createButton("Button", "greet(name)")

# checkbox example
# list = ['A', 'B']
# chk_box_list = []
#
# def callback():
#
#
# for i in list:
#     chk = createCheckBox(i, False, callback())
#     chk_box_list.append(chk)

# chk_box = []
#
# def callback():
#     if chk_box[0].getSelection() == True:
#         print('Checkbox selected')
#     else:
#         print('Checkbox unselected')
#
# chk_box.append(createCheckBox("CheckBox", False, "callback()"))

# Example Combo viewer
# def callback(combo):
#     print(combo.getSelection().getFirstElement())
#
# combo_instance = createComboViewer(['A', 'B', 'C', 'D', 'E', 'F'], False, print("Something selected"))
#
# createButton("Submit", "callback(combo_instance)")

# Example ProgressBar
# def callback(progress_bar, bool):
#     if bool:
#         if(progress_bar.getSelection() != 100):
#             new_prog = progress_bar.getSelection() + 20
#             progress_bar.setSelection(new_prog)
#     else:
#         if(progress_bar.getSelection() != 0):
#             new_prog = progress_bar.getSelection() - 20
#             progress_bar.setSelection(new_prog)
#
#
# progress_bar = createProgressBar(20, 100)
#
# createButton("Progress++", "callback(progress_bar, True)")
# createButton("Progress--", "callback(progress_bar, False)")

# Example of Radio Button
# def radioCallback():
#     print("Radio button pressed")
#
# def buttonCallback(button):
#     if button.getSelection():
#         button.setSelection(False)
#
# radio = createRadioButton("Radio", False, "radioCallback()")
#
# createButton("reset", "buttonCallback(radio)")

# Example Text
# def callback(name): 
#     print(f"Thank you for providing your name : {name.getText()}")
#
# setColumnCount(2)
# label = createLabel("Enter first Name:")
# name = createText()
#
# createButton("Submit", "callback(name)", "2/2")

# Example textbox
# def callback(name): 
#     print(f"Thank you for providing your review : \n{name.getText()}")
#
# setColumnCount(2)
# label = createLabel("Enter review:")
# name = createTextBox("2/1-3 o! o")
#
# createButton("Submit", "callback(name)","2/4 >")

# Example Label
# name = "Dev"
# age = 23
#
# createLabel(f"I am {name}, I am {23} years old.")








