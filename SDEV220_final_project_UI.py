from PyQt6 import QtCore, QtGui, QtWidgets
import db_config
from __init__ import install_requirements
import podcast
import sys
import os
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtCore import QUrl
import save_plan

#If user has a path issue then this will make it more understandable for the user
try:
    install_requirements()
except ModuleNotFoundError:
    print("Module wasn't found try checking your PATHS or downloading will pip3.12 instead of pip ")


#calls the functions as variables

skillclasses = db_config.return_skillclasses()
skillroles = db_config.return_skillroles()
skillpaths = db_config.return_skillpaths()


class skill_paths:
    
    def __init__(self,id:list,skillpathname:list,skillpathdescription:list) -> None:
        """
        :param id: Must be a list of all id's from the skillpaths table
        :param skillpathname: Must be a list of all skillpathnames of the skillpaths table
        :param skillpathdescription: Must be a list of all skillpathdescriptions of the skillpaths table
        """

        self.id = id
        self.skillpathname = skillpathname
        self.skillpathdescription =skillpathdescription

    def get_index_by_id(self,given_id):
        """
        :return: Returns the index of the given_id or will print an exception if it doesn't exactly match
        
        """ 
        try:
            match given_id:
                case None:
                    pass
                case _ : return self.id.index(given_id)


        except ValueError:
            print(f"{given_id} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_skillpathname(self,given_skillpathname):
        """
        :return: Returns the index of the given_skillpathname or will print an exception if it doesn't exactly match
        
        """
        try:
            match given_skillpathname:
                case None:
                    pass
                case _ : return self.skillpathname.index(given_skillpathname)


        except ValueError:
            print(f"{given_skillpathname} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_skillpathdescription(self,given_skillpathdescription):
        """
        :return: Returns the index of the given_skillpathdescription or will print an exception if it doesn't exactly match
        
        """

        try:
            match given_skillpathdescription:
                case None:
                    pass
                case _ : return self.skillpathdescription.index(given_skillpathdescription)


        except ValueError:
            print(f"{given_skillpathdescription} doesn't exist:::: Maybe try again with different spelling or Capitalization")

#Turns skillroles into a class
class skill_roles:
    def __init__(self,id:list,Rolename:list,Roledescription:list) -> None:
        """
        :param id: Must be a list of all id of the skillroles table
        :param Rolename: Must be a list of all Rolenames of the skillroles table
        :param Roledesciption: Must be a list of all Roledesciptions of the skillroles table
        """
        self.id = id
        self.Rolename = Rolename
        self.Roledescription = Roledescription


    def get_index_by_id(self,given_id):
        """
        :return: Returns the index of the given_id or will print an exception if it doesn't exactly match
        
        """


        try:
            match given_id:
                case None:
                    pass
                case _ : return self.id.index(given_id)


        except ValueError:
            print(f"{given_id} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_RoleName(self,given_Rolename):
        """
        :return: Returns the index of the given_Rolename or will print an exception if it doesn't exactly match
        
        """
         
        try:
            match given_Rolename:
                case None:
                    pass
                case _ : return self.Rolename.index(given_Rolename)


        except ValueError:
            print(f"{given_Rolename} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_RoleDescription(self,given_Roledescription):
        """
        :return: Returns the index of the given_Roledescription or will print an exception if it doesn't exactly match
        
        """ 
        try:
            match given_Roledescription:
                case None:
                    pass
                case _ : return self.Roledescription.index(given_Roledescription)


        except ValueError:
            print(f"{given_Roledescription} doesn't exist:::: Maybe try again with different spelling or Capitalization")

#turns skillclasses into a class
class skill_classes:
    def __init__(self,ClassID:list,Rolename:list,id:list) -> None:
        """
        :param ClassID: Must be a list of all ClassIDs of the skill_classes table
        :param Rolename: Must be a list of all Rolenames of the skill_classes table
        :param id: Must be a list of all id of the skill_classes table
        """
        self.ClassID =ClassID
        self.Rolename = Rolename
        self.id = id

    def get_index_by_ClassID(self,given_ClassID):
        """
        :return: Returns the index of the given_ClassID or will print an exception if it doesn't exactly match
        
        """ 

        try:
            match given_ClassID:
                case None:
                    pass
                case _ : return self.ClassID.index(given_ClassID)


        except ValueError:
            print(f"{given_ClassID} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_Rolename(self,given_Rolename):
        """
        :return: Returns the index of the given_Rolename or will print an exception if it doesn't exactly match
        
        """ 

        try:
            match given_Rolename:
                case None:
                    pass
                case _ : return self.Rolename.index(given_Rolename)


        except ValueError:
            print(f"{given_Rolename} doesn't exist:::: Maybe try again with different spelling or Capitalization")


    def get_index_by_id(self,given_id):
        """
        :return: Returns the index of the given_id or will print an exception if it doesn't exactly match
        
        """ 
        try:
            match given_id:
                case None:
                    pass
                case _ : return self.id.index(given_id)

        except ValueError:
            print(f"{given_id} doesn't exist:::: Maybe try again with different spelling or Capitalization")



Classes = skill_classes([x[0] for x in skillclasses],[x[1] for x in skillclasses],[x[2] for x in skillclasses])

Roles = skill_roles([x[0] for x in skillroles],[x[1] for x in skillroles],[x[2] for x in skillroles])


#This is a test of the class and the get_index_by_id
Paths = skill_paths([x[0] for x in skillpaths],[x[1] for x in skillpaths],[x[2] for x in skillpaths])




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 562)
        
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView_2 = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(0, 0, 381, 501))
        self.columnView_2.setObjectName("columnView_2")
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(375, 0, 421, 501))
        self.columnView.setObjectName("columnView")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.path_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.path_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.path_vertical_layout.setObjectName("path_vertical_layout")

        #skill_label
        self.skill_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.skill_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.skill_label.setObjectName("skill_label")
        self.path_vertical_layout.addWidget(self.skill_label)

        #skill combo box
        self.skill_combo_box = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.skill_combo_box.setObjectName("skill_combo_box")
        self.path_vertical_layout.addWidget(self.skill_combo_box)

        #populate items from database
        items = ["",*[x[1] for x in skillpaths]]
        self.skill_combo_box.addItems(items)
        self.skill_combo_box.currentIndexChanged.connect(self.on_skill_combo_box_changed)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.path_vertical_layout.addItem(spacerItem)
        
        #role_label
        self.role_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.role_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.role_label.setObjectName("role_label")
        self.path_vertical_layout.addWidget(self.role_label)

        #role combo box
        self.rol_combo_box = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.rol_combo_box.setObjectName("rol_combo_box")
        self.rol_combo_box.currentIndexChanged.connect(self.on_rol_combo_box_changed)
        self.path_vertical_layout.addWidget(self.rol_combo_box)

        #spacer
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.path_vertical_layout.addItem(spacerItem2)

        
        #spacer
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.path_vertical_layout.addItem(spacerItem1)

        #Vertical layout
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 0, 415, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #skill description
        self.skill_description = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.skill_description.setObjectName("skill_description")
        self.verticalLayout_2.addWidget(self.skill_description)

        #skill list
        self.skill_description_list = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.skill_description_list.setObjectName("skill_description_list")
        self.skill_description_list.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.skill_description_list)
        
        #role Label
        self.role_description_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.role_description_label.setObjectName("role_description_label")
        self.verticalLayout_2.addWidget(self.role_description_label)

        #role_list_view
        self.Role_list_view = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.Role_list_view.setObjectName("Role_list_view")
        self.verticalLayout_2.addWidget(self.Role_list_view)
        self.Role_list_view.setWordWrap(True)

        
        #Role list
        self.Role_description_list = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.Role_description_list.setObjectName("Role_description_list")
        self.Role_description_list.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.Role_description_list)

        #Add media players to the layoutwidget2
        self.media_player = QMediaPlayer(self.verticalLayoutWidget_2)
        self.audio_output = QAudioOutput(self.verticalLayoutWidget_2)
        self.media_player.setAudioOutput(self.audio_output)
        

        self.create_controls()

    def create_controls(self):
        # Play button
        self.play_button = QPushButton('Play')
        self.play_button.clicked.connect(self.player)

        # Stop button
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.media_player.stop)
        
        #Adds play and stop button
        self.verticalLayout_2.addWidget(self.play_button)
        self.verticalLayout_2.addWidget(self.stop_button)
    
        
        #Classes label
        self.classes_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.classes_label.setObjectName("classes_label")
        self.verticalLayout_2.addWidget(self.classes_label)
       
       #classes list
        self.Class_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.Class_list.setObjectName("Class_list")
        self.verticalLayout_2.addWidget(self.Class_list)
       
       #Clear button
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 500, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushbutton_clicked)
       
        #print button
        self.print_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.print_button.setGeometry(QtCore.QRect(685, 500, 111, 41))
        self.print_button.setObjectName("Print All")
        self.print_button.clicked.connect(self.force_print)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def player(self):
        try:
            self.media_player.setSource(QUrl.fromLocalFile(podcast.retrieve_and_play([skillroles[[x[1] for x in skillroles].index(self.rol_combo_box.currentText())][0]])))
            self.media_player.play()
        except ValueError:
            pass

    def retranslateUi(self, MainWindow):
        myFont = QtGui.QFont()
        myFont.setBold(True)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Path Finder"))
        self.skill_label.setText(_translate("MainWindow", "Select a Skill Path:"))        
        self.skill_label.setFont(myFont)

        #Sets Icon img
        app_icon = QtGui.QIcon()
        app_icon.addFile(f"{os.getcwd()}"+r"\icon"+r"\Path.jpeg")
        MainWindow.setWindowIcon(app_icon)

        self.skill_description.setText(_translate("MainWindow", "Skill Description:"))
        self.skill_description.setFont(myFont)

        self.role_label.setText(_translate("MainWindow", "Select A Role from the skill Path:"))
        self.role_label.setFont(myFont)
        self.role_description_label.setText(_translate("MainWindow", "Role Description:"))
        self.role_description_label.setFont(myFont)
        
        self.classes_label.setText(_translate("MainWindow", "Classes"))
        self.classes_label.setFont(myFont)
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton.setFont(myFont)
        self.print_button.setText("Force Print")
        self.print_button.setFont(myFont)

    def force_print(self):
        try:
            if self.rol_combo_box.currentText()!="":
                if self.Class_list.currentItem()!= None:
                    save_plan.create_and_write("Path",skill_path=self.skill_combo_box.currentText(),path_desc=self.skill_description_list.text(),role=self.rol_combo_box.currentText(),classes=self.Class_list.currentItem())
        except TypeError:
            pass



    def on_skill_combo_box_changed(self, index):


        #Clears all the labels and fields at start of call to help reduce confusion of user.
        self.rol_combo_box.clear()
        self.Class_list.clear()
        self.Role_list_view.clear()
        self.skill_description_list.clear()

        print("skill combo selected")
        selectedItem = self.skill_combo_box.currentText()
        
        #checks if the selected item exists in the database then adds all skill descriptions
        if selectedItem is not None:
            if selectedItem != "":
                if selectedItem in [x[1] for x in skillpaths]:
                    ItemDescription = skillpaths[[x[1] for x in skillpaths].index(selectedItem)][2]
                    print("item descption",ItemDescription)
                    self.skill_description_list.setText(ItemDescription) 
                
                #checks if the selected item has an ID and then adds all Rolenames
                if skillpaths[[x[1] for x in skillpaths].index(selectedItem)][0] in [x[0][0] for x in skillroles]:            
                    items = ["",*[x[1] for x in skillroles if x[0][0]==skillpaths[[x[1] for x in skillpaths].index(selectedItem)][0]]]
                    self.rol_combo_box.addItems(items)
        else:   
            self.rol_combo_box.clear()
            self.Class_list.clear()
            self.Role_list_view.clear()
            self.skill_description_list.clear()

    def on_rol_combo_box_changed(self, index):            
        print("role combo selected")
        selectedItem = self.rol_combo_box.currentText()
        print("role combo box",selectedItem)
        if selectedItem != "":
            if selectedItem in [x[1] for x in skillroles]:
                roledescription = skillroles[[x[1] for x in skillroles].index(selectedItem)][2] 
                self.Role_list_view.setText(roledescription)
                
                #checks to make sure the selected item's id matches anything in skillclasses then returns the class id and class descriptor along with a spacer
                items = [x[0]+":   "+x[1] for x in skillclasses if x[2]==skillroles[[x[1] for x in skillroles].index(selectedItem)][0]]

                _translate = QtCore.QCoreApplication.translate
                self.classes_label.setText(_translate("MainWindow", "Classes required for " + selectedItem))    
                self.Class_list.clear()
                self.Class_list.addItems(items)
        else:
            self.Class_list.clear()
            self.Role_list_view.clear()



    def on_pushbutton_clicked(self):
        self.rol_combo_box.clear()
        self.Class_list.clear()
        self.Role_list_view.clear()
        self.skill_description_list.clear()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #QSqlDatabase.close()
    sys.exit(app.exec())