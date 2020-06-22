git clone https://github.com/NVIDIA/ansible-role-nvidia-docker.git ansible-role-nvidia-docker
cd ansible-role-nvidia-docker
cp ../installnvidiadocker.yaml tests/installnvidiadocker.yaml
ansible-playbook  --inventory ../inventory.cfg tests/installnvidiadocker.yaml
cd ..
rm -r -f ansible-role-nvidia-docker
