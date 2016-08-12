var PlayerHistoryPointsGraph = function () {
    this.margin  = 20;
    this.width = 1500;
    this.height = 250;

    this.max_data_length = 8;
    this.max_value = 2300;
    this.years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012];

    this.scale_x = d3.scale.linear().domain([0, this.max_data_length]).range([0, this.width]);
    this.scale_y = d3.scale.linear().domain([0, this.max_value]).range([this.height, 0]);

    this.graph = d3.select('#graph')
                   .append('svg:svg')
                   .attr('width', this.width)
                   .attr('height', this.height)
                   .append('svg:g')
                   .attr('transform', "translate(" + this.margin + "," + this.margin + ")");

    this.xAxis = d3.svg.axis().scale(this.scale_x).tickSize(-this.height);
    this.graph.append('svg:g').attr('class', 'x axis').call(this.xAxis).attr("transform", "translate(0," + this.height + ")");

    this.yAxisLeft = d3.svg.axis().scale(this.scale_y).orient('left');
    this.graph.append('svg:g').attr('class', 'y axis').call(this.yAxisLeft).attr("transform", "translate(-25,0)");

    this.add_player_points_history = function (points_history) {
        var self = this;
        var line = d3.svg.line()
                         .x(function(d, i){ return self.scale_x(i); })
                         .y(function(d){ return self.scale_y(d); });

        var plot_data = _.map(points_history, function(p){ return p[1]; });
        this.graph.append('svg:path').attr('d', line(plot_data));
    }
}

console.log('yay');
$(document).ready(function() {
    var graph = new PlayerHistoryPointsGraph();
    var data = [[2005, 500], [2006, 700], [2007, 1500], [2008, 1200], [2009, 2000], [2010, 1900], [2011, 2000], [2012, 2100]];
    graph.add_player_points_history(data);
});
