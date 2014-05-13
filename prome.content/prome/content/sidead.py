from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.indexer import indexer

from prome.content import MessageFactory as _


class ISideAd(form.Schema, IImageScaleTraversable):
    """
    AD at sidebar
    """

    showAtHomePage = schema.Bool(
        title=_(u'Show at home page'),
        description=_(u'if not checked, this ad will not show at home page, but will show at other pages'),
        required=False,
    )

    adImage = NamedBlobImage(
        title=_(u'side AD image'),
        description=_(u'AD Image'),
        required=True,
    )

    adLink = schema.URI(
        title=_(u'side AD Url'),
        description=_(u'input ad url, include http://'),
        required=True,
    )


class SideAd(Container):
    grok.implements(ISideAd)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ISideAd)
    grok.require('zope2.View')
    grok.name('view')


@indexer(ISideAd)
def showAtHomePage_indexer(obj):
     return obj.showAtHomePage
grok.global_adapter(showAtHomePage_indexer, name='showAtHomePage')
