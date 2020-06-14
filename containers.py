import os
import wave
from tempfile import TemporaryFile

import requests
import simpleaudio as sa
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


def download_file(url):
    resp = requests.get(url, stream=True)

    if resp.status_code != 200:
        print("Oops! Couldn't download a .wav file!")
        return False
    temp_file = TemporaryFile()
    temp_file.write(resp.raw.read())

    return temp_file


class InstallDialog(QDialog):
    def __init__(self, parent):
        super(QDialog, self).__init__(parent)
        self.setWindowTitle('Install mode')

        label = QLabel("Install sound as...")

        kill_sound_btn = QPushButton("Killsound")
        hit_sound_btn = QPushButton("Hitsound")

        kill_sound_btn.clicked.connect(self.accept)
        hit_sound_btn.clicked.connect(self.reject)


        buttons_hbox = QHBoxLayout()
        buttons_hbox.addWidget(kill_sound_btn)
        buttons_hbox.addWidget(hit_sound_btn)

        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addLayout(buttons_hbox)
        self.setLayout(self.layout)


class SoundContainer(QHBoxLayout):
    def __init__(self, song_title, download_link, author, tf_path, main_window_ptr):
        super().__init__()

        self.main_window_ptr = main_window_ptr
        self.tf_path = tf_path
        self.sound = download_file(download_link)
        self.play_obj = None
        self.download_link = download_link

        if not self.sound:
            print("Error! Couldn't download .wav file!")
            exit(-1)

        title = QLabel(song_title + ' (by ' + author + ')')

        buttons_hbox = QHBoxLayout()
        buttons_hbox.setAlignment(Qt.AlignRight)

        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons_hbox)

        play_button = QPushButton('Play')
        play_button.clicked.connect(self.on_play_btn_clicked)
        play_button.setIcon(QIcon('img/play.png'))

        stop_button = QPushButton('Stop')
        stop_button.clicked.connect(self.on_stop_btn_clicked)
        stop_button.setIcon(QIcon('img/stop.png'))

        install_button = QPushButton('Install')
        install_button.clicked.connect(self.on_install_btn_clicked)
        install_button.setIcon(QIcon('img/download.png'))

        buttons_hbox.addWidget(play_button)
        buttons_hbox.addWidget(stop_button)
        buttons_hbox.addWidget(install_button)

        self.addWidget(title)
        self.addWidget(buttons_widget)

    def on_play_btn_clicked(self, widget):
        self.sound.seek(0)

        wave_read = wave.open(self.sound, 'rb')
        audio_data = wave_read.readframes(wave_read.getnframes())
        num_channels = wave_read.getnchannels()
        bytes_per_sample = wave_read.getsampwidth()
        sample_rate = wave_read.getframerate()

        wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
        self.play_obj = wave_obj.play()

    def on_stop_btn_clicked(self, widget):
        self.play_obj.stop()

    def on_install_btn_clicked(self, widget):
        dialog = InstallDialog(self.main_window_ptr)
        response = dialog.exec_()

        if response == 1:  # Install as killsound
            sound_name = 'killsound.wav'
        elif response == 0:  # Hitsound
            sound_name = 'hitsound.wav'
        else:  # In case user closes dialog window
            dialog.destroy()
            return

        os.chdir(self.tf_path + '/tf')
        # In case if there's no 'custom' folder in tf
        if 'custom' not in os.listdir():
            os.mkdir('custom')
            os.chdir('custom')

            os.mkdir('tf2hitsounds')
            os.chdir('tf2hitsounds')

            os.mkdir('sound')
            os.chdir('sound')

            os.mkdir('ui')
            os.chdir('ui')
        else:
            os.chdir('custom')
            # In case if there's no 'tfhitsounds' folder in tf/custom
            if 'tf2hitsounds' not in os.listdir():
                os.mkdir('tf2hitsounds')
                os.chdir('tf2hitsounds')

                os.mkdir('sound')
                os.chdir('sound')

                os.mkdir('ui')
                os.chdir('ui')
            else:
                os.chdir('tf2hitsounds/sound/ui')

        with open(sound_name, 'wb') as file:
            self.sound.seek(0)
            file.write(self.sound.read())

        dialog.destroy()


class HudContainer:
    pass


class CfgContainer:
    pass
