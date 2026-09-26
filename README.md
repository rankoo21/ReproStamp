# ReproStamp

ReproStamp is a GenLayer Intelligent Contract and web app for auditable reproducibility checks. A study owner registers a claim plus three independent HTTPS artifacts. Validators fetch the paper, code, and data pages themselves through nondeterministic web access, reach a consensus verdict, and store SHA-256 receipts for all three byte streams.

Lifecycle: `PENDING` → `AUDITED`, or `WITHDRAWN`. The contract rejects unsafe URLs, duplicate study IDs, and artifact sets that do not span at least two hostnames. The UI uses the same wrapped wallet provider for connect and writes, including `wallet_getSnaps` compatibility.

- Contract: `contracts/repro_stamp.py`
- Tests: `python -m pytest tests -q`
- Live address: `0xEb88AFD12E88986C0d7971731F81721dcB9d7044`
- Network: GenLayer Studionet
