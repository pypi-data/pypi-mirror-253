"""Web idioms for expressionive.py.

These build on the HTML elements provided by expressionive.py, to
produce some HTML fragments that I might use in several of my
projects."""

import os

from expressionive.expressionive import htmltags as T

def namify(x):
    """Convert a string to a form suitable for use as an anchor name."""
    return x.replace(' ', '_')

def make_name_with_email(name, email):
    """Wrap a name in an email href."""
    return (T.a(href="email:"+email)[name]
            if email and email != ""
            else name)

def row(*things):
    """Returns an untemplated table row for its arguments."""
    return T.table(width="100%")[T.tr[[T.td(valign="top")[thing] for thing in things]]]

def wrap_box(*things):
    """Returns a flex container box contains its arguments."""
    return (T.div(class_='flex-container')[[T.div[thing]
                                            for thing in things
                                            if thing]]
            if any(things)
            else None)

def labelled_section(title, body):
    """Returns a titled version of the body, at h2 level."""
    return T.div[T.h2[title], body] if body else None

def labelled_subsection(title, body):
    """Returns a titled version of the body, at h3 level."""
    return T.div[T.h3[title], body] if body else None

def switchable_panel(switcher_id, panels, labels, order, initial=None, title=None):
    """Return a group of panels, only one of which is displayed at a time.

    - panels is a dictionary binding keys to the panel contents,
    - labels is a dictionary binding the same keys to button labels.
    - order is the order of the keys in the button row,
    - initial is the button to be selected initially.
    """
    return T.table(class_='switcher', id_=switcher_id)[
        T.tr(align="center")[title or switcher_id.title()],
        T.tr(align="center")[T.td[[T.div(class_='choice', name=choice)[panels[choice]]
                                   for choice in order]]],
        T.tr(align="center")[
            T.td[[[T.button(class_=('active'
                                    if choice == initial
                                    else 'inactive'),
                            name=choice, onclick="select_version('%s', '%s')"%(switcher_id, choice))[labels[choice]]]
                  for choice in order]]]]

def linked_image(charts_dir, image_name, label, fallback=None, title=None):
    """Returns a group of image panels each image to a larger version of itself."""
    periods = ('all_time', 'past_year', 'past_quarter', 'past_month', 'past_week')
    return switchable_panel(
        label,
        panels={period: [
            T.div(class_='choice', name=period)[
                (T.a(href="%s-%s-large.png" % (image_name, period))[
                    T.img(src="%s-%s-small.png" % (image_name, period))]
                 # TODO: this isn't right, is it looking in the right directory?
                 if os.path.isfile(os.path.join(charts_dir, "%s-%s-small.png" % (image_name, period)))
                 else fallback or T.p[f"Image set {image_name} not found"])]
        ]
                for period in periods},
        labels={period: period.capitalize().replace('_', ' ') for period in periods},
        order=periods,
        initial='past_quarter',
        title=title)

class SectionalPage:

    """Holder for collecting section to make up a page.
    Each section has an H2 heading, and these are used to make a table of contents.
    Empty sections are not added."""

    def __init__(self):
        self._sections = []

    def add_section(self, title, body):
        if body:
            self._sections.append((title, body))

    def toc(self):
        return [T.h2["Table of contents"],
                T.ul[[T.li[T.a(href="#"+namify(section[0]))[section[0]]]
                      for section in self._sections
                      if section[0]]]]

    def sections(self):
        return [[T.div(class_='section')
                 [(T.h2[T.a(name=namify(section[0]))[section[0]]])
                  if section[0]
                  else [],
                  T.div(class_='sectionbody')[section[1]]]
                 for section in self._sections]]
