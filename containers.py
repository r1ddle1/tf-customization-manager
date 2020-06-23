from os import mkdir, listdir
from tempfile import TemporaryFile
from wave import open as wave_open

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from requests import get as requests_get
from simpleaudio import WaveObject

# Let's load icons in advance instead of loading 'em every time __init__ is called
play_icon = None
stop_icon = None
install_icon = None
parent = None


def _download_file(url):
    resp = requests_get(url, stream=True)

    if resp.status_code != 200:
        print("Oops! Couldn't download a .wav file!")
        return False
    temp_file = TemporaryFile()
    temp_file.write(resp.raw.read())

    return temp_file


class InstallDialog(QDialog):
    def __init__(self, _parent):
        super(QDialog, self).__init__(_parent)
        self.setWindowTitle('Install mode')

        label = QLabel('Install sound as...')

        kill_sound_btn = QPushButton('Killsound')
        hit_sound_btn = QPushButton('Hitsound')

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
    def __init__(self, song_title, download_link, author, tf_path, main_window_ptr, parent_):
        super().__init__()

        # Load icons (only once!)
        global play_icon, stop_icon, install_icon, parent

        if not play_icon:
            play_icon = QIcon('img/play.png')
            stop_icon = QIcon('img/stop.png')
            install_icon = QIcon('img/download.png')
            parent = parent_

        self.song_title = song_title
        self.main_window_ptr = main_window_ptr
        self.tf_path = tf_path
        self.sound = None
        self.play_obj = None
        self.download_link = download_link

        title = QLabel(song_title + ' (by ' + author + ')')

        buttons_hbox = QHBoxLayout()
        buttons_hbox.setAlignment(Qt.AlignRight)

        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons_hbox)

        play_button = QPushButton()
        play_button.clicked.connect(self.on_play_btn_clicked)
        play_button.setIcon(play_icon)

        stop_button = QPushButton()
        stop_button.clicked.connect(lambda: self.play_obj.stop())
        stop_button.setIcon(stop_icon)

        install_button = QPushButton()
        install_button.clicked.connect(self.on_install_btn_clicked)
        install_button.setIcon(install_icon)

        buttons_hbox.addWidget(play_button)
        buttons_hbox.addWidget(stop_button)
        buttons_hbox.addWidget(install_button)

        self.addWidget(title)
        self.addWidget(buttons_widget)

    def on_play_btn_clicked(self):
        try:
            if not self.sound:
                self.sound = _download_file(self.download_link)
            self.sound.seek(0)

            wave_read = wave_open(self.sound, 'rb')
            audio_data = wave_read.readframes(wave_read.getnframes())
            num_channels = wave_read.getnchannels()
            bytes_per_sample = wave_read.getsampwidth()
            sample_rate = wave_read.getframerate()

            wave_obj = WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
            self.play_obj = wave_obj.play()
        except ValueError:
            print("Error! Couldn't play sound")

    def on_install_btn_clicked(self):
        dialog = InstallDialog(self.main_window_ptr)
        response = dialog.exec_()

        if response == 1:  # Install as killsound
            sound_name = 'killsound.wav'
            parent.current_ks = self.song_title
        elif response == 0:  # Hitsound
            sound_name = 'hitsound.wav'
            parent.current_hs = self.song_title
        else:  # In case user closes dialog window
            dialog.destroy()
            return

        # Do not use os.chdir() because it brakes icon loading!

        # In case if there's no 'custom' folder in tf
        if 'custom' not in listdir(self.tf_path + '/tf'):
            mkdir(self.tf_path + '/tf/custom')
            mkdir(self.tf_path + '/tf/custom/tf2hitsounds')
            mkdir(self.tf_path + '/tf/custom/tf2hitsounds/sound')
            mkdir(self.tf_path + '/tf/custom/tf2hitsounds/sound/ui')
        else:
            # In case if there's no 'tf2hitsounds' folder in tf/custom
            if 'tf2hitsounds' not in listdir(self.tf_path + '/tf/custom'):
                mkdir(self.tf_path + '/tf/custom/tf2hitsounds')
                mkdir(self.tf_path + '/tf/custom/tf2hitsounds/sound')
                mkdir(self.tf_path + '/tf/custom/tf2hitsounds/sound/ui')

        with open(self.tf_path + '/tf/custom/tf2hitsounds/sound/ui/' + sound_name, 'wb') as file:
            self.sound.seek(0)
            file.write(self.sound.read())

        dialog.destroy()


class HudContainer:
    pass


class CfgContainer:
    pass
