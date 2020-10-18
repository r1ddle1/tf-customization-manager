#ifndef CONFIGMANAGER_H
#define CONFIGMANAGER_H

// This is not tf config manager, it's TFCM's cfg file manager!

#include <QDir>
#include <map>
#include <fstream>
#include <iostream>

#include "pugi/pugixml.hpp"


#define CONFIG_FILE_NAME "config.xml"
#define TF_PATH_KEY "team_fortress_path"

class ConfigManager
{
public:
    ConfigManager();
    static bool config_exists();
    static QString get_value(QString key);
    static bool set_value(QString key, QString value);

private:
    static std::map<QString, QString> _key_values;
    static bool save_config_to_disk();
    static bool parse_config();
};


#endif // CONFIGMANAGER_H
