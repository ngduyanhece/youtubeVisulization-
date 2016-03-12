d3.json("./data.json", function(error, data) {
	var videoData = data.items;
	var nestedData = d3.nest().key(function(el){ return parseInt(el.snippet.publishedAt)}).entries(videoData);
	nestedData.pop();
	// create the set of data key is the year value is the number of video 
	console.log(nestedData);
	var vis = d3.select("#visualisation"),
    WIDTH = 1000,
    HEIGHT = 450,
    MARGINS = {
        top: 20,
        right: 20,
        bottom: 20,
        left: 50
    };
	var xExtent = d3.extent(nestedData, function(d) {
		return d.key;
	});
	var yExtent = d3.extent(nestedData, function(d) {
		return d.values.length;
	});
	xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain(xExtent);
	yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain(yExtent);
	xAxis = d3.svg.axis().scale(xScale);
	yAxis = d3.svg.axis().scale(yScale).orient("left");
	vis
		.append("svg:g")
		.attr("class","axis")
		.attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
		.call(xAxis);
	vis.append("svg:g").attr("class","axis").attr("transform", "translate(" + (MARGINS.left) + ",0)").call(yAxis);
	//generator
	var lineGen = d3.svg.line()
  .x(function(d) {
    return xScale(d.key);
  })
  .y(function(d) {
    return yScale(d.values.length);
  })
	.interpolate("basis");
	
	vis.append('svg:path')
  .attr('d', lineGen(nestedData))
  .attr('stroke', 'green')
  .attr('stroke-width', 2)
  .attr('fill', 'none');
	
	vis.append("text")
    .attr("class", "x-label")
    .attr("text-anchor", "end")
    .attr("x", WIDTH /2)
    .attr("y", HEIGHT + 30)
    .text("YEAR");
	vis.append("text")
    .attr("class", "y-label")
    .attr("text-anchor", "end")
    .attr("y", 6)
    .attr("dy", 10)
		.attr("x", -100)
    .attr("transform", "rotate(-90)")
    .text("NUMBER OF NEW JAVASCRIPT VIDEO ON YOUTUBE");
});