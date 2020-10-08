#ifndef UTILS_HPP
#define UTILS_HPP

#include <iostream>
#include <fstream>
#include <curl/curl.h>

#include <sys/stat.h>
#include <time.h>

#include <QDir>


std::FILE* download_file(const char* url);

void download_file_to_disk(const char* url, const char* file_path);

const char* get_file_creation_date(const char* file_path);

bool is_tf_path(QString path);



#endif // UTILS_HPP
