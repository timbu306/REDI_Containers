# Minikube Installation and Usage on Windows with PowerShell and Hyper-V

This guide provides simple instructions to:

- Enable Hyper-V and management tools
- Install Minikube and kubectl CLI tools
- Start a Minikube cluster using the Hyper-V driver
- Verify that Minikube and kubectl are set up correctly

---

## Step 1: Open PowerShell as Administrator

Search for "PowerShell" in the Start menu, right-click and select **Run as Administrator**.

---

## Step 2: Enable Hyper-V and Management Tools

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

## Step 3: Install Minikube

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

## Step 4: Install kubectl CLI

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

## Step 5: Start Minikube with Hyper-V Driver

Before starting, you can remove any old clusters:

```powershell
minikube delete --all --purge
```

Start Minikube using the Hyper-V driver:

```powershell
minikube start --driver=hyperv
```

If you see errors about the Hyper-V PowerShell module, ensure it's installed and enabled (see Step 2).

---

## Step 6: Verify Minikube and kubectl

Check Minikube status:

```powershell
minikube status
```

You should see "Running" for host, kubelet, and apiserver.

Check kubectl access to the cluster:

```powershell
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## Troubleshooting

- If Minikube fails to start due to missing or corrupt config files, run:

```powershell
minikube delete --all --purge
Remove-Item -Recurse -Force "$env:USERPROFILE\.minikube"
```

- Run PowerShell as Administrator for all commands that modify system features or machine-level environment variables.

- If Hyper-V is unavailable or problematic, consider using the Docker driver instead (requires Docker Desktop):

```powershell
minikube start --driver=docker
```

---

This README is formatted for GitHub and uses fenced code blocks for command sequences to make it easy to copy and paste into PowerShell.
