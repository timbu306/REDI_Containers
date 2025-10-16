# 🎉 Minikube Quick Start — Windows & macOS (Separate Guides)

Pick your OS below — each section is self-contained. The 30-minute hands-on demo is common and placed at the end.

---

## 🔹 Windows Only — Minikube + kubectl (Follow only this section if on Windows)

Quick checklist: Run PowerShell as Administrator, enable Hyper-V if you want the Hyper-V driver, download minikube & kubectl, add to PATH, restart terminal.

### 1) Open PowerShell as Administrator 🪟
- Search "PowerShell", right-click → Run as Administrator.

### 2) Enable Hyper-V & management tools ⚙️
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
# Or just tools:
# Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All
Restart-Computer
```

### 3) Install Minikube 🧩
```powershell
New-Item -Path 'C:' -Name 'minikube' -ItemType Directory -Force
Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' `
  -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' `
  -UseBasicParsing
# Add to PATH (machine)
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
# Close & reopen PowerShell to pick up PATH changes
```

### 4) Install kubectl 🐳
```powershell
Invoke-WebRequest -OutFile 'C:\kubectl.exe' `
  -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' `
  -UseBasicParsing
# Add C:\ to PATH if needed (or place kubectl in C:\minikube)
# Close & reopen PowerShell
```

### 5) Start Minikube ▶️
```powershell
# Clean old
minikube delete --all --purge
# Start with Hyper-V driver (or use docker if preferred)
minikube start --driver=hyperv
# If you have issues starting minikube please try docker driver instead, check command in Troubleshooting below
```

### Quick Windows Troubleshooting 🛠️
- If `minikube` not found → reopen PowerShell or check PATH.
- Hyper-V errors → ensure virtualization is enabled in BIOS and Hyper-V features are installed.
- Want Docker driver instead? Install Docker Desktop and run:
  `minikube start --driver=docker`

---

## 🍏 macOS Only — Homebrew + Minikube + kubectl (Follow only this section if on macOS)

Quick checklist: Install Homebrew (if needed), add brew to your shell, install kubectl & minikube, choose driver (docker or hyperkit), restart terminal if shell config changed.

### 1) Install Homebrew (if needed) 🍺
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- After install, follow the post-install output to add brew to your shell.
- For Apple Silicon (zsh example):
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
# Close & reopen Terminal or run the eval above
```

### 2) Install kubectl & minikube via Homebrew 📦
```bash
brew update
brew install kubectl minikube
```

### 3) Choose & install a driver (Docker recommended) 🐋 or hyperkit 🐎
- Docker driver:
  - Install Docker Desktop and start it, then:
  ```bash
  minikube start --driver=docker
  ```
- hyperkit (lightweight VM):
  ```bash
  brew install hyperkit
  minikube start --driver=hyperkit
  ```
- If brew or shell config changed: close & reopen Terminal.

### Quick macOS Troubleshooting 🛠️
- If brew command not found → ensure shell env is configured and reopen Terminal.
- If minikube fails with driver errors → confirm Docker Desktop is running or hyperkit has correct permissions.
- Need more resources: `minikube start --memory=4096 --cpus=2`

---

## 🚀 Common 30-minute Hands-on Demo (Windows & macOS) — Deploy a tiny web app

Goal: Start minikube, deploy nginx, expose it, scale, view logs, then cleanup. Works on both OSes — use PowerShell on Windows and bash on macOS.

Estimated duration: ~30 minutes

1) Start / verify cluster (5–10 min)
```bash
minikube start
minikube status
# If using PowerShell, same commands work in PowerShell after PATH set.
```

2) Deploy nginx (5 min)
```bash
kubectl create deployment hello-minikube --image=nginx:latest
kubectl get deployments
kubectl get pods -o wide
```

3) Expose service & open in browser (5 min)
```bash
kubectl expose deployment hello-minikube --type=NodePort --port=80
minikube service hello-minikube --url
# or open directly:
minikube service hello-minikube
# Alternative port-forward:
kubectl port-forward svc/hello-minikube 8080:80
# then open http://localhost:8080
```

4) Scale (5 min)
```bash
kubectl scale deployment hello-minikube --replicas=3
kubectl get pods
```

5) Inspect logs & exec (5 min)
```bash
POD=$(kubectl get pods -l app=hello-minikube -o jsonpath="{.items[0].metadata.name}")
kubectl logs $POD
kubectl exec -it $POD -- /bin/sh
# inside: ls /usr/share/nginx/html ; exit
```

6) Cleanup (2–5 min)
```bash
kubectl delete service hello-minikube
kubectl delete deployment hello-minikube
# or remove cluster:
minikube delete
```

Common Troubleshooting (quick)
- CrashLoopBackOff / pull errors → `kubectl describe pod <pod>` and `kubectl get events`.
- Pod Pending → increase minikube resources: `minikube start --memory=4096 --cpus=2`.
- kubectl context wrong → `kubectl config current-context` (should be `minikube`).

---

## 🔗 Useful Links & References

- Minikube official: https://minikube.sigs.k8s.io/
- Kubernetes docs: https://kubernetes.io/docs/home/
- kubectl install docs: https://kubernetes.io/docs/tasks/tools/
- Minikube drivers & troubleshooting: https://minikube.sigs.k8s.io/docs/drivers/
- Homebrew (macOS): https://brew.sh/
- Docker Desktop: https://www.docker.com/products/docker-desktop

---

Enjoy experimenting! 🚀
