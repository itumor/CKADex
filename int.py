#importing required module
import os

# Using system() method to
# execute shell commands
os.system('kubeadm init --apiserver-advertise-address $(hostname -i) --pod-network-cidr 10.5.0.0/16')
os.system('kubectl apply -f https://raw.githubusercontent.com/cloudnativelabs/kube-router/master/daemonset/kubeadm-kuberouter.yaml')
os.system('kubectl get no')
