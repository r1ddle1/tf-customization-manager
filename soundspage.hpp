#ifndef SOUNDSPAGE_HPP
#define SOUNDSPAGE_HPP

#include <iostream>

#include "pagebase.hpp"
#include "soundcontainer.hpp"
#include "fileparser.hpp"

#define MAX_SOUNDS_COUNT_ON_PAGE 10

class SoundsPage: public PageBase
{
public:
    SoundsPage();
    ~SoundsPage() {}

    virtual void on_refresh_db_clicked();
};

#endif // SOUNDSPAGE_HPP
