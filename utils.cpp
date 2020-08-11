#include "utils.hpp"

#ifdef WIN32
  #define stat _stat
#endif


static size_t write_data(void* ptr, size_t size, size_t nmemb, FILE* stream)
{
    return fwrite(ptr, size, nmemb, stream);
}


std::FILE* download_file(const char* url)
{
    curl_global_init(CURL_GLOBAL_ALL);

    /* init the curl session */
    CURL* curl_handle = curl_easy_init();

    /* set URL to get here */
    curl_easy_setopt(curl_handle, CURLOPT_URL, url);

    /* Switch on full protocol/debug output while testing */
    curl_easy_setopt(curl_handle, CURLOPT_VERBOSE, 0L);

    /* disable progress meter, set to 0L to enable it */
    curl_easy_setopt(curl_handle, CURLOPT_NOPROGRESS, 1L);

    /* send all data to this function  */
    curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, write_data);

    /* open the file */
    FILE* pagefile = std::tmpfile();
    if (pagefile) {
        /* write the page body to this file handle */
        curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, pagefile);

        /* get it! */
        curl_easy_perform(curl_handle);
    }


    /* cleanup curl stuff */
    curl_easy_cleanup(curl_handle);

    curl_global_cleanup();

    return pagefile;
}


void download_file_to_disk(const char* url, const char* file_path)
{
    FILE* file = download_file(url);
    std::rewind(file);

    std::ofstream write_file(file_path);

    char c;
    while ((c = getc(file)) != EOF)
    {
        write_file << c;
    }

    fclose(file);
    write_file.close();
}


const char* get_file_creation_date(const char* file_path)
{
    struct stat t_stat;
    stat(file_path, &t_stat);

    struct tm* timeinfo = localtime(&t_stat.st_mtime);

    char* modified_time = new char[50];
    strftime(modified_time, 50, "%X\n%x", timeinfo);
    std::cout << modified_time << '\n';
    return modified_time;
}
