import asyncio
from noetl.plugin import Plugin, parse_args, Namespace, logger, NatsConfig, NatsStreamReference
from noetl.payload import Payload, PubAck, AppConst

DISPATCHER = AppConst.DISPATCHER
REVISION_NUMBER = AppConst.REVISION_NUMBER
PLAYBOOK_NAME = AppConst.PLAYBOOK_NAME
METADATA = AppConst.METADATA
PLUGIN_NAME = AppConst.PLUGIN_NAME
IMAGE_URL = AppConst.IMAGE_URL
METADATA_COMMAND_TYPE = AppConst.METADATA_COMMAND_TYPE
# events
EVENT_PLAYBOOK_REGISTERED = AppConst.EVENT_PLAYBOOK_REGISTERED
EVENT_PLAYBOOK_EXECUTION_REGISTERED = AppConst.EVENT_PLAYBOOK_EXECUTION_REGISTERED
EVENT_PLUGIN_REGISTERED = AppConst.EVENT_PLUGIN_REGISTERED

# commands

COMMAND_REGISTER_PLAYBOOK = AppConst.COMMAND_REGISTER_PLAYBOOK
COMMAND_REGISTER_PLUGIN = AppConst.COMMAND_REGISTER_PLUGIN
COMMAND_REGISTER_PLAYBOOK_EXECUTION = AppConst.COMMAND_REGISTER_PLAYBOOK_EXECUTION


class Registrar(Plugin):

    async def playbook_register(self, payload: Payload):
        await payload.playbook_put()
        payload.retain_keys(keys=[REVISION_NUMBER, PLAYBOOK_NAME, METADATA])
        _ = await payload.event_write(event_type=EVENT_PLAYBOOK_REGISTERED, plugin=DISPATCHER)

    async def plugin_register(self, payload: Payload):
        await payload.plugin_put()
        payload.retain_keys(keys=[REVISION_NUMBER, PLUGIN_NAME, IMAGE_URL, METADATA])
        _ = await payload.event_write(event_type=EVENT_PLUGIN_REGISTERED, plugin=DISPATCHER)

    async def register_playbook_execution_request(self, payload: Payload):
        await payload.snapshot_playbook()
        _ = await payload.event_write(event_type=EVENT_PLAYBOOK_EXECUTION_REGISTERED, plugin=DISPATCHER)

    async def switch(self, payload: Payload):
        match payload.get_value(METADATA_COMMAND_TYPE):

            case "RegisterPlaybook":
                await self.playbook_register(payload=payload)

            case "RegisterPlugin":
                await self.plugin_register(payload=payload)

            case "RegisterPlaybookExecution":
                await self.register_playbook_execution_request(payload=payload)


if __name__ == "__main__":
    # args = parse_args(
    #     description="NoETL Registrar Plugin",
    #     default_nats_url="nats://localhost:32222",
    #     default_nats_pool_size=10,
    #     default_plugin_name="registrar",
    #     default_nats_subscription_subject="noetl.command.registrar.>",
    #     default_nats_subscription_stream="noetl",
    #     default_nats_subscription_queue="noetl-registrar",
    #     default_nats_command_prefix="noetl.command",
    #     default_nats_command_stream="noetl",
    #     default_nats_event_prefix="noetl.event",
    #     default_nats_event_stream="noetl",
    #     default_prom_host="localhost",
    #     default_prom_port=9091
    # )
    args = parse_args(
        description="NoETL Registrar Plugin",
        nats_url=("NATS_URL", "nats://localhost:32222", "NATS server URL"),
        nats_pool_size=("NATS_POLL_SIZE", 10, "NATS pool size"),
        plugin_name=("PLUGIN_NAME", "registrar", "Plugin name"),
        nats_subscription_subject=("NATS_SUBSCRIPTION_SUBJECT", "noetl.command.registrar.>", "NATS subject for subscription"),
        nats_subscription_stream=("NATS_SUBSCRIPTION_STREAM", "noetl", "NATS subscription stream"),
        nats_subscription_queue=("NATS_SUBSCRIPTION_QUEUE", "noetl-registrar", "NATS JetStream subscription group queue"),
        nats_command_prefix=("NATS_COMMAND_PREFIX", "noetl.command", "NATS subject prefix for commands"),
        nats_command_stream=("NATS_COMMAND_STREAM", "noetl", "NATS JetStream name for commands"),
        nats_event_prefix=("NATS_EVENT_PREFIX", "noetl.event", "NATS subject prefix for events"),
        nats_event_stream=("NATS_EVENT_STREAM", "noetl", "NATS JetStream name for events"),
        prom_host=("PROM_HOST", "localhost", "Prometheus host"),
        prom_port=("PROM_PORT", 9091, "Prometheus port")
    )
    registrar_plugin = Registrar()
    registrar_plugin.initialize_nats_pool(NatsConfig(
        nats_url=args.nats_url,
        nats_pool_size=args.nats_pool_size,
    ))
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(registrar_plugin.run(args=args))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.info(f"Dispatcher plugin error: {str(e)}.")
    finally:
        loop.run_until_complete(registrar_plugin.shutdown())
