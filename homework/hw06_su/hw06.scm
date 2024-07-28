(define (square n) (* n n))

(define (pow base exp) 
    (cond ((= exp 0) 1)
          ((= exp 1) base)
          ((even? exp) (square (pow base (/ exp 2))))
          (else (* base (pow base (- exp 1)))))
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))


(define (ascending? s) 
    (cond ((null? s) #t)
          ((null? (cdr s)) #t)
          ((<= (car s) (cadr s)) (ascending? (cdr s)))
          (else #f))
    )

(define (my-filter pred s) 
    (cond ((null? s) nil)
          ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
          (else (my-filter pred (cdr s)))
            ))
        
; (my-filter even? '(1 2 3 4 5))

; (define (no-repeats s)
;     (define seen '())
;     (my-filter (lambda (x) (lambda (y) (not (= x y)))) s)
; )


(define (no-repeats s)
        (if (null? s) s
                (cons (car s) (no-repeats (my-filter (lambda (x) (not (= x (car s)))) (cdr s))))
        )
)

(no-repeats '(5 5 4 3 2 1))



; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
  ______________________________________________)

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                     (larger-values first rest))
             (define with-first
                     ______________________________________________)
             (define without-first
                     ______________________________________________)
             (if ______________________________________________
                 with-first
                 without-first))))
