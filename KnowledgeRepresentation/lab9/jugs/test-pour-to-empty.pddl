;test if planner can pour an entire jug into other
(define (problem test-pour-to-empty)
	(:domain jug-pouring)
	(:objects
		jug-13l jug-7l - jug)
	(:init
		(= (pour-counter) 0)
		(= (capacity jug-13l) 13)
		(= (capacity jug-7l) 7)
		(= (amount jug-13l) 0)
		(= (amount jug-7l) 7))
	(:goal 
		(and
			(= (amount jug-7l) 0)
			(= (amount jug-13l) 7)))
)