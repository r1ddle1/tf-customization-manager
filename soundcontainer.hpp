#ifndef SOUNDCONTAINER_H
#define SOUNDCONTAINER_H

#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>


class SoundContainer : public QWidget
{
    Q_OBJECT
public:
    SoundContainer(QString name, QString author, QString download_link);
    ~SoundContainer();
    void play_audio();
    void stop_audio();

private:
    const QString _download_link;
};

#endif // SOUNDCONTAINER_H
