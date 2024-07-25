(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
          ((= num1 num2) 0)
          (else 1))
    )

(define (make-adder num) 
    (lambda (x) (+ num x))
    )

(define (composed f g) 
    (lambda (x) (f (g x)))
    )

(define (repeat f n) 
    (cond ((= n 1) f)
          (else (composed f (repeat f (- n 1))))    
    ))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (define big (max a b))
    (define small (min a b))
    (cond ((= (modulo big small) 0) small)
          (else (gcd small (modulo big small)))))

(define (duplicate lst) 
    (cond ((null? lst) nil)
          (else 
                (define first (car lst))
                (cons first (cons first (duplicate (cdr lst))))))
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
    (cond ((null? s) '())
          ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
          (else (cons (fn (car s)) (deep-map fn (cdr s)))))
)

(define (double x) (* 2 x))

(expect (deep-map double '(1 2 3)) (2 4 6))
