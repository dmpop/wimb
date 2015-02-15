%#template for editing an item
<p>Edit the item number {{no}}</p>
<form action="/edit/{{no}}" method="get">
<input type="text" name="description" value="{{old[0]}}" size="100" maxlength="100"><br />
<input type="text" name="serial_no" value="{{old[1]}}" size="50" maxlength="100"><br />
<input type="submit" name="save" value="save">
</form>
