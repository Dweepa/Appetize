<?php
  $res = array();
  extract($_GET);
  $file = fopen("places.txt","r");
  while(!feof($file)){
    $line = trim(fgets($file));
    if(strncasecmp($term,$line,strlen($term))==0){
      $res[]=$line;

    }
  }
  echo json_encode($res);
?>

