import logging
from django.test import TestCase
from core import views


logger = logging.getLogger()


class ContentsGeneratorTests(TestCase):
    print('ContentsGeneratorTests Initialized')
    generator = views.RandomContentsGenerator()

    # Generate Random Contents
    contents_line = 300
    extracted_text_count = 10000000
    text_file_path = 'data/contents/wiki.txt'
    print('Creating {} lined {} Contents...'.format(
        contents_line, extracted_text_count))
    generate_contents_result = generator.get_sample_text_list(
        contents_line,
        extracted_text_count,
        text_file_path
    )
    generator.save_generated_contents(generate_contents_result)

    def setUp(self):
        pass

    def test_contents_generated(self):
        self.assertEqual(
            self.generate_contents_result,
            self.extracted_text_count
        )
