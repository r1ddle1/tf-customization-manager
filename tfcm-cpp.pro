QT       += core gui multimedia
LIBS += -lcurl

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11, console
INCLUDEPATH += include/

# The following define makes your compiler emit warnings if you use
# any Qt feature that has been marked deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    cfgspage.cpp \
    configmanager.cpp \
    fileparser.cpp \
    hudspage.cpp \
    include/pugi/pugixml.cpp \
    main.cpp \
    mainwindow.cpp \
    pagebase.cpp \
    requesttfpathdialog.cpp \
    soundcontainer.cpp \
    soundspage.cpp \
    utils.cpp

HEADERS += \
    cfgspage.h \
    configmanager.h \
    fileparser.hpp \
    hudspage.hpp \
    mainwindow.hpp \
    pagebase.hpp \
    requesttfpathdialog.h \
    soundcontainer.hpp \
    soundspage.hpp \
    utils.hpp

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    img/delete.png \
    img/install.png \
    img/next.png \
    img/play.png \
    img/prev.png \
    img/refresh.png \
    img/stop.png
