# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.
class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass

    def testtest(self):
        self.assertEqual(1,1)

    def test_korean_proofread(self):
        import korean
        result = korean.l10n.proofread(u"이준행은(는) 직립보행을 한다.")
        self.assertEqual(result, u"이준행은 직립보행을 한다.")

    def test_korean_proofreadi_fail(self):
        import korean
        result = korean.l10n.proofread(u"이준행은(는) 직립보행을 한다.")
        self.assertNotEqual(result, u"이준행는 직립보행을 한다.")

    def test_korean_proofread_tag(self):
        from django.template import Context, Template
        rendered = Template(
                '{% load proofread %}'
                '{{ string|proofread }}'
                ).render(Context({
                    'string': u'이준행은(는) 직립보행을 한다.',
                    }))
        self.assertEqual(rendered, u"이준행은 직립보행을 한다.")
