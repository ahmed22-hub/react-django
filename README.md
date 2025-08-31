📌 Project Resume – React + Django + MySQL + CI/CD
📖 About the Project

This repository is a full-stack web application template that demonstrates how to integrate modern web technologies with a DevOps workflow.
It provides a ready-to-use architecture for scalable projects like e-commerce, dashboards, or management systems.

🏗️ Tech Stack

Frontend: ReactJS (responsive, modern UI)

Backend: Django REST Framework (secure API)

Database: MySQL

Containerization: Docker & Docker Compose

CI/CD: Jenkins + Ansible

Code Quality: SonarQube

Monitoring: Prometheus + Grafana

Orchestration (optional): Kubernetes

🔄 Architecture Overview
Frontend (React)  <-->  Backend (Django REST)  <-->  MySQL DB
         │                    │
         │                    └─> SonarQube (Code Quality)
         │
   Jenkins CI/CD  ──> Docker Build & Push ──> Ansible Deployment
         │
 Prometheus + Grafana (Monitoring & Metrics)

🚀 Setup & Usage
1. Clone the Repo
git clone https://github.com/ahmed22-hub/react-django.git
cd react-django

2. Run with Docker Compose
docker-compose up --build -d


Frontend → http://localhost:3000

Backend → http://localhost:8000

SonarQube → http://localhost:9000
 (admin/admin)
 <img width="4580" height="1790" alt="Flowchart" src="https://github.com/user-attachments/assets/022ccc57-7418-4984-9173-395aacde81b3" />

⚙️ CI/CD Pipeline (Jenkins)

Clone Repo → Fetch latest code from GitHub

Install & Test → Run tests (React + Django)

SonarQube Analysis → Code quality & static analysis

Docker Build & Push → Publish images to Docker Hub

Ansible Deployment → Auto-deploy to dev/prod VM

Notifications → Slack/Email on build status
<img width="1358" height="697" alt="pipline step with blue ocean plugin " src="https://github.com/user-attachments/assets/66b109c6-e5bf-4e70-94ad-5c4cd4ce0a73" />


📊 Monitoring & Quality

Prometheus → Collects system & app metrics
<img width="1363" height="683" alt="prothemus target after deploiments jenkins " src="https://github.com/user-attachments/assets/2e2aad1f-3e4c-4e50-83a3-24decf9f3732" />


Grafana → Dashboards for CPU, RAM, Disk, Network
<img width="1363" height="637" alt="graph grafana apres deploiment" src="https://github.com/user-attachments/assets/6575c8dd-4f4b-46f6-82e0-332956fef6e3" />

SonarQube → Code analysis (bugs, vulnerabilities, smells)
<img width="1351" height="687" alt="sonarqube " src="https://github.com/user-attachments/assets/0248e82f-17eb-4ad6-bd75-68d5da87eafe" />

🌱 Future Extensions

Add Kubernetes deployment manifests

Integrate Helm charts

Extend monitoring with Alertmanager

👨‍💻 Author

Developed & maintained by Ahmed Masmoudi
🔗 GitHub: ahmed22-hub

1. 📂 Project Structure

Show how your repo is organized so contributors can navigate quickly:

react-django/
│── frontend/              # React app
│── backend/               # Django app
│── docker-compose.yml
│── Dockerfile.frontend
│── Dockerfile.backend
│── ansible-setup/         # Ansible playbooks
│── jenkins/               # Jenkins pipeline (Jenkinsfile)
│── monitoring/            # Prometheus & Grafana configs
│── k8s/                   # (Optional) Kubernetes manifests
│── docs/                  # Documentation & guides
│── README.md

2. 🛠️ Prerequisites

List tools required before running the project (helpful for teammates or recruiters):

Docker & Docker Compose

Node.js & npm (for local frontend dev)

Python 3.x & pip (for local backend dev)

Jenkins (for CI/CD)

Ansible (for deployment)

SonarQube (for code analysis)

3. 🧪 Testing

Explain how tests are run for both frontend and backend. Example:

# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test


5. 📦 Deployment Environments

Add a small table showing your dev/prod setup (from your guide file):

VM	Purpose	Specs	IP
jenkins-vm	CI/CD (Jenkins)	2 vCPU, 4GB RAM	192.168.40.128
dev-vm	Development deployment	1 vCPU, 2GB RAM	192.168.40.129
prod-vm	Production deployment	1 vCPU, 2GB RAM	192.168.40.130
<img width="1366" height="704" alt="dev_vm" src="https://github.com/user-attachments/assets/b20def7d-7db7-435f-856f-7dafac83e6e0" />
<img width="1360" height="699" alt="prod_machine" src="https://github.com/user-attachments/assets/34054ce1-a750-499c-95b3-66c7bc5294e9" />

6. 📜 License

If you want others to reuse it:

MIT (open collaboration)

GPL (strong copyleft)

Or a custom license (if private)

7. 🙌 Contribution Guide

Encourage open-source collaboration:

## 🤝 Contribution
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-xyz`)
3. Commit changes (`git commit -m 'Add feature xyz'`)
4. Push to branch (`git push origin feature-xyz`)
5. Open a Pull Request



