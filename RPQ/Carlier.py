import schrage

def find_b(order,U,C):
    for i in range(len(order)):
        if U == C[i] + order[i].get_q():
            b = i
    return b

def find_a(order,U,b):
    a = 0
    for i in range(len(order)):
        prep = 0
        for j in range(i, b):
            prep += order[j].get_p()
        if U == order[i].get_r() + +order[b].get_q():
            return i
    return a

def find_c(a, b, order):
    c = None
    for i in range(a, b):
        if (order[i].get_q()) < (order[b].get_q()):
             c = i
    return c

def find_RPQ(order, b, c):
    R_prim = order[c+1].get_r()
    P_prim = 0
    Q_prim = order[c+1].get_q()

    for i in range(c+1, b):
        if order[i].get_r() < R_prim:
            R_prim = order[i].get_r()
        if order[i].get_q() < Q_prim:
            Q_prim = order[i].get_q()
        P_prim += order[i].get_p()

    return R_prim, P_prim, Q_prim

def order_only_id(order):
    order_only_id = []
    for task in order:
        order_only_id.append(task.id)
    return order_only_id

class Carlier:
    def __init__(self, UB):
        self.UB = UB

    def carlier(self,tasks):
        order, U, C = schrage.schrage(tasks)
        i = 0

        if U < self.UB:
            self.UB = U

        b = find_b(order, U, C)
        a = find_a(order, U, b)
        c = find_c(a, b, order)

        if c is None:
            return self.UB,order_only_id(order)

        R_prim, P_prim, Q_prim = find_RPQ(order, b, c)
        R_saved = order[c].get_r()
        order[c].change_r(max(order[c].get_r(), P_prim + R_prim))

        LB = schrage.schrage_pmtn(tasks)
        if LB < self.UB:
            self.carlier(tasks)

        order[c].change_r(R_saved)
        Q_saved = order[c].get_q()
        order[c].change_q(max(order[c].get_q(), P_prim + Q_prim))

        LB = schrage.schrage_pmtn(tasks)
        if LB < self.UB:
            self.carlier(tasks)

        order[c].change_q(Q_saved)
        return self.UB, order_only_id(order)

    def carlier_heapq(self,tasks):
        order, U, C = schrage.schrage_heapq(tasks) # wywolanie schrage, przypisanie kolejnosci , Cmaxa i kolejnych cwil czasowcyh

        if U < self.UB:   # sprawdzenie czy Cmax jest mniejszy niz ograniczenie górne
            self.UB = U   # przypisanie ograniczenia górnego jako Cmaxa

        b = find_b(order, U, C)  # znalezienie zadania b, ostatniego na sciezce kryrtycznej
        a = find_a(order, U, b) # znalezienia zadania a, pierwsze zzadanie po którym nie wystepuje przestoj pomiedzy a i b
        c = find_c(a, b, order) # znalazienie C jako najdalsze między a i b, którego Q jest mniejsze niz Q(b)

        if c is None:    # sprawdzenie czy istnieje c, jezeli nie obecne rozwiazenie jest optymalne
            return self.UB,order_only_id(order) # zwrocenie Cmaxa i kolejnosci(tylko po id zadań)
        #znalezieie R'P'Q' miedzy c i b
        # R' najdluszczy czas przygotowania, P' łaczny czas wykonywania, Q' najdluszy czas dostarczenia
        R_prim, P_prim, Q_prim = find_RPQ(order, b, c)
        R_saved = order[c].get_r() # zapisanie zadania referencyjnego
        order[c].change_r(max(order[c].get_r(), P_prim + R_prim)) # zmiana R zadania referencyjnego tak aby wykonywało sie ostatnie

        LB = schrage.schrage_pmtn_heapq(tasks)  # dolne ograniczenie jako Cmax z algorytmu schrage z przerwaniami
        if LB < self.UB:
            self.carlier(tasks)     # rekurencyjne wywołanie algorytmu

        order[c].change_r(R_saved) # wczytania zadania referencyjnego
        Q_saved = order[c].get_q() # zapisanie Q zadania referencyjnego
        order[c].change_q(max(order[c].get_q(), P_prim + Q_prim)) # zmiana Q zadania referencyjnego, aby było wykonywane jako pierwsze
        LB = schrage.schrage_pmtn_heapq(tasks)
        if LB < self.UB:
            self.carlier(tasks)

        order[c].change_q(Q_saved)
        return self.UB, order_only_id(order)

    def carlier2(self,tasks):
        order, U, C = schrage.schrage(tasks)
        i = 0

        if U < self.UB:
            self.UB = U

        b = find_b(order, U, C)
        a = find_a(order, U, b)
        c = find_c(a, b, order)

        if c is None:
            return self.UB,order_only_id(order)

        R_prim, P_prim, Q_prim = find_RPQ(order, b, c)
        R_saved = order[c].get_r()
        order[c].change_r(max(order[c].get_r(), P_prim + R_prim))

        LB = schrage.schrage_pmtn(tasks)
        if LB < self.UB:
            self.UB = min( self.carlier(tasks))

        order[c].change_r(R_saved)
        Q_saved = order[c].get_q()
        order[c].change_q(max(order[c].get_q(), P_prim + Q_prim))

        LB = schrage.schrage_pmtn(tasks)
        if LB < self.UB:
            self.carlier(tasks)

        order[c].change_q(Q_saved)
        return self.UB, order_only_id(order)