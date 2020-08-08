#ifndef AUDIOPLAYER_HPP
#define AUDIOPLAYER_HPP

#include <QMediaPlayer>

class AudioPlayer
{
public:
    static AudioPlayer* GetInstance();
    void play_audio(const QMediaContent& url);
    void stop_audio();
private:
    QMediaPlayer* _media_player;
};

#endif // AUDIOPLAYER_HPP
