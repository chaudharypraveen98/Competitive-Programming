## **[Calendar Module](https://www.hackerrank.com/challenges/calendar-module)** 

The calendar module allows you to output calendars and provides additional useful functions for them.<br>class calendar.TextCalendar([firstweekday])<br>This class can be used to generate plain text calendars.

Sample Code  
<code>>>> import calendar</code>
<code>>>> </code>
<code>>>> print calendar.TextCalendar(firstweekday=6).formatyear(2021)</code>
```
January

Su	Mo	Tu	We	Th	Fr	Sa
 	 	 	 	 	1	2
3	4	5	6	7	8	9
10	11	12	13	14	15	16
17	18	19	20	21	22	23
24	25	26	27	28	29	30
31
.
.
.
December

Su	Mo	Tu	We	Th	Fr	Sa
 	 	 	1	2	3	4
5	6	7	8	9	10	11
12	13	14	15	16	17	18
19	20	21	22	23	24	25
26	27	28	29	30	31	
```

**Sample Input 0**  
```08 12 2021```

**Sample Output 0**  
```WEDNESDAY```

**Explanation 0**  
```The day on December 8th 2021 was WEDNESDAY.```