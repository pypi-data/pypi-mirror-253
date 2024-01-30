# PESIC - PetroElektroSbyt Integrated Client

## Установка

```bash
$ pip3 install -U pesic
```

## Использование

```python
from pesic.api import PESClient
import asyncio

username = "88005553535"
password = "ЧемУкогоТоЗанимать"

async def main():
    client = PESClient(username=username, password=password)
    # Получить список групп в личном кабинете
    await client.get_groups()
    # Получить список учетных записей для группы с ID 123456
    await client.get_group_accounts(group_id=123456)
    # Получить детали для учетной записи с ID 654321
    await client.get_account_details(account_id=654321)
    # Получить детали счетчиков для учетной записи с ID 654321
    await client.get_meters_info(account_id=account)
    # Передать показания для однотарифного счетчика 
    data = [{'scale_id': 1, 'scale_value': 9136}]
    # Передать показания для двухтарифного счетчика 
    data = [{'scale_id': 2, 'scale_value': 9136}, {'scale_id': 3, 'scale_value': 2775}]
    await client.set_meters_reading(account_id=654321, readings=data)
    # Закрыть соединение
    await client.close()

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
```

## Отладка

Bash:
```bash
export PESIC_LOGLEVEL="DEBUG"
```

Powershell:
```powershell
$env:PESIC_LOGLEVEL="DEBUG" 
```
## Предостережение

Личный кабинет ПетроЭлектроСбыт поддерживает несколько типов учетных записей. Как классические, для передачи показаний потребления электроэнергии, так и учетные записи поставщиков холодной и горячей воды и, возможно, какие-то еще.

Метод ```set_meters_reading``` выполняет несколько проверок: 
- количество новых показаний в обновлении должно совпадать с текущим количеством счетчиков;
- текущий счетчик должен иметь все переданные ```scale_id```;
- текущий счетчик должен иметь показания меньше, чем те, что переданы в ```scale_value``` для данного ```scale_id```

Метод set_meters_reading в данный поддеживает только обновление однотарифных и двухтарифных счетчиков электроэнергии. Обновление счетчиков холодной и горячей воды не тестировалось и в данный момент не поддерживается.