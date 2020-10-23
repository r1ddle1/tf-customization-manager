#ifndef CFGPAGE_H
#define CFGPAGE_H

#include "pagebase.hpp"

class CfgsPage: public PageBase
{
public:
    CfgsPage();
    virtual void load_db() override;
};

#endif // CFGPAGE_H
