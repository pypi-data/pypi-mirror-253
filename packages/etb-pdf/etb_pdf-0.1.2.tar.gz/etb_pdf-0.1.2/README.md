[![Upload Python Package](https://github.com/HFxLhT8JqeU5BnUG/etb-pdf/actions/workflows/python-publish.yml/badge.svg)](https://github.com/HFxLhT8JqeU5BnUG/etb-pdf/actions/workflows/python-publish.yml)

Pdf.write() args:

rows: list of dictionaries of data to be filled into PDF

map(optional): dictionary that maps values from rows to field names in the PDF

for example, if fields are ["Name", "Age"]

and rows are [{"foo" : "John", "bar" : 25}, {"foo" : "Jane", "bar" : 30}], 

then map should be: {"Name" : "foo", "Age" : "bar"}

naming(optional): very simple naming convention dict.

naming["static_name"] will be the first part of the file name

naming["dynamic_name_key"] will be appended after a underscore. it will pull the (post mapping, if applicable) key value from each row and append it to the file name.

for example (using the rows and map from above), if naming = {"static_name" : "output", "dynamic_name_key" : "Name"}

then the file names will be: "output_John.pdf" and "output_Jane.pdf"

required_keys: *if map is not None*: if True, all values in map dictionary will be asserted

if you pass an iterable, then each value in the map dictionary that is in the iterable will be asserted