<?php

$localhost="localhost";
$username="admin";
$password="admin";
$database="sensor";

$mysqli = new mysqli($localhost,$username,$password,$database);

$sql = "SELECT datetime, water_count FROM soil_sensor";
$result = mysqli_query($mysqli,$sql);
$dateTemp = array();
$index = 0;
while ($row = mysqli_fetch_array($result,MYSQL_NUM))
{$dateTemp[$index]=$row;$index++;}

//echo json_encode($dateTemp, JSON_NUMERIC_CHECK);

mysqli_close();

?>

<!DOCTYPE html>
<html>
<head>
<title>HighChart</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.js"></script>
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.13/moment-timezone-with-data-2012-2022.min.js"></script>

</head>
<body>

<script type="text/javascript">
$(function () {

$('#container').highcharts({
chart: {
type: 'line'
},
time: {
timezone: 'Europe/Oslo'
},
title: {
text: 'Soil_Moisture_Status vs Time'
},
xAxis: {
title: {
text: 'Time'
},
type: 'datetime',
},
yAxis: {
title: {
text: 'Moisture_Status'
}
},
series: [{
name: 'Count_of_Watered',
data: <?php echo json_encode($dateTemp, JSON_NUMERIC_CHECK);?>
}]
});
});

</script>
<script src="charts/js/highcharts.js"></script>
<script src="charts/js/modules/exporting.js"></script>

<div class="container">
<br/>
<h2 class="text-center">Plant Moisture Sensor - Watered vs. Time</h2>
<div class="row">
<div class="col-md-10 col-md-offset-1">
<div class="panel panel-default">
<div class="panel-heading">Dashboard</div>
<div class="panel-body">
<div id="container"></div>
</div>
</div>
</div>
</div>
</div>

</body>
</html>
