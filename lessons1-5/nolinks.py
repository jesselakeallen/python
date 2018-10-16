#page =('<div id="top_bin"><div id="top_content" class="width960">'
#'<div class="udacity float-left"><a href="http://udacity.com">')
page = 'tacobell'
def get_next_target(s):
    start_link = s.find('<a href="')
    print start_link
    if start_link != -1:
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote+1)
	url = s[start_quote+1:end_quote]
	return url, end_quote
    else:
	url = None
	end_quote = 0
	return url, end_quote
url, endpos = get_next_target(page)

print url, endpos
