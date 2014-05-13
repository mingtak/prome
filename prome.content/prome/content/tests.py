import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import prome.content

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['prome.content'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              prome.content)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='prome.content',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='prome.content.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='prome.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for ClassIntro
        ztc.ZopeDocFileSuite(
            'ClassIntro.txt',
            package='prome.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Slide
        ztc.ZopeDocFileSuite(
            'Slide.txt',
            package='prome.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for SideAd
        ztc.ZopeDocFileSuite(
            'SideAd.txt',
            package='prome.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for YoutubeVideo
        ztc.ZopeDocFileSuite(
            'YoutubeVideo.txt',
            package='prome.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),



        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
