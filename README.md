# DSA 8420 Support Files

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Support scripts, templates, and helper files for the labs and assignments of **DATA_SCI 8420: Cloud Computing for Data Analytics** at the University of Missouri.

**Contents:** [Repository structure](#repository-structure) · [Module overview](#module-overview) · [Usage notes](#usage-notes) · [Acknowledgments](#acknowledgments) · [Citation](#preferred-citation) · [License](#license)

## Repository Structure

```text
dsa8420_support_files/
├── module3/
│   └── tutorial_helper_files/        # Kubernetes fundamentals
│       ├── analysis.py                 # Sample analysis script
│       ├── python-job.yaml             # Job manifest
│       └── python-pod.yaml             # Pod manifest
├── module4/                          # Data copy and storage
│   ├── main.py                         # Module 4 main script
│   └── development_files/
│       ├── persistent_volume.yml       # PersistentVolume manifest
│       ├── persistent_volume_new.yml   # Updated PersistentVolume manifest
│       ├── pod_pvc.yml                 # Pod mounting a PVC
│       ├── pod_python.yml              # Python pod manifest
│       ├── job_copy_data.yml           # Data-copy Job manifest
│       ├── process_image.py            # Image processing script
│       ├── image1.npy                  # Sample data
│       └── image2.npy                  # Sample data
├── module5/
│   └── development_files/            # GPU training and model workflows
│       ├── e501_job_template.yml       # E501 job template
│       ├── e501_pod_smoketest.yml      # Smoke-test pod
│       ├── job_hf_generate.yml         # Hugging Face generation job
│       ├── pod_github_clone.yml        # GitHub clone pod
│       ├── pod_hf_setup.yml            # Hugging Face setup pod
│       └── run_llm.py                  # LLM execution script
├── module6/
│   └── development_files/            # Containerization and CI/CD
│       ├── .gitlab-ci.yml              # GitLab CI/CD pipeline
│       ├── Dockerfile                  # Container build instructions
│       └── requirements.txt            # Python dependencies
├── .gitattributes
├── .gitignore
├── LICENSE                           # MIT License
└── README.md
```

## Module Overview

| Module | Focus | Key files |
|---|---|---|
| 3 | Kubernetes fundamentals: running containerized Python as pods and jobs | `python-pod.yaml`, `python-job.yaml`, `analysis.py` |
| 4 | Persistent storage and data copying | `persistent_volume*.yml`, `pod_pvc.yml`, `job_copy_data.yml`, `process_image.py`, `main.py` |
| 5 | GPU training jobs, Hugging Face setup and generation, GitHub integration | `e501_job_template.yml`, `job_hf_generate.yml`, `pod_hf_setup.yml`, `run_llm.py` |
| 6 | Containerization and automated builds | `Dockerfile`, `requirements.txt`, `.gitlab-ci.yml` |

## Usage Notes

These files are meant to be used alongside your active lab instructions and course modules on the primary course platform. Customize job templates (resource requests, paths, namespaces) to match your cluster environment, for example Hellbender HPC or Nautilus.

## Acknowledgments

Special thanks to **Dr. Soliman Khan** (Teaching Assistant, Fall 2025) for his assistance in developing and refining several of these helper files and templates.

## Preferred Citation

Please cite these materials **only with permission**:

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

This repository is licensed under the terms of the [MIT License](LICENSE).
