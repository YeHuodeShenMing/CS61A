(define first (cons 'a (cons 'b nil)))

(define with-cons
        (cons first
            (cons 'c (cons 'd (cons (cons 'e nil) nil)))
        )
    )
    (draw with-cons)  ; Uncomment this line to draw with-cons
