#include "soundspage.hpp"

SoundsPage::SoundsPage(): PageBase("Sound Browser")
{
    auto db = FileParser::get_sound_db();

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

    _scroll_area->setWidget(_pages[0]);
    _scroll_area->setWidgetResizable(true);

}

void SoundsPage::on_refresh_db_clicked()
{
    std::cout << "clicked\n";
}
