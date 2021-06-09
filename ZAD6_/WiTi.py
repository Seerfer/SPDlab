import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
class WiTi_Task:
    def __init__(self, task_number, p, w, t):
        self.id: int = task_number
        self.p: int = p
        self.w: int = w
        self.t: int = t

class WiTi_Instance:
    tasks: list # lista wszystkich zadań, będą po kolei dla wygody
    tasks_number: int # liczba wszystkich zadań

    @staticmethod
    def load_from_file(name):
        """ Metoda wczytująca instancje z pliku - to zostawiam Państwu, na razie na sztywno dodana mała instancja."""
        instance = WiTi_Instance()
        with open(os.path.join(THIS_FOLDER, name), "r") as data:
            line = int(data.readline())
            instance.tasks_number = line
            instance.tasks = []
            for id in range(line):
                p, w, t = data.readline().split()
                instance.tasks.append(WiTi_Task(id, int(p), int(w), int(t)))
        return instance

    def get_p(self, task_number):
        return self.tasks[task_number].p

    def get_w(self, task_number):
        return self.tasks[task_number].w

    def get_t(self, task_number):
        return self.tasks[task_number].t

def solve_witi_with_solver(file):
    from ortools.sat.python import cp_model  # importujemy model CP z biblioteki or-tools

    instance = WiTi_Instance.load_from_file(file)

    model = cp_model.CpModel()  # inicjalizacja modelu - przechowa nasze zmienne oraz ograniczenia naszego problemu
    sum_p = 0
    sum_wt = 0
    for task_number in range(instance.tasks_number):  # iterujemy po wszystkich zadaniach:
        sum_p = sum_p + instance.get_p(task_number)
        sum_wt = sum_wt + (instance.get_w(task_number) * instance.get_t(task_number))

    Cmax_max_value = sum_p  # dla pewności o jeden za dużo
    WTsum_max_value = sum_wt
    cmax_min_value = WTsum_min_value = 0  # nic nie jest ujemne w naszym wypadku

    WT_sum = model.NewIntVar(WTsum_min_value, WTsum_max_value, 'Witi objective')

    model_start_vars = []
    model_ends_vars = []
    model_interval_vars = []
    model_late_vars = []


    for task_number in range(instance.tasks_number):
        suffix = f"t:{task_number}"
        start_var = model.NewIntVar(cmax_min_value, Cmax_max_value, 'start_' + suffix)
        end_var = model.NewIntVar(cmax_min_value, Cmax_max_value, 'end_' + suffix)
        interval_var = model.NewIntervalVar(start_var, instance.get_p(task_number), end_var, 'interval_' + suffix)
        late_var = model.NewIntVar(WTsum_min_value, WTsum_max_value, 'late_' + suffix)

        model_start_vars.append(start_var)
        model_ends_vars.append(end_var)
        model_interval_vars.append(interval_var)
        model_late_vars.append(late_var)

    model.AddNoOverlap(model_interval_vars)

    for task_number in range(instance.tasks_number):
        model.Add(model_late_vars[task_number] >= 0)
        model.Add(model_late_vars[task_number] >= (model_ends_vars[task_number] - instance.get_t(task_number)) * instance.get_w(task_number))

    model.Add(WT_sum >= sum(model_late_vars))

    model.Minimize(WT_sum)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300.0

    status = solver.Solve(model)

    if (status is not cp_model.OPTIMAL):
        status_readable = "not optimal solution :( "
    else:
        status_readable = "optimum found!"

    pi_order = []
    for task_number in range(instance.tasks_number):
        pi_order.append((task_number, solver.Value(model_start_vars[task_number])))
    pi_order.sort(key=lambda x: x[1])
    pi_order = [x[0] for x in pi_order]

    print(f"Script ended\nSuma ważonych spóżnień: {solver.ObjectiveValue()}\norder: {pi_order}\nis optimal? {status_readable}")
    return solver.ObjectiveValue(), pi_order, status_readable

solve_witi_with_solver("WiTi.txt")


