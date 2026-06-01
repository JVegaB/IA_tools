# Paybook / Syncfy Webhooks Knowledge

Este documento resume la documentación revisada de Paybook/Syncfy sobre webhooks:

- `https://github.com/Paybook/code-samples/tree/master/webhooks`
- `https://github.com/Paybook/code-samples/tree/master/webhooks/sync`

## Proposito

Los webhooks son callbacks HTTP enviados por Syncfy a una URL configurada cuando hay cambios relacionados con credenciales o datos sincronizados. El webhook no debe tratarse como la fuente final de datos, sino como una notificacion de que existen cambios disponibles para consultar mediante la API.

## Eventos Soportados

Los eventos documentados principales son:

- `credential_create`: se creo una nueva credencial.
- `credential_update`: se actualizo una credencial existente.
- `refresh`: se agregaron o actualizaron datos de una credencial existente.

En la coleccion de Postman y en `methods.md` tambien aparece:

- `documents_completed`: finalizo el procesamiento de datos de un documento via `v1/job`.

La documentacion principal no describe en detalle `documents_completed`, por lo que debe validarse antes de depender de ese evento.

## Registro De Webhooks

El recurso usado para administrar webhooks es:

```text
/v1/webhooks
```

Operaciones documentadas:

- `GET /v1/webhooks`: lista webhooks registrados para una API key.
- `POST /v1/webhooks`: crea un nuevo webhook.
- `DELETE /v1/webhooks/:id_webhook`: elimina un webhook.

Algunos ejemplos antiguos usan `POST` con `X-Http-Method-Override: GET` o `X-Http-Method-Override: DELETE`. La documentacion mas nueva muestra `GET` y `DELETE` directos.

## Hosts Documentados

Hay inconsistencias entre las fuentes:

- `https://sync.paybook.com/v1`
- `https://api.syncfy.com/v1`

Antes de implementar en produccion, confirmar con la API key real cual host esta vigente para la cuenta.

## Autenticacion

Los ejemplos usan el header:

```text
Authorization: api_key api_key=YOUR_API_KEY
```

Cuando se consultan endpoints recibidos en una notificacion, el ejemplo Python agrega tambien el usuario:

```text
Authorization: api_key api_key=YOUR_API_KEY,id_user=ID_USER
```

## Crear Un Webhook

Payload base:

```json
{
  "id_environment": "574894bf7848066d138b4570",
  "url": "https://WEBHOOK_DOMAIN/my_webhook",
  "events": ["credential_create", "credential_update", "refresh"]
}
```

Valores documentados para `id_environment`:

- Sandbox: `574894bf7848066d138b4570`
- Production: `574894bf7848066d138b4571`

Parametros:

- `id_environment`: entorno donde se registra el webhook.
- `url`: URL publica que recibira las notificaciones.
- `events`: lista de eventos a recibir.
- `delay`: opcional, segundos de espera antes de enviar la notificacion. Default `0`.
- `id_user`: opcional, limita notificaciones a un usuario especifico.

La coleccion Postman tambien muestra soporte para `headers` personalizados:

```json
{
  "headers": {
    "X-custom-header": "SATTESTER",
    "Y-custom-header": "ENVPROD",
    "Z-custom-header": "TEST-DECLARA-MENSUAL"
  }
}
```

Esto puede servir como mecanismo simple de validacion del webhook si no hay firma nativa disponible.

## Objeto Webhook

Ejemplo documentado:

```json
{
  "id_webhook": "5d9bab5b8c91e73b2e4c75d3",
  "id_user": null,
  "is_disabled": 1,
  "events": ["credential_create", "credential_update", "refresh"],
  "url": "https://webhook_domain/my_webhook",
  "delay": 0,
  "ct_failed": 1001,
  "dt_created": "2019-10-07T21:17:15+00:00",
  "dt_modified": "2020-03-20T05:37:43+00:00"
}
```

Campos comunes:

- `id_webhook`: identificador del webhook.
- `id_user`: usuario asociado, si aplica.
- `events`: eventos configurados.
- `url`: URL registrada.
- `delay`: retraso configurado.
- `is_disabled`: indica si esta deshabilitado.
- `ct_failed`: contador de fallos.
- `dt_created` / `dt_create`: fecha de creacion.
- `dt_modified` / `dt_modify`: fecha de modificacion.

La documentacion usa variantes de nombres (`dt_created` vs `dt_create`, `dt_modified` vs `dt_modify`), por lo que conviene manejar estos campos con tolerancia al consultar webhooks.

## Payload De Notificacion

Estructura general:

```json
{
  "endpoints": {
    "credential": ["/v1/credentials/ID_CREDENTIAL"]
  },
  "event": "credential_create",
  "id_credential": "ID_CREDENTIAL",
  "id_external": null,
  "id_job": "ID_JOB",
  "id_job_uuid": "ID_JOB_UUID",
  "id_site": "ID_SITE",
  "id_site_organization": "ID_SITE_ORGANIZATION",
  "id_site_organization_type": "ID_SITE_ORGANIZATION_TYPE",
  "id_user": "ID_USER",
  "is_executing": 1
}
```

Campos clave:

- `event`: tipo de evento recibido.
- `endpoints`: rutas relativas que deben consultarse para obtener datos actualizados.
- `id_credential`: credencial afectada.
- `id_user`: usuario relacionado.
- `id_job` / `id_job_uuid`: identificadores del job de sincronizacion.
- `id_external`: identificador externo, si fue configurado.
- `is_executing`: aparece en eventos de credencial y puede indicar que la ejecucion sigue en curso.

## `credential_create`

Indica que se creo una nueva credencial.

Ejemplo:

```json
{
  "endpoints": {
    "credential": ["/v1/credentials/ID_CREDENTIAL"]
  },
  "event": "credential_create",
  "id_credential": "ID_CREDENTIAL",
  "id_external": null,
  "id_job": "ID_JOB",
  "id_job_uuid": "ID_JOB_UUID",
  "id_site": "ID_SITE",
  "id_site_organization": "ID_SITE_ORGANIZATION",
  "id_site_organization_type": "ID_SITE_ORGANIZATION_TYPE",
  "id_user": "ID_USER",
  "is_executing": 1
}
```

Accion esperada:

1. Consultar `endpoints.credential`.
2. Guardar o actualizar la credencial localmente.
3. Registrar el job para idempotencia y trazabilidad.

## `credential_update`

Indica que una credencial existente fue actualizada.

El payload es practicamente igual al de `credential_create`, cambiando `event` a `credential_update`.

Accion esperada:

1. Consultar `endpoints.credential`.
2. Actualizar estado de autorizacion, bloqueo, 2FA, fechas de sincronizacion u otros campos relevantes.
3. Evitar duplicados usando `id_job_uuid`, `id_credential` y `event`.

## `refresh`

Indica que se agregaron o actualizaron datos de una credencial existente.

La documentacion menciona estos casos:

- Nueva cuenta agregada.
- Nuevas transacciones agregadas.
- Cuenta existente actualizada.
- Transaccion existente actualizada.

Ejemplo:

```json
{
  "endpoints": {
    "accounts": [
      "/v1/accounts?id_credential=ID_CREDENTIAL&limit=5000&skip=0"
    ],
    "credential": [
      "/v1/credentials/ID_CREDENTIAL"
    ],
    "transactions": [
      "/v1/transactions?id_credential=ID_CREDENTIAL&limit=5000&skip=0"
    ],
    "attachments": [
      "/v1/attachments?id_credential=ID_CREDENTIAL&limit=5000&skip=0"
    ]
  },
  "event": "refresh",
  "id_credential": "ID_CREDENTIAL",
  "id_external": null,
  "id_job": "ID_JOB",
  "id_job_uuid": "ID_JOB_UUID",
  "id_site": "ID_SITE",
  "id_site_organization": "ID_SITE_ORGANIZATION",
  "id_site_organization_type": "ID_SITE_ORGANIZATION_TYPE",
  "id_user": "ID_USER"
}
```

En `webhooks/sync/events.md`, los endpoints de `refresh` pueden venir paginados con `limit=5000` y distintos valores de `skip`, por ejemplo:

```text
/v1/transactions?id_credential=ID_CREDENTIAL&limit=5000&skip=0&wbhk=1
/v1/transactions?id_credential=ID_CREDENTIAL&limit=5000&skip=5000&wbhk=1
/v1/transactions?id_credential=ID_CREDENTIAL&limit=5000&skip=10000&wbhk=1
```

Tambien pueden aparecer endpoints de attachments como:

```text
/v1/attachments/export?id_credential=ID_CREDENTIAL&limit=5000&skip=0&wbhk=1
```

Accion esperada:

1. Consultar `endpoints.credential`.
2. Consultar todos los endpoints en `accounts`.
3. Consultar todos los endpoints en `transactions`.
4. Consultar `attachments` si el payload los incluye.
5. Procesar cada pagina enviada por Syncfy.
6. Hacer upsert de datos usando IDs estables (`id_account`, `id_transaction`, `id_credential`, etc.).

## Recomendaciones De Implementacion

El endpoint receptor deberia:

1. Aceptar `POST`.
2. Parsear JSON.
3. Validar que `event` exista y sea soportado.
4. Validar headers personalizados si se configuraron al crear el webhook.
5. Responder rapido con `2xx`.
6. Encolar el procesamiento pesado en background.
7. Usar idempotencia para evitar procesar dos veces el mismo evento.
8. Consultar los endpoints enviados en el payload usando la API de Syncfy.
9. Registrar errores, payload recibido y resultado del procesamiento.

Claves sugeridas para idempotencia:

- `id_job_uuid`
- `id_job`
- `event`
- `id_credential`

Una clave compuesta razonable puede ser:

```text
{event}:{id_job_uuid}:{id_credential}
```

## Seguridad

La documentacion revisada no menciona firma HMAC, secreto compartido nativo ni header oficial de verificacion del webhook.

Medidas recomendadas:

- Usar HTTPS siempre.
- Configurar headers personalizados al registrar el webhook y validarlos al recibir la notificacion.
- Usar una ruta dificil de adivinar si no hay mejor mecanismo disponible.
- Aplicar allowlist de IPs si Syncfy/Paybook la ofrece.
- No confiar en el payload como fuente final; validar consultando los endpoints de Syncfy.
- Registrar intentos fallidos o eventos con estructura inesperada.

## Consideraciones Operativas

- No bloquear la respuesta HTTP mientras se descargan cuentas, transacciones o attachments.
- Procesar `refresh` de forma asincrona porque puede incluir muchas paginas.
- Manejar reintentos de llamadas a Syncfy.
- Manejar endpoints ausentes: por ejemplo, algunos payloads de `refresh` pueden no traer `attachments`.
- Guardar el payload crudo para auditoria y depuracion.
- Monitorear errores de procesamiento y latencia.
- Evitar asumir que todos los campos siempre llegan con valor; `id_external` puede venir `null`.

## Observaciones Sobre Los Ejemplos Del Repositorio

- El ejemplo `webhooks/code/python/main_webhook.py` parece no estar listo para ejecutarse tal cual: usa `event` sin asignarlo y el formato publicado tiene problemas de indentacion.
- El README de Python contiene una version mas clara del flujo.
- El README general dice que `DELETE /webhooks/:id_webhook` "actualiza" un webhook, pero por el metodo y ejemplos debe interpretarse como eliminacion.
- Existen diferencias de nombres de campos de fecha entre documentos.

## Flujo Recomendado

1. Registrar webhook en Sandbox con `id_environment`, `url`, `events` y headers personalizados.
2. Exponer endpoint HTTPS que reciba `POST`.
3. Validar headers personalizados.
4. Guardar payload crudo.
5. Responder `200` inmediatamente.
6. Encolar procesamiento.
7. Segun `event`, consultar los endpoints indicados en `endpoints`.
8. Hacer upsert de credenciales, cuentas, transacciones y attachments.
9. Registrar el resultado usando `id_job_uuid` para trazabilidad.
10. Repetir validacion en Production con el `id_environment` correspondiente.
