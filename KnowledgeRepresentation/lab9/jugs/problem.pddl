(define (domain jug-pouring)
	(:requirements :typing :fluents)
	(:types jug)
	(:functions
		;amount of water in a jug
		(amount ?j - jug)
		;capacity of a jug
		(capacity ?j - jug)
		;how many actions were already done
		(pour-counter))
	;pour entire jug
	(:action pour-to-empty
		:parameters (?jug1 ?jug2 - jug)
		:precondition 
			; jugs should be different
			; first jug can't be empty
	 		; the second jug has to have enough empty space
	 	:effect 
	 		; mark first jug as empty
			; add amount from the first jug to the second
			; increase pour-counter
	)
	;pour only part of the jug
	(:action pour-partly
		:parameters (?jug1 ?jug2 - jug)
		:precondition 
			; jugs should be different
			; first jug can't be empty
			; second jug should have less space than water contained in the first jug
		:effect 
			; decrease the amount of the water in the first jug
			; mark the second jug as full
			; increase pour-counter
	)
)