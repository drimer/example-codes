This is an example of hot to use the libraries Twisted, Tornado and Aiohttp
to perform tasks asynchronously. I wrote these (and adapted a little bit to
my likes) at a talk in EuroPython 2016, given by Anton Caceres.

First we'll start with `twisted_example.py`, which delays all requests 5
seconds. Then, it writes a response depending on the contents of the GET
paramter called "q". To test it, run the following command while running
`python twisted_example.py`:

$ curl localhost:8080

If we leave the twisted server running during the rest of the example, and
run `python aiohttp_example.py`, we'll see that it makes three requests
asynchronously, and prints the results.

The same is done with `python tornado_example.py`.