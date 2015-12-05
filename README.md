# Crawl

A command line script to crawl websites.

*Usage*

    crawl --help

## Requirements

- python 2.7 or >3.3
- qt

## Install

*OS X*
    brew install qt
    git clone https://github.com/local-projects/crawl.git
    cd crawl
    python setup.py install --record uninstall.txt

## Uninstall

    cat uninstall.txt | xargs rm -rf

## TODO:

- Graph visualization of site (a visual site map)
- Full backup of site (downloads all html/css/js/images/video. Ie, generates a static version of the site)
- Multiple threads with user-specified amount (defaulting to 1)
- Better ajax loading detection (can currently just wait a set time per page)