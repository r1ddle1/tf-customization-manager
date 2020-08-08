#ifndef FILEPARSER_H
#define FILEPARSER_H

#include <vector>
#include <QString>
#include <iostream>

#include "pugi/pugixml.hpp"

using namespace std;

// Improve compile time
#define PUGIXML_NO_XPATH

#define SOUND_DB_FILE_URL "https://raw.githubusercontent.com/r1ddle1/tfcm-databases/master/sounds.xml"

#define HUD_DB_FILE_NAME "huds.xml"
#define SOUND_DB_FILE_NAME "sounds.xml"
#define CFG_DB_FILE_NAME "cfgs.xml";

struct SoundInfoStruct {
    SoundInfoStruct(QString _title, QString _author, QString _download_link)
        : title(_title)
        , author(_author)
        , download_link(_download_link)
    {

    }
    QString title;
    QString author;
    QString download_link;
};

class FileParser
{
public:
    FileParser() = delete;

    static vector<SoundInfoStruct> get_sound_db();

};

#endif // FILEPARSER_H
