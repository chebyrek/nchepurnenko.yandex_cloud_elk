Text file 
=========

This role creates a text file with desired content

Requirements
------------

Linux 

Role Variables
--------------

|Variable|Description|
|--------|-----------|
|path|The path to the created file|
|content|Desired file content|


Usage
-------
```
    - hosts: localhost
      roles:
         - text_file_role
```

