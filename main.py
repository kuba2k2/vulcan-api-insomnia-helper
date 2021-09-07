import asyncio
import json
import sys
from datetime import datetime
from os.path import isfile

from vulcan import Account, Keystore, Vulcan

PATH = sys.argv[1] if len(sys.argv) > 1 else "."
ks_file = f"{PATH}/keystore.json"


async def main():
    if not isfile(ks_file):
        device_model = datetime.now().strftime("%Y-%m-%d")
        device_model = f"Insomnia vulcan-api-helper {device_model}"
        device_model = (
            input(f"Input a device model string [{device_model}]: ") or device_model
        )
        keystore = Keystore.create(device_model=device_model)
        with open(ks_file, "w") as f:
            f.write(keystore.as_json)
        print(f"Keystore saved to {ks_file}")
    else:
        with open("keystore.json") as f:
            keystore = Keystore.load(f)
        print(f"Using keystore from {ks_file} ({keystore.device_model})")

    token = input("Enter token: ")
    symbol = input("Enter symbol: ")
    pin = input("Enter pin: ")

    account = await Account.register(keystore, token, symbol, pin)
    client = Vulcan(keystore, account)
    await client.select_student()
    student = client.student

    env = {
        "headers": keystore.as_dict,
        "symbol": symbol,
        "school": student.unit.code,
        "unitId": student.unit.id,
        "pupilId": student.pupil.id,
        "periodId": student.current_period.id,
        "loginId": account.login_id,
    }

    json_file = f"{PATH}/env_{symbol}_{student.pupil.id}.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(env, f)

    print(json.dumps(env, indent=4))
    print(f"Environment saved as {json_file}")

    exit()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_forever()
