## Project setup

================
.. continue from 16:46 Tutorial 4
Project setup instructions here.

```bash
mkdir -p local
cp core/project/settings/templates/settings.dev.py ./local/settings.dev.py
cp core/project/settings/templates/settings.unittests.py ./local/settings.unittests.py
```

```bash
make shell

from core.config.models import Config
Config.objects.create(owner=None, transaction_fee=1)
```
