
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Title here</title>
</head>
<body>
  <?php
  $target_dir = "Uploads/";
  $target_file = $target_dir . basename($_FILES["fileName"]["name"]);
  move_uploaded_file($_FILES["fileName"]["tmp_name"], $target_file);
  echo "Phone number: ";
  echo $_POST["username"];
  echo "<br>";

  $command = escapeshellcmd('python send_sms.py');
  $output = shell_exec($command);
  echo $output;

  $txt = "data.txt";
  $fh = fopen($txt, 'w+');
  if (isset($_POST['username'])) { // check if both fields are set
    $txt=$_POST['username'];
    file_put_contents('data.txt',$txt."\n",FILE_APPEND); // log to data.txt
    exit();
  }
  fwrite($fh,$txt); // Write information to the file
  fclose($fh); // Close the file

  #shell_exec("python /Applications/XAMPP/htdocs/send_sms.py");
  $command = escapeshellcmd("/usr/bin/python send_sms.py");
  $output = shell_exec($command);
  echo $output;
  echo  "php_works";



  ?>
</body>
</html>
