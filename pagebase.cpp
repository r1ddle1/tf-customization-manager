#include "pagebase.hpp"


PageBase::PageBase(QString browser_name, const char* db_path, const char* db_url)
    : _DB_FILE_PATH(db_path)
    , _DB_URL(db_url)
{
    QHBoxLayout *main_layout = new QHBoxLayout();
    setLayout(main_layout);

    create_options_part(main_layout);
    create_browser_part(main_layout, browser_name);
}

PageBase::~PageBase()
{
    //dtor
}

void PageBase::on_refresh_db_clicked()
{
    download_file_to_disk(_DB_URL, _DB_FILE_PATH);
    load_db();
}

void PageBase::on_go_back_button_pressed()
{
    if (_current_page_index) {
        // Looks like without takeWidget() function being called
        // Qt deletes the object
        _scroll_area->takeWidget();
        _scroll_area->setWidget(_pages[--_current_page_index]);
        _current_page_label->setText("Page " +
                                     QString::number(_current_page_index + 1));
    }
}

void PageBase::on_go_forward_button_pressed()
{
    if (_current_page_index != _pages.size() - 1) {
        _scroll_area->takeWidget();
        _scroll_area->setWidget(_pages[++_current_page_index]);
        _current_page_label->setText("Page " +
                                     QString::number(_current_page_index + 1));
    }
}


void PageBase::create_options_part(QHBoxLayout* main_layout)
{
    _options_layout = new QVBoxLayout();

    QHBoxLayout *refresh_layout = new QHBoxLayout();

    _last_refresh_label = new QLabel("Last refresh:\n???");
    QPushButton *refresh_db_button = new QPushButton("Refresh DB");

    refresh_db_button->setIcon(QIcon("img/refresh.png"));

    refresh_layout->addWidget(_last_refresh_label);
    refresh_layout->addWidget(refresh_db_button);

    connect(refresh_db_button,
            &QPushButton::clicked,
            this,
            &PageBase::on_refresh_db_clicked);

    _options_layout->addLayout(refresh_layout);

    main_layout->addLayout(_options_layout);

}


void PageBase::create_browser_part(QHBoxLayout* main_layout,
                                   QString &browser_name)
{
    QVBoxLayout *browser_part = new QVBoxLayout();

    QLabel *browser_label = new QLabel(browser_name);
    browser_part->addWidget(browser_label, 0, Qt::AlignHCenter);

    _scroll_area = new QScrollArea();
    browser_part->addWidget(_scroll_area);

    QHBoxLayout *page_switching_hbox = new QHBoxLayout();
    QPushButton *go_back_btn = new QPushButton();
    QPushButton *go_forward_btn = new QPushButton();
    _current_page_label = new QLabel("Page 1");

    go_back_btn->setIcon(QIcon("img/prev.png"));
    go_forward_btn->setIcon(QIcon("img/next.png"));

    // Connect buttons...
    connect(go_back_btn,
            &QPushButton::clicked,
            this,
            &PageBase::on_go_back_button_pressed);

    connect(go_forward_btn,
            &QPushButton::clicked,
            this,
            &PageBase::on_go_forward_button_pressed);

    page_switching_hbox->addWidget(go_back_btn);
    page_switching_hbox->addWidget(_current_page_label);
    page_switching_hbox->addWidget(go_forward_btn);
    page_switching_hbox->setAlignment(Qt::AlignHCenter);

    browser_part->addLayout(page_switching_hbox);

    main_layout->addLayout(browser_part);
}
