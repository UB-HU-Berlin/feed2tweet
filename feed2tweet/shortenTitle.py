#!/usr/bin/python3
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
# Copyright © 2015-2017 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

'''Shorten the title of a feed if it is too long for the tweet'''

#3rd party libraries imports
import feedparser

class shortenTitle(object):
    '''Constructor of shortenTitle class'''
    def __init__(self, elements, entry):
        self.elements = elements
        self.entry = entry
        self.main()
        
    def main(self):
        '''Main of the shortenTitle class'''
        #Max length for title = 140 - 23(link) -1(space between link and Title)
        maxlengthTitle = 116
        #maxlengthTitle - len(' ...')
        slicelength = 112
        #only shorten if it is relevant for the post
        if 'title' in self.elements:
            if(len(self.entry['title']) > maxlengthTitle):
                #Cut out the first 112 characters and append '...'
                tmptitle = self.entry['title'][:slicelength]
                if(tmptitle[:-1] != ' '):
                    newentry = ''
                    tmptitles = tmptitle.split(' ')
                    for i in range(len(tmptitles) - 1):
                        newentry += tmptitles[i] + ' '
                    newentry += '...'
                    self.entry['title'] = newentry
                else:
                    tmptilte += '...'
                    self.entry['title'] = tmptitle 
        
        
    @property
    def shortendtitle(self):
        '''Return the shortend title'''
        return self.entry['title'] 
