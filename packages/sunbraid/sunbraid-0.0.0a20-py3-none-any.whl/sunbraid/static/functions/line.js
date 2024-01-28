function createLinePlot(data, elementId) {
    // 1. Set Up SVG Canvas
    const margin = { top: 10, right: 30, bottom: 30, left: 30 },
        width = 500 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

    const svg = d3.select("#" + elementId)
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", `translate(${margin.left},${margin.top})`);
    
            
    svg.append("rect")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .attr("x", -margin.left)
            .attr("y", -margin.top)
            .attr("fill", "white")
            .attr("opacity", 0.8);
    // 2. Parse and Organize Data
    const sumstat = d3.group(data, d => d.color + "-" + d.linestyle);

    // Create x-axis scale and axis
    const x = d3.scaleLinear()
    .domain(d3.extent(data, d => d.x))
    .range([0, width]); // 'width' should be your chart's width

    const xAxis = d3.axisBottom(x)
    .tickValues(data.map(d => d.x))
    .tickFormat(d => {
        const label = data.find(item => item.x === d)?.xlabel;
        return label ? label : "";
    });

    // Append x-axis to your SVG
    svg.append("g")
    .attr("class", "x-axis")
    .attr("transform", `translate(0, ${height})`) // 'height' should be your chart's height
    .call(xAxis);
                
    const maxDottedY = d3.max(data.filter(d => d.linestyle === 'dotted'), d => d.value);
    const maxSolidY = d3.max(data.filter(d => d.linestyle === 'solid'), d => d.value);
    const maxY = 0.6*(maxDottedY + maxSolidY)
    const y = d3.scaleLinear()
                .domain([1, maxY])
                .range([ height, 0 ]);
    svg.append("g").call(d3.axisLeft(y));

    // 4. Line Generator
    const line = d3.line()
                .x(d => x(d.x))
                .y(d => y(d.value));

    // 5. Drawing Lines
    svg.selectAll(".line")
    .data(sumstat)
    .join("path")
        .attr("fill", "none")
        .attr("stroke", d => d[0].split("-")[0])
        .attr("stroke-width", 1.5)
        .attr("d", d => line(d[1]))
        .attr("stroke-dasharray", d => d[1][0].linestyle === "dotted" ? "3,3" : "");
}