# Crawl.

Recursively crawls a given url or urls. Will loop indefinitely (by default) until all links with the same base url are crawled. Links with a different base url are not crawled but their HTTP status code is checked.

## Requirements

* Python 2.7 or >3.3
* QT
* Xvfb

## Install

**OS X**

    brew install qt
    pip install git+https://github.com/local-projects/crawl.git

If you get an error, run `xcode-select --install` and retry.

**Debian based Distros (including Ubuntu)**

    apt-get install qt5-default libqt5webkit5-dev libxslt1-dev xvfb
    pip install git+https://github.com/local-projects/crawl.git

## Usage

    crawl <url>... [options]

## Options

`--depth=<level>`
Recursive depth to check. Must be an integer greater than or equal to 0. 0 checks the given page, 1 checks one page deep, etc. If not set, depth is unlimited.

`--exclude=<regex>`
Regular Expression that, if matched, skips the link regardless of domain. Matches against the full url,  including http scheme.

`--include=<regex>`
If set, domain based logic is ignored. Instead links matching this regex will be recursively crawled. Links not matching the regex will still have their HTTP status code checked. Matches against the full url, including the http scheme.

`--check-images`
If set, HTTP status codes for images will be pulled.

`--save-images=<path>`
If set, images will be downloaded and saved into the given path. Will be saved into subdirectories matching the downloaded image's path. Supports large files.

`--screenshot=<path>`
If set, a screenshot for each page crawled will be saved to the path specified.

`--width=<int>`
Used in conjunction with --screenshot. Sets the viewport width. Defaults to 1366 if not set.

`--height=<int>`
Used in conjunction with --screenshot. Sets the viewport height. Defaults to the full rendered page height if left blank.

`--execute=<program>`
If set, the given string specifying a shell command will be run with the page source (after executed by a javascript engine) used as input. Runs for each page crawled. Output is sent to stdout.

`--print-status=<regex>`
If set, URLs with an http status code matching the regex will have the url printed. [default: .*]

`--wait=<seconds>`
Used to allow ajax feeds to load into the DOM since I can't find a better way to detect it yet. Only needed on ajax heavy sites. Defaults to the site-specified crawl delay if given by the site (and robots.txt is not ignored). 0 if not. Setting this overrides any site specified delays.

`--http-basic=<user:pass>`
If a site is behind HTTP Basic Authentication, give the username and password separated by a colon.

`--ignore-robots`
If set, the robots.txt file will be ignored. It is enforced by default.

`--version`
Show version.

`-h --help`
Show this screen.

## Examples

Crawl an entire website, printing bad links.

    crawl http://www.localprojects.com --print-status='(?!200)'

Crawl an entire website, printing bad links while ignoring 'mailto' and 'tel' links.

    crawl http://www.localprojects.com --print-status='(?!200)' --exclude='^(mailto|tel).*'

Crawl an entire website, printing bad links and bad images.

    crawl http://www.localprojects.com --print-status='(?!200)' --check-images

Crawl mulitple sites.

    crawl http://www.localprojects.com http://www.brookfieldplaceny.com

Take a screenshot of a single page using full rendered height, into the current directory.

    crawl http://www.localprojects.com/news --depth=0 --screenshot=.

Crawl an entire website, excluding all https links

    crawl http://www.localprojects.com --exclude='^https.*'

Crawl an entire website, ignoring all pages behind a particular path

    crawl http://www.localprojects.com --exclude='http://www.localprojects.com/project/.*'

Crawl based on a regex instead of base url. The given url is the starting point. 

    crawl http://www.localprojects.com --include='https?://(.*?\.)?localprojects\.(com|net).*'

Crawl an entire website, outputting the number of times "Jake Barton" is used on each page.

    crawl http://www.localprojects.com --execute='grep -c "Jake Barton"'

Crawl an entire website, printing the post-javascript evaluated html for each page.

    crawl http://www.localprojects.com --execute='cat'

Crawl an entire website that's behind http basic authentication.

    crawl http://www.localprojects.com --http-basic="<username>:<password>"

## TODO

* Graph visualization of site (a visual site map)
* Full backup of site (downloads all html/css/js/images/video. Ie, generates a static version of the site)
* Multiple threads with user-specified amount (defaulting to 1)
* Better ajax loading detection (can currently just wait a set time per page)
