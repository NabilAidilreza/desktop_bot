import urllib.request
import urllib.parse
import re
import webbrowser

# Main function is search_on_YT. It takes in a search term and plays first video on web browser
# Return string of video status

def search_on_YT(search_term):
    # Search and play first yt video found #
    if len(search_term) == 0:
        return 'No search term supplied...'
    word_list = search_term.split()
    reply_string = ''
    if len(word_list) == 1:
        reply_string = word_list[0]
    else:
        reply_string = '+'.join(word_list)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + reply_string)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    webbrowser.get().open(url)
    return "Playing first video on search term: " + search_term + ' on YouTube\n'