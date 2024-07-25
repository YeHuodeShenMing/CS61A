(define (insert element lst index)
        (cond ((null? lst) (list element))
              ((= index 0) (cons element lst))
              (else (cons (car lst) (insert element (cdr lst) (- index 1))))))

    (expect (insert 2 '(1 7 9) 2) (1 7 2 9))

    (expect (insert 'a '(b c) 0) (a b c))
