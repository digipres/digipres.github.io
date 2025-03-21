#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
# To produce a table summary of contributions to MediaWiki installations,
# 
# * COPTR, i.e. since c. November 2013
# * File Formats
# * DPC?
# 

from __future__ import print_function
import os
import sys
import re
import pprint
import string
import sys
import collections
import datetime
import yaml

import pywikibot as pywikibot

def RecentChangesPageGenerator(start=None, end=None, reverse=False,
                               namespaces=None, pagelist=None,
                               changetype=None, showMinor=None,
                               showBot=None, showAnon=None,
                               showRedirects=None, showPatrolled=None,
                               topOnly=False, step=None, total=None,
                               user=None, excludeuser=None, site=None):

    """
    Generate pages that are in the recent changes list.

    @param start: Timestamp to start listing from
    @type start: pywikibot.Timestamp
    @param end: Timestamp to end listing at
    @type end: pywikibot.Timestamp
    @param reverse: if True, start with oldest changes (default: newest)
    @type reverse: bool
    @param pagelist: iterate changes to pages in this list only
    @param pagelist: list of Pages
    @param changetype: only iterate changes of this type ("edit" for
        edits to existing pages, "new" for new pages, "log" for log
        entries)
    @type changetype: basestring
    @param showMinor: if True, only list minor edits; if False, only list
        non-minor edits; if None, list all
    @type showMinor: bool or None
    @param showBot: if True, only list bot edits; if False, only list
        non-bot edits; if None, list all
    @type showBot: bool or None
    @param showAnon: if True, only list anon edits; if False, only list
        non-anon edits; if None, list all
    @type showAnon: bool or None
    @param showRedirects: if True, only list edits to redirect pages; if
        False, only list edits to non-redirect pages; if None, list all
    @type showRedirects: bool or None
    @param showPatrolled: if True, only list patrolled edits; if False,
        only list non-patrolled edits; if None, list all
    @type showPatrolled: bool or None
    @param topOnly: if True, only list changes that are the latest revision
        (default False)
    @type topOnly: bool
    @param user: if not None, only list edits by this user or users
    @type user: basestring|list
    @param excludeuser: if not None, exclude edits by this user or users
    @type excludeuser: basestring|list

    """

    if site is None:
        site = pywikibot.Site()
    for item in site.recentchanges(start=start, end=end, reverse=reverse,
                                   namespaces=namespaces, pagelist=pagelist,
                                   changetype=changetype, showMinor=showMinor,
                                   showBot=showBot, showAnon=showAnon,
                                   showRedirects=showRedirects,
                                   showPatrolled=showPatrolled,
                                   topOnly=topOnly, step=step, total=total,
                                   user=user, excludeuser=excludeuser):
        yield(item)

def month_diff(d1, d2): 
    """Return the number of months between d1 and d2, 
    such that d2 + month_diff(d1, d2) == d1
    """
    diff = (12 * d1.year + d1.month) - (12 * d2.year + d2.month)
    return diff

# Process the arguments:
pywikibot.handleArgs()

FIRST_TEXT_SIZE = 256

def enumerate_ff_formats(site):
    template = pywikibot.Page(site,"Template:FormatInfo")
    source = {}
    source['stats'] = {}
    formats = []
    total_formats = 0
    total_w_extension = 0
    total_w_pronom = 0
    total_w_fdd = 0
    total_w_mimetype = 0
    total_w_egff = 0
    total_w_uti = 0
    for page in site.page_embeddedin(template):
        # Check if it's an electronic file format:
        # Doesn't really work because Programming Languages are not also classes as EFFs
#        eff = False
#        for cat in page.categories():
#            if cat.title() == "Category:Electronic File Formats":
#                eff = True
#        if not eff:
#            print("Skipping page '%s' as it is not categorised as an electronic file format." % page.title())
#            continue
        # Pick out the useful data:
        fmt = {}
        fmt['name'] = page.title()
        fmt['source'] = page.title(as_url=True)
        fmt['pageStartText'] = page.text
        # String Macros:
        fmt['pageStartText'] = re.sub('\{\{.*\}\}', '', fmt['pageStartText'], flags=re.DOTALL)
        fmt['pageStartText'] = re.sub('\s+', ' ', fmt['pageStartText'], flags=re.MULTILINE).strip()
        # Trim:
        if len(fmt['pageStartText']) > FIRST_TEXT_SIZE:
            fmt['pageStartText'] = fmt['pageStartText'][:FIRST_TEXT_SIZE] + '...'

        def add_ar(fmt, key, values):
            for param in values:
                fmt[key] = fmt.get(key, [])
                fmt[key].append(param)

        # Store the categories:
        for cat in page.categories():
            add_ar(fmt, 'categories', [cat.title().replace('Category:','')])

        # Loop through templates:
        for t in page.templatesWithParams():
            if t[0].title() == "Template:Ext":
                add_ar(fmt, 'extensions', t[1])
                total_w_extension += 1

            elif t[0].title() == "Template:Mimetype":
                add_ar(fmt, 'mimetypes', t[1])
                total_w_mimetype += 1

            elif t[0].title() == "Template:PRONOM":
                add_ar(fmt, 'pronom', t[1])
                total_w_pronom += 1

            elif t[0].title() == "Template:LoCFDD":
                add_ar(fmt, 'fdd', t[1])
                total_w_fdd += 1

            elif t[0].title() == "Template:EGFF":
                add_ar(fmt, 'egff', t[1])
                total_w_egff += 1

            elif t[0].title() == "Template:UTI":
                add_ar(fmt, 'uti', t[1])
                total_w_uti += 1
            
            elif t[0].title() == "Template:FormatInfo":
                for param in t[1]:
                    if param.startswith('released='):
                        fmt["released"] = param.replace('released=','').strip()

            elif t[0].title() == "Template:Magic":
                fmt['hasMagic'] = True
                add_ar(fmt, 'magic', t[1])
            
            elif t[0].title() == "Template:Type Code":
                add_ar(fmt, 'TypeCode', t[1])
            
            elif t[0].title() == "Template:DexvertSamples":
                add_ar(fmt, 'DexvertSamples', t[1])
            
            elif t[0].title() == "Template:CdTextfiles":
                add_ar(fmt, 'CdTextfiles', t[1])
            
            elif t[0].title() == "Template:Wikidata":
                add_ar(fmt, 'wikidata', t[1])
            
            elif t[0].title() == "Template:SACFTPURL":
                add_ar(fmt, 'SACFTPURL', t[1])
            else:
                print("Unrecognised template: "+str(t))
        total_formats += 1
        if total_formats % 20 == 0:
            print("Processed %s format pages..." % total_formats)
            # For debugging:
            #break
        formats.append(fmt)

    # And write out:
    source['formats'] = formats
    source['stats']['total_formats'] = total_formats
    source['stats']['total_w_egff'] = total_w_egff
    source['stats']['total_w_fdd'] = total_w_fdd
    source['stats']['total_w_pronom'] = total_w_pronom
    source['stats']['total_w_mimetype'] = total_w_mimetype
    source['stats']['total_w_extension'] = total_w_extension
    source['stats']['total_w_uti'] = total_w_uti
    source['source_prefix'] = "http://fileformats.archiveteam.org/wiki/"
    with open("digipres.github.io/_sources/registries/mediawikis/ffw.yml", 'w') as outfile:
        outfile.write( yaml.safe_dump(source, default_flow_style=False) ) 


# Process a site:
def contribs(fam):
    # Set up the site
    pywikibot.config.family = fam
    site = pywikibot.Site()

    enumerate_ff_formats(site)

# Process contributions from FileFormats:
contribs("ff")

# Process contributions from COPTR:
#contribs("coptr")


