<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>What's in my Bag</title>
<p>Edit the item number {{no}}</p>
<form action="/edit/{{no}}" method="GET">
<input type="text" name="description" value="{{old[0]}}" size="100" maxlength="100"><br />
<input type="text" name="serial_no" value="{{old[1]}}" size="50" maxlength="100"><br />
<input type="submit" name="save" value="Save">
</form>
