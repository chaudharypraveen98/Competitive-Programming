## **Athlete Sort**

> **You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.**


 | Rank | age |  height |             |rank |  age |  height|
 |:---: |:---:|  :---:  |   :---:     |:---:|:---: |  :---: |
 |   1  | 32  |   190   |  sort based |  5  |  24  |   176  |
 |   2  | 35  |   175   |  on k=1     |  4  |  26  |   195  |
 |   3  | 41  |   188   | --------->  |  1  |  32  |   190  |
 |   4  | 26  |   195   | i.e (age)   |  2  |  35  |   175  |
 |   5  | 24  |   176   |             |  3  |  41  |   188  |

 
Note that  is indexed from  to , where  is the number of attributes.
Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

#### **Input Format**

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Check the sample below for clarity.

##### **Sample Input 0**

5 3     <br>
10 2 5  <br>
7 1 0   <br>
9 9 9   <br>
1 23 12 <br>
6 5 9   <br>
1       <br>

##### **Sample Output 0**

7 1 0    <br>
10 2 5   <br>
6 5 9    <br>
9 9 9    <br>
1 23 12  <br>

##### **Explanation 0**<br>

The details are sorted based on the second attribute, since  is zero-indexed.
