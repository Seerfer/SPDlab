import plotly.figure_factory as ff
import pandas as pd


def gantt(schedule, times):
    times = list((map(list, zip(*times))))
    tmp = [[None for _ in range(len(times[0]))] for _ in range(len(times))]
    for i in range(len(times)):  # tasks
        for j in range(len(times[0])):  # machines
            if i == 0:
                if j == 0:
                    tmp[i][j] = times[schedule[i] - 1][j]
                    df = pd.DataFrame([dict(Start=0, Finish=tmp[i][j],
                                            Task=f"Machine {str(j + 1)}", Resource=f"Task: {schedule[i]}")])
                else:
                    tmp[i][j] = (tmp[i][j - 1] + times[schedule[i] - 1][j])
                    df = df.append(pd.DataFrame([dict(Start=tmp[i][j - 1], Finish=tmp[i][j],
                                                      Task=f"Machine {str(j + 1)}", Resource=f"Task: {schedule[i]}")]))
            else:
                if j == 0:
                    tmp[i][j] = tmp[i - 1][j] + times[schedule[i] - 1][j]
                    df = df.append(pd.DataFrame([dict(Finish=tmp[i][j], Start=tmp[i - 1][j],
                                                      Task=f"Machine {str(j + 1)}", Resource=f"Task: {schedule[i]}")]))
                else:
                    tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1]) + times[schedule[i] - 1][j]
                    df = df.append(pd.DataFrame([dict(Finish=tmp[i][j], Start=max(tmp[i - 1][j], tmp[i][j - 1]),
                                                      Task=f"Machine {str(j + 1)}", Resource=f"Task: {schedule[i]}")]))

    colors_list = [
        "magenta", "olive",
        "blue", "orange",
        "green", "red",
        "purple", "pink",
        "gray", "cyan",
        "brown", "yellow",
        "black", "gold",
        "coral", "limegreen",
        "aqua", "silver",
        "navy", "violet",
        "skyblue", "tomato"
    ]

    colors = {}
    for i in range(len(times)):
        colors[f"Task: {i+1}"] = colors_list[i]

    print(colors)

    fig = ff.create_gantt(df, index_col='Resource', show_colorbar=True,
                          group_tasks=True)
    fig.update_yaxes(autorange="reversed")
    fig.layout.xaxis.type = 'linear'
    fig.show()
