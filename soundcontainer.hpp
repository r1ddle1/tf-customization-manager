#ifndef SOUNDCONTAINER_H
#define SOUNDCONTAINER_H

#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <iostream>
#include <QSoundEffect>

#include "utils.hpp"

class SoundContainer : public QWidget
{
    Q_OBJECT
public:
    SoundContainer(QString name, QString author, QString download_link);
    ~SoundContainer();
    void on_play_button_clicked();
    void on_stop_button_clicked();

private:
    QSoundEffect _sound_data;
    const QString _download_link;
};

#endif // SOUNDCONTAINER_H
