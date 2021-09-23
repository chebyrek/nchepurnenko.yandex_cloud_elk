#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: text_file

short_description: Create text file and add content to it

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Create text file and add content to it

options:
    path:
        description: the path where a file will be create.
        required: true
        type: str
    content:
        description: content 
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - nchepurnenko.yandex_cloud_elk.my_doc_fragment_name

author:
    - Nikolay Chepurnenko
'''

EXAMPLES = r'''
# Pass in a path
- name: Test with a path
  nchepurnenko.yandex_cloud_elk.text_file:
    path: /home/user/file.txt

# pass in a path and content
- name: Test with a path and content
  nchepurnenko.yandex_cloud_elk.text_file:
    path: /home/user/file.txt
    content: this is content for my file

# fail the module
- name: Test failure of the module
  nchepurnenko.yandex_cloud_elk.text_file:
    path: /home/user/file.txt
    content: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: The output message that the module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible.module_utils._text import to_text
import os.path


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    # if module.check_mode:
    #     module.exit_json(**result)
    try:
        if not os.path.exists(module.params['path']):
            with open(module.params['path'], 'wb') as f:
                f.write(to_bytes(module.params['content']))
            result['changed'] = True
            result['message'] = to_bytes("New file was created")
        else:
            with open(module.params['path'], 'r') as f:
                if module.params['content'] == to_text(f.read()):
                    result['changed'] = False
                    result['message'] = to_bytes("File with desired content already exists")
                else:
                    with open(module.params['path'], 'wb') as f:
                        f.write(to_bytes(module.params['content']))
                    result['changed'] = True
                    result['message'] = to_bytes("Changed file content")
    except OSError as err:
        module.fail_json(msg='{} {}'.format(err.strerror, err.filename), **result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    # result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    # if module.params['new']:
    # result['changed'] = changed

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['content'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
