#include "soundspage.hpp"

SoundsPage::SoundsPage(): PageBase("Sound Browser")
{
}

void SoundsPage::on_refresh_db_clicked()
{
    std::cout << "clicked\n";
}
