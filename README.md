# Project 5
ENGO 551

The purpose of this web application is to allow a user to draw a polyline on the map, and return the simplified polyline using the Turf.js "Simplify" function.
The user can click on the "Draw" button, and use mouse clicks on the map to select the points that join their polyline together. When the "Simplify" button is clicked,
they will be shown the simplified version of their line in a different colour. They can then click the "Delete" button to start over. The "Delete" button can also
by clicked to erase the drawn line prior to simplifying if the user wishes to start over. There is also a help button with a question mark icon that can be clicked
to display a popup with the instructions for using the web app.

index.html -
This is the only page in the application. The headers and styles are set first. In the body, three buttons are made for "Draw", "Delete", and "Simplify". The map
is initialized in the mapbox light style and is centered on Calgary. A popup is created for when users click on the "Help" question mark icon. It contains some
basic instructions for using the application. The question mark icon is created using the leaflet easy button plugin. Colour styles are set for the drawn line and
simplified line layers so the user can distinguish them. When the user first visits the site, only the "Draw" button is enabled (since there is nothing to delete
or simplify yet). They can select "Draw", and then click on the map to select the points that connect their polyline. Each time the mouse is clicked, the latitude
and longitude are added to an array to store the polyline points. The array coordinates are added to a geojson variable, which is added to the layer and then added
to the map. Once the user starts drawing, the "Draw" button becomes diabled and the "Delete" and "Simplify" buttons become enabled. When the user is done drawing
they can click "Simplify" or "Delete". The "Simplify" button will remove the click event listener and add the array of polyline coordinates to a Turf lineString.
Then, Turf Simplify is used on the lineString to return the simplified line. The simplified line is added to a different layer and then added to the map. The
"Simplify" button disables when it is clicked. The "Delete" button also removes the click event listener. It removes all layers from the map and empties the array
of coordinates for the drawn polyline. Clicking the "Delete" button also disables the "Draw" and "Simplify" buttons and enables the "Draw" button.
