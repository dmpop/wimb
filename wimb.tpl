<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
</head>
<title>What's in My Bag</title>
<div id="content">
<h1>What's in My Bag</h1>
<table border="0">
<tr><th>Item</th><th>Serial no.</th><th>Note</th></tr>
%for row in rows:
    %id = row[0]
    %item = row[1]
    %serial_no = row[2]
    %note = row[3]
    <tr>
    <td>{{item}}</td>
    <td class="col1">{{serial_no}}</td>
    <td class="col2">{{note}}</td>
    <td><a href="/edit/{{id}}"><img src="static/svg/edit.svg" height="16"></a></td>
    <td><a href="/delete/{{id}}"><img src="static/svg/trash.svg" height="16"></a></td>
  </tr>
%end
</table>
<p><a href="add"><img src="static/svg/file-plus.svg" height="24"></a></p>
<p><a href="https://github.com/dmpop/wimb">WIMB on GitHub</a></p>
</div>