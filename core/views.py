import re
import random
import logging
import linecache

from django.conf import settings

from core.models import Content, Attach


logger = logging.getLogger()


class RandomContentsGenerator:
    extracted_name_list = []

    def __init__(self):
        with open('data/names/english_names.csv', encoding='utf8') as infile:
            for line in enumerate(infile):
                self.extracted_name_list.append(line)
        pass

    def get_sample_text_list(
            self, contents_line, extracted_text_count, text_file_path):
        """get_sample_text_list

        :param contents_line: How many lines generated contents will have.
        :param extracted_text_count: How many contents will be generated.
        :param text_file_path: The location of target file.
        :return: A list with randomly generated contents.
        """
        total_lines = 0
        complete_count = 0

        with open(text_file_path, encoding='utf8') as infile:
            for line in enumerate(infile):
                total_lines += 1

        for count in range(extracted_text_count):
            extracted_text = ''
            random_line = random.randrange(1, total_lines - contents_line)
            print('Generating {}th content...'.format(complete_count+1))
            for index in range(contents_line):
                caught_line = linecache.getline(
                    text_file_path,
                    random_line +
                    index
                )
                extracted_text += caught_line
            result = self.save_generated_contents(extracted_text)
            if result:
                self.save_attach_to_contents(result.id)
            complete_count += 1

        return complete_count

    def save_generated_contents(self, content):
        """save_generated_contents

        :param content: content text for save
        :return:
        """
        try:
            writer_name = random.choice(self.extracted_name_list)
            writer_name = re.sub('\n', '', writer_name[1])
            title = content[:100]
            content = content
            instance = Content.objects.create(
                writer_name=writer_name,
                title=title,
                content=content
            )
            return instance
        except Exception as e:
            print(e)
            return False

    def save_attach_to_contents(self, content_id):
        """save_attach_to_contents

        :param content_id: target content id
        :return:
        """
        save_chance = random.random()
        if save_chance < 0.6:
            attach_file_name = random.choice(settings.ATTACH_FILES)
            attach_file_path = '{}attaches/{}'.format(
                settings.MEDIA_ROOT,
                attach_file_name
            )

            try:
                instance = Attach.objects.create(
                    content_id=content_id,
                    file_original_name=attach_file_name,
                    file_path=attach_file_path
                )
                return instance
            except Exception as e:
                print(e)
                return False
        else:
            False

    def delete_generated_contents(self):
        try:
            instance = Content.objects.all()
            instance.delete()
        except Exception as e:
            logger.debug(e)
        pass

    def get_sample_attach_list(self):
        pass

    def get_sample_words_list(self):
        pass

    def get_sample_names_list(self):
        pass
