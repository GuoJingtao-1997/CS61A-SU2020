;Q1
(define (factorial x)
    (if (= x 1) x
        (* x (factorial (- x 1))) 
    )    
)

;Q2
(define (fib n)
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 2)) (fib (- n 1))))
    )
)

;Q3
(define (my-append a b)
    (cond
        ((Null? a) b)
        (else (cons (car a) (my-append (cdr a) b)))
    )
)

;Q4
(define (insert element lst index)
    (if (= index 0) (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)

;Q5
(define (duplicate lst)
    (if (Null? lst) '()
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)