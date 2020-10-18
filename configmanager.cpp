#include "configmanager.h"

std::map<QString, QString> ConfigManager::_key_values;

ConfigManager::ConfigManager()
{

}

bool ConfigManager::config_exists()
{
    return QDir().exists(CONFIG_FILE_NAME);
}

QString ConfigManager::get_value(QString key)
{
    if (!ConfigManager::_key_values.size()) {
        parse_config();
    }

    for (auto i = _key_values.begin(); i != _key_values.end(); ++i) {
        if (i->first == key)
            return i->second;
    }
    // In case of error we return empty string
    return "";
}

bool ConfigManager::set_value(QString key, QString value)
{
    if (!ConfigManager::_key_values.size()) {
        parse_config();
    }


    bool key_exists = false;
    for (auto i = _key_values.begin(); i != _key_values.end(); ++i) {
        if (i->first == key) {
            i->second = value;
            key_exists = true;
        }
    }

    if (!key_exists) {
        _key_values.insert(std::make_pair(key, value));
    }

    return save_config_to_disk();
}

bool ConfigManager::save_config_to_disk()
{
    // I could use pugi xml for this but who cares?
    // TODO: Optimize this class
    std::ofstream file(CONFIG_FILE_NAME);

    if (!file.is_open())
        return false;

    file << "<settings>\n";

    for (auto &i : _key_values) {
        file << "<item key=\"" + i.first.toStdString() + "\" value=\""
                + i.second.toStdString() + "\" />\n";
    }
    file << "</settings>\n";
    file.close();
    return true;
}

bool ConfigManager::parse_config()
{
    pugi::xml_document doc;
    pugi::xml_parse_result parse_result = doc.load_file(CONFIG_FILE_NAME);

    if (!parse_result)
        return false;

    std::map <QString, QString> result;

    auto settings = doc.first_child();
    for (auto i = settings.first_child(); i; i = i.next_sibling()) {
        QString key_name = i.attribute("key").value();
        QString value = i.attribute("value").value();
        result.insert(std::make_pair(key_name, value));
    }

    _key_values = result;
    return true;
}

