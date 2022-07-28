#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1


def findAdmin():
        f = open("link.txt","r");
        link = raw_input("Điền tên website \n(ex : example.com hoặc www.example.com ): ")
        print "\n\nLink website: \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "đã được tìm thấy => ",req_link

def Credit():
        Space(9); print " ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂( ☠ )▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂"
        Space(9); print "┃   +++    Admin Login Web    +++    ┃"
        Space(9); print "┃       Được code bởi Phạm Chiến     ┃"
        Space(9); print "┃       The Cyber VieSociety         ┃"
        Space(9); print "┃           t.me/viesociety          ┃"
        Space(9); print "┃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂( ☠ )▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂┃"

Credit()
findAdmin()
