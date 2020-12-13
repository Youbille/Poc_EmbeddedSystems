<?php
echo(exec('sudo python3 HeatBache.py',$result));
print_r($result);
echo("<img src = heatMap.png>");
echo "<br>";
echo("The humidity is at 56.4% \n");
echo"<br>";
echo nl2br("The pressure is of 982hPa");
?>
