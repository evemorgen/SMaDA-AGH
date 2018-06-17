(define (domain hanoi-towers)
	;fluents are conditions, that can change
	(:requirements :adl :typing :fluents)
	(:types
		object 
		disk rod - object)
	;defintion of available fluents
	(:functions 
		;size of the object represented as a number
		(size ?x - object)
		;counter of all the planned moves
		(move-counter))
	(:predicates
		(on-top ?x - disk ?y - object))
	(:action move-disk
		:parameters (?disk - disk ?from - object ?on - object)
		:precondition (and 
			;the disk has to be moved somewhere else
			(not (= ?from ?on))
			(on-top ?disk ?from)
			;adl is used to check whether the disk is clear
			(not (exists (?disk2 - disk) (on-top ?disk2 ?disk)))
			(not (exists (?disk2 - disk) (on-top ?disk2 ?on)))
			;arithmetic condition
			(< (size ?disk) (size ?on)))
		:effect (and
			(not (on-top ?disk ?from))
			(on-top ?disk ?on)
			;change value of a fluent
			(increase (move-counter) 1)))
)