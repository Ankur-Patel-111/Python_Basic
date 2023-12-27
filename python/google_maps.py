# open google map enter any location.
import sys,webbrowser
map_string=' '.join(sys.argv[1:])
webbrowser.open('https://www.google.com/maps/place/'+map_string)
