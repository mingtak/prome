#-*- coding:utf-8 -*-
from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContentTitle
#IAboveContentTitle, IBelowContentBody


#設定viewlet介面、pt檔目錄
grok.context(Interface)
grok.templatedir('viewlet_templates')


class PromeMainMenu(grok.Viewlet):
    grok.viewletmanager(IPortalHeader)


class PromeSlide(grok.Viewlet):
    grok.viewletmanager(IPortalHeader)


class PromeClassIntro(grok.Viewlet):
    grok.viewletmanager(IPortalHeader)


class PromeRowLeft(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)


class PromeRowMiddle(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)

class PromeRowRight(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)

class PageHeader(grok.Viewlet):
    grok.viewletmanager(IPortalHeader)

#下列可再新增viewlet, 可用的interface可查詢 plone.app.layout.viewlets.interfaces
