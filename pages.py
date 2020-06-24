from PyQt5.QtWidgets import QStackedWidget, QErrorMessage, QFrame

import file_parser
from containers import *


class SoundsPage(QWidget):
    def __init__(self, tf_path, main_window_ptr):
        super(SoundsPage, self).__init__()

        self.tf_path = tf_path
        self.main_window_ptr = main_window_ptr  # For creating dialogs
        self.main_layout = QHBoxLayout()

        self.hitsound = None
        self.killsound = None

        self._load_current_sounds()
        if self.hitsound:
            print('hitsound is installed')
        if self.killsound:
            print('its installed too')

        self._load_cfg()

        self._create_options_part()
        self._create_browser_part()

        self._switch_to_page(0)

        self.setLayout(self.main_layout)
        self.show()

    def _create_options_part(self):
        main_vbox = QVBoxLayout()
        main_vbox.setAlignment(Qt.AlignCenter)
        main_vbox.setSpacing(30)

        # Refresh part
        refresh_hbox = QHBoxLayout()

        refresh_label = QLabel('#REFRESH_LABEL')
        refresh_btn = QPushButton('Refresh DB')
        refresh_btn.setIcon(QIcon('img/refresh.png'))
        refresh_btn.clicked.connect(self._refresh_db)

        refresh_hbox.addWidget(refresh_label)
        refresh_hbox.addWidget(refresh_btn, alignment=Qt.AlignRight)

        # Kill sound part
        ks_part = QWidget()

        vert_ks_layout = QVBoxLayout()
        ks_part.setLayout(vert_ks_layout)

        ks_label = QLabel('Current Killsound')
        ks_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        vert_ks_layout.addWidget(ks_label)

        ks_frame_layout = QHBoxLayout()

        ks_frame = QFrame()
        ks_frame.setFrameStyle(QFrame.StyledPanel)
        ks_frame.setLayout(ks_frame_layout)
        vert_ks_layout.addWidget(ks_frame)

        play_curr_ks_btn = QPushButton('Play')
        play_curr_ks_btn.setIcon(QIcon('img/play.png'))
        play_curr_ks_btn.clicked.connect(lambda: play_sound(self.killsound))
        ks_frame_layout.addWidget(play_curr_ks_btn)

        del_curr_ks_btn = QPushButton('Delete')
        del_curr_ks_btn.setIcon(QIcon('img/delete.png'))
        del_curr_ks_btn.clicked.connect(lambda: self._delete_current_sound('killsound'))
        ks_frame_layout.addWidget(del_curr_ks_btn)

        # Hit sound part
        hs_part = QWidget()

        vert_hs_layout = QVBoxLayout()
        hs_part.setLayout(vert_hs_layout)

        hs_label = QLabel('Current HitSound')
        hs_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        vert_hs_layout.addWidget(hs_label)

        hs_frame_layout = QHBoxLayout()

        hs_frame = QFrame()
        hs_frame.setFrameStyle(QFrame.StyledPanel)
        hs_frame.setLayout(hs_frame_layout)
        vert_hs_layout.addWidget(hs_frame)

        play_curr_hs_btn = QPushButton('Play')
        play_curr_hs_btn.setIcon(QIcon('img/play.png'))
        play_curr_hs_btn.clicked.connect(lambda: play_sound(self.hitsound))
        hs_frame_layout.addWidget(play_curr_hs_btn)

        del_curr_hs_btn = QPushButton('Delete')
        del_curr_hs_btn.setIcon(QIcon('img/delete.png'))
        del_curr_hs_btn.clicked.connect(lambda: self._delete_current_sound('hitsound'))
        hs_frame_layout.addWidget(del_curr_hs_btn)

        # End
        main_vbox.addLayout(refresh_hbox)
        main_vbox.addWidget(ks_part)
        main_vbox.addWidget(hs_part)

        self.main_layout.addLayout(main_vbox)

    def _create_browser_part(self):
        browser_part = QVBoxLayout()
        browser_part.setSpacing(0)
        self.browser_stack = QStackedWidget()
        self.max_pages_count = 100
        self.current_page_index = 0  # Index of pages begins with 0
        self.sounds = file_parser.get_db('sounds_db')

        browser_label = QLabel('Sounds Browser')
        browser_label.setAlignment(Qt.AlignCenter)

        # Page switching buttons
        page_switching_hbox = QHBoxLayout()
        page_switching_hbox.setAlignment(Qt.AlignHCenter)
        page_switching_hbox.setSpacing(0)

        go_back_btn = QPushButton()
        go_forward_button = QPushButton()
        self.current_page_text = QLabel('Page 1')

        go_back_btn.setIcon(QIcon('img/prev.png'))
        go_forward_button.setIcon(QIcon('img/next.png'))

        go_back_btn.clicked.connect(lambda: self._switch_to_page(self.current_page_index - 1))
        go_forward_button.clicked.connect(lambda: self._switch_to_page(self.current_page_index + 1))

        page_switching_hbox.addWidget(go_back_btn)
        page_switching_hbox.addWidget(self.current_page_text)
        page_switching_hbox.addWidget(go_forward_button)

        self._switch_to_page(self.current_page_index)

        browser_part.addWidget(browser_label)
        browser_part.addWidget(self.browser_stack)
        browser_part.addLayout(page_switching_hbox)

        self.main_layout.addLayout(browser_part)

    def _delete_current_sound(self, sound):
        import os
        try:
            os.remove(self.tf_path + '/tf/custom/tf2hitsounds/sound/ui/' + sound + '.wav')
        except FileNotFoundError:
            dialog = QErrorMessage(self.main_window_ptr)
            dialog.showMessage("Error! There's no installed " + sound)
        finally:
            del os

    def _load_current_sounds(self):
        # Check dirs...
        if 'custom' not in listdir(self.tf_path + '/tf'):
            return
        elif 'tf2hitsounds' not in listdir(self.tf_path + 'tf/custom'):
            return
        elif 'sound' not in listdir(self.tf_path + 'tf/custom/tf2hitsounds/'):
            return
        elif 'ui' not in listdir(self.tf_path + 'tf/custom/tf2hitsounds/sound/'):
            return

        contents = listdir(self.tf_path + 'tf/custom/tf2hitsounds/sound/ui/')
        if 'hitsound.wav' in contents:
            self.hitsound = open(self.tf_path + 'tf/custom/tf2hitsounds/sound/ui/hitsound.wav', 'rb')

        if 'killsound.wav' in contents:
            self.killsound = open(self.tf_path + 'tf/custom/tf2hitsounds/sound/ui/killsound.wav', 'rb')

    def _load_cfg(self):
        # cfg = file_parser.get_config('sounds')
        # if not cfg:
        #     return
        # self.current_hs = cfg['current_hs']
        # self.current_ks = cfg['current_ks']
        pass

    def save_cfg(self):
        # values = {
        #     'current_hs': self.current_hs,
        #     'current_ks': self.current_ks
        # }
        # file_parser.write_config(values, 'sounds')
        pass

    def _refresh_db(self):
        for i in self.browser_stack.children()[1:]:  # Ignore QStackedLayout
            self.browser_stack.removeWidget(i)
        self.sounds = file_parser.refresh_db('sounds_db')
        self._load_current_page()

    def _load_current_page(self):
        layout = QVBoxLayout()

        sound_containers = self.sounds[10 * self.current_page_index:10 * (self.current_page_index + 1)]

        for i in sound_containers:
            new_sound_container = SoundContainer(i['title'],
                                                 i['link'],
                                                 i['author'],
                                                 self.tf_path,
                                                 self.main_window_ptr,
                                                 self)
            layout.addLayout(new_sound_container)

        self.browser_stack.currentWidget().setLayout(layout)

    def _switch_to_page(self, page_index):
        if page_index > self.max_pages_count or page_index < 0:
            return

        self.current_page_index = page_index
        self.current_page_text.setText("Page " + str(page_index + 1))

        if page_index < len(self.browser_stack.children()) - 1:  # First children -- QStackedLayout
            self.browser_stack.setCurrentIndex(self.current_page_index)
        else:
            self.browser_stack.addWidget(QWidget())
            self.browser_stack.setCurrentIndex(page_index)

            self._load_current_page()

    def on_sound_installed(self):
        self._load_current_sounds()