#include "soundspage.hpp"

SoundsPage::SoundsPage(): PageBase("Sound Browser",
                                   SOUND_DB_FILE_NAME,
                                   SOUND_DB_FILE_URL)
{
    load_db();
}

void SoundsPage::load_db()
{
    // First, destroy all children
    for (auto &i : _pages) {
        delete i;
    }
    _pages.clear();

    // Second, download new db
    auto db = FileParser::get_sound_db();

    // Third, use the db
    for (int i = 0; i < db.size(); i += MAX_SOUNDS_COUNT_ON_PAGE) {
        QVBoxLayout *layout = new QVBoxLayout();

        for (int j = i; j < i + MAX_SOUNDS_COUNT_ON_PAGE; ++j) {
            auto &elem = db[j];
            layout->addWidget(new SoundContainer(elem.title,
                                                 elem.author,
                                                 elem.download_link));
        }

        QWidget *page = new QWidget();
        page->setLayout(layout);

        _pages.push_back(page);
    }
    _scroll_area->setWidget(_pages[_current_page_index]);
    _scroll_area->setWidgetResizable(true);


    // Fourthly get creation date of the db & use it too
    _last_refresh_label->setText(QString("Last refresh:\n") +
                                 get_file_creation_date(SOUND_DB_FILE_NAME));
}
