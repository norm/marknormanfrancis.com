from flourish import helpers
from flourish.generators import (
    IndexGenerator,
    PageGenerator,
)

from sassutils.builder import build_directory
from shutil import rmtree
from os import makedirs


class SassGenerator:
    @classmethod
    def as_generator(cls):
        def generator(flourish, url, global_context=None, report=False):
            self = cls(flourish, url, global_context, report)
            return self.generate()
        return generator

    def __init__(self, flourish, url, global_context, report):
        self.report = report

    def generate(self):
        files = build_directory(
            'sass',
            'output',
            output_style = 'expanded',
            strip_extension = True,
        )
        for entry in files:
            file = files[entry]
            if self.report:
                print('->', file)


class DatedArchive(IndexGenerator):
    order_by = ('published')


class AllTagsIndex(IndexGenerator):
    template_name = 'tag_index.html'

    def get_objects(self, tokens):
        tags = [
            tag['tag']
            for tag in 
                self.flourish.get_valid_filters_for_tokens(['tag'])
        ]
        self.source_objects = sorted(tags)


class YearIndex(DatedArchive):
    template_name = 'year.html'


class MonthIndex(DatedArchive):
    template_name = 'month.html'


class DayIndex(DatedArchive):
    template_name = 'day.html'


class TagIndex(DatedArchive):
    template_name = 'tag.html'


class Homepage(IndexGenerator):
    order_by = ('-published')
    template_name = 'homepage.html'
    sources_exclude = {'noindex': True}
    # limit = 20


class Archives(IndexGenerator):
    template_name = 'archives.html'


def global_context(self):
    return {
        'all_valid_dates': helpers.all_valid_dates(self.flourish),
    }

GLOBAL_CONTEXT = global_context


SOURCE_URL = (
    '/#slug',
    PageGenerator.as_generator(),
)

URLS = (
    (
        '/',
        'homepage',
        Homepage.as_generator(),
    ),
    (
        '/archives',
        'archives',
        Archives.as_generator(),
    ),
    (
        '/#year/',
        'year-index',
        YearIndex.as_generator()
    ),
    (
        '/#year/#month/',
        'month-index',
        MonthIndex.as_generator()
    ),
    (
        '/#year/#month/#day/',
        'day-index',
        DayIndex.as_generator()
    ),
    (
        '/tags/',
        'tags-index',
        AllTagsIndex.as_generator()
    ),
    (
        '/tags/#tag/',
        'tags-tag-index',
        TagIndex.as_generator()
    ),
    (
        '/site.css',    # FIXME does all target files, not only this
        'css',
        SassGenerator.as_generator()
    ),
)
