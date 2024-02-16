import sys
from PyQt5.QtCore import Qt, QUrl, QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QProgressBar

class MusicPlayer(QMainWindow):
def init(self):
super().init()

    self.setWindowTitle("Music Player")
    self.setWindowIcon(QIcon("Image .png"))

    self.player = QMediaPlayer()

    self.central_widget = QWidget(self)
    self.setCentralWidget(self.central_widget)

    self.layout = QVBoxLayout(self.central_widget)

    # Play button
    self.play_button = QPushButton("Play")
    self.play_button.clicked.connect(self.play_music)
    self.layout.addWidget(self.play_button)

    # Pause button
    self.pause_button = QPushButton("Pause")
    self.pause_button.clicked.connect(self.pause_music)
    self.layout.addWidget(self.pause_button)

    # Stop button
    self.stop_button = QPushButton("Stop")
    self.stop_button.clicked.connect(self.stop_music)
    self.layout.addWidget(self.stop_button)

    # Volume slider
    self.volume_slider = QSlider(Qt.Horizontal)
    self.volume_slider.setMinimum(0)
    self.volume_slider.setMaximum(100)
    self.volume_slider.setSliderPosition(50)
    self.volume_slider.valueChanged.connect(self.set_volume)
    self.layout.addWidget(self.volume_slider)

    # Real-time progress bar
    self.progress_bar = QProgressBar()
    self.progress_bar.setObjectName("progressBar")
    self.layout.addWidget(self.progress_bar)

    # Remaining time label
    self.remaining_time_label = QLabel()
    self.remaining_time_label.setObjectName("remainingTimeLabel")
    self.layout.addWidget(self.remaining_time_label)

    # Apply stylesheet
    self.setStyleSheet("""
        #progressBar {
            background-color: #bdc3c7;
            height: 6px;
            margin-bottom: 10px;
        }

        #progressBar::chunk {
            background-color: #2ecc71;
            width: 0;
            height: 100%;
        }

        #remainingTimeLabel {
            font-size: 12px;
            margin-top: 5px;
            text-align: right;
        }
    """)

    self.player.positionChanged.connect(self.update_progress_bar)

def play_music(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Select Music File", "", "Music Files (*.mp3 *.wav)")
    if file_path:
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.player.play()

def pause_music(self):
    self.player.pause()

def stop_music(self):
    self.player.stop()

def set_volume(self, value):
    self.player.setVolume(value)

def update_progress_bar(self, position):
    duration = self.player.duration()
    if duration > 0:
        progress = int(position / duration * 100)
        self.progress_bar.setValue(progress)

        remaining_time = duration - position
        remaining_time = QTime(0, 0).addMSecs(remaining_time)
        remaining_time_str = remaining_time.toString("mm:ss")
        self.remaining_time_label.setText(remaining_time_str)
if name == "main":
app = QApplication(sys.argv)
player = MusicPlayer()
player.show()
sys.exit(app.exec_())
