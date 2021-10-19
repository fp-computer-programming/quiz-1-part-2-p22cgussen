<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    Python Quiz 1 - Part 2
</h1>

<h2 align="center">Due before 10:50 AM on 10/19 (25 pts.)</h2>

Zeller's congruence is an algorithim developed by Christian Zeller to calculate the day of the week when given a date. The formula is as follows:

![zeller_congruence](https://i.imgur.com/JODDuGH.png)

## Where: ##

`h` is the day of the week

|`h`| Day of Week|
|:-:|:----------:|
| 0 | Saturday   |
| 1 | Sunday     |
| 2 | Monday     |
| 3 | Tuesday    |
| 4 | Wednesday  |
| 5 | Thursday   |
| 6 | Friday     |

`q` is the day of the month

`m` is the month (January and February are counted as months 13 and 14 of the previous year.)

| `m` |   Month   |
|:---:|:---------:|
|  3  | March     |
|  4  | April     |
|  5  | May       |
|  6  | June      |
|  7  | July      |
|  8  | August    |
|  9  | September |
|  10 | October   |
|  11 | November  |
|  12 | December  |
|  13 | January   |
|  14 | February  |

`j` is the century (i.e. year/100)

`k` is the year of the century (i.e. year % 100)

__NOTE: All division in the formula is integer division.__

---

Write a program that prompts the user to enter a year, month, and day of the month. The program should then display the name of the day of the week. Below is a sample of what the console should look like once the code has been run:

```
Enter the year of the date: 1540
Enter the month of the date: 9
Enter the day of the date: 27

9/27/1540 was a Friday.
```

<p align="center">Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
