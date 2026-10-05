## EDA of the dataset:

- ### `Location` columns has 14 categories, and almost of all of them are related with target variable. 

     `Accommdation` `bus garage` and `camping` has the highly co related category as per the data.

     < as the demand higher in accommodation , bus garage and camping>
```
Location              Demand(Mean)
accommodation         29.055829
apartment             18.746507
bus garage            28.587586
camping               25.525288
company               16.247879
golf                  16.718299
hotel                 14.704900
market                16.567338
public area           17.906683
public institution    17.399318
public parking lot    17.186767
resort                17.280838
restaurant            17.813123
sightseeing           15.245129
Name: Demand, dtype: float64
```

- ### Public Area and apartments are the location, where we have the maximum number of EV charging spots.

```Location           Count
public area           14082
apartment             14038
resort                 8854
hotel                  8600
company                7558
public institution     7023
public parking lot     3396
market                 3005
restaurant             2222
camping                1630
sightseeing            1203
golf                   1029
accommodation           187
bus garage               29
Name: count, dtype: int64
```

- ###  `Start day` in our dataset is 30/09/2021 and `End date` is 30/09/2022 


```
      StartDay      EndDay
min  2021-09-30  2021-10-01
max  2022-09-30  2022-09-30
```

- ### `Charger Type` and its relation with demand, as we can see Charger Type 1 is bit more in demand than our Type 0. though is only 2% .
```
ChargerType
0    17.054121
1    18.955911
Name: Demand, dtype: float64
```

- ### As per the below data, we can say that though the charger Type 1 count is very less as compared to the Type 0. 

```ChargerType
0    57903
1    14953
Name: count, dtype: int64

```

- ### *Charger company* columns, company 1 is more almost double of the company 0

```
ChargerCompany
1    45713
0    27143
Name: count, dtype: int64
```

- ### *Charger Company* columns does not have much relation with our demand, as in the below data we can see that doesnt matter which company's charger it is, both have almost same demand rate.

```
ChargerCompany
0    16.696717
1    17.888424
Name: Demand, dtype: float64
```

- ### *Charger Company* relation with `Duration` Columns and its count
    - Company type 1 takes more times to charge EV

```
Company  Duration Mean      Count
0	    104.27152488671112	27143
1	    179.05523592851048	45713
```

- ### *Charger Type* relation with `Duration` columns
    - Charger Type 1 takes very less time to charge EV as compared to Type 0

```
Charger Type  Duration Mean         Count
0	           180.94314629639223	57903
1	           35.995653046211466	14953
```

- ### *Demand* by per month, as we can see In winters, there is high demand of EV Charging ports, 
    - August and July months have the highest Demand as per the data. 

```
StartMonth      Demand
8               143041.27
7               139686.65
6               117564.42
5               115283.83
9               111771.80
1               109639.33
4               104253.67
3               103896.05
2               103141.96
12              85158.09
11              71741.55
10              64933.48
Name: Demand, dtype: float64
```

- ### the Below data shows the `demand by Days`. as it is clearly visible, on Working days, charging ports are highly demands as compared to the weekends.


```
StartDayOfWeek      Demand
Thursday            194701.00
Wednesday           190691.34
Friday              190548.48
Tuesday             182012.40
Monday              179069.35
Saturday            173037.99
Sunday              160040.66
Name: DemandPerDay, dtype: float64

```

- ### Below data shows the avg of demands for each day. and it almost same.

```
StartDayOfWeek      Demand
Friday              17.31
Monday              17.35
Saturday            17.41
Sunday              17.81
Thursday            17.62
Tuesday             17.10
Wednesday           17.53
Name: DemandPerDay, dtype: float64
```

- ### `Demand by shift`
        - as per the data, in night there is bit high demand as compared to the day timing shift.

```
Shift       Demand
Day         15.50
Night       18.67
Name: Demand, dtype: float64
```

### `count by shift `

```
Shift       Demand
Day         28259
Night       44567
Name: Demand, dtype: int64

```