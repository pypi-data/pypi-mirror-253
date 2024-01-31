"""
se-cli: The swiss army command-line for Cast.AI SE`s.

Usage:
    se-cli demo <prep|off> <eks|aks|gcp> [--cluster_id <cluster_id>] [-h|--help] [-d|--debug]
    se-cli snapshot <analyze> <brief|detailed> [--cluster_id <cluster_id>] [-h|--help] [-d|--debug]
    se-cli audit <analyze> [--cluster_id <cluster_id>] [-h|--help] [-d|--debug]

Options:
    -h, --help  Show this help message and exit
    -d, --debug  Enable debug logging
    -c, --cluster_id <cluster_id>  (Optional) Specify the cluster ID (will assume correct kubectl context)

Commands:
    demo      Manage the demo environment
    snapshot  Manage snapshots
    audit     Manage audit logs

Subcommands for "demo":
    on       Prep demo environment for demo (Get off hibernation)
    off      Hibernate demo environment
    refresh  Disable BinPacking and prep demo

Optional subcommands for "demo" (overrides -c, --cluster_id <cluster_id> picks cluster_id from config file of cloud)
    eks     Use EKS config cluster_id and context
    aks     Use AKS config cluster_id and context
    gcp     (not supported yet)

"""
import sys

from orchestrators.demo_orch import DemoOrchestrator
from orchestrators.snapshot_orch import SnapshotOrchestrator
from orchestrators.audit_orch import AuditOrchestrator
from services.misc_svc import init

from docopt import docopt


commands_table = {
    "demo": DemoOrchestrator,
    "snapshot": SnapshotOrchestrator,
    "audit": AuditOrchestrator,
}

if __name__ == '__main__':
    try:
        # TODO: check version once pypi is up
        parsed_options = docopt(__doc__, sys.argv[1:])
        cfg = init(parsed_options)
        orchestrator_class = commands_table[cfg.app_inputs["command"]]
        main_orch = orchestrator_class(cfg)
        main_orch.execute()
    except Exception as e:
        print(f"An error occurred: {e}")
