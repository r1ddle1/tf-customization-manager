#ifndef HUDSPAGE_HPP
#define HUDSPAGE_HPP

#include "pagebase.hpp"

class HudsPage: public PageBase
{
public:
    HudsPage();
    virtual void load_db() override;
};

#endif // HUDSPAGE_HPP
