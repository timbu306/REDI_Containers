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

This README adds visual icons for faster scanning and includes macOS steps (Homebrew, kubectl, minikube) alongside the existing Windows instructions. Keep the terminal closed and reopened after PATH/shell changes to pick up environment updates.
