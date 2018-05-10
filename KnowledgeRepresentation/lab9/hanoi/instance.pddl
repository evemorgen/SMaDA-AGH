(define (problem standard-hanoi-problem)
	(:domain hanoi-towers)
	(:objects 
		disk1 disk2 disk3 disk4 disk5 - disk
		rod1 rod2 rod3 - rod)
	(:init
		;initialize fluents with value
		(= (move-counter) 0)
		(= (size rod1) 6)
		(= (size rod2) 6)
		(= (size rod3) 6)
		(= (size disk1) 1)
		(= (size disk2) 2)
		(= (size disk3) 3)
		(= (size disk4) 4)
		(= (size disk5) 5)
		(on-top disk5 rod1)
		(on-top disk4 disk5)
		(on-top disk3 disk4)
		(on-top disk2 disk3)
		(on-top disk1 disk2)
	)
	(:goal
		(and
			(on-top disk5 rod3)
			(on-top disk4 disk5)
			(on-top disk3 disk4)
			(on-top disk2 disk3)
			(on-top disk1 disk2)
		)
	)
	;define the metric of the problem, and here
	;we want to minimize number of moves
	(:metric minimize (move-counter))
)