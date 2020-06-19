// from data.js
var tableData = data;
var tbody = d3.select("tbody");
// var table = d3.select("ufo-table");

// filter.on("click", runEnter);
// // form.on("submit", runEnter);

// YOUR CODE HERE!
tableData.forEach(function(UFO) {
    // console.log(WR)
    var row = tbody.append("tr")
    Object.entries(UFO).forEach(function([key, value]) {
        // console.log(key, value);
        var cell = row.append("td")
        cell.text(value)
    })

});

console.log(tableData);
var button = d3.select("#filter-btn");
var form = d3.select("#form");
button.on("click", runEnter);
form.on("submit", runEnter);


function runEnter() {
    tbody.remove();
    // Prevent the page from refreshing
    d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    // Use the form input to filter the data by blood type

    console.log(inputValue);
    console.log(tableData);
    var filteredData = tableData.filter(datetime => datetime.datetime === inputValue);
    console.log(filteredData);


    filteredData.forEach(function(append) {
        var table = d3.select("#ufo-table")
        var row = table.append("tr")
        console.log(row)
        Object.entries(append).forEach(function([key, value]) {
            var cell = row.append("td")
            cell.text(value)
        })
    })



};