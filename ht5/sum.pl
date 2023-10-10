% Rules Сумма элементов списка
summ_list([], 0).
summ_list([Head|Tail], Sum) :-
    summ_list(Tail, SumTmp), Sum is SumTmp + Head.

% Query
?- summ_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Sum)