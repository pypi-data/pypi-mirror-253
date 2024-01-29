# topsis-yashas-102103726
topsis-yashas-102103726 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).
## Installation
Use pip package manager to install topsis-yashas-102013726. 

        pip install topsis-yashas-102103726
## Usage
Enter csv filename followed by .csv extentsion, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-) and the output csv file name. 

        topsis-yashas-102103726 sample.csv "1,1,1,1" "+,-,+,+ output.csv"

### Notes

* The first column and first row are removed by the library before processing, in attempt to remove indices and headers.
* Make sure the csv does not contain categorical values.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).