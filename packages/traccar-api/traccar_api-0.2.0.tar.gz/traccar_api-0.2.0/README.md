## Import

```
from external_services.traccar_api.api import TraccarApi
```

## Initial
```
traccar = TraccarApi(URL, MAIL, PASS)
 ```

## Login

```
current_user = traccar.login()

```

## Bulks
 ```
 server = traccar.get_server()
 ```
```
devices = traccar.get_devices()
```
```
devices_criteria = traccar.get_device(device_ids=[3, 38], device_unique_ids=["01442517SKYD066", "01433630SKYC6D3"])
```
```
users = traccar.get_users()
```
```
drivers = traccar.get_drivers()
```
```
groups = traccar.get_groups()
```
## Singles

```
device = traccar.get_device(device_unique_ids=["01433630SKYC6D3"])
```
```
user = traccar.get_user(1)
```
```
driver = traccar.get_driver(301)
```
## Permissions
```
permissions = traccar.get_current_user_permissions()
```
```
link_driver1_device1 = traccar.link_diver_device(driver_id=301, device_id=3)
```
```
link_driver2_device1 = traccar.link_diver_device(driver_id=302, device_id=3)
```
```
unlink_driver1_device1 = traccar.unlink_diver_device(driver_id=301, device_id=3)
```
```
unlink_driver2_device1 = traccar.unlink_diver_device(driver_id=302, device_id=3)
```
# Errors
```
test_errors = traccar.test_error()
```
# LogOut
```
traccar.logout()
```