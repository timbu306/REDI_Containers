# 🛠️ Minikube Installation and Usage on Windows & macOS

This guide provides simple instructions to:

- ✅ Enable Hyper-V / system virtualization and management tools
- 📦 Install Minikube and kubectl CLI tools
- ▶️ Start a Minikube cluster using a chosen driver
- 🔍 Verify that Minikube and kubectl are set up correctly

---

## Step 1: Open PowerShell as Administrator (Windows) 🪟

Search for "PowerShell" in the Start menu, right-click and select **Run as Administrator**.

---

## Step 2: Enable Hyper-V and Management Tools (Windows) ⚙️

Run these commands in an elevated PowerShell window to enable Hyper-V and its management features:

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
```

If you only want the PowerShell module and management tools:

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All
```

Restart your computer afterwards:

```powershell
Restart-Computer
```

---

## Step 3: Install Minikube (Windows) 🐧➡️🪟

Create a directory and download the Minikube executable:

```powershell
New-Item -Path 'C:' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' `
  -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' `
  -UseBasicParsing
```

Add Minikube to the system PATH (machine-level):

```powershell
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
```

Close and reopen PowerShell to pick up the PATH change.

---

## Step 4: Install kubectl CLI (Windows) 🐳

Download kubectl executable (adjust version or URL as needed):

```powershell
Invoke-WebRequest -OutFile 'C:\kubectl.exe' `
  -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' `
  -UseBasicParsing
```

Add C:\ (or the folder where kubectl.exe is located) to the system PATH if not already present:

```powershell
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:", [EnvironmentVariableTarget]::Machine)
}
```

Close and reopen PowerShell.

---

## macOS — Install Homebrew, kubectl and Minikube 🍏🍺

Prereqs: macOS 10.14+ recommended. You can use the Docker driver (Docker Desktop) or hyperkit.

1) Install Homebrew (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2) Ensure Homebrew is in your shell environment (important on Apple Silicon):

- For zsh (default on modern macOS):

```bash
# Add Homebrew to your shell (example for Apple Silicon)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

- For Intel macs, brew may be in /usr/local; follow the Homebrew post-install output.

Close and reopen your Terminal (or run the eval command above) to ensure brew is available.

3) Install kubectl and minikube via Homebrew:

```bash
brew update
brew install kubectl minikube
```

4) (Optional) Install hyperkit driver (lightweight VM driver) or use Docker driver:

- Docker driver (recommended if Docker Desktop is installed and running):

```bash
# Start Docker Desktop first, then:
minikube start --driver=docker
```

- hyperkit driver (requires installation and permissions):

```bash
brew install hyperkit
# Then start minikube with hyperkit:
minikube start --driver=hyperkit
```

If you installed Homebrew or changed shell config, close and reopen Terminal before running minikube.

---

## Step 5: Start Minikube with Hyper-V Driver (Windows) / Example Starts (macOS) ▶️

Before starting, you can remove any old clusters (Windows example):

```powershell
minikube delete --all --purge
```

Windows start (Hyper-V):

```powershell
minikube start --driver=hyperv
```

macOS start examples (see macOS section for driver choice):

```bash
# Docker driver
minikube start --driver=docker

# or hyperkit
minikube start --driver=hyperkit
```

If you see errors about drivers or the virtualization stack, follow the driver-specific installation steps above.

---

## Step 6: Verify Minikube and kubectl ✅

Check Minikube status:

```bash
minikube status
```

You should see "Running" for host, kubelet, and apiserver.

Check kubectl access to the cluster:

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## Troubleshooting 🩺

- If Minikube fails to start due to missing or corrupt config files, run:

```bash
minikube delete --all --purge
# Windows PowerShell:
# Remove-Item -Recurse -Force "$env:USERPROFILE\.minikube"
# macOS / Linux:
rm -rf "$HOME/.minikube"
```

- Always run commands that modify system features or machine-level environment variables as Administrator (Windows) or with appropriate privileges on macOS.
- If Hyper-V is unavailable or problematic on Windows, or you prefer containers, use the Docker driver:

```bash
minikube start --driver=docker
```

---

## 🚀 30-minute Hands-on Demo — Run a simple web app on Minikube (for absolute beginners)

Goal: In ~30 minutes you'll start Minikube, deploy an nginx web app, expose it, scale it, view logs, and clean up. Commands work on macOS/Linux (bash) and Windows PowerShell (adjust prompts).

Estimated time:
- Setup & start cluster: 5–10 min
- Deploy & expose app: 5–10 min
- Inspect, scale & logs: 5–10 min
- Cleanup & troubleshooting: 5 min

Steps:

1) Ensure cluster is running (5–10 min)
- Start or verify Minikube:
  - macOS / Linux:
    ```bash
    minikube start
    minikube status
    ```
  - Windows PowerShell:
    ```powershell
    minikube start
    minikube status
    ```
- Troubleshoot:
  - If `minikube` not found: reopen your Terminal/PowerShell or ensure PATH was updated.
  - If `minikube status` shows "Stopped", rerun `minikube start` and wait for "Running".

2) Deploy a small web app (nginx) (5 min)
```bash
kubectl create deployment hello-minikube --image=nginx:latest
kubectl get deployments
kubectl get pods -o wide
```
- Expected: a pod with name like hello-minikube-xxxxx enters Running state.
- If pod is Pending for >2 min: run `kubectl describe pod <pod-name>` to see why (image pull, resources, etc).

3) Expose the app and open it in your browser (5 min)
- Expose as NodePort and use minikube to get URL:
```bash
kubectl expose deployment hello-minikube --type=NodePort --port=80
minikube service hello-minikube --url
# or to open a browser:
minikube service hello-minikube
```
- Alternative: port-forward locally:
```bash
kubectl port-forward svc/hello-minikube 8080:80
# then open http://localhost:8080
```
- Troubleshoot:
  - If `minikube service` fails, ensure Minikube driver is running and the service exists (`kubectl get svc`).
  - If port-forward stuck, try another local port (e.g., 8081:80).

4) Scale the deployment and observe behavior (5 min)
```bash
kubectl scale deployment hello-minikube --replicas=3
kubectl get pods
kubectl get pods -o wide
```
- Confirm 3 pods are Running. Use `kubectl describe deployment hello-minikube` to inspect rollout details.

5) Inspect logs and exec into a pod (5 min)
```bash
# find a pod name:
POD=$(kubectl get pods -l app=hello-minikube -o jsonpath="{.items[0].metadata.name}")
kubectl logs $POD
# exec (nginx uses /bin/sh)
kubectl exec -it $POD -- /bin/sh
# inside pod, you can run:
# ls /usr/share/nginx/html
# exit
```
- Troubleshoot:
  - If `kubectl logs` is empty or shows errors, try `kubectl describe pod $POD` for events.

6) Clean up (2–5 min)
```bash
kubectl delete service hello-minikube
kubectl delete deployment hello-minikube
# or remove everything:
minikube delete
```

Quick troubleshooting cheatsheet
- CrashLoopBackOff / Error pulling image:
  - `kubectl describe pod <pod>` → read Events. Try `kubectl get events --sort-by=.metadata.creationTimestamp`.
  - Ensure image name is valid and cluster has network access.
- Pod in Pending due to resources:
  - Minikube may need more memory/CPUs: restart with more resources:
    `minikube start --memory=4096 --cpus=2`
- kubectl context issues:
  - Ensure kubectl is using minikube cluster: `kubectl config current-context` should be `minikube`.
- Can't access service in browser:
  - Use `minikube service hello-minikube --url` and open that URL.
  - If using port-forward, ensure the command is running in a foreground terminal.

Tips for learning
- Try editing the nginx default page by creating a ConfigMap or using a custom image.
- Run `kubectl explain deployment` to learn object fields.
- Explore the dashboard: `minikube dashboard` opens a web UI for resources.

If you get stuck, try these recovery steps
- Restart cluster: `minikube delete && minikube start`
- Check Minikube logs: `minikube logs`
- Inspect Kubernetes events: `kubectl get events --all-namespaces`

Have fun exploring! This simple demo covers basic Kubernetes concepts: pods, deployments, services, scaling, logs, and troubleshooting — all on your local Minikube cluster.
