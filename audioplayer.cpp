#include "audioplayer.hpp"


AudioPlayer* AudioPlayer::GetInstance()
{
    static AudioPlayer a;
    return &a;
}

void AudioPlayer::play_audio(const QMediaContent& url)
{
    if (!_media_player) {
        _media_player = new QMediaPlayer();
    }
    _media_player->setMedia(url);
    _media_player->play();
}

void AudioPlayer::stop_audio()
{
    if (_media_player) {
        _media_player->stop();
    }
}
