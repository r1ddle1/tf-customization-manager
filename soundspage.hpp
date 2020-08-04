#ifndef SOUNDSPAGE_HPP
#define SOUNDSPAGE_HPP

#include "pagebase.hpp"
#include <iostream>

class SoundsPage: public PageBase
{
public:
    SoundsPage();
    ~SoundsPage() {}

    virtual void on_refresh_db_clicked();
};

#endif // SOUNDSPAGE_HPP
