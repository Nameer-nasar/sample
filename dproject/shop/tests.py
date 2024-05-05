from django.test import TestCase


def demo(str1, str2):
    return str1 + str2


class test_string(TestCase):
    def test_concert(self):
        self.assertEquals(demo("hi", "hello"), "hihello")
