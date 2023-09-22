import webbrowser


# Main function is search_on_engine. It takes in a search term and opens on web browser
# Return string of web status


def search_on_engine(search_term,site):
    # Search the term on a search engine #
    if search_term == '':
        return 'No search term supplied...'
    snippet = ''
    if site in ['google','bing','searchencrypt']:
        snippet = 'search?q='
    elif site in ['duckduckgo']:
        snippet = '?q='
    else:
        snippet = 'search?q='
        site = 'google'
    url = f'https://{site}.com/{snippet}' + search_term
    webbrowser.get().open(url)
    return 'Here is what I found for query: ' + search_term