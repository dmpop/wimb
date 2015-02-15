<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>What's in my Bag</title>
<p>Delete item number {{no}}?</p>
<form action="/delete/{{no}}" method="GET">
<input type="submit" id="btn" class="warning" name="delete" value="Delete">
</form>
