started 6-29-17
nat ventura

I'm following along with this pygame rpg tutorial
by someone called 'Meloonatic Melons' on Youtube.
-- https://www.youtube.com/watch?v=C-z9nUttMcI

I'm trying to clean up a lot of the code and global variables
along the way, but it's pretty slow-going.

I haven't even gotten to making a little protagonist character yet,
but my terrain builder map_maker.py is pretty cool when it works.

I'm having issues accessing the tuples in my two-dimensional lists
of terrain coordinates though, which means my terrain isn't "refreshing"
as a new terrain with different painted textures.

But the window is definitely blinking a lot and the fps is really low?
So at least something's happening.

I know there's definitely multiple ways to access tuples from a list..
I tried the operator.attrgetter, and def `__getitem__`
but I don't think I followed through with either of them the right way?
Like fed my list in and got the outputs out correctly?

Stack Overflow people's explanations of list comprehension
were also a bit confusing, but hopefully will make sense soon.

xNV