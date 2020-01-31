
# Lists and Maps Lab

### Introduction

Ok, so now that we have a sense of how to read from and alter a list in Python, let's see how our knowledge of lists can help us in creating data visualizations by plotting maps.

### Working with lists and maps

As we know, lists are used to store a collection of data.  In describing a city, we can use lists to organize our data in all sorts of ways.  For example, here is a list of neighborhoods in the city of Buenos Aires.


```python
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
```

> Press shift + enter on this cell and all following code cells.

Assign the variable `palermo` to the first element of the `neighborhoods` list.


```python
palermo = None
palermo = neighborhoods[0]
```

Now assign the variable `la_boca` to the last element of our list.


```python
la_boca = None
la_boca = neighborhoods[-1]
```

Beyond the neighborhoods, another thing that we can think of representing as a collection are the coordinates of a city, latitude and longitude.  Below, our `coordinates` list contains the coordinates for Buenos Aires.  The first element is latitude and the second is longitude.


```python
coordinates = [-34.6037, -58.3816]
```

Set `ba_latitude` to equal the latitude of Buenos Aires and set `ba_longitude` to the longitude of Buenos Aires.


```python
ba_latitude = None
ba_latitude = -34.6037
```


```python
ba_longitude = None
ba_longitude = -58.3816
```

Now let's see if we can display this as a map.

First we download a mapping library with `pip`. Remember a library is simply a tool comprised of code hosted somewhere else on the internet and which we download to use in our current project. Pip is another tool that allows us to easily download various Python libraries from the Internet.  


```python
!pip install folium
```

Press shift + enter on the above code, and our `folium` library is available to us.  Now we just tell Python that we will be using `folium` in our codebase by writing `import folium` in the next cell. Once the import is complete we will be able to display some maps with the help of `folium`.


```python
import folium
buenos_map = folium.Map([ba_latitude, ba_longitude])
buenos_map
```

All of that from a couple of lines of code.  Let's understand it:

```python
import folium
buenos_map = folium.Map([ba_latitude, ba_longitude])
buenos_map
```

> [Folium](https://github.com/python-visualization/folium) is a mapping library built on Python.  We created a representation of a map, by referencing the `folium.Map` function and passing through a list.  That list represents the latitude and longitude, just like we saw previously.  The map object is stored as the variable `buenos_map`.  Since `buenos_map` is the last line of a cell, the map is displayed.

Now we can also add a marker to this map.  For now, let's start by adding a marker for our Buenos Aires coordinates.


```python
buenos_marker = folium.Marker([ba_latitude, ba_longitude])
buenos_marker.add_to(buenos_map)
```

So we used the `folium` library to create a marker.  We specified the coordinates of the marker as a list. Finally, we added the marker to our map with the `add_to` function.

Let's see our updated map!  We see our map by referencing our `buenos_map` variable.


```python
buenos_map
```

Great! Note that both the map object and the map marker are just stored as variables.


```python
buenos_marker
```

And just like any other piece of
data in Python, we can place this marker in a list, and then retrieve it from the list.


```python
buenos_markers = [buenos_marker]
```


```python
buenos_markers[0]
```

Recall our `neighborhoods` list from above.  The coordinates in the markers below match the neighborhoods in our `neighborhoods` list, respectively.


```python
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
marker_one = folium.Marker([-34.5711, -58.4233])
marker_two = folium.Marker([-34.5895, -58.3974])
marker_three = folium.Marker([-34.6212, -58.3731])
marker_four = folium.Marker([-34.6177, -58.3621])
marker_five = folium.Marker([-34.603722,  -58.381592])
marker_six = folium.Marker([-34.6345, -58.3631])
neighborhood_markers = [marker_one, marker_two, marker_three, marker_four, marker_five, marker_six]
```

Assign `la_boca_marker` equal to the last marker.


```python
la_boca_marker = None
la_boca_marker = neighborhood_markers[-1]
```

Below, we will rewrite `buenos_map` variable to create a new map of Buenos Aires, but this time we will add `la_boca_marker` to the map and zoom in a bit using the `zoom_start` attribute.


```python
import folium
buenos_map = folium.Map([ba_latitude, ba_longitude], zoom_start = 12)
la_boca_marker.add_to(buenos_map)
buenos_map
```

Now that we plotted `la_boca_marker` we don't need the marker anymore.  So, let's remove this last element from our `neighborhood_markers` list.


```python
neighborhood_markers.pop()
```


```python
print(len(neighborhood_markers)) # 5
print(neighborhood_markers[-1] == marker_five) # True
```

Now assign `recoleta_marker` to the second marker in the `neighborhood_markers` list.  This time, we won't reassign our `buenos_map` so we should expect both `la_boca_marker` and `recoleta_marker` to appear!


```python
recoleta_marker = None
recoleta_marker = neighborhood_markers[1]
```


```python
recoleta_marker.add_to(buenos_map)
buenos_map
```

Don't worry if this feels tedious and manual. When we get up to loops in Python, we will see how to easily plot all of the markers in our list.


```python
for marker in neighborhood_markers:
    marker.add_to(buenos_map)
buenos_map
```

But that's a lesson for another day.

### Summary

In this lesson we saw how to select information from a list and then plot that information with maps.  We saw that lists can make good arguments to methods, as they represent an ordered collection of information, like latitude followed by longitude.  In just a few lessons we saw how to use Python to make visualizations with our data going forward.
