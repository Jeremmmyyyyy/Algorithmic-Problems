# Codeforce competition for the course CS-250 Algorithms

The goal of this competition was to solve two algorithmic problems that you can find just below. There were 10 public tests and their inputs/results were available [here](https://github.com/Jeremmmyyyyy/Codeforce/tree/main/tests).

You had to code the most efficient and optimized algorithms to pass all 80 tests

# Table of Contents
1. [Problem A : Mad Max Hitchhickers Road](#A)
2. [Problem B : Snowy road](#B)


## Problem A : Mad Max Hitchhickers Road<a name="A"></a>

>time limit per test : 2 seconds<br>
memory limit per test : 256 megabytes<br>
inputstandard : input<br>
outputstandard : output<br>
To finish his latest adventure, Max needs to ride from the Citadel to Gas Town. The last mad getaway from the remnants of Joe's army has left him almost without fuel, with little hope of making it all the way through. However, he has a plan — get the fuel along the way!

The two settlements are connected by a straight road. Along the road, there are n 
 hitchhiker posts. The post number one is located at the Citadel, and the post number n
 at Gas Town. Along the road m
 hitchhikers wait for the passing vehicles. Hitchhiker number i
 stands at post ai
 and wants to get to some other post bi
 closer to Gas Town. When passing by each of the posts, Max can decide to give a lift to one the hitchhikers waiting there. If that happens they immideately give him fi
 liters of gasoline and give him ci
 cans of dog food, which is a popular barter commodity on the wasteland.

Max recently installed an archotech engine into his car. Thanks to that, regardless of the load he only have to expend one liter of fuel to travel between any two adjacent posts. However, due to the peculiarities of the constructions his car can only fit one passenger now, which means that he can accomodate only one hitchhiker at a time.

Max values his reputation, so if he decides to lift someone he must drop them off exactly at the location where they want to go. Additionally, he is in a bit of a rush, so he will only travel towards Gas Town. Finally, his car can hold any amount of dog food cans and gasoline thanks to the movie magic!

Your task is to check whether Max can get to his destination by helping the hitchhikers, and if so find the maximum amount of dog food that he can earn along the way.

### Input
The first line contains three integers: 2≤n≤2000 , 0≤m≤2000 and 0≤f≤109 — the number of posts, hitchhikers and the initial amount of liters of gasoline that Max has.

Next follow m lines. Line number i contains the description of the hitchhiker number i — integers 1≤ai≤n−1, 2≤bi≤n, 0≤ci≤109 and 0≤fi≤109 being respectively the post number where the hitchhiker stands, their destination and amounts of dog food in cans and gasoline in liters that they are willing to pay. It is guaranteed that ai<bi.

### Output
If Max cannot reach Gas Town by any means, output "Impossible" (case sensitive). Otherwise, output a single non-negative integer — the number of dog food cans that Max can earn along the way.

### Examples

input :
```
3 2 1
1 3 3 2
2 3 4 1
```
output :
```
4
``` 
input :
```
3 2 0
1 2 3 0
2 3 4 0
```
output :
```
Impossible
```

### Note :
It doesn't matter how much gas Max will have when he reaches Gas Town, as long as he can do it.

Keep in mind the possibility of integer overflow.

In the first example, to get 4
 cans of dog food, Max expends all of his fuel to reach the post number 2
, where he picks up the only hitchhiker standing there. They give Max 1
 liter of gasoline, which he expends to reach Gas Town where he drops the hitchhiker off. He could have instead picked up the hitchhiker at post 1
, but then he would only earn 3
 cans since he wouldn't be able to pick up the hitchhiker at post 2
 since he cannot travel back.


## Problem B : Snowy road<a name="B"></a>

>time limit per test : 2.5 s<br>
memory limit per test : 256MB<br>
inputstandard : input<br>
outputstandard : output<br>

The weather is especially bad this winter in Berland. A heavy snowstorm passed last night over the city of Bertown and covered some road with snow of variable thickness and completely destroyed other roads.

Bertown road network consists of n
 intersections, connected by bidirectional roads. For each road a municipal weather services reported the thickness of snow covering this road in millimeters.

Gilbert wants to ride an e-bike from his house, located at intersection number s
, to his work at intersection t
. He doesn't feel particularly adventurous today, so he would like to avoid the roads with a lot of snow. In particular, he would like to find a route from his house to work such that the maximum amount of snow on a road on this route is minimal. However, since he doesn't want to be terribly late, he also wants to find the shortest among all of these routes.

This is why he is asking you to help him.

### Input
The first line of the input contains four integers: 1≤n≤30000
, 0≤m≤30000
, 1≤s,t≤n
, which are the number of intersections and the number of intact roads in Bertown, as well as the locations of Gilberts' house and work.

Next m
 lines contain the description of Bertown's road network. Line i
 contains four integers: 1≤ai,bi≤n
, 1≤wi,ci≤109
, where ai,bi
 are the road's endpoints, wi
 is the length of the road and ci
 is the high of snow on the road in millimeters. It is guaranteed that ai≠bi
, and any two intersections are connected by at most one road,

### Output
If there is no possible path connecting s
 to t
, output "Impossible" (case sensitive).

Otherwise output two integers: the minimum value c
 such that there exists a path between s
 and t
 going only on roads with snow height at most c
, and the minimum length of such path.

If s=t
, both numbers should be 0
.

### Examples
input :
```
3 3 1 3
1 3 1 3
1 2 10 1
2 3 10 2
```
output :
```
2 20
```
input :
```
2 0 1 2
```
output :
```
Impossible
```
### Note
Keep in mind integer overflow.

Please do not use the class queue.PriorityQueue in Python, as it slow. Use heapq instead.
