(define (average x y) (/ (+ x y) 2))

(define (square x) (* x x))

(define (sqrt x)
    (define (update guess) 
        (if (= (square guess) x)
            guess
            (update (average guess (/ x guess)))
        ))
    (update 1)
)

; ; (define (plus4 x) (+ x 4))

; ; ((lambda (x y z) (+ x y (square z))) 1 2 3)

; ; (define (judge x) 
; ;     (cond ((> x 10) (print 'big))
; ;           ((> x 5) (print 'medium))
; ;           (else (print 'small))))

; ; (define (judge x) (print (cond
; ;                              ((> x 10) 'big)
; ;                              ((> x 5) 'mudium)
; ;                              (else 'small)
; ;                              )))

; (define (judge x) 
;     (if (> x 10) (begin
;                      (print 'big)
;                      (print 'guy)
;                      )
;                  (begin
;                      (print 'small)
;                      (print 'hey))
;                  )
;     )

; (define c (let ((a 3)
;                 (b (+ 2 2)))
;                 (sqrt (+ (* a a) (* b b)))))
            
; (define (twice fn) (fn) (fn))

; (define (line) (fd 50))

; (define s (cons 1 (cons 2 nil)))

; (map (lambda (s) (cons 5 s)) (filter list? '(5 (6 7) 8 (9))))


(define (even-subsets s)
    (if (null? s) nil)
    (append )
    )





















