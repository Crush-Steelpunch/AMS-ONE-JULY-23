# Ansible playbooks and other things

## Ad Hoc commands

`ansible host-pattern -m <module> -a moduleargs>`

`ansible-doc -l`  list all ansible modules installed

Usefull starter modules
- ansible.builtin.shell
- ansible.builtin.command
- ansible.builtin.apt
- ansible.builtin.systemd
- ansible.builtin.systemd_service
- ansible.builtin.file
- ansible.builtin.copy
- ansible.builtin.debug


`ansible localhost -m apt -a "name=nginx state=present" -b`


`ansible localhost -m ansible.builtin.file -a "path=/home/ubuntu/ansidir state=directory"`  Idempotent


`ansible localhost -m ansible.builtin.command -a "mkdir /home/ubuntu/ansicmddir"`  Not Idempotent
ansible.builtin.
`ansible localhost -m ansible.builtin.systemd_service -a "name=nginx state=restarted" -b`

## Settiung up ansible ssh

copy the key to the ansible manager

`scp -i ~/Downloads/InstructorLeonKey.pem  ~/Downloads/InstructorLeonKey.pem   ubuntu@3.10.51.193:~/`

Make the file more secure
`chmod 600 InstructorLeonKey.pem`