# 🛒 E-commerce MVP (Kubernetes + KinD + PostgreSQL)

This is a simple microservices-based e-commerce MVP project running in a local Kubernetes cluster using [KinD (Kubernetes in Docker)](https://kind.sigs.k8s.io/). It consists of:

- 🐍 A Python backend (API)
- 🌐 A React or static frontend
- 🐘 A PostgreSQL database
- 🐳 Dockerized services
- ☸️ Kubernetes manifests for deployments

---

## 📁 Folder Structure

ecommerce-mvp/
├── backend/ # Python backend app
├── frontend/ # Frontend static files or React app
├── k8s/ # Kubernetes manifests
│ ├── backend-deployment.yaml
│ ├── frontend-deployment.yaml
│ ├── postgres-deployment.yaml
│ ├── configmap.yaml
│ ├── secret.yaml
│ └── kind-config.yaml
├── README.md
└── .gitignore



---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/ecommerce-mvp.git
cd ecommerce-mvp

2. Create KinD cluster
bash
Copy
Edit
kind create cluster --config k8s/kind-config.yaml
3. Deploy all services
bash
Copy
Edit
kubectl apply -f k8s/
Wait a few seconds, then check:

bash
Copy
Edit
kubectl get pods
kubectl get svc
🌐 Access the App
The frontend is exposed via a NodePort service.

Find the port:

bash
Copy
Edit
kubectl get svc frontend
Then open in your browser:

arduino
Copy
Edit
http://localhost:<NodePort>
🐘 PostgreSQL Test (Optional)
Connect using psql:
bash
Copy
Edit
kubectl run psql-client --image=postgres:15-alpine -it --rm --restart=Never -- bash
Inside the container:

bash
Copy
Edit
psql -h postgres -U admin -d ecommerce
Password: password123

You should see:

makefile
Copy
Edit
ecommerce=#
Create a test table:
sql
Copy
Edit
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name TEXT
);
\dt
You should see the table listed. Exit with \q.

📦 Environment Variables
Managed using:

k8s/configmap.yaml: non-sensitive env vars (e.g., DB host, name)

k8s/secret.yaml: sensitive data (e.g., DB user, password)

Used by backend and PostgreSQL pods via envFrom.

🧹 Cleanup
To delete the cluster:

bash
Copy
Edit
kind delete cluster
📌 Tech Stack
Kubernetes (KinD)

Docker

Python (FastAPI or Flask)

PostgreSQL

GitHub

👤 ovo
[Your Name]
GitHub: @ovodom

yaml
Copy
Edit

---

## ✅ Push to GitHub

Make sure you're in your repo folder, then:

```bash
git add README.md
git commit -m "Add final README"
git push origin master