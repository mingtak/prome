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

from plone.app.contenttypes.interfaces import IImage
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget


class ISlide(form.Schema, IImageScaleTraversable):

#    form.widget(slides=AutocompleteFieldWidget)
    slides = RelationList(
        title=_(u"Slide show images"),
        description=_(u'Select slide image, the image size must be width:height as 1140:430'),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=IImage.__identifier__,
            ),
        ),
        required=True,
    )

    slidesUrl = schema.Text(
        title=_(u"Slides Url link"),
        description=_(u'Slides url link setting, one line, one url, must be one to one.'),
        required=True,
    )

    belowSlideTextLine1 = schema.TextLine(
        title=_(u'Below slide text line 1'),
        description=_(u'Can use "em" tag, to highlight inside text'),
        required=True,
    )

    belowSlideTextLine2 = schema.TextLine(
        title=_(u'Below slide text line 2'),
        required=True,
    )

    buttonUrl = schema.URI(
        title=_(u'Button Url'),
        description=_(u'Button Url, must include http://'),
        required=True,
    )

    learnMoreUrl = schema.URI(
        title=_(u'Learn more Url'),
        description=_(u'Learn more Url, must include http://'),
        required=True,
    )


class Slide(Container):
    grok.implements(ISlide)


class SampleView(grok.View):
    grok.context(ISlide)
    grok.require('zope2.View')
    # grok.name('view')
