import sys
import multiprocessing
import os

from dotenv import load_dotenv, find_dotenv
from source.domain.context_domain_name.business.context_rule_check_integrations import (
    CheckIntegrations,
)


def main() -> str:
    process_number = multiprocessing.cpu_count()

    _num_of_workers = os.getenv("NUM_OF_WORKERS")
    num_of_workers = int(_num_of_workers if _num_of_workers else "0")

    check_integrations = CheckIntegrations()
    with multiprocessing.Pool(processes=process_number) as pool:
        pool.map(check_integrations.integrations_status, [num_of_workers])

    print(f"All {num_of_workers} tasks completed")
    return


def init():
    if __name__ == "__main__":
        load_dotenv(find_dotenv())
        sys.exit(main())


init()
