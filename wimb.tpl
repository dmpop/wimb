%#template to generate a HTML table
<head>
<link rel="stylesheet" type="text/css" href="static/styles.css">
</head>
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
