from flourish import filters
from flourish import helpers
from flourish.generators import base
from flourish.generators import calendar
from flourish.generators import sass


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


class Archives(base.IndexGenerator):
    template_name = 'archives.html'


def global_context(self):
    return {
        'all_valid_dates': helpers.publication_range(self),
        'publication_dates': self.publication_dates,
    }

GLOBAL_CONTEXT = global_context

TEMPLATE_FILTERS = {
    'ordinal': filters.ordinal,
    'month_name': filters.month_name,
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
)
