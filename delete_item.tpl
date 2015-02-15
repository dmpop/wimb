<head>
<link rel="stylesheet" type="text/css" href="../static/styles.css">
</head>
<p>Delete item number {{no}}?</p>
<form action="/delete/{{no}}" method="GET">
<input type="submit" id="btn" class="warning" name="delete" value="Delete">
</form>
