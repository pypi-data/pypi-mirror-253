import asyncio
from noetl.plugin import Plugin, parse_args, logger, NatsConfig
from noetl.payload import Payload, AppConst, RawStreamMsg
from noetl.playbook import Playbook

METADATA_EVENT_TYPE=AppConst.METADATA_EVENT_TYPE
# events
EVENT_PLAYBOOK_EXECUTION_REQUEST_FAILED = AppConst.EVENT_PLAYBOOK_EXECUTION_REQUEST_FAILED
EVENT_PLAYBOOK_REGISTRATION_REQUESTED =  AppConst.EVENT_PLUGIN_REGISTRATION_REQUESTED
EVENT_PLAYBOOK_EXECUTION_REQUESTED = AppConst.EVENT_PLAYBOOK_EXECUTION_REQUESTED
EVENT_PLUGIN_REGISTRATION_REQUESTED = AppConst.EVENT_PLUGIN_REGISTRATION_REQUESTED
EVENT_PLAYBOOK_REGISTERED = AppConst.EVENT_PLAYBOOK_REGISTERED
EVENT_PLUGIN_REGISTERED = AppConst.EVENT_PLUGIN_REGISTERED


# commands
COMMAND_REGISTER_PLAYBOOK = AppConst.COMMAND_REGISTER_PLAYBOOK
COMMAND_REGISTER_PLUGIN = AppConst.COMMAND_REGISTER_PLUGIN
COMMAND_REGISTER_PLAYBOOK_EXECUTION = AppConst.COMMAND_REGISTER_PLAYBOOK_EXECUTION
REGISTRAR = AppConst.REGISTRAR


class Dispatcher(Plugin):

    async def register_playbook(self, payload: Payload):
        _ = await payload.command_write(command_type=COMMAND_REGISTER_PLAYBOOK, plugin=AppConst.REGISTRAR)

    async def register_plugin(self, payload: Payload):
        _ = await payload.command_write(command_type=COMMAND_REGISTER_PLUGIN, plugin=AppConst.REGISTRAR)

    async def register_playbook_execution_request(self, payload: Payload):
        _ = await payload.command_write(command_type=COMMAND_REGISTER_PLAYBOOK_EXECUTION, plugin=AppConst.REGISTRAR)

    async def emit_playbook_command(self, payload: Payload):
        logger.info(payload.nats_reference)
        payload.add_metadata_value(key=AppConst.PAYLOAD_REFERENCE, value=payload.nats_reference.to_dict())
        logger.debug(payload.get_value(AppConst.METADATA))
        stream = payload.get_value("metadata.payloadReference.nats_msg_metadata.stream")
        seq = payload.get_value("metadata.payloadReference.nats_msg_metadata.sequence.stream")
        logger.debug(f"stream: {stream}, seq: {seq}")
        nats_msg_data: RawStreamMsg = await self.get_msg(stream=stream, sequence=seq)
        playbook_blueprint = Playbook.unmarshal(binary_data=nats_msg_data.data, nats_pool=self.nats_pool)
        logger.debug(playbook_blueprint)

        match payload.get_value(METADATA_EVENT_TYPE):
            case "PlaybookStarted":
                logger.info(playbook_blueprint)
            case "PlaybookTaskExecuted":
                logger.info(playbook_blueprint)
            case "PlaybookStepExecuted":
                logger.info(playbook_blueprint)
            case "PlaybookCompleted":
                logger.info(playbook_blueprint)
            case "playbookFailed":
                logger.info(playbook_blueprint)

    async def switch(self, payload: Payload):

        match payload.get_value(METADATA_EVENT_TYPE):
            case "PlaybookRegistrationRequested":
                await self.register_playbook(payload=payload)

            case "PluginRegistrationRequested":
                await self.register_plugin(payload=payload)

            case "PlaybookExecutionRequested":
                await self.register_playbook_execution_request(payload=payload)

            case "PlaybookExecutionRegistered":
                await self.emit_playbook_command(payload=payload)


if __name__ == "__main__":

    args = parse_args(
        description="NoETL Dispatcher Plugin",
        nats_url=("NATS_URL", "nats://localhost:32222", "NATS server URL"),
        nats_pool_size=("NATS_POLL_SIZE", 10, "NATS pool size"),
        plugin_name=("PLUGIN_NAME", "dispatcher", "Plugin name"),
        nats_subscription_subject=("NATS_SUBSCRIPTION_SUBJECT", "noetl.event.dispatcher.>", "NATS subject for subscription"),
        nats_subscription_stream=("NATS_SUBSCRIPTION_STREAM", "noetl", "NATS subscription stream"),
        nats_subscription_queue=("NATS_SUBSCRIPTION_QUEUE", "noetl-dispatcher", "NATS JetStream subscription group queue"),
        nats_command_prefix=("NATS_COMMAND_PREFIX", "noetl.command", "NATS subject prefix for commands"),
        nats_command_stream=("NATS_COMMAND_STREAM", "noetl", "NATS JetStream name for commands"),
        nats_event_prefix=("NATS_EVENT_PREFIX", "noetl.event", "NATS subject prefix for events"),
        nats_event_stream=("NATS_EVENT_STREAM", "noetl", "NATS JetStream name for events"),
        prom_host=("PROM_HOST", "localhost", "Prometheus host"),
        prom_port=("PROM_PORT", 9092, "Prometheus port")
    )

    dispatcher_plugin = Dispatcher()
    dispatcher_plugin.initialize_nats_pool(
        NatsConfig(
            nats_url=args.nats_url,
            nats_pool_size=args.nats_pool_size
        ))
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(dispatcher_plugin.run(args=args))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.info(f"Dispatcher plugin error: {str(e)}.")
    finally:
        loop.run_until_complete(dispatcher_plugin.shutdown())
