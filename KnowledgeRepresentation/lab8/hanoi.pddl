(define (domain hanoi) 
  (:requirements :strips) 		; STRIPS required
  (:types isBlock place)
  (:predicates (on ?x - isBlock ?y - isBlock) 		; block ?x is on block ?x
	       (ontable ?x - isBlock ?y - place)		; block ?x on the table
	       (clear ?x - isBlock)		; no block is on block ?x
	       (handempty)		; robot’s arm is empty
	       (holding ?x - isBlock)		; robot’s arm is holding ?x
	       (smaller ?x ?y)
	       (spaceempty ?p - place)
	       )
  (:action pick-up			; action „pick up from the table”
	     :parameters (?block - isBlock ?p - place)
	     :precondition (and (clear ?block) (ontable ?block ?p) (handempty))
	     :effect
	     (and (not (ontable ?block ?p))
		  (not (clear ?block))
		  (not (handempty))
		  (holding ?block)
		  (spaceempty ?p)
		 )
  )
  (:action put-on-table
         :parameters (?block - isBlock ?p - place)
         :precondition (and (holding ?block) (spaceempty ?p))
         :effect
         (
            and (ontable ?block ?p)
                (handempty)
                (clear ?block)
                (not (holding ?block))
                (not (spaceempty ?p))
         )
    )
  (:action put-a-on-b
        :parameters (?block_a - isBlock ?block_b - isBlock)
        :precondition (and (clear ?block_b) (holding ?block_a))
        :effect 
        (
            and (on ?block_a ?block_b)
                (clear ?block_a)
                (handempty)
                (not (clear ?block_b))
                (not (holding ?block_a))
        )
  )
  (:action take-a-off-b
        :parameters (?block_a - isBlock ?block_b - isBlock)
        :precondition (and (clear ?block_a) (on ?block_a ?block_b) (handempty))
        :effect
        (
            and (holding ?block_a)
                (clear ?block_b)
                (not (clear ?block_a))
                (not (handempty))
                (not (on ?block_a ?block_b))
        )
  )
)