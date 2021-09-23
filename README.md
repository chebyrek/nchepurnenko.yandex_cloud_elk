# Ansible Collection - nchepurnenko.yandex_cloud_elk

Module created for 08-ansible-06-module homework 
## Modules

|Module|Description|
|------|-----------|
|text_file|The module creates text file with desired content|



# Домашнее задание к занятию "08.04 Создание собственных modules"

## Основная часть

1. В виртуальном окружении создать новый `my_own_module.py` файл
2. Наполнить его содержимым:
3. Заполните файл в соответствии с требованиями ansible так, чтобы он выполнял основную задачу: module должен создавать текстовый файл на удалённом хосте по пути, определённом в параметре `path`, с содержимым, определённым в параметре `content`.
4. Проверьте module на исполняемость локально.
```sh
(venv) $ python -m ansible.modules.text_file /tmp/args.json

{"changed": true, "message": "Change file content", "invocation": {"module_args": {"path": "/home/user/test_file.txt", "content": "this is content for my file"}}}
```
5. Напишите single task playbook и используйте module в нём.
```sh
(venv) $ ansible localhost -m text_file -a "path=/home/user/test_file4.txt, content='test content'"

localhost | CHANGED => {
    "changed": true,
    "message": "New file was created"
}
```
6. Проверьте через playbook на идемпотентность.
```yml
---
- name: test my module
  hosts: localhost
  tasks:
    - name: test text_file module
      text_file:
        path: /home/user/test_file4.txt
        content: 'test content'
```
```sh
(venv) $ ansible-playbook site.yml 

PLAY [test my module] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [test text_file module] ***************************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
7. Выйдите из виртуального окружения.
8. Инициализируйте новую collection: `ansible-galaxy collection init my_own_namespace.yandex_cloud_elk`
9. В данную collection перенесите свой module в соответствующую директорию.
10. Single task playbook преобразуйте в single task role и перенесите в collection. У role должны быть default всех параметров module
11. Создайте playbook для использования этой role.
```yml
---
- name: homework
  hosts: localhost
  tasks:
    - name: create text file
      nchepurnenko.yandex_cloud_elk.text_file:
        path: /tmp/file.txt
        content: content for file
```
```sh
$ cat requirements.yml 
collections:
  - name: https://github.com/chebyrek/nchepurnenko.yandex_cloud_elk
    type: git
    version: 1.0.0user@vm1:~/repos/08-ansible-06-module/playbook
```
```sh
$ ansible-galaxy collection install -r requirements.yml 
Starting galaxy collection install process
Process install dependency map
Cloning into '/home/user/.ansible/tmp/ansible-local-69658wcs63n4/tmpmym88ik9/nchepurnenko.yandex_cloud_elkvjfhtqtf'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 27 (delta 0), reused 27 (delta 0), pack-reused 0
Unpacking objects: 100% (27/27), 6.53 KiB | 290.00 KiB/s, done.
Note: switching to '1.0.0'.
```
```
$ ansible-playbook site.yml

PLAY [homework] ****************************************************************************************

TASK [Gathering Facts] *********************************************************************************
ok: [localhost]

TASK [create text file] ********************************************************************************
changed: [localhost]

PLAY RECAP *********************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
12. Заполните всю документацию по collection, выложите в свой репозиторий, поставьте тег `1.0.0` на этот коммит.
13. Создайте .tar.gz этой collection: `ansible-galaxy collection build` в корневой директории collection.
```sh
$ ansible-galaxy collection build
Created collection for nchepurnenko.yandex_cloud_elk at /home/user/repos/nchepurnenko/yandex_cloud_elk/nchepurnenko-yandex_cloud_elk-1.0.0.tar.gz
```
14. Создайте ещё одну директорию любого наименования, перенесите туда single task playbook и архив c collection.
15. Установите collection из локального архива: `ansible-galaxy collection install <archivename>.tar.gz`
```sh
$ ansible-galaxy collection install nchepurnenko-yandex_cloud_elk-1.0.0.tar.gz -p .
Starting galaxy collection install process
[WARNING]: The specified collections path '/home/user/repos/08-ansible-06-module/playbook' is not part
of the configured Ansible collections paths
'/home/user/.ansible/collections:/usr/share/ansible/collections'. The installed collection won't be
picked up in an Ansible run.
Process install dependency map
Starting collection install process
Installing 'nchepurnenko.yandex_cloud_elk:1.0.0' to '/home/user/repos/08-ansible-06-module/playbook/ansible_collections/nchepurnenko/yandex_cloud_elk'
nchepurnenko.yandex_cloud_elk:1.0.0 was installed successfully
```
16. Запустите playbook, убедитесь, что он работает.
```sh
$ ansible-playbook site.yml 
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost
does not match 'all'

PLAY [homework] ****************************************************************************************

TASK [Gathering Facts] *********************************************************************************
ok: [localhost]

TASK [create text file] ********************************************************************************
ok: [localhost]

PLAY RECAP *********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
17. В ответ необходимо прислать ссылку на репозиторий с collection

