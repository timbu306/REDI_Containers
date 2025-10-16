# 🪟 Minikube on Windows — PowerShell + Hyper-V / Docker

This self-contained guide covers Windows only. Follow these PowerShell steps in an elevated (Run as Administrator) PowerShell.

---

## ✅ Step 1 — Enable Hyper-V & management tools

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
# or only tools:
# Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All

Restart-Computer
```

---

## ✅ Step 2 — Install Minikube

```powershell
New-Item -Path 'C:' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' `
  -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' `
  -UseBasicParsing

# Add to machine PATH
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
# Close and reopen PowerShell to pick up PATH
```

---

## ✅ Step 3 — Install kubectl

```powershell
Invoke-WebRequest -OutFile 'C:\kubectl.exe' `
  -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' `
  -UseBasicParsing

# Ensure C:\ is in machine PATH if kubectl placed there
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:", [EnvironmentVariableTarget]::Machine)
}
# Close and reopen PowerShell
```

---

## ▶️ Step 4 — Start Minikube (examples)

Remove old clusters and start with Hyper-V:

```powershell
minikube delete --all --purge
minikube start --driver=hyperv
```

Or use Docker driver (if Docker Desktop installed):

```powershell
minikube start --driver=docker
```

---

## 🔍 Verify

```powershell
minikube status
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## 🚀 30-minute Hands-on Demo (Windows PowerShell)

Goal: start cluster, deploy nginx, expose, scale, inspect logs, cleanup.

1) Start cluster and confirm:
```powershell
minikube start
minikube status
```

2) Deploy nginx:
```powershell
kubectl create deployment hello-minikube --image=nginx:latest
kubectl get deployments
kubectl get pods -o wide
```

3) Expose and open:
```powershell
kubectl expose deployment hello-minikube --type=NodePort --port=80
minikube service hello-minikube --url
# or open GUI:
minikube service hello-minikube
```
Alternative port-forward:
```powershell
kubectl port-forward svc/hello-minikube 8080:80
# open http://localhost:8080
```

4) Scale:
```powershell
kubectl scale deployment hello-minikube --replicas=3
kubectl get pods
```

5) Logs and exec:
```powershell
$pod = kubectl get pods -l app=hello-minikube -o jsonpath="{.items[0].metadata.name}"
kubectl logs $pod
kubectl exec -it $pod -- powershell
# or use cmd/sh depending on image
```

6) Cleanup:
```powershell
kubectl delete service hello-minikube
kubectl delete deployment hello-minikube
# or full cleanup
minikube delete
```

---

## 🩺 Windows Troubleshooting (quick)

- minikube not found: close/reopen PowerShell, ensure PATH updated.
- CrashLoopBackOff / image pull: kubectl describe pod <pod>; check network.
- Pod stuck Pending: consider more resources:
  ```powershell
  minikube start --memory=4096 --cpus=2 --driver=docker
  ```
- Check minikube logs: `minikube logs`

This Windows file is complete — no macOS steps here.
