from datetime import date
from flourish import filters
from flourish import helpers
from flourish.generators import atom
from flourish.generators import base
from flourish.generators import calendar
from flourish.generators import sass
from flourish.source import SourceFile

from django.utils.html import linebreaks, urlize
from django.template.defaultfilters import (
    capfirst,
    pluralize,
    striptags,
    truncatewords_html,
)
import markdown2


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

    def get_context_data(self):
        context = super().get_context_data()

        # software packages -- get just one entry for each package
        rel = self.flourish.sources\
                    .filter(type='release').order_by('published')
        context['releases'] = {}
        for src in rel:
            context['releases'][src.package] = src

        # youtube videos -- get just one entry per channel
        yt = self.flourish.sources\
                    .filter(origin__contains='youtube').order_by('published')
        context['youtube_videos'] = {}
        for src in yt:
            context['youtube_videos'][src.origin_link_url] = src

        context['latest_photos'] = self.flourish.sources\
                    .filter(type='photo').order_by('-published')[:8]

        context['latest_weeknote'] = self.flourish.sources\
                    .filter(subject='weeknotes').order_by('-published')[0]

        context['github_activities'] = self.flourish.sources\
                    .filter(
                        origin='github', type='repository_activity'
                    ).order_by('-published')[:10]

        context['latest_gifs'] = self.flourish.sources\
                    .filter(origin='gifs').order_by('-published')[:6]

        context['latest_writing'] = self.flourish.sources\
                    .filter(
                        type__in=['article','thread']
                    ).exclude(
                        subject='weeknotes',
                        draft__set='',
                    ).order_by('-published')[:8]

        context['latest_tweets'] = self.flourish.sources\
                    .filter(
                        origin='twitter-cackhanded',
                    ).exclude(
                        type__in=['photo','thread'],
                    ).order_by('-published')[:12]

        context['everything_else'] = self.flourish.sources\
                    .exclude(
                        type__in=['article', 'recipe', 'timeless', 'index-splash'],
                    ).exclude(
                        origin__in=['gifs', 'foursquare', 'instagram', 'github',],
                    ).exclude(
                        origin__contains='youtube',
                    ).exclude(
                        origin__contains='twitter',
                    ).order_by('-published')

        context['fixmes'] = self.flourish.sources\
                    .filter(fixme__set='', draft__unset='')
        context['drafts'] = self.flourish.sources\
                    .filter(draft__set='')

        return context


class SourcePage(base.SourceGenerator):
    def get_objects(self, tokens):
        objects = super().get_objects(tokens)
        # an "index-splash" page is a way of adding text to index pages
        # without having to create endless template fragments
        if objects[0].type == 'index-splash':
            raise self.DoNotGenerate
        return objects


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
    def get_context_data(self):
        context = super().get_context_data()
        try:
            splash = self.current_path[1:] + '_splash'
            context['splash'] = self.flourish.get(splash)
        except SourceFile.DoesNotExist:
            pass
        return context


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


class MnfArticlesFeed(atom.AtomGenerator):
    sources_filter = {'origin': 'mnf', 'type': 'article',}

    def get_feed_title(self):
        return 'marknormanfrancis.com articles'


class FirehoseFeed(atom.AtomGenerator):
    def get_feed_title(self):
        return 'everything marknormanfrancis.com'


def markdown(text):
    return markdown2.markdown(text)


def isoweek_start(isoweek):
    return date.fromisocalendar(isoweek[0], isoweek[1], 1)


def isoweek_end(isoweek):
    return date.fromisocalendar(isoweek[0], isoweek[1], 7)


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
    'markdown': markdown,
    'truncate': truncatewords_html,
    'strip': striptags,
    'capfirst': capfirst,
    'isoweek_start': isoweek_start,
    'isoweek_end': isoweek_end,
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
    SourcePage(
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
    MnfArticlesFeed(
        path = '/index.atom',
        name = 'atom-feed',
    ),
    FirehoseFeed(
        path = '/firehose.atom',
        name = 'firehose-feed',
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
