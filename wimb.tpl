%#template to generate a HTML table

<p>What's in My Bag:</p>
<table border="0">
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
        %end
  </tr>
%end
</table>
