Annex A

Computational Thinking Exercise: "Smart School Canteen Queue"
Activity 1: Computational Thinking Exercise
https://docs.google.com/document/d/1pUr402mgd1XVoL4Q91B6KuFzVudyA92-NG1HlXBlo0I/edit?usp=sharing
Section: 9 - OXYGEN			  		                	Score: _______________
C# / Name: SOFIA DENISE P. HILARIO      		  	Date: 08-05-2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.

Your group's task is to decompose this problem into smaller, manageable parts that could be solved using Computational Thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem:
The main problem is that the process for buying food at the PSHS School Canteen is slow.

Step 2: Identify Three to Four Sub-Problems
Please list possible sub-problems.
1.
The students have yet to decide what they want to eat before arriving at the cashier desk.

2.
The cashier does not have a computational tool to quickly calculate totals and change.

3.
The system is unorganized and cannot track nor update food items automatically.



Step 3: Define Computational Thinking Approaches
For each sub-problem, identify the appropriate Computational Thinking (CT) skill and suggest a possible solution.
Sub-Problem
CT Skill

Example Solution
The students have yet to decide what they want to eat before arriving at the cashier desk.
- Algorithm Design
- Algorithm works well in this problem as instead of merely aiming for the goal of [buying food], they instead follow a sequence of [choose food] -> [wait in line] -> [pay for food].
The cashier does not have a computational tool to quickly calculate totals and change.
- Decomposition
- Decomposition can be used here by breaking the total amount into smaller pieces, a.k.a. by the list of items bought by the student. By keeping a list of items, and instead of trying to add everything together all at once (adding the ones first, then tens to quickly come up with the total), the calculating speed can be enhanced and made more efficient.
The system is unorganized and cannot track nor update food items automatically.
- Algorithm Design
- Algorithm design works with this problem by creating a routine on paper: that is, to [list how much servings of food item] -> [update the count for every X student that orders], to properly keep track of how many food items there is left.

Step 4: Design a Solution
Choose one of the identified sub-problems.
Draw a flowchart or write a pseudocode that shows how the problem can be solved.
1. The students have yet to decide what they want to eat before arriving at the cashier desk.
if (student_food) AND (chose_food) AND (pay_food) THEN
	OUTPUT "Food
else (student_leaves) THEN
	OUTPUT "No food"
