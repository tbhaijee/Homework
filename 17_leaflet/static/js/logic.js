// Adding tile layer
var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    maxZoom: 18,
    id: "mapbox/light-v10",
    accessToken: API_KEY
});

var satmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    maxZoom: 18,
    id: "mapbox/satellite-v9",
    accessToken: API_KEY
});

// Creating map object
var myMap = L.map("map", {
    center: [34.0522, -118.2437],
    zoom: 8,
    layers: [streetmap, satmap]

});
var myboundary = new L.LayerGroup();
var overLays = {
    "Fault Line": myboundary
};
streetmap.addTo(myMap);
// satmap.addTo(myMap);
var typeofMaps = {
    "Street Map": streetmap,
    "Satellite Map": satmap
};
L.control.layers(typeofMaps, overLays).addTo(myMap)

// Load in geojson data
var geoData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var boundary = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json"

console.log(geoData);

var geojson;

// Grab data with d3
d3.json(geoData, function(data) {
    L.geoJson(data, {
        pointToLayer: function(feature, lnglat) {
            return L.circle(lnglat, {
                color: getColor(feature.properties.mag),
                fillOpacity: 0.5,
                radius: (feature.properties.mag) * 2000
            })
        },
        onEachFeature: function(feature, layer) {
            layer.bindPopup("<H3>Location:</h3>" + feature.properties.place + "<h3>Magnitude:</h3> " + feature.properties.mag + "<h3>Date:</h3>" + new Date(feature.properties.time));
        }
    }).addTo(myMap);

});

d3.json(boundary, function(bounddata) {
    L.geoJson(bounddata, {
        color: "orange",
        weight: 3

    }).addTo(myboundary);
    myboundary.addTo(myMap);
})

function getColor(d) {
    return d > 5 ? '#ff3333' :
        d > 4 ? '#ff6633' :
        d > 3 ? '#ff9933' :
        d > 2 ? '#ffcc33' :
        d > 1 ? '#ffff33' :
        '#ccff33';
}

// Add legend to the map
var legend = L.control({ position: 'bottomright' });

legend.onAdd = function(map) {

    var div = L.DomUtil.create('div', 'info legend'),
        mags = [0, 1, 2, 3, 4, 5],
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < mags.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(mags[i] + 1) + '"></i> ' +
            mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(myMap);