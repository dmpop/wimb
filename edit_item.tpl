<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
</head>
<title>What's in My Bag</title>
<div id="content">
<h1>Edit Entry</h1>
<form action="/edit/{{no}}" method="GET">
<p><input type="text" name="item" value="{{old[0]}}" size="50" maxlength="254"></p>
<p><input type="text" name="serial_no" value="{{old[1]}}" size="50" maxlength="100"></p>
<p><input type="submit" id="btn" name="save" value="Save"></p>
</form>
<p><a href="/wimb">Back</a></p>
</div>
