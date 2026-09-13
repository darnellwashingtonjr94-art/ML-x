# 🚀 ML-x

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

(Imagine you are running a cool virtual amusement park. The **frontend** is the shiny ticket booth and colorful rides that everyone sees, the **backend** is the secret machine room running the whole show behind the walls, and **Terraform** is the magic construction crew that instantly builds the entire park grounds wherever you want. **ML-x** is the master blueprint that packages all of this together so you can pack it up in a box and spin up the whole park anywhere with one click!)

## 🎯 What this is?
**ML-x** is a fully containerized, cloud-provisioned full-stack application workspace. It couples a robust backend service with an interactive frontend, automated infrastructure provisioning via Terraform, and streamlined Docker orchestration.

## ⚙️ What this does?
*   **Orchestrates Services:** Spins up the frontend and backend simultaneously using Docker Compose.
*   **Automates Infrastructure:** Provisions cloud resources declaratively using Terraform scripts.
*   **Streamlines Deployments:** Packages code and dependencies into isolated, reproducible container environments.

## 🧠 How does this work?
1.  **Provision:** Terraform sets up the underlying cloud infrastructure environment.
2.  **Containerize:** Docker builds the images using the root `Dockerfile` and services configuration.
3.  **Run:** Docker Compose links the `backend` API and `frontend` interface together into a unified operational stack.

## 🛠️ What problems this solves?
*   **"It works on my machine" Syndrome:** Eliminates environment mismatches by locking everything down inside standard containers.
*   **Manual Cloud Setup:** Removes tedious manual server configurations through code-driven infrastructure (IaC).
*   **Fragmented Codebases:** Keeps your UI, server logic, and infrastructure cleanly organized in one predictable layout.

## 🔥 Why is this cool?
It bridges the entire gap from code to cloud. You don't just get an app—you get the entire infrastructure automated and ready to launch locally or deploy into production instantly with zero friction.

## 📋 What is the requirements?
*   **Docker & Docker Compose:** Latest stable release
*   **Terraform:** v1.0+
*   **Node.js / npm:** v18+ (for package dependencies and lockfile tracking)
*   **OS:** Linux, macOS, or Windows (WSL2)

## 💻 How to install this?
```bash
# 1. Clone the repository
git clone [https://github.com/Credkellar-boop/ML-x.git](https://github.com/Credkellar-boop/ML-x.git)

# 2. Navigate into the directory
cd ML-x

# 3. Spin up the entire stack with Docker Compose
docker-compose up --build
