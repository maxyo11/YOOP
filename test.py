import sys

### Test if python runs in virtualenv
def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
if is_venv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')


for i in range(0,50):

    print(i)