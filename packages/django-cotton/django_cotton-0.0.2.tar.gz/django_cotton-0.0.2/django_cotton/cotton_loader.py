import hashlib
import os
import re
import warnings

from bs4.formatter import HTMLFormatter
from django.template.loaders.base import Loader as BaseLoader
from django.core.exceptions import SuspiciousFileOperation
from django.template import TemplateDoesNotExist
from django.utils._os import safe_join
from django.template import Template
from django.core.cache import cache
from django.template import Origin

from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

class Loader(BaseLoader):
    is_usable = True

    def __init__(self, engine, dirs=None):
        super().__init__(engine)
        self.dirs = dirs

    def get_template(self, template_name, skip=None):
        """
        Call self.get_template_sources() and return a Template object for
        the first template matching template_name. If skip is provided, ignore
        template origins in skip. This is used to avoid recursion during
        template extending.
        """

        tried = []

        for origin in self.get_template_sources(template_name):
            if skip is not None and origin in skip:
                tried.append((origin, "Skipped to avoid recursion"))
                continue

            try:
                contents = self.get_contents(origin)
            except TemplateDoesNotExist:
                tried.append((origin, "Source does not exist"))
                continue
            else:
                return Template(
                    contents,
                    origin,
                    origin.template_name,
                    self.engine,
                )

        raise TemplateDoesNotExist(template_name, tried=tried)

    def get_contents(self, origin):

        # try:
        #     mtime = os.path.getmtime(origin.name)
        # except FileNotFoundError:
        #     raise TemplateDoesNotExist(origin)


        # Generate a hash for the template name
        # template_hash = hashlib.sha256(origin.template_name.encode()).hexdigest() + str(mtime)
        # cached_template_path = os.path.join('/tmp', template_hash)

        # Check if the processed template is already cached
        # if os.path.exists(cached_template_path):
        #     with open(cached_template_path, 'r') as f:
        #         return f.read()

        # Todo, also check timestamp
        # Todo, also provide a cache invalidation command cotton invalidate

        # If not cached, process the template
        compiled_template = self._compile_template(origin.name)

        # Cache the processed template
        # with open(cached_template_path, 'w') as f:
        #     f.write(compiled_template)

        return compiled_template

        # for filepath in self.get_template_sources(template_name, template_dirs):
        # For caching system
        try:
            with open(origin.name, 'r') as f:
                content = f.read()


            # Get the file's last modification time
            mtime = os.path.getmtime(origin.name)
            # Compile the content
            compiled = self._compile_cotton_to_django(content)
            # compiled = content
            compiled = "{% load cotton_component %}" + compiled
            cleaned = self._fix_django_attribute_parsing(compiled)

            return cleaned  # Return the compiled content along with a modified origin
            # return compiled, f"{origin.name}:{mtime}"
        except FileNotFoundError:
            raise TemplateDoesNotExist(origin)

    def _compile_template(self, template_name):
        try:
            with open(template_name, 'r') as f:
                content = f.read()

            # Compile the content
            compiled = self._compile_cotton_to_django(content)
            cleaned = self._fix_django_attribute_parsing(compiled)

            return cleaned  # Return the compiled content along with a modified origin
            # return compiled, f"{origin.name}:{mtime}"
        except FileNotFoundError:
            raise TemplateDoesNotExist(template_name)

    def _fix_django_attribute_parsing(self, contents):
        """Django's template parser adds ="" to empty attribute-like parts in any html-like node, i.e. <div {{ something }}> gets
        compiled to <div {{ something }}=""> Then if 'something' is holding attributes sets, the last attribute value is
        not quoted. i.e. model=test not model="test"."""
        cleaned_content = re.sub('}}=""', '}}', contents)
        return cleaned_content

    def get_dirs(self):
        return self.dirs if self.dirs is not None else self.engine.dirs

    def get_template_sources(self, template_name):
        """ Return an Origin object pointing to an absolute path in each directory
        in template_dirs. For security reasons, if a path doesn't lie inside
        one of the template_dirs it is excluded from the result set. """
        if not template_name.endswith('.cotton.html'):
            raise TemplateDoesNotExist(template_name)
        for template_dir in self.get_dirs():
            try:
                name = safe_join(template_dir, template_name)
            except SuspiciousFileOperation:
                # The joined path was located outside of this template_dir
                # (it might be inside another one, so this isn't fatal).
                continue

            yield Origin(
                name=name,
                template_name=template_name,
                loader=self,
            )

    def _remove_whitespace_in_tags_for_bs4_happiness(self, html_content):
        # Regular expression to match Django template tags and remove whitespace
        pattern = re.compile(r'\{\{\s*(.*?)\s*\}\}')
        # Replace matched template tags with their trimmed content
        return pattern.sub(r'{{\1}}', html_content)

    def _compile_cotton_to_django(self, html_content):
        """ Convert cotton <x-* syntax to {%. """

        html_content = self._remove_whitespace_in_tags_for_bs4_happiness(html_content)

        soup = BeautifulSoup(html_content, 'html.parser')


        self._transform_named_slots(soup)
        self._transform_components(soup)

        return str(soup)

    def _transform_named_slots(self, soup):
        """ Replace <x-slot> tags with the {% cotton_slot %} template tag """
        for x_slot in soup.find_all('x-slot'):
            slot_name = x_slot.get('name', '').strip()
            inner_html = ''.join(str(content) for content in x_slot.contents)

            cotton_slot_tag = f'{{% cotton_slot {slot_name} %}}{inner_html}{{% end_cotton_slot %}}'
            x_slot.replace_with(BeautifulSoup(cotton_slot_tag, 'html.parser'))

        return soup

    def _transform_components(self, soup):
        """ Replace <x-[component path]> tags with the {% cotton_component %} template tag """
        for tag in soup.find_all(re.compile('^x-'), recursive=True):
            component_name = tag.name[2:]  # Remove the 'x-' prefix

            # Convert dot notation to path structure and replace hyphens with underscores
            path = component_name.replace('.', '/').replace('-', '_')

            # Construct the opening tag
            opening_tag = '{{% cotton_component cotton/{}.cotton.html'.format(path)
            for attr, value in tag.attrs.items():
                if attr == 'class':
                    value = '"' + ' '.join(value) + '"'
                opening_tag += ' {}={}'.format(attr, value)
            opening_tag += ' %}'

            # Construct the closing tag
            closing_tag = '{% end_cotton_component %}'

            if tag.contents:
                tag_soup = BeautifulSoup(tag.decode_contents(), 'html.parser')
                self._transform_components(tag_soup)

                # Create new content with opening tag, tag content, and closing tag
                new_content = opening_tag + str(tag_soup) + closing_tag

            else:
                # Create new content with opening tag and closing tag
                new_content = opening_tag + closing_tag

            # Replace the original tag with the new content
            new_soup = BeautifulSoup(new_content, 'html.parser')
            tag.replace_with(new_soup)

        return str(soup)
