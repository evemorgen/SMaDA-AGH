(define (problem test-pour-partly)
	(:domain jug-pouring)
	(:objects
		jug-13l jug-7l - jug)
	(:init
		(= (capacity jug-13l) 13)
		(= (capacity jug-7l) 7)
		(= (amount jug-13l) 13)
		(= (amount jug-7l) 0))
	(:goal 
		(and
			(= (amount jug-7l) 7)
			(= (amount jug-13l) 6)))
)