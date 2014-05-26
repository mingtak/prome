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


class INormalPage(form.Schema, IImageScaleTraversable):

    body = RichText(
        title = _(u'detail text'),
    )

class NormalPage(Container):
    grok.implements(INormalPage)


class SampleView(grok.View):

    grok.context(INormalPage)
    grok.require('zope2.View')
    grok.name('view')


class SampleView2(grok.View):

    grok.context(INormalPage)
    grok.require('zope2.View')
    grok.name('normal view')
