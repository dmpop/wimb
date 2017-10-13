<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
</head>
<title>What's in My Bag</title>
<div id="content">
<h1>Add New Entry</h1>
<form action="/add" method="GET">
<p>Item</p>
<p><input type="text" size="50" maxlength="254" name="item"></p>
<p>Serial Number</p>
<p><input type="text" size="50" maxlength="100" name="serial_no"></p>
<p>Note</p>
<p><input type="text" size="50" maxlength="254" name="note"></p>
<p><input type="submit" id="btn" name="add" value="Add"></p>
</form>
<p><a class="btn" href="/wimb">Back</a></p>
</div>
