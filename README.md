# DSA 8420 Support Files

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Support scripts, templates, and helper files for the labs and assignments of **DATA_SCI 8420: Cloud Computing for Data Analytics** at the University of Missouri.

## Repository Structure

```text
dsa8420_support_files/
├── module3/tutorial_helper_files/  # Kubernetes fundamentals helpers
│   ├── analysis.py               # Sample analysis script
│   ├── python-job.yaml           # Kubernetes Job manifest
│   └── python-pod.yaml           # Kubernetes Pod manifest
├── module4/                        # Data-copy and storage helpers
│   ├── development_files/        # Additional module 4 dev assets
│   └── main.py                   # Module 4 main script
├── module5/development_files/      # GPU training and model workflows
│   ├── e501_job_template.yml     # E501 job template manifest
│   ├── e501_pod_smoketest.yml    # Smoketest pod manifest
│   ├── job_hf_generate.yml       # Hugging Face generation job manifest
│   ├── pod_github_clone.yml      # GitHub clone pod manifest
│   ├── pod_hf_setup.yml          # Hugging Face setup pod manifest
│   └── run_llm.py                # LLM execution script
├── module6/development_files/      # Containerization and CI/CD assets
│   ├── .gitlab-ci.yml            # GitLab CI/CD pipeline configuration
│   ├── Dockerfile                # Container build instructions
│   └── requirements.txt          # Python package requirements
├── .gitattributes                  # Git attributes configuration
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
└── README.md                       # Repository overview

```

## Overview of Support Contents

* **Module 3:** Kubernetes fundamentals manifests and helper scripts for running containerized Python jobs and pods.
* **Module 4:** Storage helpers, parameterized manifests, and main script workflows.
* **Module 5:** GPU training job templates, Hugging Face setup/generation manifests, GitHub integration pods, and LLM execution scripts.
* **Module 6:** Containerization build definitions (`Dockerfile`, `requirements.txt`) and automated CI/CD pipeline configurations (`.gitlab-ci.yml`).

## Usage Notes

These files are meant to be used alongside your active lab instructions and course modules on the primary course platform. Ensure you customize any job templates (such as resource requests or paths) to match your active cluster environment (e.g., Hellbender HPC or Nautilus).

## Acknowledgments

Special thanks to **Dr. Soliman Khan** (Teaching Assistant during Fall 2025) for his valuable assistance in developing and refining several of these helper files and templates.

## Preferred Citation

**ONLY with permission** to reference these materials, and use:

```bibtex
@misc{dastour2026cloud,
  author      = {Dastour, Hatef},
  title       = {DSA 8420: Cloud Computing for Data Analytics},
  institution = {University of Missouri},
  year        = {2026},
  note        = {Restricted course material; used with instructor permission}
}

```

## License

This repository is licensed under the terms of the MIT License.