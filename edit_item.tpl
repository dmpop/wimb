<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>What's in My Bag</title>
<h1>Edit item number {{no}}</h1>
<form action="/edit/{{no}}" method="GET">
<p><input type="text" name="item" value="{{old[0]}}" size="50" maxlength="254"></p>
<p><input type="text" name="serial_no" value="{{old[1]}}" size="50" maxlength="100"></p>
<p><input type="submit" id="btn" name="save" value="Save"></p>
</form>
