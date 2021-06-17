from flourish import filters
from flourish import helpers
from flourish.generators import base
from flourish.generators import calendar
from flourish.generators import sass

from django.utils.html import linebreaks, urlize
from django.template.defaultfilters import pluralize


class AllTagsIndex(base.IndexGenerator):
    template_name = 'tag_index.html'

    def get_objects(self, tokens):
        tags = [
            tag['tag']
            for tag in 
                self.flourish.get_valid_filters_for_tokens(['tag'])
        ]
        self.source_objects = sorted(tags)


class MostRecentFirstMixin:
    order_by = '-published'


class TagIndex(MostRecentFirstMixin, base.IndexGenerator):
    template_name = 'tag.html'


class Homepage(MostRecentFirstMixin, base.IndexGenerator):
    template_name = 'homepage.html'
    sources_exclude = {'noindex': True}
    # limit = 20


class NewPosts(base.IndexGenerator):
    template_name = 'base_template.html'
    order_by = 'published'

    def get_objects(self, tokens):
        objects = super().get_objects(tokens)
        if objects.count() == 0:
            raise self.DoNotGenerate
        return objects


class BaseIndex(base.IndexGenerator):
    template_name = 'base_template.html'
    order_by = 'published'


class Subject(BaseIndex):
    pass


class SubjectTopic(BaseIndex):
    pass


class FixMe(NewPosts):
    sources_filter = {'fixme__set': '', 'draft__unset': ''}


class Drafts(NewPosts):
    sources_filter = {'draft__set': ''}


class Archives(base.IndexGenerator):
    template_name = 'archives.html'


class NotFound(base.StaticGenerator):
    template_name = 'base_template.html'


def global_context(self):
    return {
        'publication_range': helpers.publication_range(self),
        'publication_dates': self.publication_dates,
        'fixme_set': self.sources.filter(fixme__set='', draft__unset=''),
        'draft_set': self.sources.filter(draft__set=''),
    }

GLOBAL_CONTEXT = global_context

TEMPLATE_FILTERS = {
    'ordinal': filters.ordinal,
    'month_name': filters.month_name,
    'linebreaks': linebreaks,
    'urlise': urlize,
    'pluralise': pluralize,
}


PATHS = (
    sass.SassGenerator(
        path = '/css/#sass_source.css',
        name = 'css',
    ),
    Homepage(
        path = '/',
        name = 'homepage',
    ),
    Archives(
        path = '/archives',
        name = 'archives',
    ),
    calendar.CalendarYearGenerator(
        path = '/#year/',
        name = 'year-index',
    ),
    calendar.CalendarMonthGenerator(
        path = '/#year/#month/',
        name = 'month-index',
    ),
    calendar.CalendarDayGenerator(
        path = '/#year/#month/#day/',
        name = 'day-index',
    ),
    AllTagsIndex(
        path = '/tags/',
        name = 'tags-index',
    ),
    TagIndex(
        path = '/tags/#tag/',
        name = 'tags-tag-index',
    ),
    base.SourceGenerator(
        path = '/#slug',
        name = 'source',
    ),
    Subject(
        path = '/#subject/',
        name = 'subject-index',
    ),
    SubjectTopic(
        path = '/#subject/#topic/',
        name = 'subject-topic-index',
    ),
    FixMe(
        path = '/fixme',
        name = 'fixme',
    ),
    Drafts(
        path = '/drafts',
        name = 'drafts',
    ),
    NotFound(
        path = '/404',
        name = 'not-found',
    ),
)
