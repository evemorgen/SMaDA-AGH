(define (domain jug-pouring)
	(:requirements :typing :fluents)
	(:types jug)
	(:functions
		(amount ?j - jug)
		(capacity ?j - jug)
		(pour-counter)
        )
    (:action pour
		:parameters (?jug1 ?jug2 - jug)
		:precondition (and
			(not (= ?jug1 ?jug2))
			(> (amount ?jug1) 0))
	 	:effect (and
                            (increase (pour-counter) 1)
                            (when (>= (- (capacity ?jug2) (amount ?jug2)) (amount ?jug1)) (and
                                  (assign (amount ?jug1) 0)
                                  (increase (amount ?jug2) (amount ?jug1))
                                  )
                            )
                            (when (< (- (capacity ?jug2) (amount ?jug2)) (amount ?jug1)) (and
                                  (decrease (amount ?jug1) (- (capacity ?jug2) (amount ?jug2)))
                                  (assign (amount ?jug2) (capacity ?jug2))
                                  )
                            )
                        )
    )
    (:action fountain
                :parameters (?jug - jug)
                :precondition (= 0 0)
                :effect (
                    assign (amount ?jug) (capacity ?jug)
                )
    )
)
