var map = L.map('mapid').setView({lon: 90.412, lat: 23.810}, 11.1);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map);


$.ajax({
    type: "GET",
    url: `http://127.0.0.1:5000/find_path/${source}/${destination}`,
})
    .done(function (Response) {
        console.log(Response);
        latlngs = Response['path'];
        var polyline = L.polyline(latlngs, {color: 'black', weight: 5}).addTo(map);

        var source_circle = L.circle(latlngs[0], {
            color: 'pink',
            fillColor: 'lightpink',
            fillOpacity: 0.5,
            radius: 450
        }).addTo(map);

        var destination_circle = L.circle(latlngs[latlngs.length - 1], {
            color: 'green',
            fillColor: 'lightgreen',
            fillOpacity: 0.5,
            radius: 450
        }).addTo(map);
    })
    .fail(function (Response) {
    });


