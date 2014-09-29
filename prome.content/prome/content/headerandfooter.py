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


from prome.content import MessageFactory as _


class IHeaderAndFooter(form.Schema, IImageScaleTraversable):
    """
    Page header and footer information setup
    """
    header_aboutus_url = schema.TextLine(
        title=_(u'About us url'),
        description=_(u'Page header, about us, link url, must include http://'),
        required=True,
    )

    header_tel = schema.TextLine(
        title=_(u'tel number'),
        description=_(u'Page header, TEL Number'),
        required=True,
    )

    footer_block_1 = RichText(
        title=_(u'Page footer, block 1'),
        description=_(u'Page footer, block 1, must be html format'),
        required=True,
    )

    footer_block_2 = RichText(
        title=_(u'Page footer, block 2'),
        description=_(u'Page footer, block 2, must be html format'),
        required=True,
    )

    footer_block_3 = RichText(
        title=_(u'Page footer, block 3'),
        description=_(u'Page footer, block 3, must be html format'),
        required=True,
    )

    footer_block_4 = RichText(
        title=_(u'Page footer, block 4'),
        description=_(u'Page footer, block 4, must be html format'),
        required=True,
    )

    facebookLink = schema.TextLine(
        title=_(u'Facebook URL'),
        required=False,
    )

    googleLink = schema.TextLine(
        title=_(u'Google+ URL'),
        required=False,
    )

    emailAddress = schema.TextLine(
        title=_(u'Email address'),
        required=False,
    )


class HeaderAndFooter(Container):
    grok.implements(IHeaderAndFooter)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IHeaderAndFooter)
    grok.require('zope2.View')

    # grok.name('view')
