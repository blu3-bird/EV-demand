## EDA of the dataset:

- #### `Location` columns has 14 categories, and almost of all of them are related with target variable. 

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

- #### Public Area and apartments are the location, where we have the maximum number of EV charging spots.

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

####  `Start day` in our dataset is 30/09/2021 and `End date` is 30/09/2022 


```
      StartDay      EndDay
min  2021-09-30  2021-10-01
max  2022-09-30  2022-09-30
```

### `Charger Type` and its relation with demand, as we can see Charger Type 1 is bit more in demand than our Type 0. though is only 2% .
```
ChargerType
0    17.054121
1    18.955911
Name: Demand, dtype: float64
```

#### As per the below data, we can say that though the charger Type 1 count is very less as compared to the Type 0. 

```ChargerType
0    57903
1    14953
Name: count, dtype: int64

```

#### *Charger company* columns, company 1 is more almost double of the company 0

```
ChargerCompany
1    45713
0    27143
Name: count, dtype: int64
```

#### *Charger Company* columns does not have much relation with our demand, as in the below data we can see that doesnt matter which company's charger it is, both have almost same demand rate.

```
ChargerCompany
0    16.696717
1    17.888424
Name: Demand, dtype: float64
```

#### *Charger Company* relation with `Duration` Columns and its count
    - Company type 1 takes more times to charge EV

```
Company  Duration Mean      Count
0	    104.27152488671112	27143
1	    179.05523592851048	45713
```

#### *Charger Type* relation with `Duration` columns
    - Charger Type 1 takes very less time to charge EV as compared to Type 0

```
Charger Type  Duration Mean         Count
0	           180.94314629639223	57903
1	           35.995653046211466	14953
```
