# ML-x

A full-stack, production-ready machine learning template. Unifies a Next.js 14 frontend with a Python 3.11 FastAPI backend capable of multi-framework inference (PyTorch, TensorFlow, XGBoost, Scikit-learn).

## Architecture
- **Frontend:** Next.js 14 (App Router), React, Tailwind CSS
- **Backend:** FastAPI, Python 3.11
- **ML Frameworks:** PyTorch, TensorFlow, XGBoost, Scikit-learn
- **Infrastructure:** Docker Compose (local), Terraform (AWS)
- **CI/CD:** GitHub Actions (Linting, Testing, Trivy/Bandit Security Scans)

## Quick Start (Local Development)

1. Ensure Docker and Docker Compose are installed.
2. Clone the repository and navigate to the root directory.
3. Start the stack:
   ```bash
   make up
