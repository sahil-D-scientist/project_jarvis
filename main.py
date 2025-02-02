import Main1  # Import your Jarvis AI script
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTimer, Qt, QDate, QTime, QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from myfile0 import Ui_MainWindow
import sys
from Main1 import run_alexa


class JarvisThread(QThread):
    """ Runs Jarvis (run_alexa) in a separate thread """
    def __init__(self):
        super(JarvisThread, self).__init__()
        self.running = True

    def run(self):
        """ Keep running Jarvis AI """
        print("[INFO] Jarvis is starting...")
        while self.running:
            try:
                run_alexa()  # Ensure it runs only when clicked
            except Exception as e:
                print(f"[ERROR] Jarvis encountered an error: {e}")
            self.msleep(500)  # Prevent UI from freezing

    def stop(self):
        """ Safely stop Jarvis AI """
        print("[INFO] Stopping Jarvis AI...")
        self.running = False
        self.quit()
        self.wait()
        print("[INFO] Jarvis AI Stopped!")


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ensure UI is displayed properly
        self.show()

        # Connect buttons
        self.ui.pushButton.clicked.connect(self.startTask)  # Run Jarvis
        self.ui.pushButton_2.clicked.connect(self.stopTask)  # Stop Jarvis

        # Initialize Jarvis Thread (but don't start it yet)
        self.jarvis_thread = None

    def startTask(self):
        """ Starts animations and Jarvis AI only when clicked """
        print("[INFO] Starting animations and Jarvis...")

        # Load GIF animations
        self.ui_movie1 = QtGui.QMovie("Jarvis_Gui (2).gif")
        self.ui.Gif3.setMovie(self.ui_movie1)
        self.ui_movie1.start()

        self.ui_movie2 = QtGui.QMovie("im (1).gif")
        self.ui.gif2.setMovie(self.ui_movie2)
        self.ui_movie2.start()

        # Update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        # Start Jarvis in a separate thread when clicked
        if self.jarvis_thread is None or not self.jarvis_thread.isRunning():
            print("[INFO] Starting Jarvis thread...")
            self.jarvis_thread = JarvisThread()
            self.jarvis_thread.run()
        else:
            print("[WARNING] Jarvis thread already running!")

    def stopTask(self):
        """ Stops Jarvis AI """
        if self.jarvis_thread and self.jarvis_thread.isRunning():
            print("[INFO] Stopping Jarvis AI...")
            self.jarvis_thread.stop()
            self.jarvis_thread = None

    def showTime(self):
        """ Displays time and date in the UI """
        current_time = QTime.currentTime().toString()
        current_date = QDate.currentDate().toString()
        self.ui.textBrowser.setText(f"Date: {current_date}")
        self.ui.textBrowser_2.setText(f"Time: {current_time}")


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = Main()
    sys.exit(app.exec_())
