
# Lists and Maps Lab

### Introduction

Ok, so now that we have a sense of how to read from a list and alter a list in Python, let's see how our knowledge of lists can help us in creating data visualizations by plotting maps. 

### Working with lists and maps

As we know, lists are used to store a collection of data.  In describing a city, we can use lists to organize our data in all sorts of ways.  For example, here is a list of neighborhoods in the city of Buenos Aires.


```python
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
```

> Press shift + enter on this cell and all following code cells.

Select the first element of the list, and assign it to the variable `palermo`.


```python
palermo = None
```

Select the last element of the list, and assign it to the variable la_boca.


```python
la_boca = None
```

Beyond the neighborhoods, another thing that we can think of representing as a collection are the coordinates of a city, latitude and longitude.  The first attribute is latitude and the second is longitude.


```python
coordinates = [-34.6037, -58.3816]
```

Set the latitude of Buenos Aires equal to `ba_latitude` and set the longitude to be Buenos Aires to be `ba_longitude`.


```python
ba_latitude = None
```


```python
ba_longitude = None
```

Now let's see if we can display this as a map.

First we download a mapping library with `pip`. Remember a library is simply a tool comprised of code hosted somewhere else on the internet and which we download to use in our current project. Pip is another tool that allows us to easily download various Python libraries from the Internet.  


```python
!pip install folium
```

Press shift + enter on the above code, and our `folium` library is available to us.  Now we just tell Python that we will be using `folium` in our codebase by writing `import folium` in the next cell. Once the import is complete we will be able to display some maps with the help of `folium`.


```python
import folium
buenos_map = folium.Map([-34.6037, -58.3816])
buenos_map
```

All of that from a couple of lines of code.  Let's understand it:

```python
import folium
buenos_map = folium.Map([-34.6037, -58.3816])
buenos_map
```

> [Folium](https://github.com/python-visualization/folium) is a mapping library built on Python.  We created a representation of a map, by referencing the `folium.Map` function and passing through a list.  That list represents the latitude and longitude, just like we saw previously.  The map object is stored as the variable `buenos`.  Since `buenos` is the last line of a cell, the map is displayed.

Now we can also add a marker to this map.


```python
buenos_marker = folium.Marker([-34.6037, -58.3816])
buenos_marker.add_to(buenos_map)
```




    <folium.map.Marker at 0x109767208>



So we used the `folium` library to create a marker.  We specified the coordinates of the marker as a list. Finally, we added the marker to our map with the `add_to` function.

Let's see our updated map!  We see our map simply by referencing our `buenos_map` variable.


```python
buenos_map
```

Great! Note that both the map object and the map marker are just stored as variables.


```python
buenos_marker
```




    <folium.map.Marker at 0x109767208>



And just like any other piece of
data in Python, we can place this marker in a list, and then retrieve it from the list.


```python
buenos_markers = [buenos_marker]
```


```python
buenos_markers[0]
```




    <folium.map.Marker at 0x109767208>



Here are some other markers to add to our map:


```python
neighborhood_markers = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
marker_one = folium.Marker([-34.5711, -58.4233])
marker_two = folium.Marker([-34.5895, -58.3974])
marker_three = folium.Marker([-34.6212, -58.3731])
marker_four = folium.Marker([-34.6177, -58.3621])
marker_five = folium.Marker([-34.603722,  -58.381592])
marker_six = folium.Marker([-34.6345, -58.3631])
neighborhood_markers = [marker_one, marker_two, marker_three, marker_four, marker_five, marker_six]
```

Select the last marker and assign it equal to `la_boca_marker`.


```python
la_boca_marker = None
```


```python
import folium
buenos_map = folium.Map([-34.6037, -58.3816], zoom_start = 12)
la_boca_marker.add_to(buenos_map)
buenos_map
```

Now that we plotted `la_boca` we don't need the marker anymore.  So remove this last element from our `neighborhood_markers` list.


```python
neighborhood_markers.pop()
```




    <folium.map.Marker at 0x109865e80>




```python
print(len(neighborhood_markers)) # 6
print(neighborhood_markers[-1] == marker_five) # True
```

Now select the second marker in the list and set that equal to `recoleta`.


```python
recoleta = None
```


```python
buenos_map = folium.Map([-34.6037, -58.3816], zoom_start = 12)
recoleta.add_to(buenos_map)
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
