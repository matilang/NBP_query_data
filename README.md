# NBP_query_data
Simple serwer using data from National Polish Bank API, to display plain data.

## Implementation
To use the program we need to download all of the files from repository (main.py and three .html files).
It is important that the template folder is in the same folder as main.py.
After that we can just run the program in IDE. Or from cmd in folder where is main file
'python main.py'

## Commands

To query operation 1, run this command in the browser:
```
http://localhost:5000/api/exchange_rate/{table}/{code}/{date}
```
{table} - A or B<br>
{code} - short name of the currency<br>
{date} - date in YYYY-MM-DD format

To query operation 2, run this command in the browser:
```
http://localhost:5000/api/average_value/{table}/{code}/last/{num}
```
{table} - A or B<br>
{code} - short name of the currency<br>
{num} - number of last quotations N (N <= 255)

To query operation 3, run this command in the browser:
```
http://localhost:5000/api/buy_sell_difference/c/{code}/last/{num}
```
{code} - short name of the currency <br>
{num} - number of last quotations N (N <= 255)<br>
Here we are always using table C
