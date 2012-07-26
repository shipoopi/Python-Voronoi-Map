var points =     [[226,159],[491,21],[490,225],[89,241],[170,152],[180,237],[51,47],[219,326],[472,305],[487,398],[331,235],[365,165],[130,162],[312,89],[242,112]];

function redraw(v){
    var canvas = $('#voronoi')[0];
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0,0,500,500);
    ctx.fillStyle = 'black';
    var drawPoints = [];
    for(i = 0; i < points.length; i++){
        drawPoints.push(new Point(points[i][0], points[i][1]));
        ctx.fillRect(points[i][0]-2, points[i][1]-2, 4,4);
    }


    v.Compute(drawPoints, 500,500);
    var edges = v.GetEdges();
    var cells = v.GetCells();
    ctx.lineWidth = 3;
    ctx.strokeStyle = '#000';
    for(i = 0; i < edges.length; i++){
        var e = edges[i];
        ctx.beginPath();
        ctx.moveTo(e.start.x, e.start.y);
        ctx.lineTo(e.end.x, e.end.y);
        ctx.closePath();
        ctx.stroke();
    }
}
$('document').ready(function(){
    var v = new Voronoi()
    redraw(v)
    $('input[name=redraw]').click(function(){
        redraw(v);
    })
})