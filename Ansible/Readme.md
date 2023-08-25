# Ansible playbooks and other things

`ansible host-pattern -m <module> -a moduleargs>`

`ansible-doc -l`  list all ansible modules installed

Usefull starter modules
- ansible.builtin.shell
- ansible.builtin.command
- ansible.builtin.apt
- ansible.builtin.systemd
- ansible.builtin.systemd_service
- ansible.builtin.file


`ansible localhost -m apt -a "name=nginx state=present" -b`


`ansible localhost -m ansible.builtin.file -a "path=/home/ubuntu/ansidir state=directory"`  Idempotent


`ansible localhost -m ansible.builtin.command -a "mkdir /home/ubuntu/ansicmddir"`  Not Idempotent
ansible.builtin.
`ansible localhost -m ansible.builtin.systemd_service -a "name=nginx state=restarted" -b`