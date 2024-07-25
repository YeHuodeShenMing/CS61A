(define (interleave lst1 lst2)
    ; 'YOUR-CODE-HERE
    (cond 
        ((and (null? lst1) (null? lst2)) '())
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) 
                    (cons (car lst2) 
                        (interleave (cdr lst1) (cdr lst2)))))
    )
)
