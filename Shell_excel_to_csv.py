#
import pandas as pd
from prefect import task, Flow
from prefect.tasks.shell import ShellTask


@task()
def get_dataframe():
    return pd.read_excel('./top2000.xlsx')


my_task = ShellTask()

with Flow("shell") as f:
    output = my_task(command="in2csv top2000.xlsx | tee top2000.csv | ls")

flow_state = f.run()
shell_output = flow_state.result[output].result
print(shell_output)