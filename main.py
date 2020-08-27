import smtplib

from PyQt5 import QtCore, QtGui, QtWidgets

from emailSpammer import emailLOGIN, gui

class main:
    def __init__(self):
        pass
    #Email Log-in
    def loginEmail(self, email, password):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, password)
    #Check credentials
    def checkLogin(self):
        global email, password
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            self.loginEmail(email, password)
            self.secondWindow()
        except smtplib.SMTPAuthenticationError:
            self.ui.label_3.setVisible(True)
        except Exception as e:
            print(e)
    #Send emails
    def sendEmail(self):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(email, password)
            for mails2 in gui.listaEMAIL:
                for mail in mails2:
                    try:
                        server.sendmail(email, mail, gui.messaggio)
                        self.ui2.textBrowser.append("Email sent to: " + mail + "\n")
                    except Exception:
                        self.ui2.textBrowser.append("Something went wrong!")
            self.ui2.textBrowser.append("DONE!")
            server.quit()
        except Exception as e:
            print(e)
    #First Frame
    def firstWindow(self):
        self.firstWindow = QtWidgets.QMainWindow()
        self.ui = emailLOGIN.Ui_MainWindow()
        self.ui.setupUi(self.firstWindow)
        self.ui.pushButton.clicked.connect(self.checkLogin)

        self.firstWindow.show()

    #Second Frame
    def secondWindow(self):
        self.secondWindow = QtWidgets.QMainWindow()
        self.ui2 = gui.Ui_MainWindow()
        self.ui2.setupUi(self.secondWindow)
        self.ui2.pushButton_2.clicked.connect(self.sendEmail)
        self.secondWindow.show()
#Application running
if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    main = main()
    main.firstWindow()
    sys.exit(app.exec_())


