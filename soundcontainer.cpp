#include "soundcontainer.hpp"

SoundContainer::SoundContainer(QString name, QString author, QString download_link)
{
    _media_content = new QMediaContent(QUrl(download_link));

    QHBoxLayout *main_layout = new QHBoxLayout();
    setLayout(main_layout);

    QString label_text = "<b>" + name + "</b>" + "\n<i>by " + author;

    QLabel *label = new QLabel(label_text);

    QHBoxLayout *buttons_layout = new QHBoxLayout();

    QPushButton *play_btn = new QPushButton();
    QPushButton *stop_btn = new QPushButton();
    QPushButton *install_btn = new QPushButton();

    play_btn->setIcon(QIcon("img/play.png"));
    stop_btn->setIcon(QIcon("img/stop.png"));
    install_btn->setIcon(QIcon("img/install.png"));

    connect(play_btn,
            &QPushButton::clicked,
            this,
            &SoundContainer::play_audio);

    connect(stop_btn,
            &QPushButton::clicked,
            this,
            &SoundContainer::stop_audio);

    buttons_layout->setAlignment(Qt::AlignRight);

    main_layout->addWidget(label);
    main_layout->addLayout(buttons_layout);

    buttons_layout->addWidget(play_btn);
    buttons_layout->addWidget(stop_btn);
    buttons_layout->addWidget(install_btn);
}


SoundContainer::~SoundContainer()
{
    // TODO: Realize freeing memory
}


void SoundContainer::play_audio()
{
    AudioPlayer::GetInstance()->play_audio(*_media_content);
}

void SoundContainer::stop_audio()
{
    AudioPlayer::GetInstance()->stop_audio();
}
