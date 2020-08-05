#include "fileparser.hpp"


vector<SoundInfoStruct> FileParser::get_sound_db()
{
    pugi::xml_document doc;
    pugi::xml_parse_result parse_result = doc.load_file(SOUND_DB_FILE_NAME);
    if (!parse_result) {
        std::cerr << "Plz download DB!\n";
        exit(EXIT_FAILURE);
    }

    vector<SoundInfoStruct> result;

    auto db = doc.first_child();
    for (auto i = db.first_child(); i; i = i.next_sibling()) {
        result.push_back(SoundInfoStruct(
                             i.attribute("title").value(),
                             i.attribute("author").value(),
                             i.attribute("link").value()));
    }
    return result;
}
