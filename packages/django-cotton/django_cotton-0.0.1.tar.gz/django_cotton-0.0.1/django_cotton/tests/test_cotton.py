import re
from unittest import skip

from django.test import TestCase


class CottonTestCase(TestCase):

    def test_parent_component_is_rendered(self):
        response = self.client.get('/parent')
        self.assertContains(response, '<div class="i-am-parent">')

    def test_child_is_rendered(self):
        response = self.client.get('/child')
        self.assertContains(response, '<div class="i-am-parent">')
        self.assertContains(response, '<div class="i-am-child">')

    def test_self_closing_is_rendered(self):
        response = self.client.get('/self-closing')
        self.assertContains(response, '<div class="i-am-parent">')

    def test_named_slots_correctly_display_in_loop(self):
        response = self.client.get('/named-slot-in-loop')
        self.assertContains(response, 'item name: Item 1')
        self.assertContains(response, 'item name: Item 2')
        self.assertContains(response, 'item name: Item 3')

    def test_attribute_passing(self):
        response = self.client.get('/attribute-passing')
        self.assertContains(response, '<div attribute_1="hello" and-another="woo1" thirdforluck="yes">')

    @skip("Not ready yet")
    def test_attribute_merging(self):
        response = self.client.get('/attribute-merging')
        print(response.content.decode('utf-8'))
        self.assertContains(response, '<div class="form-group extra-class">')