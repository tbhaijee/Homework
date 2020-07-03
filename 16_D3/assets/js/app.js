// @TODO: YOUR CODE HERE!
//step1: setup our chart
var svgwidth = 960;
var svgheight = 500;
var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 50
}

// calculate chart width and height
var width = svgwidth - margin.right - margin.left;
var height = svgheight - margin.top - margin.bottom;

// step2: creat svg wrappper and chart

var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgwidth)
    .attr("height", svgheight);

var chartgroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);
// step3 : import data from csv and log errors
d3.csv("./assets/data/data.csv").then(function(jourdata) {
    //parse date 
    jourdata.forEach(function(data) {
        data.id = +data.id;
        data.state = +data.state;
        data.poverty = +data.poverty;
        data.povertyMoe = +data.povertyMoe;
        data.age = +data.age;
        data.ageMoe = +data.ageMoe;
        data.healthcare = +data.healthcare;
        data.smokes = +data.smokes;

    });

    var xlinearscale = d3.scaleLinear()
        .domain([8, d3.max(jourdata, d => d.poverty)])
        .range([0, width])
    var ylinearscale = d3.scaleLinear()
        .range([height, 0])
        .domain([4, d3.max(jourdata, d => d.healthcare)])

    //create axes
    var bottomaxis = d3.axisBottom(xlinearscale)

    var leftaxis = d3.axisLeft(ylinearscale);

    // append x axis

    chartgroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomaxis);

    //append yaxis
    chartgroup.append("g")
        .call(leftaxis);

    // create circles
    var circlesGroup = chartgroup.selectAll("circle")
        .data(jourdata)
        .enter()
        .append("circle")
        .attr("cx", d => xlinearscale(d.poverty))
        .attr("cy", d => ylinearscale(d.healthcare))
        .attr("r", "20")
        .attr("fill", "blue")
        .attr("opacity", "0.5")
        .text("10", "10", "sans-serif", "10px", "white");

    var circleLabels = chartgroup.selectAll(null).data(jourdata).enter().append("text");

    circleLabels
        .attr("x", function(d) {
            return xlinearscale(d.poverty);
        })
        .attr("y", function(d) {
            return ylinearscale(d.healthcare);
        })
        .text(function(d) {
            return d.abbr;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "15px")
        .attr("text-anchor", "middle")
        .attr("fill", "white");




    // Create axes labels
    chartgroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare (%)");

    chartgroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
        .attr("class", "axisText")
        .text("In Poverty(%)");


}).catch(function(error) {
    console.log(error)
});