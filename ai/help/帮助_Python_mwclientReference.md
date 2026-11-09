# 帮助:Python/mwclientReference

来源：https://www.huijiwiki.com/wiki/%E5%B8%AE%E5%8A%A9%3APython/mwclientReference
revid：34762 · 抓取时间：2026-11-09T14:27:10+08:00

---


==Site==
<code>classmwclient.client.Site(host, path='/w/', ext='.php', pool=None, retry_timeout=30, max_retries=25, wait_callback=<function Site.<lambda>>, clients_useragent=None, max_lag=3, compress=True, force_login=True, do_init=True, httpauth=None, reqs=None, consumer_token=None, consumer_secret=None, access_token=None, access_secret=None, client_certificate=None, custom_headers=None, scheme='https')</code>
:A MediaWiki site identified by its hostname.

<pre>>>> import mwclient
>>> site = mwclient.Site('en.wikipedia.org')</pre>

Do not include the leading “http://”.

Mwclient assumes that the script path (where index.php and api.php are located) is ‘/w/’. If the site uses a different script path, you must specify this (path must end in a ‘/’).

'''Examples'''

<pre>>>> site = mwclient.Site('vim.wikia.com', path='/')
>>> site = mwclient.Site('sourceforge.net', path='/apps/mediawiki/mwclient/')
allcategories(start=None, prefix=None, dir='ascending', limit=None, generator=True, end=None)</pre>
:Retrieve all categories on the wiki as a generator.

<code>allimages(start=None, prefix=None, minsize=None, maxsize=None, limit=None, dir='ascending', sha1=None, sha1base36=None, generator=True, end=None)</code>
:Retrieve all images on the wiki as a generator.

<code>alllinks(start=None, prefix=None, unique=False, prop='title', namespace='0', limit=None, generator=True, end=None)</code>
:Retrieve a list of all links on the wiki as a generator.

<code>allpages(start=None, prefix=None, namespace='0', filterredir='all', minsize=None, maxsize=None, prtype=None, prlevel=None, limit=None, dir='ascending', filterlanglinks='all', generator=True, end=None)</code>
:Retrieve all pages on the wiki as a generator.

<code>allusers(start=None, prefix=None, group=None, prop=None, limit=None, witheditsonly=False, activeusers=False, rights=None, end=None)</code>
:Retrieve all users on the wiki as a generator.

<code>api(action, http_method='POST', *args, **kwargs)</code>
:Perform a generic API call and handle errors.

All arguments will be passed on.

'''Example'''

To get coordinates from the GeoData MediaWiki extension at English Wikipedia:

<pre>>>> site = Site('en.wikipedia.org')
>>> result = site.api('query', prop='coordinates', titles='Oslo|Copenhagen')
>>> for page in result['query']['pages'].values():
...     if 'coordinates' in page:
...         print '{} {} {}'.format(page['title'],
...             page['coordinates'][0]['lat'],
...             page['coordinates'][0]['lon'])
Oslo 59.95 10.75
Copenhagen 55.6761 12.5683</pre>

'''Returns''':	The raw response from the API call, as a dictionary.

<code>ask(query, title=None)</code>
Ask a query against Semantic MediaWiki.

API doc: [https://semantic-mediawiki.org/wiki/Ask_API Ask_API]

'''Returns''':	Generator for retrieving all search results, with each answer as a dictionary. If the query is invalid, an APIError is raised. A valid query with zero results will not raise any error.

'''Examples'''

<pre>>>> query = "[[Category:my cat]]|[[Has name::a name]]|?Has property"
>>> for answer in site.ask(query):
>>>     for title, data in answer.items()
>>>         print(title)
>>>         print(data)</pre>

<code>blocks(start=None, end=None, dir='older', ids=None, users=None, limit=None, prop='id|user|by|timestamp|expiry|reason|flags')</code>
:Retrieve blocks as a generator.

'''Returns''':	
*Generator yielding dicts, each dict containing:
*user: The username or IP address of the user
*id: The ID of the block
*timestamp: When the block was added
*expiry: When the block runs out (infinity for indefinite blocks)
*reason: The reason they are blocked
*allowusertalk: Key is present (empty string) if the user is allowed to
*edit their user talk page
*by: the administrator who blocked the user
*nocreate: key is present (empty string) if the user’s ability to create
*accounts has been disabled.
*Return type:	mwclient.listings.List
*checkuserlog(user=None, target=None, limit=10, dir='older', start=None, end=None)[source]
*Retrieve checkuserlog items as a generator.

<code>chunk_upload(file, filename, ignorewarnings, comment, text)</code>
:Upload a file to the site in chunks.

This method is called by Site.upload if you are connecting to a newer MediaWiki installation, so it’s normally not necessary to call this method directly.

'''Parameters''':	
*file (file-like object) – File object or stream to upload.
*params (dict) – Dict containing upload parameters.

<code>email(user, text, subject, cc=False)</code>
:Send email to a specified user on the wiki.

<pre>>>> try:
...     site.email('SomeUser', 'Some message', 'Some subject')
... except mwclient.errors.NoSpecifiedEmail:
...     print('User does not accept email, or has no email address.')</pre>

'''Parameters''':	
*user (str) – User name of the recipient
*text (str) – Body of the email
*subject (str) – Subject of the email
*cc (bool) – True to send a copy of the email to yourself (default is False)

'''Returns''':	Dictionary of the JSON response

'''Raises''':	
*NoSpecifiedEmail (mwclient.errors.NoSpecifiedEmail) – User doesn’t accept email
*EmailError (mwclient.errors.EmailError) – Other email errors

<code>expandtemplates(text, title=None, generatexml=False)</code>
:Takes wikitext (text) and expands templates.

API doc: [https://www.mediawiki.org/wiki/API:Expandtemplates API:Expandtemplates]

<code>exturlusage(query, prop=None, protocol='http', namespace=None, limit=None)</code>
:Retrieve the list of pages that link to a particular domain or URL,as a generator.This API call mirrors the <code>Special:LinkSearch</code> function on-wiki.

Query can be a domain like ‘bbc.co.uk’. Wildcards can be used, e.g. ‘*.bbc.co.uk’. Alternatively, a query can contain a full domain name and some or all of a URL: e.g. <code>‘*.wikipedia.org/wiki/*’</code>

See [https://meta.wikimedia.org/wiki/Help:Linksearch https://meta.wikimedia.org/wiki/Help:Linksearch] for details.

'''Returns''':	
Generator yielding dicts, each dict containing:
*url: The URL linked to.
*ns: Namespace of the wiki page
*pageid: The ID of the wiki page
*title: The page title.
*Return type:	mwclient.listings.List

<code>get(action, *args, **kwargs)</code>
:Perform a generic API call using GET.

This is just a shorthand for calling api() with http_method=’GET’. All arguments will be passed on.

'''Returns''':	The raw response from the API call, as a dictionary.

<code>logevents(type=None, prop=None, start=None, end=None, dir='older', user=None, title=None, limit=None, action=None)</code>
:Retrieve logevents as a generator.

<code>login(username=None, password=None, cookies=None, domain=None)</code>
:Login to the wiki using a username and password. The method returns nothing if the login was successful, but raises and error if it was not.

'''Parameters''':	
*username (str) – MediaWiki username
*password (str) – MediaWiki password
*cookies (dict) – Custom cookies to include with the log-in request.
*domain (str) – Sends domain name for authentication; used by some MediaWiki plug-ins like the ‘LDAP Authentication’ extension.

'''Raises''':	
*LoginError (mwclient.errors.LoginError) – Login failed, the reason can be obtained from e.code and e.info (where e is the exception object) and will be one of the API:Login errors. The most common error code is “Failed”, indicating a wrong username or password.
*MaximumRetriesExceeded – API call to log in failed and was retried until all retries were exhausted. This will not occur if the credentials are merely incorrect. **See*MaximumRetriesExceeded for possible reasons.
*APIError – An API error occurred. Rare, usually indicates an internal server error.

<code>post(action, *args, **kwargs)</code>
:Perform a generic API call using POST.

This is just a shorthand for calling api() with http_method=’POST’. All arguments will be passed on.

'''Returns''':	The raw response from the API call, as a dictionary.

<code>random(namespace, limit=20)</code>
:Retrieve a generator of random pages from a particular namespace.

limit specifies the number of random articles retrieved. namespace is a namespace identifier integer.

Generator contains dictionary with namespace, page ID and title.

<code>raw_api(action, http_method='POST', *args, **kwargs)</code>
:Send a call to the API.

<code>raw_call(script, data, files=None, retry_on_error=True, http_method='POST')</code>
:Perform a generic request and return the raw text.

In the event of a network problem, or a HTTP response with status code 5XX, we’ll wait and retry the configured number of times before giving up if retry_on_error is True.

requests.exceptions.HTTPError is still raised directly for HTTP responses with status codes in the 4XX range, and invalid HTTP responses.

'''Parameters''':	
*script (str) – Script name, usually ‘api’.
*data (dict) – Post data
*files (dict) – Files to upload
*retry_on_error (bool) – Retry on connection error
*http_method (str) – The HTTP method, defaults to ‘POST’

'''Returns''':	
The raw text response.

<code>raw_index(action, http_method='POST', *args, **kwargs)</code>
:Sends a call to index.php rather than the API.

<code>recentchanges(start=None, end=None, dir='older', namespace=None, prop=None, show=None, limit=None, type=None, toponly=None)</code>
:List recent changes to the wiki, à la Special:Recentchanges.

<code>revisions(revids, prop='ids|timestamp|flags|comment|user')</code>
:Get data about a list of revisions.

See also the <code>Page.revisions()</code> method.

API doc: [https://www.mediawiki.org/wiki/API:Revisions https://www.mediawiki.org/wiki/API:Revisions]

Example: Get revision text for two revisions:

<pre>>>> for revision in site.revisions([689697696, 689816909], prop='content'):
...     print revision['*']</pre>

'''Parameters''':	
*revids (list) – A list of (max 50) revisions.
*prop (str) – Which properties to get for each revision.

'''Returns''':	A list of revisions

<code>search(search, namespace='0', what=None, redirects=False, limit=None)</code>
:Perform a full text search.

API doc: [https://www.mediawiki.org/wiki/API:Search https://www.mediawiki.org/wiki/API:Search]

'''Example'''

<pre>>>> for result in site.search('prefix:Template:Citation/'):
...     print(result.get('title'))</pre>

'''Parameters''':	
*search (str) – The query string
*namespace (int) – The namespace to search (default: 0)
*what (str) – Search scope: ‘text’ for fulltext, or ‘title’ for titles only. Depending on the search backend, both options may not be available. For instance CirrusSearch doesn’t support ‘title’, but instead provides an “intitle:” query string filter.
*redirects (bool) – Include redirect pages in the search (option removed in MediaWiki 1.23).

'''Returns''':	Search results iterator

'''Return type''':	mwclient.listings.List

<code>upload(file=None, filename=None, description=<nowiki>''</nowiki>, ignore=False, file_size=None, url=None, filekey=None, comment=None)</code>
:Upload a file to the site.

Note that one of file, filekey and url must be specified, but not more than one. For normal uploads, you specify file.

'''Parameters''':	
*file (str) – File object or stream to upload.
*filename (str) – Destination filename, don’t include namespace prefix like ‘File:’
*description (str) – Wikitext for the file description page.
*ignore (bool) – True to upload despite any warnings.
*file_size (int) – Deprecated in mwclient 0.7
*url (str) – URL to fetch the file from.
*filekey (str) – Key that identifies a previous upload that was stashed temporarily.
*comment (str) – Upload comment. Also used as the initial page text for new files if description is not specified.

'''Example'''

<pre>>>> client.upload(open('somefile', 'rb'), filename='somefile.jpg',
                  description='Some description')</pre>
                  
'''Returns''':	
JSON result from the API.

'''Raises''':	
*errors.InsufficientPermission
*requests.exceptions.HTTPError


<code>usercontributions(user, start=None, end=None, dir='older', namespace=None, prop=None, show=None, limit=None, uselang=None)</code>
:List the contributions made by a given user to the wiki.

API doc: [https://www.mediawiki.org/wiki/API:Usercontribs https://www.mediawiki.org/wiki/API:Usercontribs]

<code>users(users, prop='blockinfo|groups|editcount')</code>
:Get information about a list of users.

API doc: [https://www.mediawiki.org/wiki/API:Users https://www.mediawiki.org/wiki/API:Users]

<code>staticversion_tuple_from_generator(string, prefix='MediaWiki ')</code>
:Return a version tuple from a MediaWiki Generator string.

'''Example'''

“MediaWiki 1.5.1” → (1, 5, 1)

'''Parameters''':	prefix (str) – The expected prefix of the string

<code>watchlist(allrev=False, start=None, end=None, namespace=None, dir='older', prop=None, show=None, limit=None)</code>
:List the pages on the current user’s watchlist.

API doc: [https://www.mediawiki.org/wiki/API:Watchlist https://www.mediawiki.org/wiki/API:Watchlist]

==Page==
<code>classmwclient.page.Page(site, name, info=None, extra_properties=None)</code>
<code>append(text, summary=<nowiki>''</nowiki>, minor=False, bot=True, section=None, **kwargs)</code>

Append text to a section or the whole page by performing an edit operation.

<code>backlinks(namespace=None, filterredir='all', redirect=False, limit=None, generator=True)</code>
:List pages that link to the current page, similar to Special:Whatlinkshere.

API doc: https://www.mediawiki.org/wiki/API:Backlinks

<code>can(action)</code>
:Check if the current user has the right to carry out some action with the current page.

'''Example'''

<pre>>>> page.can('edit')
True</pre>

<code>categories(generator=True, show=None)</code>
:List categories used on the current page.

API doc: https://www.mediawiki.org/wiki/API:Categories

Parameters:	
generator (bool) – Return generator (Default: True)
show (str) – Set to ‘hidden’ to only return hidden categories or ‘!hidden’ to only return non-hidden ones.
Returns:	
mwclient.listings.PagePropertyGenerator

delete(reason='', watch=False, unwatch=False, oldimage=False)[source]
Delete page.

If user does not have permission to delete page, an InsufficientPermission exception is raised.

edit(text, summary='', minor=False, bot=True, section=None, **kwargs)[source]
Update the text of a section or the whole page by performing an edit operation.

embeddedin(namespace=None, filterredir='all', limit=None, generator=True)[source]
List pages that transclude the current page.

API doc: https://www.mediawiki.org/wiki/API:Embeddedin

Parameters:	
namespace (int) – Restricts search to a given namespace (Default: None)
filterredir (str) – How to filter redirects, either ‘all’ (default), ‘redirects’ or ‘nonredirects’.
limit (int) – Maximum amount of pages to return per request
generator (bool) – Return generator (Default: True)
Returns:	
Page iterator

Return type:	
mwclient.listings.List

extlinks()[source]
List external links from the current page.

API doc: https://www.mediawiki.org/wiki/API:Extlinks

images(generator=True)[source]
List files/images embedded in the current page.

API doc: https://www.mediawiki.org/wiki/API:Images

iwlinks()[source]
List interwiki links from the current page.

API doc: https://www.mediawiki.org/wiki/API:Iwlinks

langlinks(**kwargs)[source]
List interlanguage links from the current page.

API doc: https://www.mediawiki.org/wiki/API:Langlinks

links(namespace=None, generator=True, redirects=False)[source]
List links to other pages from the current page.

API doc: https://www.mediawiki.org/wiki/API:Links

move(new_title, reason='', move_talk=True, no_redirect=False)[source]
Move (rename) page to new_title.

If user account is an administrator, specify no_redirect as True to not leave a redirect.

If user does not have permission to move page, an InsufficientPermission exception is raised.

prepend(text, summary='', minor=False, bot=True, section=None, **kwargs)[source]
Prepend text to a section or the whole page by performing an edit operation.

purge()[source]
Purge server-side cache of page. This will re-render templates and other dynamic content.

redirects_to()[source]
Get the redirect target page, or None if the page is not a redirect.

resolve_redirect()[source]
Get the redirect target page, or the current page if its not a redirect.

revisions(startid=None, endid=None, start=None, end=None, dir='older', user=None, excludeuser=None, limit=50, prop='ids|timestamp|flags|comment|user', expandtemplates=False, section=None, diffto=None, slots=None, uselang=None)[source]
List revisions of the current page.

API doc: https://www.mediawiki.org/wiki/API:Revisions

Parameters:	
startid (int) – Revision ID to start listing from.
endid (int) – Revision ID to stop listing at.
start (str) – Timestamp to start listing from.
end (str) – Timestamp to end listing at.
dir (str) – Direction to list in: ‘older’ (default) or ‘newer’.
user (str) – Only list revisions made by this user.
excludeuser (str) – Exclude revisions made by this user.
limit (int) – The maximum number of revisions to return per request.
prop (str) – Which properties to get for each revision, default: ‘ids|timestamp|flags|comment|user’
expandtemplates (bool) – Expand templates in rvprop=content output
section (int) – Section number. If rvprop=content is set, only the contents of this section will be retrieved.
diffto (str) – Revision ID to diff each revision to. Use “prev”, “next” and “cur” for the previous, next and current revision respectively.
slots (str) – The content slot (Mediawiki >= 1.32) to retrieve content from.
uselang (str) – Language to use for parsed edit comments and other localized messages.
Returns:	
Revision iterator

Return type:	
mwclient.listings.List

save(*args, **kwargs)[source]
Alias for edit, for maintaining backwards compatibility.

templates(namespace=None, generator=True)[source]
List templates used on the current page.

API doc: https://www.mediawiki.org/wiki/API:Templates

text(section=None, expandtemplates=False, cache=True, slot='main')[source]
Get the current wikitext of the page, or of a specific section.

If the page does not exist, an empty string is returned. By default, results will be cached and if you call text() again with the same section and expandtemplates the result will come from the cache. The cache is stored on the instance, so it lives as long as the instance does.

Parameters:	
section (int) – Section number, to only get text from a single section.
expandtemplates (bool) – Expand templates (default: False)
cache (bool) – Use in-memory caching (default: True)
touch()[source]
Perform a “null edit” on the page to update the wiki’s cached data of it. This is useful in contrast to purge when needing to update stored data on a wiki, for example Semantic MediaWiki properties or Cargo table values, since purge only forces update of a page’s displayed values and not its store.

classmwclient.listing.Category(site, name, info=None, namespace=None)[source]

==image==
Image
classmwclient.image.Image(site, name, info=None)[source]
download(destination=None)[source]
Download the file. If destination is given, the file will be written directly to the stream. Otherwise the file content will be stored in memory and returned (with the risk of running out of memory for large files).

Recommended usage:

>>> with open(filename, 'wb') as fd:
...     image.download(fd)
Parameters:	destination (file object) – Destination file
duplicatefiles(limit=None)[source]
List duplicates of the current file.

API doc: https://www.mediawiki.org/wiki/API:Duplicatefiles

imagehistory()[source]
Get file revision info for the given file.

API doc: https://www.mediawiki.org/wiki/API:Imageinfo

imageusage(namespace=None, filterredir='all', redirect=False, limit=None, generator=True)[source]
List pages that use the given file.

API doc: https://www.mediawiki.org/wiki/API:Imageusage
