#ifndef SOUNDCONTAINER_H
#define SOUNDCONTAINER_H

#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <iostream>

#include "audioplayer.hpp"

class SoundContainer : public QWidget
{
    Q_OBJECT
public:
    SoundContainer(QString name, QString author, QString download_link);
    ~SoundContainer();
    void play_audio();
    void stop_audio();

private:
    const QMediaContent* _media_content;
};

#endif // SOUNDCONTAINER_H
