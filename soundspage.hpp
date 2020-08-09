#ifndef SOUNDSPAGE_HPP
#define SOUNDSPAGE_HPP

#include <iostream>
#include <sys/stat.h>


#ifdef WIN32
  #define stat _stat
#endif

#include "pagebase.hpp"
#include "soundcontainer.hpp"
#include "fileparser.hpp"

#define MAX_SOUNDS_COUNT_ON_PAGE 10

class SoundsPage: public PageBase
{
public:
    SoundsPage();
    ~SoundsPage() {}

    virtual void load_db() override;
private:
    void display_db();
};

#endif // SOUNDSPAGE_HPP
