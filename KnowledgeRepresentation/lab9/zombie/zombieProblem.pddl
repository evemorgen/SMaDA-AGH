(define (domain zombie-escape)
	(:requirements :typing :fluents)
	(:types human location)
	(:functions
		; fluents:
		(time ?h - human) ; - time required to pass the bridge by actor		
		(time-counter)) ; - count time
	(:predicates 
		; predicates:
		(on-side ?h - human ?l - location) ; - where is the actor
		(latern-side ?l - location)) ; - where is the lantern
	; two men cross the bridge
	(:action cross-two-men
		:parameters (?h1 - human ?h2 - human ?from - location ?to - location)
		:precondition (and
			(not (= ?from ?to))
			;(not (= ?h1 ?h2))
			(on-side ?h1 ?from)
			(on-side ?h2 ?from)
		    (latern-side ?from)
			(>= (time ?h1) (time ?h2)))           
		:effect (and
			(not (on-side ?h1 ?from))
			(not (on-side ?h2 ?from))
			(not (latern-side ?from))
			(on-side ?h1 ?to)
			(on-side ?h2 ?to)
			(latern-side ?to)
			(increase (time-counter) (time ?h1)))
	)
)
