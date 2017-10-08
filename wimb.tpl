<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
</head>
<title>What's in My Bag</title>
<div id="content">
<h1>What's in My Bag</h1>
<table border="0">
<tr><th>Item</th><th>Serial no.</th></tr>
%for row in rows:
    %item = row[1]
    %serial_no = row[2]
    <tr>
    <td>{{item}}</td>
    <td class="col3">{{serial_no}}</td>
    <td><a href="/edit/{{id}}">Edit</a></td>
    <td><a href="/delete/{{id}}">Delete</a></td>
  </tr>
%end
</table>
<p><a href="add">Add Item</a></p>
</div>
