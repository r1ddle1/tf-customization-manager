#ifndef HUDSPAGE_HPP
#define HUDSPAGE_HPP

#include "pagebase.hpp"

class HudsPage: public PageBase
{
public:
    HudsPage();
    virtual void on_refresh_db_clicked();
};

#endif // HUDSPAGE_HPP
