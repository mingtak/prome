# -*- extra stuff goes here -*-
from zope.i18nmessageid import MessageFactory

portletMessageFactory = MessageFactory('prome.portlet')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
