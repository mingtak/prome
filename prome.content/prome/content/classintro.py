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


class IClassIntro(form.Schema, IImageScaleTraversable):
    classIntroTitle = schema.Text(
        title=_(u'Class intro title'),
        required=True,
    )

    classIntroDescription = schema.Text(
        title=_(u'Class intro description'),
        required=True,
    )

    class_1_Image = NamedBlobImage(
        title=_(u'Class 1 image'),
        description=_(u'Select class image, the image size must be width:height as 145:145'),
        required=True,
    )

    class_1_Text = schema.TextLine(
        title=_(u'Class 1 title'),
        required=True,
    )

    class_2_Image = NamedBlobImage(
        title=_(u'Class 2 image'),
        description=_(u'Select class image, the image size must be width:height as 145:145'),
        required=True,
    )

    class_2_Text = schema.TextLine(
        title=_(u'Class 2 title'),
        required=True,
    )

    class_3_Image = NamedBlobImage(
        title=_(u'Class 3 image'),
        description=_(u'Select class image, the image size must be width:height as 145:145'),
        required=True,
    )

    class_3_Text = schema.TextLine(
        title=_(u'Class 3 title'),
        required=True,
    )

    newClass = RelationList(
        title=_(u"new class images"),
        description=_(u'Select new class image, the image size must be width:height as 338:338'),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=IImage.__identifier__,
            ),
        ),
        required=True,
    )

    newClassUrl = schema.Text(
        title=_(u'New class URL'),
        description=_(u'Input per line one url, and must be mapping to newClass field.'),
        required=True,
    )


#validator
@form.validator(field=IClassIntro['class_1_Image'])
@form.validator(field=IClassIntro['class_2_Image'])
@form.validator(field=IClassIntro['class_3_Image'])
def validateImage(image):
    if image._width != 145:
        raise Invalid(_(u'Image width must be 145px'))
    if image._height != 145:
        raise Invalid(_(u'Image height must be 145px'))


class ClassIntro(Container):
    grok.implements(IClassIntro)


class SampleView(grok.View):
    grok.context(IClassIntro)
    grok.require('zope2.View')
    # grok.name('view')
