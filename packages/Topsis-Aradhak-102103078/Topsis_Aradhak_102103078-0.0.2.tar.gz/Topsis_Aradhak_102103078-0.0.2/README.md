


## Topsis

TOPSIS( Technique for order for preference by similarity to Ideal solution ) for MCDM (Multiple criteria decision making) in Python compiled by Aradhak Kandhari, 102103078, TIET, Patiala.

## Installation

 Use the package manager pip to install topsis-3283. 
 ```
 pip install Topsis-Aradhak-102103078
  ```
## Example

 ```
 Topsis-Aradhak-102103078 sample.csv "1,1,1,1" "-,+,+,+" output.csv
 ```

## Please Note That
The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So the csv MUST follow the format as shown in sample.csv shown in the Example section. The input data file MUST contain three or more columns. The second to last columns of the data file MUST contain NUMERIC values. The number of weights, impacts and columns (second to last) MUST be SAME. Impacts MUST either be '+' or '-'. Impacts and Weights MUST be separated by , (comma).



## License
Â© 2024 Aradhak Kandhari

This reopsitory is licensed under MIT License. See LICENSE for details.
