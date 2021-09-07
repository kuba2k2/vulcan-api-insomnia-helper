# vulcan-api-insomnia-helper
A simple project to simplify Vulcan UONET+ API (hebe) usage in Insomnia.

This script creates a ready-to-use Insomnia environment, provided the Token, Symbol and PIN.

A Keystore is created automatically, if not existing. The device is then registered.

The environment can be used with the `@wulkanowy/insomnia-plugin-uonet-request-signer-hebe` plugin, for easy API usage.

## Usage

```bash
Kuba@KUBA-PC  /d/Dev/vulcan-api-helper
# pipenv install

Kuba@KUBA-PC  /d/Dev/vulcan-api-helper
# pipenv run python main.py
Using keystore from ./keystore.json (Insomnia vulcan-api-helper 2021-09-07)
Enter token: FK123456
Enter symbol: powiatwulkanowy
Enter pin: 123456
Getting Vulcan components...
Registering to powiatwulkanowy...
Successfully registered as jan@fakelog.cf
{
    "headers": {
        "Certificate": "....",
        "DeviceModel": "Insomnia vulcan-api-helper 2021-09-07",
        "Fingerprint": "....",
        "FirebaseToken": "....",
        "PrivateKey": "...."
    },
    "symbol": "powiatwulkanowy",
    "school": "123456",
    "unitId": 2,
    "pupilId": 111,
    "periodId": 102,
    "loginId": 207
}
Environment saved as ./env_powiatwulkanowy_111.json

Kuba@KUBA-PC  /d/Dev/vulcan-api-helper
#
```
