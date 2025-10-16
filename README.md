text
# Minikube Installation and Setup on Windows (PowerShell & Hyper-V)

This guide provides simple step-by-step instructions to install and run Minikube—a local Kubernetes single-node cluster—on a Windows machine using PowerShell and Hyper-V.

---

## Prerequisites

- Windows 10 Pro or higher with Hyper-V support
- PowerShell running as Administrator
- Internet connection

---

## Step 1: Enable Hyper-V and PowerShell Module

Open PowerShell as Administrator and run:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
Restart-Computer

text

This installs Hyper-V virtualization platform and management tools with PowerShell support.

---

## Step 2: Download and Install Minikube

Run in PowerShell:

New-Item -Path 'C:' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing

$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
[Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}

text

Close and reopen PowerShell to refresh your PATH.

---

## Step 3: Install kubectl

Download kubectl CLI:

Invoke-WebRequest -OutFile 'C:\kubectl.exe' -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' -UseBasicParsing

$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:') {
[Environment]::SetEnvironmentVariable('Path', "$oldPath;C:", [EnvironmentVariableTarget]::Machine)
}

text

Restart PowerShell again.

---

## Step 4: Start Minikube with Hyper-V Driver

In an elevated PowerShell prompt:

minikube delete --all --purge
minikube start --driver=hyperv
minikube status

text

You should see all Minikube components running with status like:

minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

text

---

## Step 5: Verify Cluster with kubectl

Test your Kubernetes cluster:

kubectl get nodes
kubectl get pods --all-namespaces

text

---

## Notes

- Make sure to run PowerShell as Administrator for Hyper-V commands.
- If you face network issues pulling container images, you may need to configure proxy settings inside Minikube.
- To stop your cluster: `minikube stop`
- To completely remove: `minikube delete`

---

This setup provides a quick local Kubernetes environment for development and testing on Windows using Minikube and Hyper-V.

---
