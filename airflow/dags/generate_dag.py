"""
The official docs meant to load all YAML DAGs at once didn't work:
https://astronomer.github.io/dag-factory/latest/getting-started/quick-start-airflow-standalone/
"""

from airflow import DAG
import dagfactory
from pathlib import Path

my_dag = Path.cwd() / "dags/mydag.yaml"
dag_factory = dagfactory.DagFactory(my_dag)

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())
