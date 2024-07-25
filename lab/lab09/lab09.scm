; (define (over-or-under num1 num2) 
;   (if (= num1 num2) 0 (if (< num1 num2) -1 1))
; )

(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1)
  )
)

; (define (make-adder num) 
;   (define (adder inc) (+ num inc))
;   adder
; )

(define (make-adder num)
  (lambda (inc) (+ num inc))
)


(define (composed f g) 
  (
    lambda (x) (f (g x))
  )
)


(define (repeat f n)
  (cond 
    ((= n 1) f)
    (else 
      (composed f (repeat f (- n 1)))
    )
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (define small (min a b))
  (define big (max a b))
  (define big (if (> (modulo big small) 0)
                  (modulo big small)
                  big))
  (define (loop i)
    (if (> i 1)
        (if (and (= (modulo big i) 0) (= (modulo small i) 0))
            i
            (loop (- i 1)))
        1))
  (loop small))
