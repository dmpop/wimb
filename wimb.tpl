<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>What's in my Bag</title>
<h1>What's in My Bag:</h1>
<table border="0">
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
        %end
  </tr>
%end
</table>
<p><a href="add">Add Item</a></p>
