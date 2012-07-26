/**
 * Created with PyCharm.
 * User: sean
 * Date: 26/07/12
 * Time: 4:35 PM
 * To change this template use File | Settings | File Templates.
 */

var reDraw = function(){
    console.log('document ready');
    var points = [];
    var width = 500;
    var height = 500;
    var numPoints = 15;
    while(points.length < numPoints){
        var point = [Math.random() * width, Math.random() * height];
        var conflict = false;
        $.each(points, function(key, existing){
            if(existing[1] == point[1]){
                conflict = true;
                return;
            }
        });
        if(!conflict){
            points.push(point)
        }
    }
    console.log('points: ', points);
    var pointString = "[";
    var canvas = $('#voronoi')[0];
    var ctx = canvas.getContext('2d');
    if(ctx){
        console.log('got context');
    }
    ctx.fillStyle = 'white';
    ctx.fillRect(0,0,width,height);
    ctx.fillStyle = 'black';
    for(i = 0; i < points.length; i++){
        var p = points[i];
        pointString += "["+parseInt(p[0]).toString()+","+parseInt(p[1]).toString()+"]";
        if(i != points.length - 1){

        }
        pointString += ",";
        ctx.fillRect(p[0], p[1], 2,2);
    }
    pointString += "]";
    console.log(pointString);
    $('span#points').empty().append(pointString);
}

$('document').ready(function(){
    reDraw();
    $('input[name=redraw]').click(reDraw);
});