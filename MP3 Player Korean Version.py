import sys
from PyQt5.QtCore import Qt, QUrl, QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QProgressBar

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setWindowIcon(QIcon("Image .png"))

        self.player = QMediaPlayer()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 재생 버튼
        self.play_button = QPushButton("재생")
        self.play_button.clicked.connect(self.play_music)
        self.layout.addWidget(self.play_button)

        # 일시정지 버튼
        self.pause_button = QPushButton("일시정지")
        self.pause_button.clicked.connect(self.pause_music)
        self.layout.addWidget(self.pause_button)

        # 정지 버튼
        self.stop_button = QPushButton("정지")
        self.stop_button.clicked.connect(self.stop_music)
        self.layout.addWidget(self.stop_button)

        # 볼륨 슬라이더
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSliderPosition(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.layout.addWidget(self.volume_slider)

        # 실시간 재생바
        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("progressBar")
        self.layout.addWidget(self.progress_bar)

        # 남은 시간 레이블
        self.remaining_time_label = QLabel()
        self.remaining_time_label.setObjectName("remainingTimeLabel")
        self.layout.addWidget(self.remaining_time_label)

        # 스타일시트 적용
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
        file_path, _ = QFileDialog.getOpenFileName(self, "음악 파일 선택", "", "음악 파일 (*.mp3 *.wav)")
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
