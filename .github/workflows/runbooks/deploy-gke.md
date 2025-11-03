# Python Application Deployment Runbook (GKE)

This runbook guides you through deploying the Python application to GKE, monitoring the rollout, and rolling back if needed.

---

## 1️⃣ Pre-requisites

- CI workflow (`Python application`) must have **passed successfully**.
- Google Cloud credentials stored in GitHub secrets (`SA_KEY`, `PROJECT_ID`).
- `kubectl` access to the GKE cluster.
- Docker image repository configured in Artifact Registry.

---

## 2️⃣ Triggering Deployment

### From GitHub Actions:

1. Go to **Actions → Build and Deploy to GKE** workflow.
2. Click **Run workflow**.
3. Select branch (default: `main`) and click **Run workflow**.

> The workflow builds the Docker image, pushes it to Artifact Registry, and deploys to GKE automatically.

---

## 3️⃣ Verify Deployment

1. Check rollout status:

```bash
kubectl rollout status deployment/gke-test
