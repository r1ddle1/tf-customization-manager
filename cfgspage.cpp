#include "cfgspage.h"

CfgsPage::CfgsPage(): PageBase("CFGs browser",
                               "#DB_NAME",
                               "#DB_LINK")
{
    load_db();
}

void CfgsPage::load_db()
{

}
