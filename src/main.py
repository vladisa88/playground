import time
import ray
from ray.job_submission import JobSubmissionClient

from job1.main import Test

# ray.init(address='51.250.31.207:6379', _node_ip_address='172.18.0.13')
ray.init()

def _run_job(match_id: int, client_id: int) -> None:
    print("Try to run job")
    client = JobSubmissionClient("http://localhost:8285")
    print("Submitting job")
    job_id = client.submit_job(
        entrypoint="ls -a && curl -LJON -s https://github.com/vladisa88/playground/archive/refs/heads/master.zip && ls -a && unzip -q playground-master.zip && ls -a && cd playground-master && ls -a && python src/job1/main.py",
        runtime_env={
            "working_dir": ".",
            "env_vars": {"MATCH_ID": str(match_id), "CLIENT_ID": str(client_id)}
        },
    )
    print("Job ID: ", job_id)


def _run_actor() -> None:
    ref = Test.remote()
    ref.main.remote()


def main() -> None:
    print("HERERERERE!!!!!")
    while True:
        for i in range(3):
            _run_job(i, i + 1)
        time.sleep(100)

if __name__ == "__main__":
    main()
