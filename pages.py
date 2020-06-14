import huds_tf_parser
from containers import *


class SoundsPage(QWidget):
    def __init__(self, tf_path, main_window_ptr):
        super(SoundsPage, self).__init__()

        self.tf_path = tf_path
        self.main_window_ptr = main_window_ptr  # For creating dialogs
        self.main_layout = QHBoxLayout()

        self.create_options_part()
        self.create_browser_part()

        self.setLayout(self.main_layout)
        self.show()

    def create_browser_part(self):
        browser_part = QVBoxLayout()
        # browser_part.setSpacing(0)
        self.current_page_index = 0
        self.browser_stack = QStackedWidget()
        self.current_page_index = 0  # Index of pages begins with 0
        self.max_pages_count = 100  # XXX: Parse page and get maximum pages count

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

        go_back_btn.clicked.connect(lambda: self.switch_to_page(self.current_page_index - 1))
        go_forward_button.clicked.connect(lambda: self.switch_to_page(self.current_page_index + 1))

        page_switching_hbox.addWidget(go_back_btn)
        page_switching_hbox.addWidget(self.current_page_text)
        page_switching_hbox.addWidget(go_forward_button)

        self.switch_to_page(self.current_page_index)

        browser_part.addWidget(browser_label)
        browser_part.addWidget(self.browser_stack)
        browser_part.addLayout(page_switching_hbox)

        self.main_layout.addLayout(browser_part)

    def create_options_part(self):
        main_vbox = QVBoxLayout()

        refresh_hbox = QHBoxLayout()
        current_ks_hbox = QHBoxLayout()
        current_hs_hbox = QHBoxLayout()

        refresh_label = QLabel('Last refresh: ?ago\nPage cached: 1')
        refresh_btn = QPushButton('Refresh')
        refresh_btn.setIcon(QIcon('img/refresh.png'))
        refresh_btn.clicked.connect(self.refresh_page)

        current_ks_label = QLabel('Current killsound:???.wav')
        del_curr_ks_btn = QPushButton('Delete')
        del_curr_ks_btn.setIcon(QIcon('img/delete.png'))
        del_curr_ks_btn.clicked.connect(lambda: self.delete_current_sound('killsound'))

        current_hs_label = QLabel('Current hitsound: ???.wav')
        del_curr_hs_btn = QPushButton('Delete')
        del_curr_hs_btn.setIcon(QIcon('img/delete.png'))
        del_curr_hs_btn.clicked.connect(lambda: self.delete_current_sound('hitsound'))

        refresh_hbox.addWidget(refresh_label)
        refresh_hbox.addWidget(refresh_btn, alignment=Qt.AlignRight)

        current_ks_hbox.addWidget(current_ks_label)
        current_ks_hbox.addWidget(del_curr_ks_btn)

        current_hs_hbox.addWidget(current_hs_label)
        current_hs_hbox.addWidget(del_curr_hs_btn)

        main_vbox.addLayout(refresh_hbox)
        main_vbox.addLayout(current_hs_hbox)
        main_vbox.addLayout(current_ks_hbox)

        self.main_layout.addLayout(main_vbox)

    def delete_current_sound(self, sound):
        import os
        try:
            os.remove(self.tf_path + '/tf/custom/tf2hitsounds/sound/ui/' + sound + '.wav')
            del os
        except FileNotFoundError:
            dialog = QErrorMessage(self.main_window_ptr)
            dialog.showMessage("Error! There's no installed " + sound)
            del os

    def refresh_page(self):
        # If there's more than 1 children we need to remove the 2nd as it's
        # old QVBoxLayout()
        if len(self.browser_stack.currentWidget().children()) == 2:
            self.browser_stack.currentWidget().children()[1].deleteLater()

        layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)

        sound_containers = huds_tf_parser.parse_sounds(self.current_page_index + 1)

        for i in sound_containers:
            title = i['title']
            author = i['author']
            download_link = i['link']

            new_sound_container = SoundContainer(title,
                                                 download_link,
                                                 author,
                                                 self.tf_path,
                                                 self.main_window_ptr)

            layout.addLayout(new_sound_container)
        self.browser_stack.currentWidget().layout().addWidget(widget)

    def switch_to_page(self, page_index):
        if page_index > self.max_pages_count or page_index < 0:
            return

        self.current_page_index = page_index
        self.current_page_text.setText("Page " + str(page_index + 1))

        if page_index < len(self.browser_stack.children()) - 1:  # First children -- QStackedLayout
            self.browser_stack.setCurrentIndex(self.current_page_index)
        else:
            widget = QWidget()
            widget.setLayout(QVBoxLayout())

            self.browser_stack.addWidget(widget)
            self.browser_stack.setCurrentIndex(page_index)

            # self.refresh_label.setText('Last refresh: {} ago\nPage cached:{}'.format('?', len(self.pages)))
            self.refresh_page()
